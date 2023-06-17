'''
A set is an unordered collection of unique elements. It is defined by enclosing a comma-separated 
sequence of elements within curly braces {}. Sets are mutable, meaning you can add or remove 
elements from them.

- Sets do not allow duplicate elements. If you try to add a duplicate element to a set, it will be 
ignored.
- Elements in a set are unordered, which means they do not have a specific position or index.
- Sets are mutable, so you can modify them by adding or removing elements.
- Sets can only contain hashable elements, which typically include immutable data types like 
numbers, strings, and tuples. Mutable objects like lists or dictionaries cannot be elements of a 
set.
- You can perform various operations on sets, such as union, intersection, difference, and more, 
using built-in methods and operators.
'''
my_set = {1, 2, 3, 4, 5}

# Add an element to the set
my_set.add(6)

# Remove an element from the set
my_set.remove(3)

# Check if an element is in the set
if 4 in my_set:
    print("4 is in the set")

# Iterate over the elements in the set
for element in my_set:
    print(element)

# Perform set operations
other_set = {4, 5, 6}
union_set = my_set.union(other_set)
intersection_set = my_set.intersection(other_set)
difference_set = my_set.difference(other_set)

# Print the resulting sets
print(union_set)
print(intersection_set)
print(difference_set)