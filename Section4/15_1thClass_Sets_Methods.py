'''
- len(set): Returns the number of elements in the set.
- isdisjoint(other_set): Checks if the current set and the given set have no common elements.
- issubset(other_set): Checks if the current set is a subset of the given set.
- issuperset(other_set): Checks if the current set is a superset of the given set.
- update(*sets): Updates the current set by adding elements from other sets or iterable.
- intersection_update(*sets): Updates the current set with the intersection of itself and 
other sets.
- difference_update(*sets): Updates the current set with the difference of itself and other 
sets.
- symmetric_difference_update(other_set): Updates the current set with the symmetric 
difference of itself and the given set.
'''


# Creating a set
fruits = {"apple", "banana", "orange"}

# add(element)
fruits.add("mango")
print(fruits)  # {'apple', 'banana', 'orange', 'mango'}

# remove(element)
fruits.remove("banana")
print(fruits)  # {'apple', 'orange', 'mango'}

# discard(element)
fruits.discard("banana")  # No error raised if element not found

# pop()
popped_element = fruits.pop()
print(popped_element)  # Randomly selected element

# clear()
fruits.clear()
print(fruits)  # set()

# copy()
fruits = {"apple", "banana", "orange"}
fruits_copy = fruits.copy()
print(fruits_copy)  # {'apple', 'banana', 'orange'}

# union(*sets)
set1 = {1, 2, 3}
set2 = {3, 4, 5}


union = set1 | set2
union_set = set1.union(set2)
print(union_set)  # {1, 2, 3, 4, 5}


# Intersection
intersection = set1 & set2
intersection_set = set1.intersection(set2) # intersection(*sets)
print(intersection_set)  # {3}


# Difference
difference = set1 - set2
difference_set = set1.difference(set2) # difference(*sets)
print(difference_set)  # {1, 2}


# Symmetric Difference
symmetric_difference = set1 ^ set2
symmetric_diff_set = set1.symmetric_difference(set2) # symmetric_difference(other_set)
print(symmetric_diff_set)  # {1, 2, 4, 5}


subset = {1, 2}
# Subset
is_subset = set1 <= set2 # issubset(other_set)
print(subset.issubset(set1))  # True 

# issuperset(other_set)
superset = {1, 2, 3, 4, 5}
is_superset = set1 >= set2
print(superset.issuperset(set1))  # True

# isdisjoint(other_set)
set3 = {6, 7, 8}
print(set1.isdisjoint(set3))  # True
