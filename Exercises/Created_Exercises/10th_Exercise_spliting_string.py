'''
Trying to understand the splitting

my_string[start:stop:step]

'''
my_string = "Henrique"
'''
[positive][negative]
[0][-8] = H; [1][-7] = e; [2][-6] = n; [3][-5] = r; [4][-4] = i; [5][-3] = q; [6][-2] = u; 
[7][-1] = e
'''
len_string = len(my_string)

# Start and stop with negative step
reversed_string = my_string[4:7:-1] # Start in [4] goes through [6] excluding [7]
print(reversed_string) # Ocurring an error, cause it's not possible goes at 4 to 7 with a negative step
reversed_string = my_string[7:3:-1] # Start in [7] goes through [4] excluding [3]
print(reversed_string) # euqi