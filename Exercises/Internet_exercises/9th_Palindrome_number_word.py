'''
Exercise 9: Check Palindrome Number
Write a program to check if the given number is a palindrome number.

A palindrome number is a number that is same after reverse. For example 545, 
is the palindrome numbers
'''

# Innfinite loop
while True:
    # Check if the user wants a palindrome number or word/phrase
    print('Write if you want a palindrome NUMBER or PHRASE')
    user_choice = input('enter your choice: ').lower()
    possible_answer = ['number','phrase']
    # Check the choice
    if user_choice not in possible_answer:
        continue
    else:
        reversed_input = '' # Variable to get the reversed word
        original_word_number = input('Write your word or phrase: ')
        if user_choice == possible_answer[0]: #Check if the user have selected number
            # Getting the input with a preselected type.
            while original_word_number.isnumeric() == False:
                original_word_number = input('Write your word or phrase: ')
            # Reversing the user input
            for i in range(len(original_word_number)):
                reversed_input += original_word_number[i::-1] # It show every letter gradually
            if original_word_number == reversed_input:
                        print('The number/word is a palindrome')
        elif user_choice == possible_answer[1]:
            # Getting the input with a preselected type.
            while original_word_number.isalpha() == False:
                original_word_number = input('Write your word or phrase: ')
            # Reversing the user input
            for i in range(len(original_word_number)):
                reversed_input = original_word_number[i::-1] # It show every letter gradually
                # Comparing the number/phrase
            if original_word_number == reversed_input:
                        print('The number/word is a palindrome')
            