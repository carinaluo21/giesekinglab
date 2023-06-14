#!/usr/bin/python

#Import the needed modules
import time
#Start keeping track of the computation time
start_time = time.time()
import math
import matplotlib.pyplot as plt
from collections import defaultdict
import numpy as np

#Get the molecule name from the name of the cube file
cubefilename = input("What is your Gaussian cube file name?")
wheretostop = cubefilename.index("_")
moleculename = cubefilename[:wheretostop]

#Start reading the cube file line by line
line = open(cubefilename).readlines()

#Ignore the first two lines, which are headers.
#Read in the data from the third line, which contains the number of atoms included in the file followed by the position of the origin of the volumetric data.
numberofatoms = abs(line[2].split()[0])
originx = float(line[2].split()[1])
originy = float(line[2].split()[2])
originz = float(line[2].split()[3])

#Read in data from the next three lines, which contain the number of voxels along each axis, followed by the axis vector#Since the sign of the number of voxels is positive, the units are bohr.
#Add 1 to each of the voxels because they will be used iteratively in range function to generate indexes for each of the volumetric elements.
x_voxels = int(line[3].split()[0]) + 1
y_voxels = int(line[4].split()[0]) + 1
z_voxels = int(line[5].split()[0]) + 1

unit_vector_length = line[3].split()[1]
#yvector = line[4].split()[2]
#zvector = line[5].split()[3]

#Read in data from the last section of the header, which contains one line for each atom.
if int(numberofatoms) >= 1:
	exec('GaussianAg1_xcoordinate, GaussianAg1_ycoordinate, GaussianAg1_zcoordinate = float(line[6].split()[2]), float(line[6].split()[3]), float(line[6].split()[4])')

if int(numberofatoms) >= 2:
	exec('GaussianAg2_xcoordinate, GaussianAg2_ycoordinate, GaussianAg2_zcoordinate = float(line[7].split()[2]), float(line[7].split()[3]), float(line[7].split()[4])')

if int(numberofatoms) >= 3:
        exec('GaussianAg3_xcoordinate, GaussianAg3_ycoordinate, GaussianAg3_zcoordinate = float(line[8].split()[2]), float(line[8].split()[3]), float(line[8].split()[4])')

if int(numberofatoms) >= 4:
        exec('GaussianAg4_xcoordinate, GaussianAg4_ycoordinate, GaussianAg4_zcoordinate = float(line[9].split()[2]), float(line[9].split()[3]), float(line[9].split()[4])')

if int(numberofatoms) >= 5:
        exec('GaussianAg5_xcoordinate, GaussianAg5_ycoordinate, GaussianAg5_zcoordinate = float(line[10].split()[2]), float(line[10].split()[3]), float(line[10].split()[4])')

if int(numberofatoms) >= 6:
        exec('GaussianAg6_xcoordinate, GaussianAg6_ycoordinate, GaussianAg6_zcoordinate = float(line[11].split()[2]), float(line[11].split()[3]), float(line[11].split()[4])')

if int(numberofatoms) >= 7:
        exec('GaussianAg7_xcoordinate, GaussianAg7_ycoordinate, GaussianAg7_zcoordinate = float(line[12].split()[2]), float(line[12].split()[3]), float(line[12].split()[4])')

if int(numberofatoms) >= 8:
        exec('GaussianAg8_xcoordinate, GaussianAg8_ycoordinate, GaussianAg8_zcoordinate = float(line[13].split()[2]), float(line[13].split()[3]), float(line[13].split()[4])')

#Get the volumetric data.
with open(cubefilename, "r") as f:
    line_num = 1
    for line in f:
        num_columns = len(line.split())
        if num_columns == 6:
            sixcolumnnumber = line_num - 1
            break
        line_num += 1

with open(cubefilename) as f, open("volumetric_data", "w") as out:
	lines=f.readlines()
	for number, line in enumerate(lines):
		if number >= sixcolumnnumber:
			out.write(line)	

f.close()

volumetric_data_list = []
with open("volumetric_data", "r") as infile:
	for line in infile.readlines():
		for string in line.split(' '):
			volumetric_data_list.append(string)

infile.close()

