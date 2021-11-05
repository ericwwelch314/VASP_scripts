#!/bin/bash
# A script used to extract the kpoints created from a GGA bandstructure calculation OUTCAR file to be added as 0-weight points at the end of the gga IBZKBT file for an HSE06 KPOINTS bandstructure file
# Make sure to use the pre-convereged WAVECAR and not CHGCAR as this is not a non-scf run
# Make sure the IBZKPT file from the gga scf run is in the non-scf band structure calculation folder when running this script

# Determine number of kpoints and add 1 to include the header ...used for proper grep command below
num_kpt=$(grep -i nkpt OUTCAR | awk '{print $4}')
#echo $num_kpt
# Parse the kpoints, print only values after the second row (NR>2), print the first 3 columns with 2 spaces between each column and add 0 to the end of each row ...finally, save the data into a .out file
grep -A $num_kpt 'k-points in reciprocal lattice and weights' OUTCAR | awk 'NR>1' | awk '{ print $1 "\t" $2 "\t" $3, 0 }' > gga_kpt.out

cat IBZKPT gga_kpt.out > hy-KPOINTS # combine the IBZKPT from gga and kpts from bands run (make sure to cp IBZKPT to the Bands directory, so the OUTCAR and IBZKPT files are in the same directory)

lines=$(wc -l < hy-KPOINTS) # wc -l < determines the number of lines in hy-KPOINTS
num_lines=${lines[0]} # this parses the first value from the lines output
let num_kpt=($num_lines-3) # this removes the number of lines in the header to count only the number of kpoints

sed -i "2s/.*/$num_kpt/" hy-KPOINTS # this replaces the number of kpts from the IBZKPT file with the total number after adding the output from the OUTCAR

rm gga_kpt.out # remove unnecssary files

