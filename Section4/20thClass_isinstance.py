'''
The isinstance() function is used in Python to check if an object belongs to a specific class or type. 
It returns True if the object is an instance of the specified class or a subclass of it, and False otherwise. 

The isinstance() function is useful when you want to perform type checking or class verification in your code. 
It allows you to handle different objects based on their class membership, enabling you to write more flexible and 
robust programs.
'''

'''
we define two classes Person and Student. We create instances of these classes, person and student, respectively. 
- The isinstance() function is used to check if each object is an instance of a specific class. 
    - The first and second print() statements return True since person and student are instances of the Person class, 
including its subclass Student.
'''
class Person:
    pass

class Student(Person):
    pass

person = Person()
student = Student()

print(isinstance(person, Person))    # Output: True
print(isinstance(student, Person))   # Output: True
print(isinstance(person, Student))   # Output: False
print(isinstance(student, Student))  # Output: True

'''
 The isinstance() function is used to check if each object belongs to any of the specified classes, 
 which are given as a tuple of classes. The first and second print() statements return True because my_list and my_dict 
 are instances of either list or dict classes.
'''
my_list = [1, 2, 3]
my_dict = {"name": "John", "age": 25}
my_tuple = (1, 2, 3)

print(isinstance(my_list, (list, dict)))   # Output: True
print(isinstance(my_dict, (list, dict)))   # Output: True
print(isinstance(my_tuple, (list, dict)))  # Output: False

# Common example
list_ = [
    'a',1,1.1,True,[0,1,2],(3,5),
    {7,5},{'nome':'Henrique'}
]

for item in list_:
    # From here now the use of isinstance(arg,class)
    if isinstance(item,bool): # Print every bool data
        print(item)
    
    if isinstance(item,list): # Print if a list
        item.append(7) # adding a number just to show
        print(item)

    if isinstance(item,(int,float)): #checking if item is int or float
        item = item**2 # Powering the item to 2
        print(f'{item:.1f}')