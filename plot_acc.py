import matplotlib.pyplot as plt

# Read data from file
data = []
input_file=input("What is your input file called?")

with open(input_file, 'r') as file:
    for line in file:
        fields = line.split()
        numbers = [float(x) for x in fields[:10]]
        label = fields[10]
        for number in numbers:
            data.append((number, label))

print(data)
#x = list(range(len(data)))
#y = [d[0] for d in data]
#labels = [d[1] for d in data]

#plt.scatter(x, y)

#plt.xticks(x, labels, rotation='vertical')

#plt.ylabel('Energy (eV)')

#output_file=input("What do you want the plot to be called?")
#plt.savefig(output_file)

