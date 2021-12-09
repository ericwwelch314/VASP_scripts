#!/usr/bin/env python3
import sys
import numpy as np
from scipy.optimize import leastsq

# Equation of state fitting and plotting script
# Eric Welch

# Import data from user inputs
vol = list(map(float,input('Enter tab separated volumes: ').strip().split())) # asks user to insert volumes
engy = list(map(float,input('Enter tab separated energies: ').strip().split())) # asks user to insert energies
v = np.array(vol) # makes the volume input a list (vector)
e = np.array(engy) # makes the energy input a list (vector) 

# Initialize data for plots and initial guesses
vfit = np.linspace(min(v),max(v),100) # makes a nice set of points for interpolation between given volume data points
a,b,c = np.polyfit(v,e,2) # fit a parabola to the data
v0 = -b/(2*a) # equilibrium volume
e0 = a*v0**2 + b*v0 + c # ground state energy
b0 = 2*a*v0 # bulk modulus
bP = 4 # derivative of bulk modulus wrt pressure

def birch_murnaghan(params,vol):
	E0, B0, BP, V0 = params
	eta = (V0/vol)**(2/3)
	return (E0 + (9*V0*B0/16)*(((eta - 1)**3)*BP + ((eta - 1)**2)*(6 - 4*eta)))
    

def murnaghan(params,vol):
	E0, B0, BP, V0 = params
	return (E0 + (B0*vol/BP)*(((V0/vol)**BP)/(BP - 1) + 1) - (V0*B0/(BP - 1)))

def minimize(pars,y,x):
	return y - birch_murnaghan(pars,x)
    
x0 = [e0, b0, bP, v0] # initial guesses
murnpars, ier = leastsq(minimize, x0, args=(e,v)) # use the least square fit from scipy

try:
	import pylab as pl
except ImportError:
	sys.stderr.write('pylab module not available, skipping plot')
	sys.exit(0)

pl.plot(v,e,'ro')
pl.plot(vfit, a*vfit**2 + b*vfit + c,'--',label='parabolic fit')
pl.plot(vfit, birch_murnaghan(murnpars,vfit), label='Murnaghan fit')
pl.plot(vfit, murnaghan(murnpars,vfit), label='Murnaghan fit')
pl.xlabel('Volume ($\AA^3$)')
pl.ylabel('Energy (eV)')
pl.legend(loc='best')

#add some text to the figure in figure coordinates
ax = pl.gca()
ax.text(0.4,0.5,'Min volume = %1.2f $\AA^3$' % murnpars[3], transform = ax.transAxes)
ax.text(0.4,0.4,'Bulk modulus = %1.2f eV/$\AA^3$ = %1.2f GPa' % (murnpars[1], murnpars[1]*160.21773), transform = ax.transAxes)
#pl.savefig('a-eos.png')
pl.show()
