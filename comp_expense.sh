#!/bin/bash

# Loop over all files in the current directory
for file in ./; do
	if [[ $file == *.log ]]; then
		software="Gaussian"
		
		elapsed_time=$(grep -m 1 "Elapsed time" "$file" | cut -d' ' -f4-)
		days=$(echo "$elapsed_time" | awk -F'[ .:]+' '{print $2}')
		hours=$(echo "$elapsed_time" | awk -F'[ .:]+' '{print $4}')
		minutes=$(echo "$elapsed_time" | awk -F'[ .:]+' '{print $6}')
 		seconds=$(echo "$elapsed_time" | awk -F'[ .:]+' '{print $8"."$9}')
    		total_minutes=$(echo "$days * 24 * 60 + $hours * 60 + $minutes + $seconds/60" | bc -l)
 	fi

  	elif [[ $file == *.out ]]; then
		software="ORCA"
		
    		total_run_time=$(grep -m 1 "TOTAL RUN TIME" "$file" | cut -d' ' -f4-)
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
	if echo "$file" | grep -q "^EOM-CCSD_"; then
    		method="EOM-CCSD"
	elif echo "$file" | grep -q "^STEOM-CCSD"; then
    		method="STEOM-CCSD"
	elif echo "$file" | grep -q "^EOM-DLPNO-CCSD"; then
		method="EOM-DLPNO-CCSD"
	elif echo "$file" | grep -q "^bt-PNO-EOM-CCSD"; then
		method="bt-PNO-EOM-CCSD"
	elif echo "$file" | grep -q "^bt-PNO-STEOM-CCSD"; then
		method="bt-PNO-STEOM-CCSD"
	elif echo "$file" | grep -q "^STEOM-DLPNO-CCSD"; then
		method="STEOM-DLPNO-CCSD"
	else
		echo "Cannot figure out the method for $file"
	fi
	
	#Figure out how many excited states
	if echo "$file" | grep -q "5"; then
		nstates="5"
	elif echo "$file" | grep -q "6"; then
		nstates="6"
	elif echo "$file" | grep -q "7"; then
		nstates="7"
	elif echo "$file" | grep -q "8"; then
		nstates="8"
	elif echo "$file" | grep -q "9"; then
		nstates="9"
	elif echo "$file" | grep -q "10"; then
		nstates="10"
	else
		echo "Cannot figure out how many states in $file"
	fi
	
	#Figure out the basis set
	if echo "$file" | grep -q "augccpvdzpp"; then
		basisset="augccpvdzpp"
	elif echo "$file" | grep -q "def2SVP"; then
		basisset="def2SVP"
	else 
		echo "Cannot figure out the basis set for $file"
	fi
	
	#Figure out if the calculation is relativistic
	if echo "$file" | grep -q "rel"; then
		rel="yes"
	else
		rel="no"
	fi 
		
	echo "For $file the software is $software the method is $method the basis set is $basis_set the states are $nstates and the time is $total_minutes minutes"
	#echo "$software $method $basis_set $nstates $rel $total_minutes" >> computationalexpense
done
