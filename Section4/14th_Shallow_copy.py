''' 
A shallow copy is a type of object copy where the new object is a separate entity but still shares 
some references with the original object. It creates a new object, but the elements or attributes 
of the new object are references to the same memory locations as the elements or attributes of the 
original object.
'''
original_list = [1, 2, 3, [4, 5]]

# Create a shallow copy of the original list
shallow_copy = original_list.copy()

# Modify an element in the shallow copy
shallow_copy[3][0] = 99

print(original_list)  # Output: [1, 2, 3, [99, 5]]
print(shallow_copy)   # Output: [1, 2, 3, [99, 5]]

# Example using dictionaries
original_dict = {"name": "John", "age": 30, "hobbies": ["reading", "painting"]}

# Create a shallow copy of the original dictionary
shallow_copy = original_dict.copy()

# Modify a value in the shallow copy
shallow_copy["age"] = 35
shallow_copy["hobbies"].append("swimming")

print(original_dict)  # Output: {'name': 'John', 'age': 30, 'hobbies': ['reading', 'painting', 'swimming']}
print(shallow_copy)   # Output: {'name': 'John', 'age': 35, 'hobbies': ['reading', 'painting', 'swimming']}