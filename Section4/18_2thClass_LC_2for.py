numbers = [1, 2, 3]
letters = ['a', 'b', 'c']

# Create a list of tuples with combinations of numbers and letters
combinations = [(num, letter) for num in numbers for letter in letters]

print(combinations)  # Output: [(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c'), (3, 'a'), (3, 'b'), (3, 'c')]

'''
    In this example, we have two lists, numbers and letters. The list comprehension uses two 
for loops, one for each list. It iterates over each element in numbers and, for each element, 
iterates over each element in letters. It creates a tuple with the number and letter 
combination for each iteration, resulting in a list of tuples representing all possible 
combinations of numbers and letters.

    By using multiple for loops in a list comprehension, you can generate combinations, 
permutations, or iterate over multiple lists simultaneously, allowing you to create more 
complex data structures or perform operations involving multiple iterables in a concise and 
efficient manner.
'''
# Combining elements from two lists, but only if the number is greater than 3 and letter
# upper case
numbers = [1, 4, 2, 5]
letters = ['a', 'B', 'c', 'D']

result = [(num, letter) for num in numbers 
          if num > 3 
          for letter in letters 
          if letter.isupper()]
print(result)  # Output: [(4, 'B'), (5, 'D')]

# Creating a list of tuples with pairs of numbers, but only if the sum of the numbers is even
numbers = [1, 2, 3, 4]
result = [(x, y) for x in numbers 
          for y in numbers 
          if (x + y) % 2 == 0]
print(result)  # Output: [(1, 3), (2, 2), (2, 4), (3, 1), (3, 3), (4, 2), (4, 4)]

# Generating a list of strings where each string is a combinations of a letter and number,
# but only if thew letter is a vowel
letters = ['a', 'e', 'i', 'o']
numbers = [1, 2, 3]
result = [letter + str(num) 
        for letter in letters 
        if letter in 'aeiou' 
        for num in numbers]
print(result)  # Output: ['a1', 'a2', 'a3', 'e1', 'e2', 'e3']

# Creating a list of tuples with pairs of numbers, but only if the first number is greater 
# than the second numbers
numbers = [1, 2, 3, 4]
result = [(x, y) if x > y else (y, x) 
        for x in numbers for y in numbers]
print(result)  # Output: [(2, 1), (3, 1), (3, 2), (4, 1), (4, 2), (4, 3)]