volumetric_data_withoutemptystrings_1 = [i.replace('\n', '') for i in volumetric_data_list]
volumetric_data_withoutemptystrings = [i for i in volumetric_data_withoutemptystrings_1 if i]
#print(volumetric_data_withoutemptystrings)

#Convert the list of strings to a list of integers.
volumetric_data_list = []
for entry in volumetric_data_withoutemptystrings:
    volumetric_data_list.append(float(entry))

#Create the indexes.
list_of_xvalues = []
list_of_yvalues = []
list_of_zvalues = []
xyz_coordinates = []
x = 0
for x in range(0, x_voxels-1):
        y = 0
        for y in range(0, y_voxels-1):
                z = 0
                for z in range(0, z_voxels-1):
                        xentry = originx + x*float(unit_vector_length)
                        yentry = originy + y*float(unit_vector_length)
                        zentry = originz + z*float(unit_vector_length)
                        list_of_xvalues.append(xentry)
                        list_of_yvalues.append(yentry)
                        list_of_zvalues.append(zentry)
                        xyz_coordinates.append((xentry, yentry, zentry))
                        z += 1
                y += 1
        x += 1


#zlist = [(list_of_zvalues[i], (volumetric_data_list[i])**2) for i in range(0, len(list_of_zvalues))]
zlist = [(list_of_zvalues[i], abs(volumetric_data_list[i])) for i in range(0, len(list_of_zvalues))]

tupz = {i:0 for i, v in zlist}
for key, value in zlist:
	tupz[key] = tupz[key]+value

gaussianzvalue = list(tupz.keys())
gaussianzvolume = list(tupz.values())

#ylist = [(list_of_yvalues[i], (volumetric_data_list[i])**2) for i in range(0, len(list_of_yvalues))]
ylist = [(list_of_yvalues[i], abs(volumetric_data_list[i])) for i in range(0, len(list_of_yvalues))]

tupy = {i:0 for i, v in ylist}
for key, value in ylist:
        tupy[key] = tupy[key]+value

gaussianyvalue = list(tupy.keys())
gaussianyvolume = list(tupy.values())

#xlist = [(list_of_xvalues[i], (volumetric_data_list[i])**2) for i in range(0, len(list_of_xvalues))]
xlist = [(list_of_xvalues[i], abs(volumetric_data_list[i])) for i in range(0, len(list_of_xvalues))]

tupx = {i:0 for i, v in xlist}
for key, value in xlist:
        tupx[key] = tupx[key]+value

gaussianxvalue = list(tupx.keys())
gaussianxvolume = list(tupx.values())











cubefilename = input("What is your Quantum Espresso cube file name?")
wheretostop = cubefilename.index("_")
moleculename = cubefilename[:wheretostop]
line = open(cubefilename).readlines()

#Ignore the first two lines, which are headers.
#Read in the data from the third line, which contains the number of atoms included in the file followed by the position of the origin of the volumetric data.
numberofatoms = line[2].split()[0]
originx = float(line[2].split()[1])
originy = float(line[2].split()[2])
originz = float(line[2].split()[3])

#Read in data from the next three lines, which contain the number of voxels along each axis, followed by the axis vector#Since the sign of the number of voxels is positive, the units are bohr.
#Add 1 to each of the voxels because they will be used iteratively in range function to generate indexes for each of the volumetric elements.
x_voxels = int(line[3].split()[0]) + 1
y_voxels = int(line[4].split()[0]) + 1
z_voxels = int(line[5].split()[0]) + 1

unit_vector_length = line[3].split()[1]
#yvector = line[4].split()[2]
#zvector = line[5].split()[3]

#Read in data from the last section of the header, which contains one line for each atom.
if int(numberofatoms) >= 1:
        exec('QuantumEspressoAg1_xcoordinate, QuantumEspressoAg1_ycoordinate, QuantumEspressoAg1_zcoordinate = float(line[6].split()[2]), float(line[6].split()[3]), float(line[6].split()[4])')

if int(numberofatoms) >= 2:
        exec('QuantumEspressoAg2_xcoordinate, QuantumEspressoAg2_ycoordinate, QuantumEspressoAg2_zcoordinate = float(line[7].split()[2]), float(line[7].split()[3]), float(line[7].split()[4])')

