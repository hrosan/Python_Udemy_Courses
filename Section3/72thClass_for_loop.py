'''
A for loop is a control flow statement that allows you to iterate over a sequence of 
values (such as a list, tuple, or string) and perform some action for each item in the
sequence.
The basic syntax of a for loop in Python is as follows:
            for item in sequence:
                # Do something with item
'''

'''
Here, item is a variable that represents the current item in the sequence,
and sequence is the sequence of values that you want to iterate over. 
The for loop will execute the indented code block once for each item in the sequence,
with the item variable set to the current item on each iteration.
For example, suppose you have a list of numbers:
                numbers = [1, 2, 3, 4, 5]
'''

# You can use a for loop to iterate over the list and print each number

numbers = [1,2,3,4,5] 
for num in numbers:
    print(num)

'''
You can also use the range() function to generate a sequence of numbers to iterate over.
The range() function takes three arguments: start, stop, and step. If you omit start,
it defaults to 0. If you omit step, it defaults to 1.

For example, the following for loop will print the numbers 0 through 4
'''
for i in range(5):
    print(i)

'''
You can also use a for loop to iterate over the characters in a string:
'''
for char in "Hello":
    print(char)