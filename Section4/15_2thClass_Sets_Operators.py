'''
Sets in Python are inherently iterable, meaning you can loop over the elements of a set using 
    various iterator functions. Here are some commonly used iterators with sets:
* for element in set: Using a for loop directly on the set allows you to iterate over each 
    element in the set.
* set.iter(): This method returns an iterator object that can be used to iterate over the set's 
    elements.
* set.keys(): This method returns an iterator over the set's elements, equivalent to 
    set.iter().
* set.values(): This method returns an iterator over the set's elements, equivalent to 
    set.iter().
* set.items(): This method returns an iterator over the set's elements, equivalent to 
    set.iter().
* enumerate(set): You can use the enumerate function to get an iterator that returns both the 
    index and the value of each element in the set.
'''
# Example set
my_set = {1, 2, 3, 4, 5}

# Using a for loop to iterate over the set
for element in my_set:
    print(element)

# Using set.iter() to iterate over the set
iterator = my_set.__iter__()
while True:
    try:
        element = iterator.__next__()
        print(element)
    except StopIteration:
        break

# Using enumerate to get the index and value of each element
for index, element in enumerate(my_set):
    print(f"Index: {index}, Element: {element}")

# Using sorted to iterate over the set's elements in sorted order
for element in sorted(my_set):
    print(element)
print()
# Using filter to filter the elements of the set
filtered_set = filter(lambda x: x > 3, my_set)
for element in filtered_set:
    print(element)