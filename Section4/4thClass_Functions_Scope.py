'''
In Python, the scope of a variable refers to the region of the code where the variable is 
accessible and can be referenced. 
The scope determines the visibility and lifetime of a variable within a program. 
Understanding function scope is important for managing variables and avoiding naming conflicts.
Here are the key points about function scope:

1 - Local Scope: Variables defined within a function have local scope. 
They are only accessible within that specific function. 
Local variables are created when the function is called and destroyed when the function 
completes execution.

2 - Global Scope: Variables defined outside of any function have global scope. 
They can be accessed from any part of the program, including inside functions. 
Global variables are created when the program starts and remain in memory until the program 
terminates.

3 - Accessing Global Variables: Within a function, you can access global variables by using 
the global keyword followed by the variable name. 
This allows you to modify the value of a global variable from within a function.

4 - Variable Shadowing: If a local variable in a function has the same name as a global 
variable, the local variable will "shadow" or take precedence over the global variable within 
the function. The local variable will be used instead of the global variable until the end of 
the function's execution.

5 - Nested Functions: In Python, functions can be defined inside other functions. 
In this case, the inner function has access to its own local variables, the variables of the 
outer function(s), and any global variables.

It's important to be mindful of variable scope to avoid unexpected behavior and to write clean 
and maintainable code. Using local variables within functions helps encapsulate data and 
prevent naming conflicts. Using global variables sparingly and with caution can help maintain 
code clarity and avoid unintended side effects.

Remember that Python follows the LEGB (Local, Enclosing, Global, Built-in) rule for variable 
resolution, which determines the order in which Python searches for a variable. 
This rule specifies the order of the scopes that Python considers when resolving a variable 
name.
'''



# Local Scope
def my_function():
    """
    Example of a function with local scope.

    Returns:
    None
    """
    local_variable = "I am a local variable"
    print(local_variable)


# Global Scope
global_variable = "I am a global variable"

def another_function():
    """
    Example of a function accessing a global variable.

    Returns:
    None
    """
    global global_variable  # Access the global variable within the function
    print(global_variable)


# Variable Shadowing
my_variable = 10

def shadowing_example():
    """
    Example of variable shadowing.

    Returns:
    None
    """
    my_variable = 20  # This local variable shadows the global variable
    print(my_variable)


# Nested Functions
def outer_function():
    """
    Example of a nested function.

    Returns:
    None
    """
    outer_variable = "I am an outer variable"

    def inner_function():
        """
        Example of an inner function accessing outer variables.

        Returns:
        None
        """
        print(outer_variable)

    inner_function()


# Example usage
my_function()
another_function()
shadowing_example()
outer_function()