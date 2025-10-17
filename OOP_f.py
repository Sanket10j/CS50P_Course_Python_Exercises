#### tuple  #### 
# is a type of datatype which is collection of values
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
# fist letter of the class should be capital    
# IT ALLOWS YOU TO INVENT YOUR OWN DATA TYPE AND GIVE NAME
# A Blue print for pieces of Objects
# By using this class as mold or blue-print, you can get types of data exactly as you designed
# Class is the definition of new data type and the Object is instantiation of that Class
# Class is blue_print of house and Object is actual created house by using that blue_print
# Class are mutable and can also be converted into immutable
# Attributes or instance variables are just properties of Class
# You can create own library of Classes


#1
class Student: # Student is now data type 
    ...
def main():
    student = get_student()
    print(f'{student.name} from {student.house}') # name and house attributes are accessed through '.'
 
def get_student():
    std = Student() # Created Object using Student Class
    std.name = input('NAME: ') # name and house are the attributes stored in std (object) by using '.'
    std.house = input('HOUSE: ') # attributes can be any kind of data type(int, str, float,..)
    return std

if __name__ == '__main__':
    main()

#2 METHOD:
# Class also contains certain Methods or functions which can be implemented inside of them
# Methods are just standard ways to determine the behaviour Class datatype
# Method is just a function in classes

class Student: 
    def __init__(self, name, house): # It is standard method called instance method
        self.name = name             # used when you want to initialize the content of object from Class 
        self.house = house           # It is the Student() function initialized this method
                                     # self gives the access to the current object that was just created     
def main():
    student = get_student()
    print(f'{student.name} from {student.house}') 

def get_student():
    name = input('NAME: ') 
    house = input('HOUSE: ') 
    student = Student(name, house) # by directly passing to Student() Class function, getting more control on correctness of data
#   object  = Class_function(Attribute 1 , Attribute 2)
# Student(name, house)  is constructor which constructs the student object in computer's memory, but till object is empty
# Student() calls __init__ method which stores the name, house attributes
# EX. It is like house blue_print where fundamental confirmation of house is same but color of house are different 
# same as Student() blue_print where attributes differes but blue_print for their storage into object is same 
    return student
if __name__ == '__main__':
    main()

#2.1 raise:
# you can create your own exception or error by using syntax 'raise'
# OOP encourage you to encapsulate all the functionality related to the Class inside the Class


class Student: 
    def __init__(self, name, house=None, nickname):# If you want to make house optional
        if not name:
            raise ValueError('Name is Missing')
        if house not in ['Mars', 'Earth', 'Moon']:
            raise ValueError('Invalid House')
        self.name = name              
        self.house = house
        self.nickname  = nickname
    
    def __str__(self): # It just convert the object into string for print
        return f'{self.name} from {self.house}'
    
    def nk_name_rxn(self): # creating own method or function in Class
        match self.nickname:
            case 'jadoo':
                return 'jum JUM'
            case 'adu':
                return 'chkali'
            case _:
                return 'hahaha'
            
def main():
    student = get_student()
    print(student) #__str__ method allows to print the object as a string as per modified in that method 
    print(student.nk_name_rxn())
    student.house = 'Sun' # means you can still overwrite and completely mislead the if conditions in Class
  
def get_student():
    name = input('NAME: ') 
    house = input('HOUSE: ')
    nickname = input('Nick Name:')
    return Student(name, house, nickname) # Just neglect the variable formation, Object will created even though

if __name__ == '__main__':
    main()


3. PROPERTIES, GETTERS & SETTERS

class Student: 
    def __init__(self, name, house):
        if not name:
            raise ValueError('Name is Missing')
        if house not in ['Mars', 'Earth', 'Moon']:
            raise ValueError('Invalid House')
        self.name = name              
        self.house = house
    
    def __str__(self):
        return f'{self.name} from {self.house}'
    
    #Getter: fn in class that gets some value
    @property #by this we have set getter
    def house(self):# name the fn as the property
        return self.house
    
    #Setter: fn in class that sets some value
    @house.setter #property itself is house
    def house(self, house):
        self.house = house 

