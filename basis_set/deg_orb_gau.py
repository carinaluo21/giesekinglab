deg_orb=int(input("How many degenerate orbitals are there?"))

if deg_orb >= 1:
	filename=input("What is your file name?")

	line_number = -1
	wavefunction_values_1 = []

	with open(filename, 'r') as file:
		for num, line in enumerate(file, start=1):
			fields = line.split()
			if len(fields) == 6:
				line_number = num
				break


	with open(filename, 'r') as file:
		for current_line, line in enumerate(file, start=1):
                	if current_line >= line_number:
                        	values = line.strip().split()
                        	wavefunction_value = [abs(float(value)) for value in values]
                        	wavefunction_values_1.extend(wavefunction_value)

if deg_orb >= 2:
        filename=input("What is your file name?")

        line_number = -1
        wavefunction_values_2 = []

        with open(filename, 'r') as file:
                for num, line in enumerate(file, start=1):
                        fields = line.split()
                        if len(fields) == 6:
                                line_number = num
                                break


        with open(filename, 'r') as file:
                for current_line, line in enumerate(file, start=1):
                        if current_line >= line_number:
                                values = line.strip().split()
                                wavefunction_value = [abs(float(value)) for value in values]
                                wavefunction_values_2.extend(wavefunction_value)

if deg_orb >= 3:
        filename=input("What is your file name?")

        line_number = -1
        wavefunction_values_3 = []

        with open(filename, 'r') as file:
                for num, line in enumerate(file, start=1):
                        fields = line.split()
                        if len(fields) == 6:
                                line_number = num
                                break


        with open(filename, 'r') as file:
                for current_line, line in enumerate(file, start=1):
                        if current_line >= line_number:
                                values = line.strip().split()
                                wavefunction_value = [abs(float(value)) for value in values]
                                wavefunction_values_3.extend(wavefunction_value)

if deg_orb == 3:
	wavefunction_values_combined = [wavefunction_values_1[i] + wavefunction_values_2[i] + wavefunction_values_3[i] for i in range(len(wavefunction_values_1))]
elif deg_orb == 2:
	wavefunction_values_combined = [wavefunction_values_1[i] + wavefunction_values_2[i] for i in range(len(wavefunction_values_1))]
else:
	print("Something is wrong")

output_file=input("What do you want the combined cube file to be called?")

with open(output_file, 'a') as file:
    line_count = 0
    for i, number in enumerate(wavefunction_values_combined, 1):
        file.write(str(number))
        file.write(' ')
        line_count += 1
        
        if line_count % 6 == 0 and (i % 200 != 0 or i == 200):
            file.write('\n')
        elif i % 200 == 0:
            file.write('\n')
            line_count = 0