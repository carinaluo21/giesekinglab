#!/bin/bash

find . -type f \( -name "*.log" -o -name "*.out" \) | while read -r filepath; do
	file="${filepath##*/}"
	if [[ $file == *.log ]]; then
		if [[ $file == "EOM-CCSD"* ]]; then
	  		if [[ $file == *"10"* ]]; then
				excitedstate_1=$(grep -m 2 "Excited State   1" "$filepath" | tail -n 1 | awk '{print $5}')
        			excitedstate_2=$(grep -m 2 "Excited State   2" "$filepath" | tail -n 1 | awk '{print $5}')
        			excitedstate_3=$(grep -m 2 "Excited State   3" "$filepath" | tail -n 1 | awk '{print $5}')
        			excitedstate_4=$(grep -m 2 "Excited State   4" "$filepath" | tail -n 1 | awk '{print $5}')
        			excitedstate_5=$(grep -m 2 "Excited State   5" "$filepath" | tail -n 1 | awk '{print $5}')
        			excitedstate_6=$(grep -m 2 "Excited State   6" "$filepath" | tail -n 1 | awk '{print $5}')
        			excitedstate_7=$(grep -m 2 "Excited State   7" "$filepath" | tail -n 1 | awk '{print $5}')
        			excitedstate_8=$(grep -m 2 "Excited State   8" "$filepath" | tail -n 1 | awk '{print $5}')
        			excitedstate_9=$(grep -m 2 "Excited State   9" "$filepath" | tail -n 1 | awk '{print $5}')
        			excitedstate_10=$(grep -m 2 "Excited State  10" "$filepath" | tail -n 1 | awk '{print $5}')
				echo "$excitedstate_1 $excitedstate_2 $excitedstate_3 $excitedstate_4 $excitedstate_5 $excitedstate_6 $excitedstate_7 $excitedstate_8 $excitedstate_9 $excitedstate_10 in $file"
			fi
		
		else 
      			echo "$file method is not recognized"
    		fi
  	elif [[ $file == *.out ]]; then
		if [[ $file == "STEOM-CCSD"* || $file == "STEOM-DLPNO-CCSD"* || $file == "EOM-DLPNO-CCSD"* ]]; then
			if [[ $file == *"10"* ]]; then
				excitedstate_1=$(grep -m 5 "IROOT=  1" "$filepath" | tail -n 1 | awk '{print $5}')
				excitedstate_2=$(grep -m 5 "IROOT=  2" "$filepath" | tail -n 1 | awk '{print $5}')
				excitedstate_3=$(grep -m 5 "IROOT=  3" "$filepath" | tail -n 1 | awk '{print $5}')
				excitedstate_4=$(grep -m 5 "IROOT=  4" "$filepath" | tail -n 1 | awk '{print $5}')
				excitedstate_5=$(grep -m 5 "IROOT=  5" "$filepath" | tail -n 1 | awk '{print $5}')
				excitedstate_6=$(grep -m 5 "IROOT=  6" "$filepath" | tail -n 1 | awk '{print $5}')
				excitedstate_7=$(grep -m 5 "IROOT=  7" "$filepath" | tail -n 1 | awk '{print $5}')
				excitedstate_8=$(grep -m 5 "IROOT=  8" "$filepath" | tail -n 1 | awk '{print $5}')
				excitedstate_9=$(grep -m 5 "IROOT=  9" "$filepath" | tail -n 1 | awk '{print $5}')
				excitedstate_10=$(grep -m 4 "IROOT= 10" "$filepath" | tail -n 1 | awk '{print $5}')
				echo "$excitedstate_1 $excitedstate_2 $excitedstate_3 $excitedstate_4 $excitedstate_5 $excitedstate_6 $excitedstate_7 $excitedstate_8 $excitedstate_9 $excitedstate_10 in $file"
			fi
		else
			echo "$file method is not recognized"
		fi
	else
    		echo "$file type is not recognized"
  	fi
done
