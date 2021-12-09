#!/usr/bin/env python3
# Script to parse the lattice vectors from a POSCAR and compute the volume using vol = mag(a * b x c) where * = dot, x = cross and a,b,c are the 3 lattice vectors
import numpy as np
import sys

fname = input('POSCAR or CONTCAR??') # Take user input for filename

# Check if the file exists in the folder
if fname == 'POSCAR':
	try:
		with open('POSCAR') as f:
			lines = f.readlines()
			data = []
			for line in lines:
				data.append(line.split())

	except FileNotFoundError:
		print('Is there a file named POSCAR in this directory?? ....can\'t complete task if there isn\'t one')
		sys.exit(1)

elif fname == 'CONTCAR':
	try:
			with open('CONTCAR') as f:
				lines = f.readlines()
				data = []
				for line in lines:
					data.append(line.split())

	except FileNotFoundError:
		print('Is there a file named CONTCAR in this directory?? ....can\'t complete task if there isn\'t one')
		sys.exit(1)

else:
	print('Incorrect filename ..must either be POSCAR or CONTCAR ...check your spelling and try again.')
	sys.exit(1)

a = (data[2])
for i in range(len(a)):
	a[i] = float(a[i])
b = (data[3])
for j in range(len(b)):
	b[j] = float(b[j])
c = (data[4])
for k in range(len(c)):
	c[k] = float(c[k])

moda = np.sqrt(a[0]**2 + a[1]**2 + a[2]**2)
modb = np.sqrt(b[0]**2 + b[1]**2 + b[2]**2)
modc = np.sqrt(c[0]**2 + c[1]**2 + c[2]**2)

v = [moda, modb, modc]
k = [1/moda, 1/modb, 1/modc]
vmax = np.max(v)
kpt = [np.rint(k[0]*vmax), np.rint(k[1]*vmax), np.rint(k[2]*vmax)]

b_cross_c = np.cross(b,c)
a_dot_b_cross_c = np.dot(a,b_cross_c)
vol = np.absolute(a_dot_b_cross_c)
print('a: ', moda)
print('b: ', modb)
print('c: ', modc)
print('Kpoint mesh: ', kpt)
num_units = int(input('Number of formula units/supercell: '))
print('(Psuedo)cubic lattice constant', (vol/num_units)**(1/3))
print('Volume (A^3) = ', vol)


