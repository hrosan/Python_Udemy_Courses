'''
A closure is a concept in programming that allows a function to remember and access variables 
from its outer, or enclosing, scope even after that scope has finished executing. In other 
words, a closure is a function bundled together with its referencing environment.
'''

def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function # Returning only the function, nothing more

closure = outer_function(10) # Calling the outer_function, it gives the value of 10 to x
result = closure(5)
print(result)  # Output: 15

'''
In this example, the outer_function is defined with a parameter x. It also defines an 
inner_function inside it, which takes a parameter y and returns the sum of x and y. 
The inner_function has access to the variable x from its enclosing scope, even after 
outer_function has finished executing.

When outer_function(10) is called, it returns the inner_function. This returned function, 
referred to as closure, maintains a reference to the value of x (which is 10) from its 
enclosing scope.

Then, closure(5) is called, and it adds the value of y (which is 5) to the remembered value of 
x (which is 10) to produce the result 15.

Closures are useful in scenarios where you want to create functions that retain access to 
certain variables, configurations, or states from an outer scope. They provide a way to 
encapsulate data within a function and create self-contained units of behavior.
'''