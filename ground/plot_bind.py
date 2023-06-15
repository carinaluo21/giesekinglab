#Import package for plotting
import matplotlib.pyplot as plt

#Initialize the lists
number_of_atoms_neutral = []
binding_energy_neutral = []

number_of_atoms_positive = []
binding_energy_positive = []

number_of_atoms_negative = []
binding_energy_negative = []

#Open each file, read in each line and store it in the appropriate list
with open("bindingenergy_neutralclusters.out", "r") as file:
	for line in file:
		fields = line.strip().split()
		if len(fields) >= 2:
			number_of_atoms_neutral.append(int(fields[0]))
			binding_energy_neutral.append(float(fields[1]))

with open("bindingenergy_positiveclusters.out", "r") as file:
	for line in file:
		fields = line.strip().split()
		if len(fields) >= 2:
			number_of_atoms_positive.append(int(fields[0]))
			binding_energy_positive.append(float(fields[1]))

with open("bindingenergy_negativeclusters.out", "r") as file:
	for line in file:
		fields = line.strip().split()
		if len(fields) >= 2:
			number_of_atoms_negative.append(int(fields[0]))
			binding_energy_negative.append(float(fields[1]))
#Sort the data
#sorted_data_neutral = sorted(zip(number_of_atoms_neutral, binding_energy_neutral))
#sorted_data_positive = sorted(zip(number_of_atoms_positive, binding_energy_positive))
#sorted_data_negative = sorted(zip(number_of_atoms_negative, binding_energy_negative))

#Extract the sorted x and y values
#x_neutral, y_neutral = zip(*sorted_data_neutral)
#x_positive, y_positive = zip(*sorted_data_positive)
#x_negative, y_negative = zip(*sorted_data_negative)

#Create a figure with subplots
fig, (ax1, ax2, ax3) = plt.subplots(1, 3)

#Create scatter plots on each subplot
ax1.scatter(number_of_atoms_positive, binding_energy_positive)
ax1.set_ylabel("Binding Energy (eV)")
ax1.set_title("Cationic Clusters")
ax1.set_xticks(range(min(number_of_atoms_positive), max(number_of_atoms_positive)+1, 1))

ax2.scatter(number_of_atoms_neutral, binding_energy_neutral)
ax2.set_xlabel("Number of Atoms")
ax2.set_title("Neutral Clusters")
ax2.set_xticks(range(min(number_of_atoms_positive), max(number_of_atoms_positive)+1, 1))

ax3.scatter(number_of_atoms_negative, binding_energy_negative)
ax3.set_title("Anionic Clusters")
ax3.set_xticks(range(min(number_of_atoms_positive), max(number_of_atoms_positive)+1, 1))

#Save the figure
plt.savefig("bindingenergy.png")
