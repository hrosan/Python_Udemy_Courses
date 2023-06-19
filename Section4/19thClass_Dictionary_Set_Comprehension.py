'''
Dictionary comprehension is a concise way to create dictionaries in Python by specifying both the keys and values 
using a compact syntax. It follows the pattern {key_expression: value_expression for item in iterable}.
'''
# Example 1: Creating a dictionary of squares for numbers from 1 to 5.
squares = {num: num**2 for num in range(1, 6)}
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Mapping names to their lengths using a list of names.
names = ['Alice', 'Bob', 'Charlie']
name_lengths = {name: len(name) for name in names}
print(name_lengths)  # Output: {'Alice': 5, 'Bob': 3, 'Charlie': 7}

# Creating a dictionary with uppercase letters as keys and their corresponding ASCII values as values.
ascii_values = {chr(num): num for num in range(65, 91)}
print(ascii_values)  # Output: {'A': 65, 'B': 66, 'C': 67, ..., 'Z': 90}

# Filtering even numbers from a list and creating a dictionary where the numbers are keys and their 
# squares are values.
numbers = [1, 2, 3, 4, 5, 6]
even_squares = {num: num**2 for num in numbers if num % 2 == 0}
print(even_squares)  # Output: {2: 4, 4: 16, 6: 36}