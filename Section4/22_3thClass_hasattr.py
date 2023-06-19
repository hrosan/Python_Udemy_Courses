'''
    The hasattr() function is used to check if an object has a specific attribute or method.
It takes two parameters: the object to be checked and the name of the attribute or method to be tested.
'''
class MyClass:
    def __init__(self):
        self.x = 10

    def my_method(self):
        print("Hello, world!")

my_obj = MyClass()

# Check if the object has the attribute 'x'
if hasattr(my_obj, 'x'):
    print("Object has 'x' attribute")
else:
    print("Object does not have 'x' attribute")

# Check if the object has the method 'my_method'
if hasattr(my_obj, 'my_method'):
    print("Object has 'my_method' method")
else:
    print("Object does not have 'my_method' method")

'''
In this example, we define a class MyClass with an attribute x and a method my_method. We create an instance of 
MyClass called my_obj. We use hasattr() to check if my_obj has the attribute x and the method my_method. 
    The hasattr() function returns True if the object has the specified attribute or method, and False otherwise.
                        Object has 'x' attribute
                        Object has 'my_method' method
    This demonstrates how hasattr() can be used to dynamically check for the existence of attributes or methods in an 
object before accessing or calling them.
'''
