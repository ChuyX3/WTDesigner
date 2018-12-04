import re, sys
import utils
from airfoil import airfoil

if len(sys.argv) >= 3:
    data = airfoil()
    filename = sys.argv[1]
    data.load_aerodynamic_data(filename)
    filename = sys.argv[2]
    data.write_aerodynamic_data(filename)
    print('Done!...')
else:
    print("Missing parameters")