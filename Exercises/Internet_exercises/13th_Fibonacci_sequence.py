'''
The Fibonacci Sequence is a series of numbers. 
The next number is found by adding up the two numbers before it. 
The first two numbers are 0 and 1.

For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. 
The next number in this series above is 13+21 = 34.

'''
import random as rd

# Infinite loop
while True:
    k0 = 0 # Initial value from Fibonacci sequence
    k1 = 1 # Second value from Fibonacci sequence
    kn = 0 # Variable to hold the sum of k1 and k2
    seq_elements = rd.randrange(10,25) # First try it goes to the 10th element
    fibonacci_string = ""
    # For the Fibonacci sequence k0 and k1 are shown first.
    # Guarantee that it happens 
    for i in range(1,seq_elements+1):
        fibonacci_string += str(k0)+" " # concatenating every fibonacci value from the seq.
        kn = k1 + k0 # Adding k1 and k2
        # That's the important part of the algorithm
        '''
        k0 = k1 and k1 = kn > Now the positions are changed
        When kn = k1 + k0 > k1 has the kn last value, and k0 has the k1 last value
        '''
        k0,k1 = k1,kn # Changing their positions
    print(fibonacci_string)
    break