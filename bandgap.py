#!/usr/bin/env python3
from pymatgen.io.vasp.outputs import Vasprun

vdata = Vasprun('vasprun.xml', separate_spins=True)

gap, cbm, vbm, is_direct = vdata.eigenvalue_band_properties

spin_up = [gap[0],cbm[0],vbm[0],is_direct[0]]
#, vbm_kpt[0], cbm_kpt[0]]
spin_down = [gap[1],cbm[1],vbm[1],is_direct[1]]
#, vbm_kpt[0], cbm_kpt[1]]
fermi = vdata.calculate_efermi()

print("Spin up: gap = %s cbm = %s fermi = %s vbm = %s is_direct = %s" % (spin_up[0], spin_up[1], fermi, spin_up[2], spin_up[3]))
print("Spin down: gap = %s cbm = %s fermi = %s vbm = %s is_direct = %s" % (spin_down[0], spin_down[1], fermi, spin_down[2], spin_down[3]))
