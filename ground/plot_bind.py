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

#Create a figure with subplots
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(25,15))

#Create scatter plots on each subplot
ax3.scatter(number_of_atoms_positive, binding_energy_positive)
ax3.set_title("Cationic", fontsize=40)
ax3.set_xticks(range(min(number_of_atoms_positive), max(number_of_atoms_positive)+1, 1))

ax2.scatter(number_of_atoms_neutral, binding_energy_neutral)
ax2.set_xlabel("Number of Atoms", fontsize=40)
ax2.set_title("Neutral", fontsize=40)
ax2.set_xticks(range(min(number_of_atoms_positive), max(number_of_atoms_positive)+1, 1))

ax1.scatter(number_of_atoms_negative, binding_energy_negative)
ax1.set_ylabel("Binding Energy (eV)", fontsize=40)
ax1.set_title("Anionic", fontsize=40)
ax1.set_xticks(range(min(number_of_atoms_positive), max(number_of_atoms_positive)+1, 1))

ax1.set_xticklabels(ax1.get_xticks(), fontsize=25)
ax2.set_xticklabels(ax2.get_xticks(), fontsize=25)
ax3.set_xticklabels(ax3.get_xticks(), fontsize=25)

ax1.set_yticklabels(ax1.get_yticks(), fontsize=25)
ax2.set_yticklabels(ax2.get_yticks(), fontsize=25)
ax3.set_yticklabels(ax3.get_yticks(), fontsize=25)

ax1.text(0, 1.05, '(a)', transform=ax1.transAxes, fontsize=40, fontweight='normal', va='top')
ax2.text(0, 1.05, '(b)', transform=ax2.transAxes, fontsize=40, fontweight='normal', va='top')
ax3.text(0, 1.05, '(c)', transform=ax3.transAxes, fontsize=40, fontweight='normal', va='top')

plt.subplots_adjust(left=0.10, right=0.95, bottom=0.1, top=0.9)
plt.savefig("bindingenergy.png", dpi=200)
plt.show()
