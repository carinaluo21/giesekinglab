# giesekinglab
This directory contains scripts that I wrote for various purposes while conducting research in the Gieseking group at Brandeis University. 

[analyze_cube_file.py](https://github.com/carinaluo21/giesekinglab/blob/f7f4662c1dfc198b9056bc1296c02b19cceea7d0/analyze_cube_file.py) is a Python script for comparing .cub files of molecular orbitals in terms of the value of the wavefunction along the x, y, and z axes. This script was used in a project for comparing orbitals generated using a plane wave basis set to orbitals generated using a Dunning basis set. 

[isom_energy.sh](https://github.com/carinaluo21/giesekinglab/blob/6f5642de118aebe512a1e2de7a519cf5a151679a/relativeisomericenergy.sh) is a Bash script that converts binding energy data into relative isomeric energy data that can be later used as an input file when plotting the relative energies of structural isomers.

[plot_isom_energy.py](https://github.com/carinaluo21/giesekinglab/blob/ba3b91320d2620ddc21d3a915f389ebdbe3b052c/plot_isom_energy.py) is a Python script that plots the relative energy of structural isomers.

[bind_disp.sh](https://github.com/carinaluo21/giesekinglab/blob/1601ab7e0fa630696b98e5c4b153d40764394237/bind_disp.sh) is a Bash script that calculates binding energy and displacement energy from single-point energies and exports this data to output files upon which further operations can be performed. 

[comp_expense.sh](https://github.com/carinaluo21/giesekinglab/blob/445bcdadf7ca8fa090cd654b0266c24837c4ef01/comp_expense.sh) is a Bash script that extracts the computational expense from EOM-CCSD-based excited state calculations and exports this data to output files upon which further operations can be performed. 

[plot_comp_expense.py](https://github.com/carinaluo21/giesekinglab/blob/ee5faa960f701f765072e8327f3e2e2a11be851b/plot_comp_expense.py) is a Python script that takes the output of [comp_expense.sh](https://github.com/carinaluo21/giesekinglab/blob/445bcdadf7ca8fa090cd654b0266c24837c4ef01/comp_expense.sh) and creates a bar chart.

[deg_orb_gau.py]() is a Python script that combines user-specified cube files into one cube file. This script was used to analyze degenerate orbitals as a set in my basis set comparison project.
