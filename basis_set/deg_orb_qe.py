import math

deg_orb=int(input("How many degenerate orbitals are there?"))
prefix=str(input("What is your prefix?"))
	
if deg_orb >= 1:
	orbital1=str(input("Your first orbital is"))
	filename1=prefix + orbital1 + ".cub"
	print(filename1)

	line_number = -1
	wavefunction_values_1 = []

	with open(filename1, 'r') as file:
		for num, line in enumerate(file, start=1):
			fields = line.split()
			if len(fields) == 6:
				line_number = num
				break
	with open(filename1, 'r') as file:
		for current_line, line in enumerate(file, start=1):
			if current_line >= line_number:
				values = line.strip().split()
				#wavefunction_value = [math.sqrt(abs(float(value))) * (-1 if float(value) < 0 else 1) for value in values]
				wavefunction_value = [math.sqrt(abs(float(value))) for value in values]
				wavefunction_values_1.extend(wavefunction_value)

if deg_orb >= 2:
	orbital2=str(input("Your second orbital is"))
	filename2=prefix + orbital2 + ".cub"
	print(filename2)
	
	line_number = -1
	wavefunction_values_2 = []
	with open(filename2, 'r') as file:
		for num, line in enumerate(file, start=1):
			fields = line.split()
			if len(fields) == 6:
				line_number = num
				break

	with open(filename2, 'r') as file:
		for current_line, line in enumerate(file, start=1):
			if current_line >= line_number:
				values = line.strip().split()
				#wavefunction_value = [math.sqrt(abs(float(value))) * (-1 if float(value) < 0 else 1) for value in values]
				wavefunction_value = [math.sqrt(abs(float(value))) for value in values]
				wavefunction_values_2.extend(wavefunction_value)

if deg_orb >= 3:
	orbital3=str(input("Your third orbital is"))
	filename3=prefix + orbital3 + ".cub"
	print(filename3)
	
	line_number = -1
	wavefunction_values_3 = []

	with open(filename3, 'r') as file:
		for num, line in enumerate(file, start=1):
			fields = line.split()
			if len(fields) == 6:
				line_number = num
				break

	with open(filename3, 'r') as file:
		for current_line, line in enumerate(file, start=1):
			if current_line >= line_number:
				values = line.strip().split()
				#wavefunction_value = [math.sqrt(abs(float(value))) * (-1 if float(value) < 0 else 1) for value in values]
				wavefunction_value = [math.sqrt(abs(float(value))) for value in values]
				wavefunction_values_3.extend(wavefunction_value)

if deg_orb == 3:
	wavefunction_values_combined = [(wavefunction_values_1[i] + wavefunction_values_2[i] + wavefunction_values_3[i])**2 for i in range(len(wavefunction_values_1))]
elif deg_orb == 2:
	wavefunction_values_combined = [(wavefunction_values_1[i] + wavefunction_values_2[i])**2 for i in range(len(wavefunction_values_1))]
else:
	print("There is an error.")

result_file=str(input("What file do you want to write the combined wavefunction values to?"))

with open(result_file, 'a') as file:
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
