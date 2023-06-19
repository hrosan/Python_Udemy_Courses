'''
    The dir() function in Python is a powerful built-in function that returns a list of names in the current local 
scope or the names of attributes and methods of an object. It can be used to explore the available attributes and 
methods of an object or to examine the variables and functions defined within a particular scope.

    The dir() function can be called without any arguments to retrieve the list of names in the current local scope. 
This includes variable names, function names, and imported module names.
'''
def greet(name):
    message = f"Hello {name}"
    print(message)

def multiply(a, b):
    return a * b

print(dir())  # Output: ['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__',
# 'greet', 'multiply']
'''
In this example, the dir() function is called without any arguments, and it returns a list of names in the current scope,
including the built-in names (__builtins__) and the names of the defined functions (greet and multiply).
The dir() function can also be used with an object as an argument to retrieve the names of its attributes and methods. 
This is useful for exploring the available functionality of an object.
'''
my_list = [1, 2, 3]
print(dir(my_list))  # Output: ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', 
# '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', 
# '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__',
#  '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__',
#  '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index',
#  'insert', 'pop', 'remove', 'reverse', 'sort']
'''
In this example, dir(my_list) is called to retrieve the names of attributes and methods available for a list object. 
The output is a list of names, including the built-in methods (append, clear, copy, etc.) and other attributes and 
methods specific to the list object.

The dir() function is a useful tool for exploring the contents and capabilities of objects, modules, and the current 
local scope. It can be used during development and debugging to gain insights into the available functionality and to 
assist in understanding the structure of objects and modules.
'''