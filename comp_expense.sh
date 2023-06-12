#!/bin/bash

find . -type f \( -name "*.log" -o -name "*.out" \) | while read -r filepath; do
	file="${filepath##*/}"
	if [[ $file == *.log ]]; then
		software="Gaussian"
		
		elapsed_time=$(grep -m 1 "Elapsed time" "$filepath" | cut -d' ' -f4-)
		days=$(echo "$elapsed_time" | awk -F'[ .:]+' '{print $2}')
		hours=$(echo "$elapsed_time" | awk -F'[ .:]+' '{print $4}')
		minutes=$(echo "$elapsed_time" | awk -F'[ .:]+' '{print $6}')
 		seconds=$(echo "$elapsed_time" | awk -F'[ .:]+' '{print $8"."$9}')
    		total_minutes=$(echo "$days * 24 * 60 + $hours * 60 + $minutes + $seconds/60" | bc -l)
  	elif [[ $file == *.out ]]; then
		software="ORCA"
		
    		total_run_time=$(grep -m 1 "TOTAL RUN TIME" "$filepath" | cut -d' ' -f4-)
    		days=$(echo "$total_run_time" | awk -F'[ .:]+' '{print $1}')
    		hours=$(echo "$total_run_time" | awk -F'[ .:]+' '{print $3}')
    		minutes=$(echo "$total_run_time" | awk -F'[ .:]+' '{print $5}')
    		seconds=$(echo "$total_run_time" | awk -F'[ .:]+' '{print $7}')
    		msec=$(echo "$total_run_time" | awk -F'[ .:]+' '{print $9}')
    		total_minutes=$(echo "$days * 24 * 60 + $hours * 60 + $minutes + $seconds/60 + $msec/60000" | bc -l)
  	else
		echo "Not sure what software $file is"
	fi
	
	#Figure out what the method is 
	if [[ $file == "EOM-CCSD"* ]]; then
		method="EOM-CCSD"
	elif [[ $file == "STEOM-CCSD"* ]]; then
    		method="STEOM-CCSD"
	elif [[ $file == "EOM-DLPNO-CCSD"* ]]; then
		method="EOM-DLPNO-CCSD"
	elif [[ $file == "bt-PNO-EOM-CCSD"* ]]; then
		method="bt-PNO-EOM-CCSD"
	elif [[ $file == "bt-PNO-STEOM-CCSD"* ]]; then
		method="bt-PNO-STEOM-CCSD"
	elif [[ $file == "STEOM-DLPNO-CCSD"* ]]; then
		method="STEOM-DLPNO-CCSD"
	else
		echo "Cannot figure out the method for $file"
	fi
	
	#Figure out how many excited states
	if [[ $file == *"5"* ]]; then
		nstates="5"
	elif [[ $file == *"6"* ]]; then
		nstates="6"
	elif [[ $file == *"7"* ]]; then
		nstates="7"
	elif [[ $file == *"8"* ]]; then
		nstates="8"
	elif [[ $file == *"9"* ]]; then
		nstates="9"
	elif [[ $file == *"10"* ]]; then
		nstates="10"
	elif [[ $file == *"20"* ]]; then
		nstates="20"
	else
		echo "Cannot figure out how many states in $file"
	fi
	
	#Figure out the basis set
	if [[ $file == *"augccpvdzpp"* ]]; then
		basis_set="augccpvdzpp"
	elif [[ $file == *"def2SVP"* ]]; then
		basis_set="def2SVP"
	elif [[ $file == *"def2TZVPD"* ]]; then
		basis_set="def2TZVPD"
	else 
		echo "Cannot figure out the basis set for $file"
	fi
	
	#Figure out if the calculation is relativistic
	if [[ $file == *"rel"* ]]; then
		rel="yes"
	else
		rel="no"
	fi 
		
	echo "For $file the software is $software the method is $method the basis set is $basis_set the states are $nstates the relativistic is $rel and the time is $total_minutes minutes"
	#echo "$software $method $basis_set $nstates $rel $total_minutes" >> computationalexpense
done
