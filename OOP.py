# tuple : is a type of datatype which is collection of values
# It is kind of list but immutable, can not change the values as list
# To use when to program defensively by mean that values should not be changed
# list and dict are mutable
#1
def main():
    student = get_student()
    if student[0] == 'sanket':
        student[1] = 'Mars'# it will give you error ''tuple do not support item assignment
# If you want to enable this, you need to return [name, house] as a list
    print(f'{student[0]} from {student[1]}')
def get_student():
    name = input('NAME: ')
    house = input('HOUSE: ')
    return (name, house) # or name, house # In this case both are considered as tuple

if __name__ == '__main__':
    main()
#2
def main():
    student = get_student()
    if student['name'] == 'sanket':
        student['house'] = 'Mars'
    print(f'{student["name"]} from {student["house"]}')
def get_student():
    student = {}
    student['name'] = input('NAME: ')
    student['house'] = input('HOUSE: ')
    return student
#OR
def get_student():
    name = input('NAME: ')
    house = input('HOUSE: ')
    return {'name': name, 'house': house}

if __name__ == '__main__':
    main()


####### CLASS ########
# IT ALLOWS YOU TO INVENT YOUR OWN DATA TYPE AND GIVE NAME
# 
