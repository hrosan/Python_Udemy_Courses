'''
List comprehension is a concise and powerful way to create lists in Python. 
It allows you to define and populate a list using a compact syntax in a single line of code. 
The basic structure of a list comprehension is as follows:

            new_list = [expression for item in iterable if condition]

    * expression: This is the expression or operation that is applied to each item in the 
iterable to generate the elements of the new list.
    * item: This represents each item in the iterable, such as a list, tuple, or range, that 
you want to iterate over.
    * iterable: This is the source of data that you want to iterate over, such as a list, 
tuple, or range.
    * condition (optional): This is an optional condition that filters the elements based on a 
specified condition. Only items that satisfy the condition are included in the new list.
'''
import random as rd

# List comprehension concept
numbers = [1, 2, 3, 4, 5]
squared_numbers = [num ** 2 for num in numbers if num % 2 == 0]
print(squared_numbers)

# Generating a list of lists using random library
list_of_lists = [[rd.randint(1,10) for i in range(7)]for i in range(3)]
print(list_of_lists)

