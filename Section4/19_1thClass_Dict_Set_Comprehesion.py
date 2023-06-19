'''
Set comprehension is a concise way to create sets in Python using a compact syntax. It follows the pattern 
                            {expression for item in iterable}.
'''

# Creating a set of even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = {num for num in numbers if num % 2 == 0}
print(even_numbers)  # Output: {2, 4, 6, 8, 10}

# Creating a set of unique characters from a string.
string = "hello world"
unique_chars = {char for char in string}
print(unique_chars)  # Output: {'r', 'o', ' ', 'h', 'w', 'l', 'e', 'd'}

# Creating a set of lengths of words in a list of strings.
words = ["apple", "banana", "cherry", "date"]
word_lengths = {len(word) for word in words}
print(word_lengths)  # Output: {5, 6, 7}
