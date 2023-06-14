#! /bin/bash

echo what is your checkpoint file named? don\'t include the .chk part 
read file

echo what orbital number?
read orbital

#Convert the .chk file to a .fchk file
formchk $file.chk $file.fchk

#Utilize the cubegen utility of Gaussian
#Documentation can be found at https://gaussian.com/cubegen/
cubegen 0 MO=$orbital $file.fchk ${file}_$orbital.cub 200 