if int(numberofatoms) >= 3:
        exec('QuantumEspressoAg3_xcoordinate, QuantumEspressoAg3_ycoordinate, QuantumEspressoAg3_zcoordinate = float(line[8].split()[2]), float(line[8].split()[3]), float(line[8].split()[4])')

if int(numberofatoms) >= 4:
        exec('QuantumEspressoAg4_xcoordinate, QuantumEspressoAg4_ycoordinate, QuantumEspressoAg4_zcoordinate = float(line[9].split()[2]), float(line[9].split()[3]), float(line[9].split()[4])')

if int(numberofatoms) >= 5:
        exec('QuantumEspressoAg5_xcoordinate, QuantumEspressoAg5_ycoordinate, QuantumEspressoAg5_zcoordinate = float(line[10].split()[2]), float(line[10].split()[3]), float(line[10].split()[4])')

if int(numberofatoms) >= 6:
        exec('QuantumEspressoAg6_xcoordinate, QuantumEspressoAg6_ycoordinate, QuantumEspressoAg6_zcoordinate = float(line[11].split()[2]), float(line[11].split()[3]), float(line[11].split()[4])')

if int(numberofatoms) >= 7:
        exec('QuantumEspressoAg7_xcoordinate, QuantumEspressoAg7_ycoordinate, QuantumEspressoAg7_zcoordinate = float(line[12].split()[2]), float(line[12].split()[3]), float(line[12].split()[4])')

if int(numberofatoms) >= 8:
        exec('QuantumEspressoAg8_xcoordinate, QuantumEspressoAg8_ycoordinate, QuantumEspressoAg8_zcoordinate = float(line[13].split()[2]), float(line[13].split()[3]), float(line[13].split()[4])')

#Get the volumetric data.
with open(cubefilename, "r") as f:
    line_num = 1
    for line in f:
        num_columns = len(line.split())
        if num_columns == 6:
            sixcolumnnumber = line_num - 1
            break
        line_num += 1

with open(cubefilename) as f, open("volumetric_data", "w") as out:
        lines=f.readlines()
        for number, line in enumerate(lines):
                if number >= sixcolumnnumber:
                        out.write(line)

f.close()

volumetric_data_list = []
with open("volumetric_data", "r") as infile:
        for line in infile.readlines():
                for string in line.split(' '):
                        volumetric_data_list.append(string)

infile.close()

volumetric_data_withoutemptystrings_1 = [i.replace('\n', '') for i in volumetric_data_list]
volumetric_data_withoutemptystrings = [i for i in volumetric_data_withoutemptystrings_1 if i]

#Convert the list of strings to a list of integers.
volumetric_data_list = []
for entry in volumetric_data_withoutemptystrings:
    volumetric_data_list.append(float(entry))

#Create the indexes.
first_list_of_xvalues = []
first_list_of_yvalues = []
first_list_of_zvalues = []
x = 0
for x in range(0, x_voxels-1):
        y = 0
        for y in range(0, y_voxels-1):
                z = 0
                for z in range(0, z_voxels-1):
                        xentry = originx + x*float(unit_vector_length)
                        yentry = originy + y*float(unit_vector_length)
                        zentry = originz + z*float(unit_vector_length)
                        first_list_of_xvalues.append(xentry)
                        first_list_of_yvalues.append(yentry)
                        first_list_of_zvalues.append(zentry)
                        z += 1
                y += 1
        x += 1

zmax = max(first_list_of_zvalues)
subtractme = zmax / 2
list_of_zvalues=[]
for num in first_list_of_zvalues:
        list_of_zvalues.append(num - subtractme)

QEAg1_zcoordinate=QuantumEspressoAg1_zcoordinate-subtractme
QEAg2_zcoordinate=QuantumEspressoAg2_zcoordinate-subtractme
if int(numberofatoms) >= 3:
        exec('QEAg3_zcoordinate=QuantumEspressoAg3_zcoordinate-subtractme')
if int(numberofatoms) >= 4:
        exec('QEAg4_zcoordinate=QuantumEspressoAg4_zcoordinate-subtractme')
if int(numberofatoms) >= 5:
        exec('QEAg5_zcoordinate=QuantumEspressoAg5_zcoordinate-subtractme')
if int(numberofatoms) >= 6:
        exec('QEAg6_zcoordinate=QuantumEspressoAg6_zcoordinate-subtractme')
