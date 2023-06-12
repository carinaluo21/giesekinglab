#! /bin/bash

echo what is your checkpoint file named? don\'t include the .chk part 
read file

echo what orbital number?
read orbital

formchk $file.chk $file.fchk
cubegen 0 MO=$orbital $file.fchk ${file}_$orbital.cub 200 
