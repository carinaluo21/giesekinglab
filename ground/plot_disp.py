import matplotlib.pyplot as plt

data = {}
with open("displacementenergy.out", "r") as file:
	for line in file:
		fields = line.strip().split()
		if len(fields) >= 4:
			geometry = str(fields[0])
			mode = int(fields[1])
			displacement = float(fields[2])
			displacement_energy = float(fields[3])
		
			key = (geometry, mode)
			if key in data:
				data[key].append((displacement, displacement_energy))	
			else:
				data[key] = [(displacement, displacement_energy)]

#Create a scatter plot
for key, value in data.items():
	x = [value[0] for value in data[key]]
	y = [value[1] for value in data[key]]
	plt.scatter(x, y, color="royalblue")
	plt.scatter(0,0, color="royalblue")
	plt.xlabel("Displacement (\u212B)", fontsize=18)
	plt.ylabel("Displacement Energy (eV)", fontsize=18)
	plt.xticks(fontsize=14)
	plt.yticks(fontsize=14)
	plt.savefig(f"{key[0]}_{key[1]}")
	plt.clf()
