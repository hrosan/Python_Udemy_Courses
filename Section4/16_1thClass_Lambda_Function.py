'''
Lambda functions can be used with various data structures such as lists, tuples, and 
dictionaries. 
'''
        # LISTS EXAMPLE
'''
map(function, iterable):
    The map() function applies a given function to each item in an iterable (e.g., a list) and 
returns an iterator that yields the results.
    It takes two arguments: the function to apply and the iterable on which to apply the 
function.
The function argument can be a lambda function or any other callable object.
'''
# Example 1: Square each element in a list
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

'''
filter(function, iterable):
    - The filter() function constructs an iterator from elements of an iterable for which a given 
function returns True.
    - It takes two arguments: the function that tests each element and the iterable to filter.
    - The function argument can be a lambda function or any other callable object that returns a 
Boolean value.
'''
# Example 2: Filter even numbers from a list
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]

        # TUPLE EXAMPLE
# Example 1: Sort a list of tuples based on the second element
'''
sorted(iterable, key=None, reverse=False):
    - The sorted() function returns a new sorted list from the elements of the provided 
iterable.
    - It takes three arguments: the iterable to sort, an optional key function to customize 
the sort order, and an optional reverse flag to reverse the order.
    - The key argument can be a lambda function or any other callable object that specifies a 
custom sorting criterion.

'''
students = [('Alice', 20), ('Bob', 18), ('Charlie', 22)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)  # Output: [('Bob', 18), ('Alice', 20), ('Charlie', 22)]
            
            # DICTIONARY EXAMPLE
# Example 1: Sort a dictionary by its values
scores = {'Alice': 80, 'Bob': 95, 'Charlie': 75}
sorted_scores = sorted(scores.items(), key=lambda x: x[1])
print(sorted_scores)  # Output: [('Charlie', 75), ('Alice', 80), ('Bob', 95)]
