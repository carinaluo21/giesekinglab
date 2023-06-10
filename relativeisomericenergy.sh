#!/bin/bash

#Make a temporary file
touch tmp

#Find the equilibrium geometries contained in the input file and print them to the output file
grep "eq.log" "fordisplacementenergy.out" > "forrelativeisomericenergy.out"

#Remove any duplicates of each equilibrium geometry and add the number of atoms in each cluster to each unique equilibrium geometry line
while IFS= read -r line; do
    logfile=$(echo "$line" | cut -d' ' -f1)
    # Check if the line already exists in the temporary file
    if grep -q "$logfile" "tmp"; then
        continue  # Skip duplicate lines
    else
        disp_energy=$(echo "$line" | cut -d' ' -f2)
        atom_num=$(echo "$logfile" | cut -c3)
        echo "$logfile" "$atom_num" "$disp_energy" >> "tmp"
    fi
done < "forrelativeisomericenergy.out"

# Overwrite the original file with the modified content
mv "tmp" "forrelativeisomericenergy.out"

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
