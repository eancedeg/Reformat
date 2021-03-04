#! /usr/bin/python3

import argparse

parser = argparse.ArgumentParser(description='reformat lmps file')
parser.add_argument('basefile', action='store', help='Base file for comparison')
parser.add_argument('lmps', action='store', help='File that will be reformated')
parser.add_argument('-o', '--output', default='output.lmps', help='File name for output file (Default: output.lmps)')

args = parser.parse_args()
file1_name = args.basefile
file2_name = args.lmps
output_name = args.output

# Lectura de ficheros
file1 = open(file1_name)
file2 = open(file2_name)
file3 = open(output_name, 'w')

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
dihedrals = int(dihedral_line.split()[0])

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

# Atom Coeff Section
atoms_list1 = {}
atoms_list2 = {}
for num in range(atom_types):
    line1 = file1.readline()
    atoms_list1[line1.split()[-1]] = line1.split()[0]
    print(line1.rstrip(), file=file3)
    line2 = file2.readline()
    atoms_list2[line2.split()[-1]] = line2.split()[0]

atoms_match = {}
for atom in atoms_list1.keys():
    if atoms_list1[atom] != atoms_list2[atom]:
        atoms_match[atoms_list2[atom]] = atoms_list1[atom]

for num in range(6 + atom_types):
    line1 = file1.readline()
    print(line1, end='', file=file3)
    line2 = file2.readline()


# Bonds reading
bond_list1 = {}
bond_list2 = {}
for bond in range(bond_types):
    line1 = file1.readline()
    bond_list1[line1.split()[-1]] = line1.split()[0]
    print(line1, end='', file=file3)
    line2 = file2.readline()
    bond_list2[line2.split()[-1]] = line2.split()[0]

bond_match = {}
for bond in bond_list2.keys():
    if bond in bond_list1 and bond_list1[bond] != bond_list2[bond]:
        bond_match[bond_list2[bond]] = bond_list1[bond]
    if bond not in bond_list1:
        reverse_bond = ','.join(reversed(bond.split(',')))
        if reverse_bond in bond_list1 and bond_list2[bond] != bond_list1[reverse_bond]:
            bond_match[bond_list2[bond]] = bond_list1[reverse_bond]

# Angle Section
for num in range(3):
    line1 = file1.readline()
    print(line1, end='', file=file3)
    line2 = file2.readline()

angle_list1 = {}
angle_list2 = {}
for angle in range(angle_types):
    line1 = file1.readline()
    print(line1, end='', file=file3)
    angle_list1[line1.split()[-1]] = line1.split()[0]
    line2 = file2.readline()
    angle_list2[line2.split()[-1]] = line2.split()[0]

angle_match = {}
for angle in angle_list2.keys():
    if angle in angle_list1 and angle_list2[angle] != angle_list1[angle]:
        angle_match[angle_list2[angle]] = angle_list1[angle]
    if angle not in angle_list1:
        reverse_angle = ','.join(reversed(angle.split(',')))
        if reverse_angle in angle_list1:
            angle_match[angle_list2[angle]] = angle_list1[reverse_angle]

# Dihedral Section
for num in range(3):
    line1 = file1.readline()
    print(line1, end='', file=file3)
    line2 = file2.readline()

dihedral_list1 = {}
dihedral_list2 = {}
for dihedral in range(dihedral_types):
    line1 = file1.readline()
    print(line1, end='', file=file3)
    dihedral_list1[line1.split()[-1]] = line1.split()[0]
    line2 = file2.readline()
    dihedral_list2[line2.split()[-1]] = line2.split()[0]

dihedral_match = {}
for dihedral in dihedral_list2.keys():
    if dihedral in dihedral_list1 and dihedral_list2[dihedral] != dihedral_list1[dihedral]:
        dihedral_match[dihedral_list2[dihedral]] = dihedral_list1[dihedral]
    if dihedral not in dihedral_list1:
        reverse_dihedral = ','.join(reversed(dihedral.split(',')))
        if reverse_dihedral in dihedral_list1:
            dihedral_match[dihedral_list2[dihedral]] = dihedral_list1[reverse_dihedral]

for num in range(3):
    line1 = file1.readline()
    print(line1, end='', file=file3)
    line2 = file2.readline()

# Atoms Section
for atom in range(atoms):
    line2 = file2.readline()
    atom_in_line = line2.split()[2]
    if atom_in_line not in atoms_match:
        print(line2, end='', file=file3)
    else:
        atom_split = line2.split()
        atom_split[2] = atoms_match[atom_in_line]
        print(' ' + ' '.join(atom_split), file=file3)

for num in range(3):
    line2 = file2.readline()
    print(line2, end='', file=file3)

# Bond Section
for bond in range(bonds):
    line2 = file2.readline()
    bond_in_line = line2.split()[1]
    if bond_in_line not in bond_match:
        print(line2, end='', file=file3)
    else:
        bond_split = line2.split()
        bond_split[1] = bond_match[bond_in_line]
        print(' ' + ' '.join(bond_split), file=file3)

for num in range(3):
    line2 = file2.readline()
    print(line2, end='', file=file3)

# Angles Section
for angle in range(angles):
    line2 = file2.readline()
    angle_in_line = line2.split()[1]
    if angle_in_line not in angle_match:
        print(line2, end='', file=file3)
    else:
        angle_split = line2.split()
        angle_split[1] = angle_match[angle_in_line]
        print(' ' + ' '.join(angle_split), file=file3)

for num in range(3):
    line2 = file2.readline()
    print(line2, end='', file=file3)

# Dihedral Section
for dihedral in range(dihedrals):
    line2 = file2.readline()
    dihedral_in_line = line2.split()[1]
    if dihedral_in_line not in dihedral_match:
        print(line2, end='', file=file3)
    else:
        dihedral_split = line2.split()
        dihedral_split[1] = dihedral_match[dihedral_in_line]
        print(' ' + ' '.join(dihedral_split), file=file3)

file1.close()
file2.close()
file3.close()
