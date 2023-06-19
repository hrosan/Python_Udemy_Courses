'''
truthy and falsy values refer to the truthiness or falsiness of a given expression or value. 
Every value in Python has an inherent truthiness or falsiness. 
When used in a boolean context, truthy values are considered "true" and falsy values are considered "false".
'''
# Truthy values
value1 = True
value2 = 10
value3 = "Hello"
value4 = [1, 2, 3]

if value1:
    print("value1 is truthy")

if value2:
    print("value2 is truthy")

if value3:
    print("value3 is truthy")

if value4:
    print("value4 is truthy")

# Falsy values
value1 = False
value2 = 0
value3 = ""
value4 = []
value5 = {}
nothing_ = None
float_ = 0.0
range_ = range(0)
set_ = set()
if not value1:
    print("value1 is falsy")

if not value2:
    print("value2 is falsy")

if not value3:
    print("value3 is falsy")

if not value4:
    print("value4 is falsy")

