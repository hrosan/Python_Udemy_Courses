'''
    Dictionary Packing:
Dictionary packing involves creating a dictionary by collecting key-value pairs using the 
** operator.
'''
name = "John"
age = 30
city = "New York"

person = {"name": name, "age": age, "city": city}
print(person)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}

'''
    Dictionary Unpacking:
Dictionary unpacking involves extracting key-value pairs from a dictionary and assigning them 
to individual variables.
'''
person = {"name": "John", "age": 30, "city": "New York"}

name, age, city = person.values()
print(name, age, city)  # Output: John 30 New York

'''
    Dictionary packing and unpacking can also be performed using the ** operator with function 
arguments. It allows passing a dictionary to a function and unpacking its key-value pairs as 
separate arguments.
'''

person = {"name": "John", "age": 30, "city": "New York"}

def greet(name, age, city):
    print(f"Hello {name}! You are {age} years old and live in {city}.")

greet(**person)  # Output: Hello John! You are 30 years old and live in New York.

'''
    Person dictionary is unpacked and passed as arguments to the greet() function using the 
** operator. The function then uses the unpacked values to generate a greeting message.
    Dictionary packing and unpacking provide flexibility in working with dictionaries, allowing 
you to easily collect or extract key-value pairs as needed.
'''

'''
To unpack two dictionaries into a new dictionary using **kwargs, you can use the unpacking 
operator ** to combine the key-value pairs of the dictionaries. Here's an example:
'''
dict1 = {"name": "John", "age": 30}
dict2 = {"city": "New York", "country": "USA"}

combined_dict = {**dict1, **dict2}

print(combined_dict)