'''
Find the sum of the series upto n terms
Write a program to calculate the sum of series up to n term. For example,
if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690
'''

while True:
    serie_number = "" # Number that would be sum, its an string 
    serie_sum = 0 # Varible to sum each number
    n_repetition = 0 # Number of repetitions
    accumulator_string = ""
    # Fulfilling the variables
    serie_number = input('Insert the number that will be iterated: ')
    n_repetition = int(input('Insert the number of repetitions: '))

    # Loop to iterate over the number
    for i in range(1,n_repetition+1):
        accumulator_string = serie_number*i # It will multiplicate the number value
        print(accumulator_string)
        serie_sum += int(accumulator_string) # Sum of each element iterated
    print(serie_sum) # Total of the sum
    break