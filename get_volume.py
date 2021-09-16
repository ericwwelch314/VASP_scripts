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

b_cross_c = np.cross(b,c)
a_dot_b_cross_c = np.dot(a,b_cross_c)
vol = np.absolute(a_dot_b_cross_c)
print('System volume (A^3) = ', vol)
