#!/bin/bash

#Read in the input and output file names
echo "What is your input file? Probably fordisplacementenergy.out"
read input_file

echo "What is your output file? Perhaps table.out"
read output_file

#Remove any duplicates of each geometry and add the number of atoms in each cluster to each unique equilibrium geometry line
while IFS= read -r line; do
    logfile=$(echo "$line" | cut -d' ' -f1)
    # Check if the line already exists in the temporary file
    if grep -q "$logfile" $input_file; then
        continue  # Skip duplicate lines
    else
        atom_num=$(echo "$logfile" | cut -c3)
        charge=$(echo "$logfile" | cut -c5)
        echo "$logfile" "$atom_num" "$charge" >> $output_file
    fi
done 

