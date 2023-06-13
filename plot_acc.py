import matplotlib.pyplot as plt

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

ax = plt.subplot(1,1,1)
v_val=1
h_val=3
verts = list(zip([-h_val,h_val,h_val,-h_val],[-v_val,-v_val,v_val,v_val]))
for number, label in data:
    x_value = label_dict[label]
    plt.scatter(x_value, number, marker=verts, s=300)

plt.xticks(list(label_dict.values()), list(label_dict.keys()), rotation=90)

plt.xlabel('Label')
plt.ylabel('Value')

output_file=input("What would you like the plot to be called?")
plt.savefig(output_file)
plt.show()

