#!/bin/bash

#Find the equilibrium geometries contained in the "fordisplacementenergy.out" file and print them to the "forrelativeisomericenergy.out" file
grep "eq.log" "fordisplacementenergy.out" > "forrelativeisomericenergy.out"

input_file="forrelativeisomericenergy.out"
output_file="forrelativeisomericenergy.out"

#Make a temporary file
tmp_file=$(mktemp)

#Remove any duplicates of each equilibrium geometry
while IFS= read -r line; do
    # Check if the line already exists in the temporary file
    if grep -Fxq "$line" "$tmp_file"; then
        continue  # Skip duplicate lines
    else
        # Append the line to the temporary file
        echo "$line" >> "$tmp_file"
    fi

done < "$input_file"

# Overwrite the original file with the modified content
mv "$tmp_file" "$output_file"

#Read the file line by line, and save the name of the log file, the number of atoms in the cluster corresponding to that log file, and print a new line containing the log file name and the number of atoms in the cluster to a temporary file
while IFS= read -r line; do
        first_field=$(echo "$line" | cut -d' ' -f1)
        third_char=$(echo "$first_field" | cut -c3)
        new_line=$(echo "$line" | sed "s/$first_field/$first_field $third_char/")
        echo "$new_line" >> temp.out
done < "forrelativeisomericenergy.out"

#Overwrite contents of the temporary file to the "forrelativeisomericenergy.out" file
mv temp.out forrelativeisomericenergy.out

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
