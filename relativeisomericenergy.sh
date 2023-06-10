#!/bin/bash

grep "eq.log" "fordisplacementenergy.out" > "forrelativeisomericenergy.out"
while IFS= read -r line; do
        first_field=$(echo "$line" | cut -d' ' -f1)
        third_char=$(echo "$first_field" | cut -c3)
        new_line=$(echo "$line" | sed "s/$first_field/$first_field $third_char/")
        echo "$new_line" >> temp.out
done < "forrelativeisomericenergy.out"
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
