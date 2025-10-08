import sys
from tabulate import tabulate
import csv

if 3 < len(sys.argv):
    sys.exit('Too many command-line arguments')
elif 3 > len(sys.argv):
    sys.exit('Too few command-line arguments')

x1,x2 = sys.argv[1].split('.')
y1,y2 = sys.argv[2].split('.')

if x2 != 'csv' or y2 != 'csv':
    sys.exit('Not a CSV file')

x = []
try:
    with open(f'{sys.argv[1]}') as bfl:

        bfile = csv.DictReader(bfl)
        for line in bfile:
            ln,fn = line['name'].lstrip().split(',')
            x.append({'first' : fn.lstrip(), 'last' : ln, 'house' : line['house']})

except FileNotFoundError:
      sys.exit(f'Could not read invalid_file.csv')

#newline='': This argument ensures that no additional newline characters are added when writing to the file.
#  In CSV files, each row is separated by a newline character. Without specifying newline='',
# the default behavior may add newline characters that are specific to the operating system
with open(f"{sys.argv[2]}", 'w', newline='') as afl:
       afile = csv.DictWriter(afl, fieldnames=['first', 'last', 'house'])

       if afl.tell() == 0:
            afile.writeheader()

       for row in x:
            afile.writerow(row)

