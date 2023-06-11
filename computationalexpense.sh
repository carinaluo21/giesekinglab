#!/bin/bash

# loop over all files in the current directory
for file in *; do
	if [[ $file == *.log ]]; then
		if grep -q "genecp" "$file"; then
			basisset="augccpvdzpp"
		else
			basisset="def2-SVP"
		fi
		elapsed_time=$(grep -m 1 "Elapsed time" "$file" | cut -d' ' -f4-)
		days=$(echo "$elapsed_time" | awk -F'[ .:]+' '{print $2}')
		hours=$(echo "$elapsed_time" | awk -F'[ .:]+' '{print $4}')
		minutes=$(echo "$elapsed_time" | awk -F'[ .:]+' '{print $6}')
 		seconds=$(echo "$elapsed_time" | awk -F'[ .:]+' '{print $8"."$9}')
    		total_minutes=$(echo "$days * 24 * 60 + $hours * 60 + $minutes + $seconds/60" | bc -l)
    		nstates=$(grep -m 1 -o 'NStates=[^,]*' "$file" | cut -c 9-)
    		method=$(grep -m 1 -o "# .*(" "$file" | cut -c 3- | rev | cut -c 2- | rev)
    		echo "$file $method $basisset $nstates $total_minutes" >> computationalexpense
 	fi

  	if [[ $file == *.out ]]; then
    		total_run_time=$(grep -m 1 "TOTAL RUN TIME" "$file" | cut -d' ' -f4-)
    		days=$(echo "$total_run_time" | awk -F'[ .:]+' '{print $1}')
    		hours=$(echo "$total_run_time" | awk -F'[ .:]+' '{print $3}')
    		minutes=$(echo "$total_run_time" | awk -F'[ .:]+' '{print $5}')
    		seconds=$(echo "$total_run_time" | awk -F'[ .:]+' '{print $7}')
    		msec=$(echo "$total_run_time" | awk -F'[ .:]+' '{print $9}')
    		total_minutes=$(echo "$days * 24 * 60 + $hours * 60 + $minutes + $seconds/60 + $msec/60000" | bc -l)
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
		fi
		
		if echo "$file" | grep -q "augccpvdzpp"; then
			basisset="augccpvdzpp"
		elif echo "$file" | grep -q "def2SVP"; then
                        basisset="def2SVP"
		fi

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
		fi
		echo "$file $method $basisset $nstates $total_minutes" >> computationalexpense
  	fi
done
