'''
while is a loop statement in Python that allows you to execute a block of code repeatedly until a 
certain condition is met.
'''
# The syntax for while loop is as follows

while ...: #instead of ..., put you condition
    ...
    # code block to be executed

'''
break is a control statement that is used to exit a loop prematurely. 
It can be used in a while loop or a for loop. When break is encountered in a loop, 
the loop is terminated immediately, and the program continues with the next statement after the loop.'''

# Here is an example that shows the use of while and break
i = 1
while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1