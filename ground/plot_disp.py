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
	plt.title(f"{key[0]} vibrational mode {key[1]}")
	plt.xlabel("Displacement (\u212B)")
	plt.ylabel("Displacement Energy (eV)")
	plt.savefig(f"{key[0]}_{key[1]}")
	plt.clf()
