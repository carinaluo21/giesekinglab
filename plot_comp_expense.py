import matplotlib.pyplot as plt

data = []

input_file=input("What is your input file called?")
basis_set=input("What basis set would you like to use?")
with open(input_file, 'r') as file:
    for line in file:
        fields = line.split()
        if fields[4] == "no" and fields[3] == "10" and fields[2] == basis_set:
            data.append([fields[1], float(fields[5])])

sorted_data = sorted(data, key=lambda x: x[1], reverse=True)

x_values = [item[0] for item in sorted_data]
y_values = [item[1] for item in sorted_data]

plt.figure(figsize=(10, 6))
plt.bar(x_values, y_values)

plt.ylabel('Minutes', fontsize=18)
plt.xticks(rotation=20, fontsize=14)
plt.yticks(fontsize=14)
output_file=input("What would you like the plot to be called?")
plt.savefig(output_file)
plt.show()
