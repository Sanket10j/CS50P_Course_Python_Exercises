i = 1
while i <= 3:
    print (" hello")
    i += 1
# += is just syntax sugar for i = i + 1

#or

for _ in [0,1,2]:
    print ('wow')
# _ is indicating as variable like i but you don't care about it's name since you are not going to use
#  it later, just necessary to use these feature

# or

for i/_ in range(3):
     print ('wow')

#or

    

# when you have some expectations like all +ve or -ve use
while True:
    if n < 0:
        continue
    else:
        break

# or

while True:
    n = int(input('what is n ?'))
    if n < 0:
        break
for _ in range(n):
     print ('wow')


# in python '' or "" used to show it as a string
#list
students = ['adi','riya','sanket']
print(students[0])
#or

students = ['adi','riya','sanket']
for student in students:
    print(student)
#or
students = ['adi','riya', 'sanket']
for student in students:
    print (students * 3)


#or
students = ['adi','riya','sanket']
for _ in students:
    print(_)
#or
students = ['adi','riya','sanket']
for _ in (3 * students):
    print(_)

#function called len for lenth that will tell you lenth of a list
# & range doesn't take a list of string, it takes a number

students = ['adi','riya','sanket']
for i in range(len(students)):
    print(i, students)

#list is kind of 1-d wherease dict for dictionary datatype is 2-d where you can associate something to something
students = {}  # empty dic, uses {} instead of []
variable = {'key': 'associated value'}
#list has locations which are numeric whereas dic allows you to use actual words(keys) as indices to get inside of it and collect value associated with it.

students = {
        'adi': 'k.g.',
        'riya': 'h.s.',
        'sanket': 'p.g.'
}
for student in students:
    print(student)
# conventionaly keys only would be selected as variable and printed

students = {
        'adi': 'k.g.',
        'riya': 'h.s.',
        'sanket': 'p.g.'
}
for student in students:
    print(student,students[student], sep=', ')

students = [
        {'name': 'adi', 'level':'k.g.'},
        {'name': 'riya', 'level':'h.s.'},
        {'name': 'sanket', 'level':'p.g.'}
]
for student in students:
    print(student)

#in python, None is specific keyword to show there is no existence of information
#Multiple dictionary in list
students = [
        {'name': 'adi', 'level':'k.g.'},
        {'name': 'riya', 'level':'h.s.'},
        {'name': 'sanket', 'level':'p.g.'}
]
for student in students:
    print(student['name'], student['level'], sep=', ')

##
def main():
    square_(4)

def square_(l):
    for i in range(l):
        for j in range(l):
            print('#', end='')
        print()

main()

#or

def main():
    square_(4)

def square_(l):
    for i in range(l):
        print('#' * l)

main()






