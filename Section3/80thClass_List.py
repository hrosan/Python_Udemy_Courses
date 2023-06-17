'''
In Python, a list is a built-in data structure that allows you to store and organize
multiple items in a single variable. Lists are mutable, which means you can modify their
contents by adding, removing, or modifying elements. Lists can contain elements of
different data types, such as integers, strings, or even other lists.
'''

fruits = ["apple", "banana", "orange"] # Example of list

'''
Lists are indexed, which means you can access individual elements by their position (index)
 in the list. Indexing in Python starts at 0, so the first element of a list has an index 
of 0, the second element has an index of 1, and so on.
'''
'''
Lists support various operations and methods. Some commonly used operations on lists 
include:

* Appending elements: Adding elements to the end of the list using the .append() method.
* Modifying elements: Changing the value of an element at a specific index.
* Slicing: Extracting a portion of a list using the slicing notation [start:end].
* Length: Getting the number of elements in a list using the len() function.
* Iteration: Looping over the elements of a list using a for loop.

Lists also have numerous methods available, such as .insert(), .remove(), .pop(), .sort(),
.reverse(), and more, which provide additional functionality for working with lists.
'''

# Accessing list elements using indexing
print(fruits[0])  # Output: "apple"
print(fruits[2])  # Output: "orange"

# Modifying list elements
fruits[1] = "cherry"
print(fruits)  # Output: ["apple", "cherry", "orange", "grape"]

# Appending elements to a list
fruits.append("kiwi")
print(fruits)  # Output: ["apple", "cherry", "orange", "grape", "kiwi"]

# Removing elements from a list
fruits.remove("orange")
print(fruits)  # Output: ["apple", "cherry", "grape", "kiwi"]

# Checking if an element exists in a list
if "banana" in fruits:
    print("Banana is in the list")
else:
    print("Banana is not in the list")

# Iterating over a list using a for loop
for fruit in fruits:
    print(fruit)

# Getting the length of a list
length = len(fruits)
print(length)  # Output: 4

# Slicing a list to extract a portion
subset = fruits[1:3]
print(subset)  # Output: ["cherry", "grape"]

# Sorting a list in ascending order
fruits.sort()
print(fruits)  # Output: ["apple", "cherry", "grape", "kiwi"]

# Removing the last item from the list
fruits.pop()
print(fruits)