#!/usr/bin/env python3
from pymatgen.io.vasp.outputs import Vasprun # Look at pymatgen documentation to see details of the Vasprun library

vdata = Vasprun('vasprun.xml', separate_spins=True) # Import vasprun.xml data.  May need to change the name of the input file.

gap, cbm, vbm, is_direct = vdata.eigenvalue_band_properties # Parse the band edge eigenvalues and determine if the gap is direct

spin_up = [gap[0],cbm[0],vbm[0],is_direct[0]] # Spin up values

spin_down = [gap[1],cbm[1],vbm[1],is_direct[1]] # Spin down values

fermi = vdata.calculate_efermi() # Fermi energy

# Print results
print("Spin up: gap = %s cbm = %s fermi = %s vbm = %s is_direct = %s" % (spin_up[0], spin_up[1], fermi, spin_up[2], spin_up[3])) 
print("Spin down: gap = %s cbm = %s fermi = %s vbm = %s is_direct = %s" % (spin_down[0], spin_down[1], fermi, spin_down[2], spin_down[3]))
