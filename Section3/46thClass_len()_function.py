'''
len() is a built-in function that returns the length of an object. 
The object can be a string, list, tuple, dictionary, set, or any other sequence-like object
'''

#1- Finding the length of a string:
my_string = "Hello, World!"
length = len(my_string)
print(length)  # Output: 13

#2. Finding the length of a list:
my_list = [1, 2, 3, 4, 5]
length = len(my_list)
print(length)  # Output: 5

''' In each of these examples, the len() function is used to find the length of an object, 
which is then stored in a variable and printed to the console '''

# Fatiamento
print(my_string[0:13:1]) # It must print "Hello World!"
# Starts at char 0, goes to the 13th char, 1 by 1
print(my_string[0:5]) # It must print "Hello"
# Starts at char 0, goes to char 5, 1 by 1
print(my_string[0::2]) # It must print "Hlo ol!"
# Starts at char 0, goes to the end, 2 step