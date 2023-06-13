import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

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


fig, ax = plt.subplots()
for number, label in data:
    x_value = label_dict[label]
    rect = Rectangle((x_value - 0.3 / 2, number - 0.6 / 2), 0.3, 0.6, edgecolor='black')
    ax.add_patch(rect)

plt.xticks(list(label_dict.values()), list(label_dict.keys()), rotation=90)

plt.xlabel('Label')
plt.ylabel('Value')

output_file=input("What would you like the plot to be called?")
plt.savefig(output_file)
plt.show()

