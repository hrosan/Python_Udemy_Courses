'''
A dictionary in Python is an unordered collection of key-value pairs. 
It is a versatile data structure that allows you to store and retrieve data using a unique key 
associated with each value. Dictionaries are commonly used when you want to store and retrieve 
data based on specific labels or names rather than numerical indices.

1. Keys: The keys in a dictionary are unique and can be of any immutable type, such as strings,
numbers, or tuples. Each key is associated with a value, forming a key-value pair.

2. Values: The values in a dictionary can be of any type, including built-in data types 
(like integers, strings, lists, etc.) or even other dictionaries.

3. Creating a Dictionary: You can create a dictionary using curly braces {} and separating the 
key-value pairs with colons :. For example: my_dict = {'key1': value1, 'key2': value2}.

4. Accessing Values: You can access the values in a dictionary by using the corresponding key. 
For example, my_dict['key1'] would retrieve the value associated with 'key1'.

5. Modifying Values: You can modify the value of a specific key by assigning a new value to it.
For example, my_dict['key1'] = new_value would update the value associated with 'key1' to 
new_value.

6. Adding and Removing Items: You can add new key-value pairs to a dictionary by assigning a 
value to a new key. You can also remove items using the del statement or the pop() method.

7. Dictionary Methods: Dictionaries have various methods that allow you to perform operations 
like getting all the keys, values, or items, checking the existence of a key, or getting the 
length of the dictionary.
'''

# Creating a dictionary
student = {'name': 'John', 'age': 20, 'grade': 'A'}

# Accessing values
print(student['name'])  # Output: John
print(student['age'])   # Output: 20

# Modifying values
student['grade'] = 'B'
print(student)  # Output: {'name': 'John', 'age': 20, 'grade': 'B'}

# Adding a new key-value pair
student['city'] = 'New York'
print(student)  # Output: {'name': 'John', 'age': 20, 'grade': 'B', 'city': 'New York'}

# Removing a key-value pair
del student['age']
print(student)  # Output: {'name': 'John', 'grade': 'B', 'city': 'New York'}