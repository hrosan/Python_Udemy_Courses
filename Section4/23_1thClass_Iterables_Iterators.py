'''
    - An iterable is an object that can be looped over, allowing you to iterate through its elements. 
    - An iterator is an object that represents a stream of data and provides the __next__() method to retrieve the 
next element from the stream.

    An iterable can be any object that implements the __iter__() method, which returns an iterator object. 
The iterator, in turn, should have a __next__() method that returns the next element in the stream or raises a 
StopIteration exception if there are no more elements.
'''
# Creating an iterable class
class MyIterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return MyIterator(self.data)

# Creating an iterator class
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        else:
            value = self.data[self.index]
            self.index += 1
            return value

# Creating an instance of MyIterable
my_iterable = MyIterable([1, 2, 3, 4, 5])

# Iterating over the elements using a for loop
for element in my_iterable:
    print(element)

# Manually iterating using the iterator
my_iterator = iter(my_iterable)
print(next(my_iterator))  # 1
print(next(my_iterator))  # 2
print(next(my_iterator))  # 3

'''
    we define a custom iterable class MyIterable that holds a list of data. The __iter__() method of MyIterable returns
an instance of MyIterator, which we also define. The __next__() method of MyIterator retrieves the next element from 
the data list until there are no more elements.

    We then create an instance of MyIterable called my_iterable and demonstrate two ways of iterating over its 
elements. First, we use a for loop, which implicitly calls iter() on the iterable to get an iterator and uses 
__next__() to retrieve each element. Second, we manually create an iterator using iter() and call next() to retrieve 
elements one by one.

    By implementing the __iter__() and __next__() methods, you can make your own objects iterable and define custom 
iteration behavior for them.
'''

# Creating a list
my_list = [1, 2, 3, 4, 5]

# Iterating over the list using a for loop
for element in my_list:
    print(element)

# Manually iterating using an iterator
my_iterator = iter(my_list)
print(next(my_iterator))  # 1
print(next(my_iterator))  # 2
print(next(my_iterator))  # 3