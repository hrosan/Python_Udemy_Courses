'''
    To import libraries in Python, you can use the import statement. There are multiple ways to import a library, each 
with its own syntax and implications. Here are the common ways to import a library:
'''
'''
    Import the entire library: You can import the entire library using the import statement followed by the library name.
    This imports the math library, and you can access its functions and attributes using the math.<function> syntax.
'''
import math



'''
    Import specific objects: You can import specific objects from a library using the from keyword. 
    This allows you to directly access those objects without using the library name. 
    This imports only the sqrt and pi objects from the math library. 
You can use them directly as sqrt(<number>) or pi.
'''
from math import sqrt, pi


'''
    Import with an alias: You can import a library or specific objects with an alias using the as keyword. 
This allows you to use a shorter or more convenient name to refer to the library or objects. 
This imports the numpy library and assigns it the alias np. You can then use np.<function> to access the 
library's functions.
For example:
'''
import numpy as np


'''
    Import everything: You can import all objects from a library using the * wildcard. This imports all objects into your 
current namespace, but it's generally discouraged as it can lead to naming conflicts. For example:
    This imports all objects from the math library, allowing you to directly use functions like sqrt() or sin() 
without prefixing with math.. However, it can make your code less readable and increase the chance of conflicts with 
other names.
'''
from math import *