#### 3.1 #####
        
class Student: 
    def __init__(self, name, house):
        if not name:
            raise ValueError('Name is Missing')
        self.name = name              
        self.house = house # this will call setter fn so no need to mention error checking here
    
    def __str__(self):
        return f'{self.name} from {self.house}'
    
    #Getter: 
    @property #by this we have set getter
    def house(self):
        return self._house #CAN NOT SHARE SAME NAME FOR  INSTANCE VARIABLE for  FN, EX.self.house AND def house()
    
    #Setter:
    @house.setter 
    def house(self, house):
        if house not in ['Mars', 'Earth', 'Moon']:# All error checking in one place 
            raise ValueError('Invalid House')
        self._house = house 

    
def main():
    student = get_student()
    student.house = 'Sun' # when python finds out the the assignment of same attribute which is the name of the setter or getter,
    #it will call that setter to proceede without assigning the value to that attribute
    print(student)
////
def main():
    student = get_student()
    student._house = 'Sun'  # although we can still change,so underscore signifies not to touch / change it 

def get_student():
    name = input('NAME: ') 
    house = input('HOUSE: ') 
    return Student(name, house) 

if __name__ == '__main__':
    main()


4. Types & Classes:

# int is just class
class int(x, base=10):

# str is just class
class str(object=''):

#Taking an object of type str and making it to lowercase by calling a method called lower, been prebuilt in str class
str.lower()

# list and dict is also class

5. Class Methods:

import random
class Hat:
    def __init__(self):
        self.houses = ['gryffindor','hufflepuff','ravenclaw','slytherin']

    def sort(self, name):
        print(name, 'is in', random.choice(self.houses))

hat = Hat()
hat.sort('Harry')    

5.1
class Hat:
    # houses is class variable
    houses = ['gryffindor','hufflepuff','ravenclaw','slytherin']

    @classmethod #defining classmethod decorator
    def sort(cls, name):
        print(name, 'is in', random.choice(cls.houses))

Hat.sort('Harry') 


5.2
class Student: 
    def __init__(self, name, house=None)
        if not name:
            raise ValueError('Name is Missing')
        if house not in ['Mars', 'Earth', 'Moon']:
            raise ValueError('Invalid House')
        self.name = name              
        self.house = house
        
    def __str__(self): 
        return f'{self.name} from {self.house}'
    
    @classmethod
    def get_student(cls):
        name = input('NAME: ') 
        house = input('HOUSE: ')
        return cls(name, house)  #Q: why not to use Student instead of cls
                
def main():
    student = get_student()
    print(student) 
       
if __name__ == '__main__':
    main()


6. INHERITANCE:

class Student():
    def __init__(self,name,house):
        if not name:
            raise ValueError('Missing name')
        self.name = name
        self.house = house
    ...
class Prof():
    def __init__(self,name,subject):
        if not name:
            raise ValueError('Missing name')
        self.name =name
        self.subject = subject
    ...    

##6.1 SUPER CLASS

class Wizard:
    def __init__(self,name):#superclass
        if not name:
            raise ValueError('Missing name')
        self.name =name
# Student and Prof class inheritate functionality of name from Wizard class
class Student(Wizard):#subclass
        def __init__(self, name,house):
            super().__init__(name)# Need to explicitly mention the particular functionality we want use from super class 
            self.house = house
        ...
class Prof(Wizard):#subclass
        def __init__(self, name,subject):
            super().__init__(name)
            self.subject = subject
        ... 

# 7. Operator Overloading:

class Vault:
    def __init__(self,R,P,D):
                 self.R = R
                 self.P = P
                 self.D = D

    def __str__(self):
        return f'{self.R} R,{self.P} P,{self.D} D'
    
    def __add__(self,other):# addition Operator Overloaded
        R = self.R + other.R
        P = self.P + other.P
        D = self.D + other.D
        return Vault(R,P,D)

potter = Vault(100,50,25)
water = Vault(125,50,125)  

Total = potter + water

                  
