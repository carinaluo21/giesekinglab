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

declare -A seen

while read -r line; do
    atom_num=$(echo "$line" | awk '{print $2}')
    disp_energy=$(echo "$line" | awk '{print $3}')

    if [[ ${seen["$atom_num"]} ]]; then
        echo "$atom_num has been seen before"
        
        if (( $(awk -v disp_energy="$disp_energy" -v min_disp_energy="${seen["$atom_num"]}" 'BEGIN { print (disp_energy < min_disp_energy) ? 1 : 0 }') )); then
            seen["$atom_num"]=$disp_energy
            echo "the new minimum disp energy for $atom_num is $disp_energy"
        fi
    else
        seen["$atom_num"]=$disp_energy
        echo "$atom_num has not been seen before, initial value is $disp_energy"
    fi
done < "forrelativeisomericenergy.out"


while read -r line; do
    atom_num=$(echo "$line" | awk '{print $2}')
    disp_energy=$(echo "$line" | awk '{print $3}')
    isom_energy=$((disp_energy - ${seen["$atom_num"]}))
    echo $atom_num $isom_energy 
done < "forrelativeisomericenergy.out"

#mv "tmp" "relativeisomericenergy.out"

#sed -i 's/_eq.log//g' relativeisomericenergy.out
