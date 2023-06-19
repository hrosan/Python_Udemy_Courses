'''
It is possible to call a method dynamically in Python using the getattr() function. 
The getattr() function allows you to retrieve an attribute or method of an object based on its name.
'''
class MyClass:
    def method1(self):
        print("This is method 1.")

    def method2(self):
        print("This is method 2.")

obj = MyClass()

method_name = "method1"
method = getattr(obj, method_name)
method()  # Output: This is method 1.

method_name = "method2"
method = getattr(obj, method_name)
method()  # Output: This is method 2.

'''
In this example, we have a class MyClass with two methods, method1 and method2. We create an instance of the class, obj.
We then use the getattr() function to retrieve the method based on its name stored in the method_name variable. 
We assign the retrieved method to the method variable. Finally, we call the method using the parentheses ().

By using getattr() with a dynamic method name, you can choose which method to call based on runtime conditions or user 
input, allowing for more flexible and dynamic program execution.
'''