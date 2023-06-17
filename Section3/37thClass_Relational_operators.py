'''
Conditional signs are used to compare two values and evaluate the result to a boolean 
(True or False). Here are the most commonly used conditional signs in Python:
== (equal to): Evaluates to True if the values on either side are equal.
!= (not equal to): Evaluates to True if the values on either side are not equal.
< (less than): Evaluates to True if the value on the left is less than the value on the right.
> (greater than): Evaluates to True if the value on the left is greater than the value on the right.
<= (less than or equal to): Evaluates to True if the value on the left is less than or equal to the value on the right.
>= (greater than or equal to): Evaluates to True if the value on the left is greater than or equal to the value on the right.
'''
x = int(input('Informe um numero: '))
y = int(input('Informe um segundo numero: '))

if x == y:
    print("x is equal to y")
elif x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
elif x <= y:
    print("x is less than or equal to y")
elif x >= y:
    print("x is greater than or equal to y")
else:
    print("None of the above")