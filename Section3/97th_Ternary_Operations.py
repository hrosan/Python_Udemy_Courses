'''
Ternary operations, also known as conditional expressions or ternary operators,
are a concise way to write conditional statements in a single line of code. 
The ternary operator allows you to evaluate a condition and choose one of two values 
based on the result of that condition

The syntax of a ternary operation in Python is as follows:
            value_if_true if condition else value_if_false

            x = 10
            result = "Even" if x % 2 == 0 else "Odd"
'''




'''
you can use a ternary operator within a for loop to determine a value or perform an 
action based on a condition for each iteration of the loop. Here's an example:

                numbers = [1, 2, 3, 4, 5]
                result = [x if x % 2 == 0 else "Odd" for x in numbers]

                print(result)  # Output: ['Odd', 2, 'Odd', 4, 'Odd']
'''

numbers = [1, 2, 3, 4, 5]
even_numbers = [x for x in numbers if x % 2 == 0]
sum_of_even_numbers = sum(x for x in numbers if x % 2 == 0)
print(even_numbers)  # Output: [2, 4]
print(sum_of_even_numbers)  # Output: 6



names = ["Alice", "Bob", "Charlie"]
modified_names = [name.upper() if len(name) > 5 else name.lower() for name in names]

print(modified_names)
