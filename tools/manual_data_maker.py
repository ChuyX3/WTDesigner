import re, sys, subprocess
import utils
from airfoil import airfoil
from complex import complex


data = airfoil()

options = [
    '"Read aerodynamic data" ',
    '"Load shape data" ',
    '"Load design data" ',
    '"Write aerodynamic data for Mathematicha" ',
    '"Export geometry" ',
    '"Close Program" '
]

cmd = 'menu.exe '
for line in options:
    cmd += line

end = False
while not end:
    utils.clrscr()
    op = subprocess.call(cmd) + 1
    if op == 1:
        filename = input('Write the in file name: ')
        data.load_aerodynamic_data(filename)
    elif op == 2:
        filename = input('Write the in file name: ')
        data.load_shape_data(filename)
    elif op == 3:
        filename = input('Write the in file name: ')
        data.load_geometry_data(filename)
    elif op == 4:
        filename = input('Write the out file name: ')
        data.write_aerodynamic_data(filename)
    elif op == 5:
        filename = input('Write the out path: ')
        transform = complex()
        transform.real = float(input('Write the X trasnform: '))
        transform.imag = float(input('Write the Y trasnform: '))
        data.write_geometry_data(filename, transform)
    elif op == 6 or op == 0:
        end = True


