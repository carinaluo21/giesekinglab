import matplotlib.pyplot as plt

data_file = input("What is the file containing the relative isomeric energy called?") 
pos_atom_num = []
pos_isom_energy = []
neutral_atom_num = []
neutral_isom_energy = []
neg_atom_num = []
neg_isom_energy = []

with open(data_file, 'r') as file:
    for line in file:
        line = line.strip().split()
        atom_num = int(line[0])
        charge = line[1]
        isom_energy = float(line[2])
        if charge == "1":
            pos_atom_num.append(atom_num)
            pos_isom_energy.append(isom_energy)
        elif charge == "0":
            neutral_atom_num.append(atom_num)
            neutral_isom_energy.append(isom_energy)
        elif charge == "-":
            neg_atom_num.append(atom_num)
            neg_isom_energy.append(isom_energy)
        else:
            print("Error")

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 4))

# Plot data in the first subplot
ax1.scatter(neg_atom_num, neg_isom_energy, color="red", label="Anionic")
ax1.set_xlabel('Atoms')
ax1.set_ylabel('Relative Energy of Structural Isomers (eV)')
ax1.legend()

# Plot data in the second subplot
ax2.scatter(neutral_atom_num, neutral_isom_energy, color="blue", label="Neutral")
ax2.set_xlabel('Atoms')
ax2.set_ylabel('Relative Energy of Structural Isomers (eV)')
ax2.legend()

# Plot data in the third subplot
ax3.scatter(pos_atom_num, pos_isom_energy, color="green", label="Cationic")
ax3.set_xlabel('Atoms')
ax3.set_ylabel('Relative Energy of Structural Isomers (eV)')
ax3.legend()

# Save the plot
output_file = input("What is the name of the file you would like to save the plot to?")
plt.savefig(output_file)
