#! /usr/bin/python3

import re

# Lectura de ficheros
file1 = open('out14aR.lmps')
file2 = open('out14aL-v1.lmps')
file3 = open('output.lmps', 'w')

line1 = file1.readline()
line2 = file2.readline()
print('')
while line:
    line = file1.readline()
    print(line, end='')

file1.close()
file2.close()
