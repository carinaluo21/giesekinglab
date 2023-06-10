import matplotlib.pyplot as plt

data_file = input("What is the file containing the relative isomeric energy called?") 
atom_num = []
isom_energy = []

with open(data_file, 'r') as file:
    for line in file:
        line = line.strip().split()
        atom_num.append(float(line[0]))
        isom_energy.append(float(line[1]))

# Create scatter plot
plt.scatter(atom_num, isom_energy)

# Set plot labels
plt.xlabel('Atoms')
plt.ylabel('Relative Isomeric Energy (eV)')

# Save the plot
output_file = input("What is the name of the file you would like to save the plot to?")
plt.savefig(output_file)
