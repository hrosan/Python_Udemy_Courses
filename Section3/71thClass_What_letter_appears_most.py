'''The .count() method is a built-in string method in Python that returns the number of 
occurrences of a given substring or character in a string.'''

# The syntax for the .count() method is as follows:
'''
--------   string.count(substring, start=0, end=len(string))    ----------
Here, string is the string you want to search for the substring or character,
 substring is the substring or character that you want to count, and start and end are
optional parameters that specify the start and end index of the search range within the 
string.
The method returns an integer representing the number of occurrences of the substring or 
character in the string. If the substring or character is not found, it returns 0.
For example, let's say you have the following string:
'''
s = "Hello, world!"
# count the number of occurrences of the letter 'l' in s
count = s.count('l')
print(count)  # output: 3

# count the number of occurrences of the substring 'or' in s
count = s.count('or')
print(count)  # output: 1
