'''
You can format a string in Python using the .format() method or using f-strings
(formatted string literals) in Python 3.6 and above.
'''
name = "Alice"
age = 25
print("My name is {} and I am {} years old.".format(name, age))

'''
In this example, {} serves as a placeholder for the variables name and age. 
The .format() method then replaces each placeholder with the corresponding value.
'''

'''
You can use the format specification mini-language to format float numbers and 
specify the precision of the decimal places.
To specify the precision, you can use the format code :.Nf where N is the number of decimal 
places you want to display.
'''
# Here's an example:
x = 3.14159265
print("The value of x is {:.2f}".format(x))