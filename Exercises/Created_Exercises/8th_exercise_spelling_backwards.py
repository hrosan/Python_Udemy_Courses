'''
Write a program that asks the user to enter a word and then prints out the word spelled
backwards.
'''
# Data input
data_input = input('Type a word, I will spell backwards: ')

# input lenght
word_lenght = len(data_input)

# Iterator
i = word_lenght-1

# While loop
while i >= 0:
    print(f'{data_input[i]}') # Printing every letter backwards
    i -= 1 # Diminishing the iterator

print('YOUR WORD WAS SPELLED')