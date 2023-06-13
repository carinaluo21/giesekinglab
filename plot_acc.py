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

labels = set(label for _, label in data)

# Assign numeric values to labels
label_dict = {label: i + 1 for i, label in enumerate(labels)}

# Generate categorical scatter plot
for number, label in data:
    x_value = label_dict[label]
    plt.scatter(x_value, number)

# Set x-axis tick labels
plt.xticks(list(label_dict.values()), list(label_dict.keys()))

plt.xlabel('Label')
plt.ylabel('Value')
plt.show()

