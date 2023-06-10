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

#Find the lowest energy isomer for each cluster size
while read -r line; do
    atom_num=$(echo "$line" | awk '{print $2}')
    disp_energy=$(echo "$line" | awk '{print $3}')
    if [[ ${seen["$field2"]} ]]; then
        if (( $(echo "$disp_energy < ${seen["$atom_num"]}" | bc -l) )); then
            seen["$atom_num"]=$min_disp_energy
            isom_energy=$(echo "$disp_energy - $min_disp_energy" | bc -l)
        elif (( $(echo "$disp_energy > ${seen["$atom_num"]}" | bc -l) )); then
            continue
        else
            echo "
    fi
  else
    # otherwise, initialize the minimum value for this field
    seen["$atom_num"]=$disp_energy
  fi
  echo "$(echo "$line" | awk '{print $1}') $atom_num $isom_energy" >> "tmp"
done < "forrelativeisomericenergy.out"

mv "tmp" "relativeisomericenergy.out"

sed -i 's/_eq.log//g' relativeisomericenergy.out