if int(numberofatoms) >= 7:
        exec('QEAg7_zcoordinate=QuantumEspressoAg7_zcoordinate-subtractme')
if int(numberofatoms) >= 8:
        exec('QEAg8_zcoordinate=QuantumEspressoAg8_zcoordinate-subtractme')

ymax = max(first_list_of_yvalues)
subtractme = ymax / 2
list_of_yvalues=[]
for num in first_list_of_yvalues:
        list_of_yvalues.append(num - subtractme)

QEAg1_ycoordinate=QuantumEspressoAg1_ycoordinate-subtractme
QEAg2_ycoordinate=QuantumEspressoAg2_ycoordinate-subtractme
if int(numberofatoms) >= 3:
        exec('QEAg3_ycoordinate=QuantumEspressoAg3_ycoordinate-subtractme')
if int(numberofatoms) >= 4:
        exec('QEAg4_ycoordinate=QuantumEspressoAg4_ycoordinate-subtractme')
if int(numberofatoms) >= 5:
        exec('QEAg5_ycoordinate=QuantumEspressoAg5_ycoordinate-subtractme')
if int(numberofatoms) >= 6:
        exec('QEAg6_ycoordinate=QuantumEspressoAg6_ycoordinate-subtractme')
if int(numberofatoms) >= 7:
        exec('QEAg7_ycoordinate=QuantumEspressoAg7_ycoordinate-subtractme')
if int(numberofatoms) >= 8:
        exec('QEAg8_ycoordinate=QuantumEspressoAg8_ycoordinate-subtractme')

xmax = max(first_list_of_xvalues)
subtractme = xmax / 2
list_of_xvalues=[]
for num in first_list_of_xvalues:
        list_of_xvalues.append(num - subtractme)

QEAg1_xcoordinate=QuantumEspressoAg1_xcoordinate-subtractme
QEAg2_xcoordinate=QuantumEspressoAg2_xcoordinate-subtractme
if int(numberofatoms) >= 3:
        exec('QEAg3_xcoordinate=QuantumEspressoAg3_xcoordinate-subtractme')
if int(numberofatoms) >= 4:
        exec('QEAg4_xcoordinate=QuantumEspressoAg4_xcoordinate-subtractme')
if int(numberofatoms) >= 5:
        exec('QEAg5_xcoordinate=QuantumEspressoAg5_xcoordinate-subtractme')
if int(numberofatoms) >= 6:
        exec('QEAg6_xcoordinate=QuantumEspressoAg6_xcoordinate-subtractme')
if int(numberofatoms) >= 7:
        exec('QEAg7_xcoordinate=QuantumEspressoAg7_xcoordinate-subtractme')
if int(numberofatoms) >= 8:
        exec('QEAg8_xcoordinate=QuantumEspressoAg8_xcoordinate-subtractme')

zlist = [(list_of_zvalues[i], math.sqrt(abs(volumetric_data_list[i]))) for i in range(0, len(first_list_of_zvalues))]

tupz = {i:0 for i, v in zlist}
for key, value in zlist:
        tupz[key] = tupz[key]+value

quantumespressozvalue = list(tupz.keys())
quantumespressozvolume = list(tupz.values())

ylist = [(list_of_yvalues[i], math.sqrt(abs(volumetric_data_list[i]))) for i in range(0, len(first_list_of_yvalues))]

tupy = {i:0 for i, v in ylist}
for key, value in ylist:
        tupy[key] = tupy[key]+value

quantumespressoyvalue = list(tupy.keys())
quantumespressoyvolume = list(tupy.values())

xlist = [(list_of_xvalues[i], math.sqrt(abs(volumetric_data_list[i]))) for i in range(0, len(first_list_of_xvalues))]

tupx = {i:0 for i, v in xlist}
for key, value in xlist:
        tupx[key] = tupx[key]+value

quantumespressoxvalue = list(tupx.keys())
quantumespressoxvolume = list(tupx.values())

plt.figure(figsize=(8,8), dpi=80)

areagaussianz = np.trapz(gaussianzvolume, gaussianzvalue)
gaussianzvolumenormalized=[i/areagaussianz for i in gaussianzvolume]
plt.scatter(gaussianzvalue, gaussianzvolumenormalized, color="red")

