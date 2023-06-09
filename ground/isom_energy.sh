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
        echo "$logfile" "$atom_num" "$charge" "$disp_energy" >> "tmp"
    fi
done < "forrelativeisomericenergy.out"

# Overwrite the original file with the modified content
mv "tmp" "forrelativeisomericenergy.out"

declare -A seen

while read -r line; do
    charge=$(echo "$line" | awk '{print $1}' | awk '{print substr($0, 5, 1)}')
    atom_num=$(echo "$line" | awk '{print $2}')
    disp_energy=$(echo "$line" | awk '{print $3}')
    
    key="$atom_num:$charge"

    if [[ ${seen["$key"]} ]]; then
        if (( $(awk -v disp_energy="$disp_energy" -v min_disp_energy="${seen["$key"]}" 'BEGIN { print (disp_energy < min_disp_energy) ? 1 : 0 }') )); then
            seen["$key"]=$disp_energy
            echo "the new minimum disp energy for $key is $disp_energy"
        fi
    else
        seen["$key"]=$disp_energy
        echo "$key has not been seen before, initial value is $disp_energy"
    fi
done < "forrelativeisomericenergy.out"

echo "${seen[@]}"

while read -r line; do
    charge=$(echo "$line" | awk '{print $1}' | awk '{print substr($0, 5, 1)}')
    atom_num=$(echo "$line" | awk '{print $2}')
    key="$atom_num:$charge"
    disp_energy=$(echo "$line" | awk '{print $3}')
    isom_energy=$(echo "$disp_energy - ${seen["$key"]}" | bc)
    echo "$disp_energy - ${seen["$key"]} for $key"
    echo $atom_num $charge $isom_energy >> "relativeisomericenergy.out"
done < "forrelativeisomericenergy.out"

#sed -i 's/_eq.log//g' relativeisomericenergy.out
