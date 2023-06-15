#!/bin/bash

Au1negative1=-135.31977404
Au1neutral=-135.18315036
Au1positive1=-134.90644798

for logfilepath in $(find -name '*.log')
do
	if [[ "$logfilepath" != *"Eq_geo"* ]]; then
		#Extract the name of the log file from the path
		logfile=$(echo "$logfilepath" | awk -F "/" '{print $NF}')
		#Extract the number of atoms from the log file name
		n=$(cut -c 3 <<< $logfile)
		#Extract the charge from the log file name
		charge=$(cut -c 5 <<< $logfile)

		#Extract the energy value from the log file
		energyvalue=$( bc <<< "$(grep -m 1 "CCSD(T)=" $logfilepath | cut -b 11-24)*1000" | cut -b 1-13 )
		echo "Got the energy value"
		#If the charge is neutral, then subtract the appropriate number of neutral atoms
		if [ "$charge" = "0" ]; then
			subtractneutralatoms=$(echo $n - 0 | bc)
			neutralatoms=$(echo $subtractneutralatoms*$Au1neutral | bc)
			positiveatoms=0
			negativeatoms=0
	
		#If the charge is negative, then subtract the appropriate number of neutral atoms and subtract one negative atom
		elif [ "$charge" = "-" ]; then
			subtractneutralatoms=$(echo $n - 1 | bc)
			neutralatoms=$(echo $subtractneutralatoms*$Au1neutral | bc)
			positiveatoms=0
			subtractnegativeatoms=1
			negativeatoms=$(echo $subtractnegativeatoms*$Au1negative1| bc)
	
		#If the charge is positive, then subtract the appropriate number of neutral atoms and one positive atom 
		elif [ "$charge" = "1" ]; then
			subtractneutralatoms=$(echo $n - 1 | bc)
			neutralatoms=$(echo $subtractneutralatoms*$Au1neutral | bc)
			positiveatoms=$(echo 1*$Au1positive1 | bc)
			negativeatoms=0
		else
  			echo "Charge is not recognized for $logfile"
  		fi
	
		#Calculate the binding energy
		bindingenergy=$(echo $energyvalue - $neutralatoms - $positiveatoms - $negativeatoms | bc)
		#Convert the binding energy from Hartrees to eV
		bindingenergyineV=$( bc <<< "$(echo "scale=12; $bindingenergy * 27.2114")" )
		#Convert the binding energy to binding energy per atom
		bindingenergyperatomineV=$( bc <<< "$(echo "scale=12; $bindingenergy * 27.2114 / $n")" )
	
		#Output the binding energies (not per atom) to a file that will have further operations performed on it to obtain the displacement energy graphs
		echo $logfile $bindingenergyineV >> fordisplacementenergy.out

		#For neutral clusters, output all the binding energies per atom to a file
		if [ "$charge" = "0" ]; then
        		echo $n $bindingenergyperatomineV >> bindingenergy_neutralclusters.ou

		#For anionic clusters, output all the binding energies per atom to a file
		elif [ "$charge" = "-" ]; then
                	echo $n $bindingenergyperatomineV >> bindingenergy_negativeclusters.out
	
		#For cationic clusters, output all the binding energies per atom to a file
		elif [ "$charge" = "1" ]; then
                	echo $n $bindingenergyperatomineV >> bindingenergy_positiveclusters.out
        	else
	 		echo "Cannot write to binding energy output file for $logfile"
	 	fi

	fi	
done

while IFS= read -r line; do
        logfile=$(echo "$line" | awk '{print $1}')
        energy=$(echo "$line" | awk '{print $2}')

        geo="${logfile:0:8}"
	logfilepath=$(find -name $logfile -print -quit)
	mode=$(grep -m 1 "vibrational mode" $logfilepath | awk '{print $4}')
	displacement=$(grep -m 1 "vibrational mode" $logfilepath | awk '{print $8}')

        last_character="${geo: -1}"

        #echo the last character of $geo is $last_character

        if [[ $last_character == "_" ]]; then
                geo="${geo%_}"
        fi

	eq_geo_filename="${geo}_eq.log"

        eq_geo_energy=$(grep -m 1 "$eq_geo_filename" fordisplacementenergy.out | head -n 1 | awk '{print $2}')
        displacement_energy=$(echo "$energy - $eq_geo_energy" | bc)
        echo $geo $mode $displacement $displacement_energy >> displacementenergy.out
done < fordisplacementenergy.out

grep -v "0.0" "displacementenergy.out" > "displacementenergy.out.temp"
mv "displacementenergy.out.temp" "displacementenergy.out"



