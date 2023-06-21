'''
    The try, except, and finally statements are used in Python for handling exceptions, allowing you to catch and 
handle errors in your code.
    * Here's an overview of how these statements work:

    * Try: The try block is used to enclose the code that may raise an exception. It is followed by one or more except 
blocks or a finally block (or both).

    * Except: The except block is used to handle specific types of exceptions that may occur within the try block. 
You can have multiple except blocks to handle different types of exceptions. If an exception occurs in the try block 
that matches the type specified in the except block, the code inside the except block will be executed. 
If the exception doesn't match any of the specified types, it will propagate to the outer scope.

    * Finally: The finally block is optional and is used to specify code that will be executed regardless of whether 
an exception occurred or not. It is typically used to perform cleanup tasks, such as closing files or releasing 
resources, that should always be executed.

    In Python, exceptions/errors are organized in a hierarchy. The base class for all exceptions is the BaseException 
class. This class is further subclassed into several more specific exception classes.

    Some commonly used exception classes in Python include:
        - Exception: The base class for all non-system-exiting exceptions.
        - ValueError: Raised when a function receives an argument of the correct type but with an invalid value.
        - TypeError: Raised when an operation or function is performed on an object of an inappropriate type.
        - FileNotFoundError: Raised when a file or directory is requested but cannot be found.
        - IndexError: Raised when a sequence subscript is out of range.
        - KeyError: Raised when a dictionary key is not found.
        - ZeroDivisionError: Raised when division or modulo
'''
try:
    # Code that may raise an exception
    x = 10 / 0  # Division by zero - raises ZeroDivisionError
except ZeroDivisionError:
    # Handle the specific exception
    print("Error: Division by zero")
except:
    # Handle any other exceptions
    print("An error occurred")
finally:
    # Code that will always be executed
    print("End of the try-except-finally block")

try:
    # Open a file for reading
    file = open("myfile.txt", "r")
    # Perform some operations on the file
    # ...
    # Close the file
    file.close()
except FileNotFoundError:
    print("Error: File not found")
except IOError:
    print("Error: Input/Output error")
finally:
    print("File operation completed")

'''
    In this example, the try block attempts to open a file for reading and perform some operations on it. 
If the file is not found, a FileNotFoundError is raised and caught by the corresponding except block. 
If any other input/output error occurs, it is caught by the IOError block. Regardless of the outcome, 
the finally block is executed to print a completion message.
'''
try:
    # Some code that may raise exceptions
    # ...
    pass
except (ValueError, TypeError) as e:
    print("Error: Value or Type mismatch")
except Exception as e:
    print("An unexpected error occurred:", e)
finally:
    print("Cleanup and final tasks")
'''
    In this example, the try block contains some code that may raise different types of exceptions. 
The except block catches both ValueError and TypeError exceptions and prints a generic error message. 
The except block with the Exception catch-all clause catches any other unexpected exceptions and prints their error 
message. Finally, the finally block is executed for cleanup and final tasks.
'''