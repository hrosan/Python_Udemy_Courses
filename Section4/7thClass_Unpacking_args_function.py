'''
Unpacking an Argument:
When you unpack an argument while calling a function, you are providing individual values 
that are extracted from a container (such as a list or tuple) using the * operator. 
These individual values are treated as separate arguments to the function.
'''

def my_function(a, b, c, d, e):
    # Access the unpacked arguments individually
    print(a, b, c, d, e)

nums = (1, 2, 3, 4, 5)
my_function(*nums)

'''
In this example, the nums tuple is unpacked using the * operator when calling the 
my_function() function. The individual elements of the nums tuple (1, 2, 3, 4, 5) are passed 
as separate arguments to the function.
By unpacking the argument, you can access and work with the individual values separately 
within the function.
'''

def soma(*args):
    total = 0
    try:
        for num in args:
            total += num
        return total
    except TypeError:
        num,*a = args
        for i in num:
            total += i
        return total 

numeros = 1,2,3,4,5
x = soma(*numeros) # Output 15
y = soma(numeros) # Output TypeError
print(x,y)
a,b,*c = numeros

'''
y = soma(numeros), the numeros tuple itself is passed as a single argument to the soma() 
function. The function expects individual arguments, not a tuple containing multiple values.

To fix the error when using y = soma(numeros), you can unpack the numeros tuple using the 
* operator during the function call, like this: y = soma(*numeros). 
This will pass the elements of the numeros tuple as separate arguments to the soma() function.
'''