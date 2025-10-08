import sys
from tabulate import tabulate
import csv

if 2 < len(sys.argv):
    sys.exit('Too many command-line arguments')
elif 2 > len(sys.argv):
    sys.exit('Too few command-line arguments')

x1,x2 = sys.argv[1].split('.')

if x2 != 'csv':
    sys.exit('Not a CSV file')

x = []
try:
    with open(f'{sys.argv[1]}') as fl:
        file = csv.DictReader(fl)
        for row in file:
            x.append(row)
        print(tabulate(x, headers='keys', tablefmt="grid"))
except FileNotFoundError:
      print('File does not exist')




