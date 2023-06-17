'''
Write a program to display all prime numbers within a range
A Prime Number is a number that cannot be made by multiplying other whole numbers.
A prime number is a natural number greater than 1 that is not a product of two smaller 
natural numbers
'''
import random as rd

while True:
    # Initializing variables
    prime_list = []
    start = rd.randint(1,20)
    endpoint = start*3
    for i in range(start,endpoint+1):
        if i > 1:
            for j in range(2,i):
                # Check the factor
                if (i%j)==0:
                    #Breaking the loop because the number don't fit the general rules
                    break
            else:
                prime_list.append(i)
    print(prime_list)
    break