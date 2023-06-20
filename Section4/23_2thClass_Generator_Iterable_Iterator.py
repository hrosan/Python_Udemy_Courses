""" 
    A generator is a special type of iterator that generates values on-the-fly instead of storing them in memory all 
at once. It allows you to create iterators in a more concise and memory-efficient way.

    Generators are defined using a special function syntax with the yield keyword instead of the return keyword. 
When a generator function is called, it returns a generator object, which can be iterated over using a loop or other 
iterator-consuming methods.

    The main advantage of generators is their ability to produce values on-demand, which reduces memory consumption. 
Instead of generating and storing all values upfront, they generate values one at a time as requested, making them suitable for working with 
large or infinite sequences.

    The yield from statement is a powerful feature in Python that simplifies the process of delegating value generation
to other generators or iterables. It helps to avoid nested loops and improves code readability.
"""
def even_numbers(n):
    for i in range(n):
        if i % 2 == 0: # Getting only the even numbers
            yield i # Return the actual value, waits for the next loop to 

# Using the generator function
numbers = even_numbers(10) # It goals from 0 to 9
for num in numbers: # Do a loop over numbers
    print(num) 
print()

'''
    You can also create generators using generator expressions, which have a similar syntax to list comprehensions but with parentheses instead of 
square brackets
'''
squares = (x**2 for x in range(5)) 
for square in squares:
    print(square)

'''
    The yield from statement is used in a generator to delegate the generation of values to another generator or iterable. It allows you to 
simplify the code when working with nested generators or when you want to yield values from an iterable directly.
'''
def generator1():
    yield 'Hello'
    yield 'World'

def generator2():
    yield 'Goodbye'
    yield 'World'

def combined_generator():
    yield from generator1()
    yield from generator2()

'''
    The combined_generator function uses yield from to delegate the generation of values to the other generators. It first yields values from 
generator1, then moves on to generator2.
'''

# Using the combined generator
for item in combined_generator():
    print(item)

'''
    By using yield from, we avoid the need for nested loops or manual iteration over the inner generators. 
It simplifies the code and improves readability.

    The yield from statement not only works with generators but also with any iterable object. It can be used with lists,
tuples, strings, and other iterable types. It allows you to yield each value from the iterable directly, 
instead of iterating over it manually.
'''
def list_generator():
    my_list = [1, 2, 3, 4, 5]
    yield from my_list

# Using the list generator
for item in list_generator():
    print(item)
