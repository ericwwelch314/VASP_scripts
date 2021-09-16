#!/bin/bash
# A script used to extract the kpoints created from a GGA bandstructure calculation OUTCAR file to be added as 0-weight points at the end of the HSE06 IBZBT file for an HSE06 KPOINTS bandstructure file

# Determine number of kpoints and add 1 to include the header ...used for proper grep command below
num_kpt=$(grep -i 'for a total of' OUTCAR | awk '{print $12 + 1}')

# Parse the kpoints, print only values after the second row (NR>2), print the first 3 columns with 2 spaces between each column and add 0 to the end of each row ...finally, save the data into a .out file
grep -A $num_kpt 'Following cartesian coordinates:' OUTCAR | awk 'NR>2' | awk '{ print $1 "  " $2 "  " $3, 0 }' > gga-kpt.out
