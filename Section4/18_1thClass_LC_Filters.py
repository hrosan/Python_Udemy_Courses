'''
    The filter() function is often used in combination with list comprehensions to create a 
new list that contains only the elements from an existing list that satisfy a specific 
condition.
    The filter() function takes two arguments: a function and an iterable. It applies the 
function to each element in the iterable and returns an iterator containing the elements for 
which the function returns True.
    Here's the general syntax for using filter() with list comprehensions:
        new_list = [expression for item in filter(function, old_list)]

    - expression is the operation or transformation you want to apply to each item that 
satisfies the condition.
    - item is a placeholder that represents each item in the filtered iterable.
    - function is a function or lambda function that defines the condition to filter the items.
    - old_list is the original list.
'''
numbers = [1, 2, 3, 4, 5]
# Filter the even numbers in the list and square them using list comprehension
squared_even_numbers = [num ** 2 for num in filter(lambda x: x % 2 == 0, numbers)]
print(squared_even_numbers)  # Output: [4, 16]

# Filter and transform strings
words = ['apple', 'banana', 'cherry', 'date']
# Filter the words that start with 'a' and convert them to uppercase
filtered_words = [word.upper() for word in filter(lambda x: x.startswith('a'), words)]
print(filtered_words)  # Output: ['APPLE']

# Filter and transform dictionaries
students = [{'name': 'Alice', 'age': 20}, {'name': 'Bob', 'age': 25}, 
            {'name': 'Charlie', 'age': 22}]
# Filter the students older than 21 and extract their names
names_of_older_students = [student['name'] 
                    for student in filter(lambda x: x['age'] > 21, students)]
print(names_of_older_students)  # Output: ['Bob', 'Charlie']

# USING TERNARY CONDITTIONS

# With numbers
numbers = [1, 2, 3, 4, 5]
# Filter the numbers and transform them based on a ternary condition
transformed_numbers = [num * 2 if num % 2 == 0 else num * 3 
                for num in filter(lambda x: x > 2, numbers)
                ]
print(transformed_numbers)  # Output: [6, 8, 10]

# With words
words = ['apple', 'banana', 'cherry', 'date']

# Filter the words and transform them based on a ternary condition
transformed_words = [word.upper() if len(word) > 5 else word.lower() 
                for word in filter(lambda x: 'a' in x, words)
                ]
print(transformed_words)  # Output: ['apple', 'BANANA', 'cherry']
