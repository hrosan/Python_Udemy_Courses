'''
Print the sum of the current number and the previous number
Write a program to iterate the first 10 numbers and in each iteration, 
print the sum of the current and previous number.
'''

acc = 0 # Accumulator for iterations
i = int(input('Enter you rang for sum: ')) #User entry

# For-loop 
for j in range(i):
    acc += j # IT MUST BE HERE, BECAUSE IT CAN REPEAT VALUES AT THE START
    if j > 0: # IF CASE TO NOT SHOW "-1" ON THE PROMPT
        print(f'Current number {j} previous number {j-1} SUM: {acc}')
    else:
        print(f'Current number {j} previous number {j} SUM: {acc}') 
    