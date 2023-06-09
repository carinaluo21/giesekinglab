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

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 5))

# Plot data in the first subplot
ax1.scatter(neg_atom_num, neg_isom_energy, label="Anionic")
ax1.set_ylabel('Relative Isomeric Energy (eV)', fontsize=18)
ax1.set_xticks(range(min(neg_atom_num), max(neg_atom_num) + 1))
ax1.set_title("Anionic", fontsize=18)
ax1.text(0, 1.08, '(a)', transform=ax1.transAxes, fontsize=18, fontweight='normal', va='top')

# Plot data in the second subplot
ax2.scatter(neutral_atom_num, neutral_isom_energy, label="Neutral")
ax2.set_xlabel('Number of Atoms', fontsize=18)
ax2.set_xticks(range(min(neutral_atom_num), max(neutral_atom_num) + 1))
ax2.set_title("Neutral", fontsize=18)
ax2.text(0, 1.08, '(b)', transform=ax2.transAxes, fontsize=18, fontweight='normal', va='top')

# Plot data in the third subplot
ax3.scatter(pos_atom_num, pos_isom_energy, label="Cationic")
ax3.set_xlabel('Atoms')
ax3.set_xticks(range(min(pos_atom_num), max(pos_atom_num) + 1))
ax3.set_title("Cationic", fontsize=18)
ax3.text(0, 1.08, '(c)', transform=ax3.transAxes, fontsize=18, fontweight='normal', va='top')

# Save the plot
output_file = input("What is the name of the file you would like to save the plot to?")
plt.savefig(output_file)
