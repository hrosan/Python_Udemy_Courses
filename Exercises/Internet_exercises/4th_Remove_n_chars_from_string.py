'''
Remove first n characters from a string
Write a program to remove characters from a string starting from zero up to n and return
 a new string.

For example:

* remove_chars("pynative", 4) so output must be tive. Here we need to remove first four 
characters from a string.
* remove_chars("pynative", 2) so output must be native. Here we need to remove first two 
characters from a string.
Note: n must be less than the length of the string.
'''
while True:
    # Word to be sliced
    user_input_word = input('Insert a word here: ')
    # How many letters will be sliced ?
    word_slice_lenght = int(input('How many letters would you like to slice up? '))
    # Varible to get the sliced word
    sliced_word = user_input_word[word_slice_lenght:]
    print(sliced_word)
    password_break = input('Would you like to leave out: ')
    while password_break.lower() not in ['yes','no']:
        password_break = input('Would you like to leave out: ')
    if password_break == 'yes':
        break
    else:
        continue