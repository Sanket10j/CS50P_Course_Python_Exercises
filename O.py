names = []

while True:
    try:
       names.append(input('name ?'))

    except EOFError:
       break

for i in sorted(names):
    print(i)
'''

'''x = input('name?')

file = open('names.txt', 'w')
# in case names.txt don't exist, open function automaticaly create it
# write clears the previous entry and overwrite
file = open('names.txt', 'a')
# it litterly append but do not leave the space
file.write(f'{x}\n')
file.close()
'''
# with open automatically close the opened file

'''
with open('names.txt') as fl:
    lines = fl.readlines()

for l in lines:
    print('hello!', l.rstrip())
#or

with open('names.txt') as fl:
    for l in fl:
        print('hello!', l.rstrip())'''

'''
n = []

with open('names.txt') as fl:
    for l in fl:
        n.append(l)
print(n)

for i in sorted(n):
    print('hello', i.rstrip())

#or

with open('names.txt') as fl:
    for l in sorted(fl):
        print('hello!', l.rstrip())

# in descending order

with open('names.txt') as fl:
    for l in sorted(fl, reverse=True):
        print('hello!', l.rstrip())
'''

'''
with open('names.csv') as fl:
    for l in fl:
        row = l.rstrip().split(',')
        print(f'age of {row[0]} is {row[1]}')
#or
with open('names.csv') as fl:
    for l in fl:
        name,age = l.rstrip().split(',')
        print(f'age of {name} is {age}')

member = []
with open('names.csv') as fl:
    for l in fl:
        name,age = l.rstrip().split(',')
        member.append(f'{name} is {age} old')
for m in sorted(member):
    print(m)'''

#or
'''
member = []
with open('names.csv') as fl:
    for l in fl:
        name,age = l.rstrip().split(',')
        people = {}
        people['name'] = name
        people['age'] = age
        #or above 3 lines can be consised
        people = {'name': name, 'age': age}

        member.append(people)

for m in member:
    print(m)
    print(m['name'],'=',m['age'])
print(member)'''

#sorted by name
'''
member = []
with open('names.csv') as fl:
    for l in fl:
        name,age = l.rstrip().split(',')
        people = {}
        people = {'name': name, 'age': age}
        member.append(people)

def get_name(x):
    return x['name']


for m in sorted(member, key=get_name):
    print(m['name'],'=',m['age'])'''

'''     no need to call get_name() fn, sorted will automatically call
    key= is method comes as function argument in python
     which takes fn for calling the function
    by which return can be got from it and can be used by original function '''

# BETTER BETTER
# why should make new fn for just for one time usage
'''
member = []
with open('names.csv') as fl:
    for l in fl:
        name,age = l.rstrip().split(',')
        people = {}
        people = {'name': name, 'age': age}
        member.append(people)

for m in sorted(member, key= lambda m: m['name']):
    print(m['name'],'=',m['age'])  '''
    #lambda is technique can used for making instantaneous fn
    # lambda fn input variable: that variable[index]

## PYTHON COMES WITH IN BUILT CSV FUNCTIONS
#1
'''
import csv
member = []
with open('names.csv') as fl:
    file = csv.reader(fl)
    for row in file:
        member.append({'name' : row[0], 'home' : row[1]})
        #or
    for name,home in file:
        member.append({'name' : name, 'home' : home})


for m in sorted(member, key= lambda m: m['home']):
    print(m['name'],'=',m['home'])
'''
#2
'''
import csv
member = []
with open('names.csv') as fl:
    file = csv.DictReader(fl)
    print(file)
    for row in file:
        member.append({'name' : row['name'], 'home' : row['home']})
        #or
       member.append(row)

for m in sorted(member, key= lambda m: m['name']):
    print(m['name'],'=',m['home'])
print(member)'''
# DictReader is better function as it depends on colomn header by which in case of swaping the
# columns it still works because it is not depended on in order we associate name for key

# TO WRITE INTO CSV FILE

#1
'''
import csv

x = input('name ?')
y = input('age ?')

with open('tp.csv', 'a') as fl:
       a = csv.writer(fl)
       a.writerow([x,y])
'''
#2
import csv

x = input('name ?')
y = input('age ?')

with open('tp2.csv', 'a') as fl:
       a = csv.DictWriter(fl, fieldnames=['Name','Age'])
       a.writerow({'Name': x, 'Age': y})



















































