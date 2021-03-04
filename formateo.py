#! /usr/bin/python3

import re

# Lectura de ficheros
file1 = open('out14aR.lmps')
file2 = open('out14aL-v1.lmps')
file3 = open('output.lmps', 'w')

for num in range(2):
    line1 = file1.readline()
    line2 = file2.readline()
    print(line1, end='', file=file3)

atom_line = file1.readline()
line2 = file2.readline()
print(atom_line, end='', file=file3)
atoms = int(atom_line.split()[0])

bonds_line = file1.readline()
line2 = file2.readline()
print(bonds_line, end='', file=file3)
bonds = int(bonds_line.split()[0])

angles_line = file1.readline()
line2 = file2.readline()
print(angles_line, end='', file=file3)
angles = int(angles_line.split()[0])

dihedral_line = file1.readline()
line2 = file2.readline()
print(dihedral_line, end='', file=file3)
dihedral = int(dihedral_line.split()[0])

for num in range(2):
    line1 = file1.readline()
    line2 = file2.readline()
    print(line1, end='', file=file3)

atom_types_line = file1.readline()
line2 = file2.readline()
print(atom_types_line, end='', file=file3)
atom_types = int(atom_types_line.split()[0])

bond_types_line = file1.readline()
line2 = file2.readline()
print(bond_types_line, end='', file=file3)
bond_types = int(bond_types_line.split()[0])

angle_types_line = file1.readline()
line2 = file2.readline()
print(angle_types_line, end='', file=file3)
angle_types = int(angle_types_line.split()[0])

dihedral_types_line = file1.readline()
line2 = file2.readline()
print(dihedral_types_line, end='', file=file3)
dihedral_types = int(dihedral_types_line.split()[0])

for num in range(8):
    line1 = file1.readline()
    line2 = file2.readline()
    print(line1, end='', file=file3)

atoms_list1 = {}
atoms_list2 = {}
for num in range(atom_types):
    line1 = file1.readline()
    atoms_list1[line1.split()[-1]] = int(line1.split()[0])
    print(line1.rstrip(), file=file3)
    line2 = file2.readline()
    atoms_list2[line2.split()[-1]] = int(line2.split()[0])

atoms_match = {}
for atom in atoms_list1.keys():
    if atoms_list1[atom] != atoms_list2[atom]:
        atoms_match[atoms_list2[atom]] = atoms_list1[atom]

atoms_subs = atoms_match.keys()

for num in range(6 + atom_types):
    line1 = file1.readline()
    print(line1, end='', file=file3)
    line2 = file2.readline()


# Bonds reading
bond_list1 = {}
bond_list2 = {}
for bond in range(bond_types):
    line1 = file1.readline()
    bond_list1[line1.split()[-1]] = int(line1.split()[0])
    print(line1, end='', file=file3)
    line2 = file2.readline()
    bond_list2[line2.split()[-1]] = int(line2.split()[0])

print(bond_list1)
print(bond_list2)

bond_match = {}
for bond in bond_list2.keys():
    if bond in bond_list1:
        pass


# while line1:
#     line1 = file1.readline()
#     print(line1, end='', file=file3)

file1.close()
file2.close()
