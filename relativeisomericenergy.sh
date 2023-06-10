#!/bin/bash

input_file="fordisplacementenergy.out"
output_file="forrelativeisomericenergy.out"

#Find the equilibrium geometries contained in the input file and print them to the output file
grep "eq.log" "$input_file" > "$output_file"

input_file="forrelativeisomericenergy.out"
output_file="forrelativeisomericenergy.out"

#Make a temporary file
tmp_file=$(mktemp)

#Remove any duplicates of each equilibrium geometry and add the number of atoms in each cluster to each unique equilibrium geometry line
while IFS= read -r line; do
    logfile=$(echo "$line" | cut -d' ' -f1)
    # Check if the line already exists in the temporary file
    if grep -q "$logfile" "$tmp_file"; then
        continue  # Skip duplicate lines
    else
        disp_energy=$(echo "$line" | cut -d' ' -f2)
        atom_num=$(echo "$logfile" | cut -c3)
        echo "$logfile" "$atom_num" "$disp_energy" >> "$tmp_file"
    fi
done < "$input_file"

# Overwrite the original file with the modified content
mv "$tmp_file" "$output_file"

while read -r line; do
  field2=$(echo "$line" | awk '{print $2}')
  field3=$(echo "$line" | awk '{print $3}')
  if [[ ${seen["$field2"]} ]]; then
    # if so, update the minimum value for this field
    if (( $(echo "$field3 < ${seen["$field2"]}" | bc -l) )); then
      seen["$field2"]=$field3
    fi
  else
    # otherwise, initialize the minimum value for this field
    seen["$field2"]=$field3
  fi
done < forrelativeisomericenergy.out

# subtract the minimum value for each field2 from all corresponding lines
while read -r line; do
  # extract second and third fields
  field2=$(echo "$line" | awk '{print $2}')
  field3=$(echo "$line" | awk '{print $3}')

  # subtract the minimum value for this field2 from field3
  min_val=${seen["$field2"]}
  new_val=$(echo "$field3 - $min_val" | bc -l)

  # print the modified line
  echo "$(echo "$line" | awk '{print $1}') $field2 $new_val" >> temp.out
done < forrelativeisomericenergy.out
mv temp.out relativeisomericenergy.out
sed -i 's/_eq.log//g' relativeisomericenergy.out
#scp displacementenergy.out carinaluo@hpcc.brandeis.edu:/home/carinaluo/research/groundstategraphs
