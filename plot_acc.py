import matplotlib.pyplot as plt

# Read data from file
data = []
input_file=input("What is your input file called?")

with open(input_file, 'r') as file:
    for line in file:
        fields = line.split()
        numbers = [float(x) for x in fields[:10]]
        label = fields[10]
        data.append((numbers, label))

# Prepare data for plotting
x = list(range(len(data)))
y = [d[0] for d in data]
labels = [d[1] for d in data]

# Create scatter plot
plt.scatter(x, y)

# Add labels to the x-axis
plt.xticks(x, labels, rotation='vertical')

plt.ylabel('Energy (eV)')

output_file=input("What do you want the plot to be called?")
plt.savefig(output_file)

