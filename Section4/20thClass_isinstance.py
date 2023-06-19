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