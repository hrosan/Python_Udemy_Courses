'''
Print the following pattern
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5
'''
while True:
    max_nmber_printed = int(input('Input the max number to be printed: ')) # User input
    for i in range(max_nmber_printed+1):
        acc = "" # Accumulator to show the pattern
        for j in range(i): # J goes from 0 to i
            acc += str(i)+" " # accumulator concatenating the strings
        print(acc)