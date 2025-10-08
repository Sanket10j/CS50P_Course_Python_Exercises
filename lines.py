

import sys

if 2 < len(sys.argv):
    sys.exit('Too many command-line arguments')
elif 2 > len(sys.argv):
    sys.exit('Too few command-line arguments')

x1,x2 = sys.argv[1].split('.')

if x2 != 'py':
    sys.exit('Not a Python file')


try:
    with open(f'{sys.argv[1]}') as fl:
        z = 0
        for l in fl:
            if l.lstrip() == '' or l.lstrip().startswith('#'):
                continue
            else:
                z += 1
        print(z)
except FileNotFoundError:
      print('File does not exist')





