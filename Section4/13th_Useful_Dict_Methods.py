# 1. dict.keys()
my_dict = {'a': 1, 'b': 2, 'c': 3}
keys = my_dict.keys() # Getting all keys from the dict
print(keys)  # Output: dict_keys(['a', 'b', 'c'])

# 2. dict.values()
values = my_dict.values() # Getting all values from the dict
print(values)  # Output: dict_values([1, 2, 3])

# 3. dict.items()
items = my_dict.items() # Getting both Key and its value inside a tuple
print(items)  # Output: dict_items([('a', 1), ('b', 2), ('c', 3)])

# 4. dict.get(key, default) > Getting the value at a specified key
value = my_dict.get('a', 0)
print(value)  # Output: 1

# 5. dict.pop(key, default)
removed_value = my_dict.pop('b') # Removes and returns the value associated with the given key
print(removed_value)  # Output: 2

# 6. dict.popitem()
key, value = my_dict.popitem() #removes and returns an arbitrary key-valu pair form the dict
print(key, value)  # Output: c 3

# 7. dict.update(other_dict)
other_dict = {'d': 4, 'e': 5}
my_dict.update(other_dict) # Update the actual dictionary with other dictionary
print(my_dict)  # Output: {'a': 1, 'd': 4, 'e': 5}

# 8. len(dict_len)
dict_len = len(my_dict)
print(dict_len) # Output 3

# 9 .setdefault(key, default_value)
my_dict.setdefault('f',"There's no f key") # Sets a default value to an specified key, that can't be inside the dict
print(my_dict['f'])

# 10. dict.clear()
my_dict.clear() # Clear the dictionary
print(my_dict)  # Output: {}

