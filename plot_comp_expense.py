import matplotlib.pyplot as plt

dx_values = []
dy_values = []

input_file=input("What is your input file called?")

with open('computationalexpense', 'r') as file:
    for line in file:
        fields = line.split()
        if fields[3] == "10" and fields[2] == "def2SVP":
            dx_values.extend([field.strip() for field in fields[1].split(',')])
            dy_values.extend([float(field.strip()) for field in fields[4].split(',')])

dy_values_sorted = sorted(dy_values, reverse=True)

plt.bar(dx_values, dy_values_sorted)
plt.xticks(rotation=30)
plt.xlabel("Method")
plt.ylabel("Time (minutes)")
plt.title("Computational Expense, 10 states/def2SVP")
plt.subplots_adjust(bottom=0.2)
plt.savefig("computationalexpense_10_def2SVP.png", dpi=500)
plt.close()

#Do the same thing for augccpvdzpp
x_values = []
y_values = []

with open('computationalexpense', 'r') as file:
    for line in file:
        fields = line.split()
        if fields[3] == "10" and fields[2] == "augccpvdzpp":
            x_values.extend([field.strip() for field in fields[1].split(',')])
            y_values.extend([float(field.strip()) for field in fields[4].split(',')])

y_values_sorted = sorted(y_values, reverse=True)

plt.bar(x_values, y_values_sorted)
plt.xticks(rotation=30)
plt.xlabel("Method")
plt.ylabel("Time (minutes)")
plt.title("Computational Expense, 10 states/augccpvdzpp")
plt.subplots_adjust(bottom=0.2)
plt.savefig("computationalexpense_10_augccpvdzpp.png", dpi=500)
plt.close()
#Plot the computationally efficient ones (EOM-CCSD, EOM-DLPNO-CCSD, STEOM-CCSD, STEOM-DLPNO-CCSD) (method is field 1) as a function of number of excited states (field 3)
# Open the file and read the lines
with open('computationalexpense', 'r') as f:
    lines = f.readlines()

# Create empty lists for x and y values
eom_ccsd_x = []
eom_ccsd_y = []
eom_dlpno_ccsd_x = []
eom_dlpno_ccsd_y = []
steom_ccsd_x = []
steom_ccsd_y = []
steom_dlpno_ccsd_x = []
steom_dlpno_ccsd_y = []
# Loop over the lines and extract the values
for line in lines:
    fields = line.split()
    if fields[1] == 'EOM-CCSD' and fields[2] == "def2SVP":
        eom_ccsd_x.append(int(fields[3]))
        eom_ccsd_y.append(float(fields[4]))
    elif fields[1] == 'EOM-DLPNO-CCSD' and fields[2] == "def2SVP":
        eom_dlpno_ccsd_x.append(int(fields[3]))
        eom_dlpno_ccsd_y.append(float(fields[4]))
    elif fields[1] == 'STEOM-CCSD' and fields[2] == "def2SVP":
        steom_ccsd_x.append(int(fields[3]))
        steom_ccsd_y.append(float(fields[4]))
    elif fields[1] == 'STEOM-DLPNO-CCSD' and fields[2] == "def2SVP":
        steom_dlpno_ccsd_x.append(int(fields[3]))
        steom_dlpno_ccsd_y.append(float(fields[4]))
eom_ccsd_x = [x - 0.2 for x in eom_ccsd_x]
eom_dlpno_ccsd_x = [x - 0.1 for x in eom_dlpno_ccsd_x]
steom_dlpno_ccsd_x = [x + 0.1 for x in steom_dlpno_ccsd_x]
steom_ccsd_x = [x + 0.2 for x in steom_ccsd_x]
#eom_dlpno_ccsd_x = [x + 0.1 for x in eom_ccsd_x]
#steom_ccsd_x = [x + 0.3 for x in eom_ccsd_x]
#steom_dlpno_ccsd_x = [x + 0.2 for x in eom_ccsd_x]
#print(eom_ccsd_x)
#print(eom_dlpno_ccsd_x)
# Create the bar chart with different colors for EOM-CCSD and EOM-DLPNO-CCSD
fig, ax = plt.subplots()
ax.bar(eom_ccsd_x, eom_ccsd_y, color='blue', label='EOM-CCSD')
ax.bar(eom_dlpno_ccsd_x, eom_dlpno_ccsd_y, color='green', label='EOM-DLPNO-CCSD')
ax.bar(steom_dlpno_ccsd_x, steom_dlpno_ccsd_y, color='orange', label='STEOM-DLPNO-CCSD')
ax.bar(steom_ccsd_x, steom_ccsd_y, color='red', label='STEOM-CCSD')
# Set the chart title and axis labels
ax.set_title('Computational Expense def2SVP')
ax.set_xlabel('Number of Excited States')
ax.set_ylabel('Time (minutes)')

# Add a legend and show the chart
ax.legend()
plt.savefig("computationalexpense_def2SVP", dpi=500)
plt.show()

