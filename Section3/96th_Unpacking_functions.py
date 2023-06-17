'''
Unpacking in Python refers to the process of extracting individual elements from a packed
collection, such as a list, tuple, or string. It allows you to assign the elements of the 
collection to separate variables, making it easier to work with and manipulate the data.

my_list = [1, 2, 3]
a, b, c = my_list
print(a, b, c)  # Output: 1 2 3

my_list = [1, 2, 3, 4, 5]
a, b, *items, c = my_list

print(a)      # Output: 1
print(b)      # Output: 2
print(items)  # Output: [3, 4]
print(c)      # Output: 5

*items: The asterisk * in front of items indicates that it is a list-like variable that will
capture any number of elements between b and c. These elements are stored as a list.

'''

my_list = [1, 2, 3, 4, 5]
print(*my_list) # Output: 1 2 3 4 5