areaquantumespressoz = np.trapz(quantumespressozvolume, quantumespressozvalue)
quantumespressozvolumenormalized=[i/areaquantumespressoz for i in quantumespressozvolume]
plt.scatter(quantumespressozvalue, quantumespressozvolumenormalized, color="blue")

plt.axvline(x=GaussianAg1_zcoordinate, label="Gaussian", color="red")
plt.axvline(x=GaussianAg2_zcoordinate, color="red")
if int(numberofatoms) >= 3:
        exec('plt.axvline(x=GaussianAg3_zcoordinate, color="red")')
if int(numberofatoms) >= 4:
        exec('plt.axvline(x=GaussianAg4_zcoordinate, color="red")')
if int(numberofatoms) >= 5:
        exec('plt.axvline(x=GaussianAg5_zcoordinate, color="red")')
if int(numberofatoms) >= 6:
	exec('plt.axvline(x=GaussianAg6_zcoordinate, color="red")')
if int(numberofatoms) >= 7:
	exec('plt.axvline(x=GaussianAg7_zcoordinate, color="red")')
if int(numberofatoms) >= 8:
	exec('plt.axvline(x=GaussianAg8_zcoordinate, color="red")')

plt.axvline(x=QEAg1_zcoordinate, label="Quantum Espresso", color="blue")
plt.axvline(x=QEAg2_zcoordinate, color="blue")
if int(numberofatoms) >= 3:
	exec('plt.axvline(x=QEAg3_zcoordinate, color="blue")')
if int(numberofatoms) >= 4:
	exec('plt.axvline(x=QEAg4_zcoordinate, color="blue")')
if int(numberofatoms) >= 5:
	exec('plt.axvline(x=QEAg5_zcoordinate, color="blue")')
if int(numberofatoms) >= 6:
	exec('plt.axvline(x=QEAg6_zcoordinate, color="blue")')
if int(numberofatoms) >= 7:
	exec('plt.axvline(x=QEAg7_zcoordinate, color="blue")')
if int(numberofatoms) >= 8:
	exec('plt.axvline(x=QEAg8_zcoordinate, color="blue")')

orbitalname=input("What is your orbital name? E.g. LUMO? HOMO? LUMO+1? etc")

plt.xlim(-10, 10)
plt.xlabel("z axis (Bohr)", fontsize=18)
plt.ylabel("Electrons/Bohr", fontsize=18)
#plt.title(orbitalname + " of " + moleculename)
plt.legend(fontsize=18, loc="lower left")
plt.savefig(moleculename + "_" + orbitalname + "_z.png")
plt.close()








plt.figure(figsize=(8,8), dpi=80)
areagaussiany = np.trapz(gaussianyvolume, gaussianyvalue)
gaussianyvolumenormalized=[i/areagaussiany for i in gaussianyvolume]
plt.scatter(gaussianyvalue, gaussianyvolumenormalized, color="red")

areaquantumespressoy = np.trapz(quantumespressoyvolume, quantumespressoyvalue)
quantumespressoyvolumenormalized=[i/areaquantumespressoy for i in quantumespressoyvolume]
plt.scatter(quantumespressoyvalue, quantumespressoyvolumenormalized, color="blue")

plt.axvline(x=GaussianAg1_ycoordinate, label="Gaussian", color="red")
plt.axvline(x=GaussianAg2_ycoordinate, color="red")
if int(numberofatoms) >= 3:
	exec('plt.axvline(x=GaussianAg3_ycoordinate, color="red")')
if int(numberofatoms) >= 4:
	exec('plt.axvline(x=GaussianAg4_ycoordinate, color="red")')
if int(numberofatoms) >= 5:
	exec('plt.axvline(x=GaussianAg5_ycoordinate, color="red")')
if int(numberofatoms) >= 6:
	exec('plt.axvline(x=GaussianAg6_ycoordinate, color="red")')
if int(numberofatoms) >= 7:
	exec('plt.axvline(x=GaussianAg7_ycoordinate, color="red")')
if int(numberofatoms) >= 8:
	exec('plt.axvline(x=GaussianAg8_ycoordinate, color="red")')

