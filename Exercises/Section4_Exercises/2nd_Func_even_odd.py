'''
Create a function to tell if the number is even or odd
'''

def even_odd(arg=0):
    answer = "even" if arg%2==0 else "odd"
    return answer


number = even_odd(7,3)
print(number)