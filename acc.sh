#!/bin/bash

echo "What would you like the output file to be called?"
read output_file

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
				echo "$excitedstate_1 $excitedstate_2 $excitedstate_3 $excitedstate_4 $excitedstate_5 $excitedstate_6 $excitedstate_7 $excitedstate_8 $excitedstate_9 $excitedstate_10 $file" >> $output_file
			fi
		
		else 
      			echo "$file method is not recognized"
    		fi
  	elif [[ $file == *.out ]]; then
		if [[ $file == "STEOM-CCSD"* || $file == "STEOM-DLPNO-CCSD"* || $file == "EOM-DLPNO-CCSD"* || $file == "bt-PNO-EOM-CCSD"* || $file == "bt-PNO-STEOM-CCSD"* || $file == "EOM-CCSD"* ]]; then
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
    				if [[ $file == "STEOM-CCSD"* ]]; then
					method="STEOM-CCSD"
     				elif [[ $file == "STEOM-DLPNO-CCSD"* ]]; then
	 				method="STEOM-DLPNO-CCSD"
      				elif [[ $file == "EOM-DLPNO-CCSD"* ]]; then
	  				method="EOM-DLPNO-CCSD"
       				elif [[ $file == "bt-PNO-EOM-CCSD"* ]]; then
	   				method="bt-PNO-EOM-CCSD"
				elif [[ $file == "bt-PNO-STEOM-CCSD"* ]]; then
	   				method="bt-PNO-STEOM-CCSD"
				elif [[ $file == "EOM-CCSD"* ]]; then
	   				method="EOM-CCSD"
				else
    					echo "Not sure what the method is for $file"
				fi

				if [[ $file == *"def2TZVPPD"* ]]; then
    					basis_set="def2TZVPPD"
	 			elif [[ $file == *"augccpvdzpp"* ]]; then
    					basis_set="augccpvdzpp"
	 			elif [[ $file == *"def2SV_P"* ]]; then
    					basis_set="def2SV_P"
	 			elif [[ $file == *"def2SVP_"* ]]; then
    					basis_set="def2SVP"
	 			elif [[ $file == *"def2SVPD"* ]]; then
    					basis_set="def2SVPD"
	 			elif [[ $file == *"def2TZVP_"* ]]; then
    					basis_set="def2TZVP"
	 			elif [[ $file == *"def2TZVPD"* ]]; then
    					basis_set="def2TZVPD"
	 			elif [[ $file == *"def2TZVPP"* ]]; then
    					basis_set="def2TZVPP"
	 			else 
     					echo "Can't figure out basis set for $file"
	  			fi
      
				echo "$excitedstate_1 $excitedstate_2 $excitedstate_3 $excitedstate_4 $excitedstate_5 $excitedstate_6 $excitedstate_7 $excitedstate_8 $excitedstate_9 $excitedstate_10 ${method}/${basis_set}" >> $output_file
			fi
		else
			echo "$file method is not recognized"
		fi
	else
    		echo "$file type is not recognized"
  	fi
done