plt.axvline(x=QEAg1_ycoordinate, label="Quantum Espresso", color="blue")
plt.axvline(x=QEAg2_ycoordinate, color="blue")
if int(numberofatoms) >= 3:
	exec('plt.axvline(x=QEAg3_ycoordinate, color="blue")')
if int(numberofatoms) >= 4:
	exec('plt.axvline(x=QEAg4_ycoordinate, color="blue")')
if int(numberofatoms) >= 5:
	exec('plt.axvline(x=QEAg5_ycoordinate, color="blue")')
if int(numberofatoms) >= 6:
	exec('plt.axvline(x=QEAg6_ycoordinate, color="blue")')
if int(numberofatoms) >= 7:
	exec('plt.axvline(x=QEAg7_ycoordinate, color="blue")')
if int(numberofatoms) >= 8:
	exec('plt.axvline(x=QEAg8_ycoordinate, color="blue")')

plt.xlim(-10, 10)
plt.xlabel("y axis (Bohr)", fontsize=18)
plt.ylabel("Electrons/Bohr", fontsize=18)
#plt.title(orbitalname + " of " + moleculename)
plt.legend(fontsize=18, loc="lower left")
plt.savefig(moleculename + "_" + orbitalname + "_y.png")
plt.close()






plt.figure(figsize=(8,8), dpi=80)
areagaussianx = np.trapz(gaussianxvolume, gaussianxvalue)
gaussianxvolumenormalized=[i/areagaussianx for i in gaussianxvolume]
plt.scatter(gaussianxvalue, gaussianxvolumenormalized, color="red")

areaquantumespressox = np.trapz(quantumespressoxvolume, quantumespressoxvalue)
quantumespressoxvolumenormalized=[i/areaquantumespressox for i in quantumespressoxvolume]
plt.scatter(quantumespressoyvalue, quantumespressoxvolumenormalized, color="blue")

plt.axvline(x=GaussianAg1_xcoordinate, label="Gaussian", color="red")
plt.axvline(x=GaussianAg2_xcoordinate, color="red")
if int(numberofatoms) >= 3:
	exec('plt.axvline(x=GaussianAg3_xcoordinate, color="red")')
if int(numberofatoms) >= 4:
	exec('plt.axvline(x=GaussianAg4_xcoordinate, color="red")')
if int(numberofatoms) >= 5:
	exec('plt.axvline(x=GaussianAg5_xcoordinate, color="red")')
if int(numberofatoms) >= 6:
	exec('plt.axvline(x=GaussianAg6_xcoordinate, color="red")')
if int(numberofatoms) >= 7:
	exec('plt.axvline(x=GaussianAg7_xcoordinate, color="red")')
if int(numberofatoms) >= 8:
	exec('plt.axvline(x=GaussianAg8_xcoordinate, color="red")')

plt.axvline(x=QEAg1_xcoordinate, label="Quantum Espresso", color="blue")
plt.axvline(x=QEAg2_xcoordinate, color="blue")
if int(numberofatoms) >= 3:
	exec('plt.axvline(x=QEAg3_xcoordinate, color="blue")')
if int(numberofatoms) >= 4:
	exec('plt.axvline(x=QEAg4_xcoordinate, color="blue")')
if int(numberofatoms) >= 4:
	exec('plt.axvline(x=QEAg4_xcoordinate, color="blue")')
if int(numberofatoms) >= 5:
	exec('plt.axvline(x=QEAg5_xcoordinate, color="blue")')
if int(numberofatoms) >= 6:
	exec('plt.axvline(x=QEAg6_xcoordinate, color="blue")')
if int(numberofatoms) >= 7:
	exec('plt.axvline(x=QEAg7_xcoordinate, color="blue")')
if int(numberofatoms) >= 8:
	exec('plt.axvline(x=QEAg8_xcoordinate, color="blue")')

plt.xlim(-10, 10)
plt.xlabel("x axis (Bohr)", fontsize=18)
plt.ylabel("Electrons/Bohr", fontsize=18)
#plt.title(orbitalname + " of " + moleculename)
plt.legend(fontsize=18, loc="lower left")
plt.savefig(moleculename + "_" + orbitalname + "_x.png")

end_time = time.time()

computation_time = (end_time - start_time)/60
print(f"Computation time: {computation_time} minutes")
