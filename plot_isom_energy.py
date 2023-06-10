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
        atom_num = line[0]
        charge = line[1]
        isom_energy = line[2]
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
            echo "error"

# Create scatter plot
plt.scatter(pos_atom_num, pos_isom_energy, color="red", label="cationic")
plt.scatter(neg_atom_num, neg_isom_energy, color="blue", label="anionic")
plt.scatter(neutral_atom_num, neutral_isom_energy, color="green", label="neutral")
plt.xlabel('Atoms')
plt.ylabel('Relative Isomeric Energy (eV)')
plt.legend()

# Save the plot
output_file = input("What is the name of the file you would like to save the plot to?")
plt.savefig(output_file)
