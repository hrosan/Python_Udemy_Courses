'''
deepcopy() is a function provided by the copy module that allows you to create a deep copy of an 
object. A deep copy creates a completely independent copy of an object, including all of its 
nested objects, recursively.

The deepcopy() function ensures that all nested objects, such as lists or dictionaries, are 
recursively copied to create a new independent object hierarchy. This way, modifications made to 
the deep copy won't propagate to the original dictionary or its nested objects.
'''
import copy

original_list = [1, 2, 3, [4, 5]]

# Create a deep copy of the original list
deep_copy = copy.deepcopy(original_list)

# Modify an element in the deep copy
deep_copy[3][0] = 99

print(original_list)  # Output: [1, 2, 3, [4, 5]]
print(deep_copy)      # Output: [1, 2, 3, [99, 5]]

# Dictionary Example
original_dict = {
    "name": "John",
    "age": 30,
    "hobbies": ["reading", "painting"]
}

# Create a deep copy of the original dictionary
deep_copy = copy.deepcopy(original_dict)

# Modify a value in the deep copy
deep_copy["age"] = 35
deep_copy["hobbies"].append("swimming")

print(original_dict)  # Output: {'name': 'John', 'age': 30, 'hobbies': ['reading', 'painting']}
print(deep_copy)      # Output: {'name': 'John', 'age': 35, 'hobbies': ['reading', 'painting', 'swimming']}