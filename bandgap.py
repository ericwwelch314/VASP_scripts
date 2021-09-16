#!/usr/bin/env python3
# Script to parse the relevant band gap data from pymatgen both from the Eigenval and Vasprun outputs
# Eigenval is usually the most reliable but double check your parameters if different values are obtained for the gap

from pymatgen.io.vasp.outputs import Eigenval, Vasprun
import numpy as np

data = Eigenval('EIGENVAL')
vdata = Vasprun('vasprun.xml')
vdata.separate_spins=True

cbm = vdata.eigenvalue_band_properties[1]
vbm = vdata.eigenvalue_band_properties[2]

vdist = vbm - vdata.calculate_efermi() # Distance between efermi and valence band max
cdist = cbm - vdata.calculate_efermi() # Distance between efermi and conduction band min

# Print band gap meta data
print('Fermi level from vasprun = ', vdata.efermi)
print('Calculated Fermi level = ', vdata.calculate_efermi())
print('Run converged (ionic)?? ', vdata.converged_ionic)
print('Run converged (electronic?? ', vdata.converged_electronic)
print('from eigenval [gap, cbm, vbm, is_band_gap_direct] = ', data.eigenvalue_band_properties)
print('from vasprun [gap, cbm, vbm, is_band_gap_direct] = ', vdata.eigenvalue_band_properties)
print('Efermi from VBM (VBM - E_f) = ', vdist)
print('Efermi from CBM (CBM - E_f) = ', cdist)

# Print the location of the fermi level with respect to the band edges
if vdist > 0:
	print('Fermi level below VBM')
elif vdist < 0:
	print('Fermi level above VBM')

if cdist > 0:
	print('Fermi level below CBM')
elif cdist < 0:
	print('Fermi level above CBM')
