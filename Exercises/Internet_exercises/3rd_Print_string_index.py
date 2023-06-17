'''
Print characters from a string that are present at an even index number
Write a program to accept a string from the user and display characters that are 
present at an even index number.

For example, str = "pynative" so you should display p, n, t, v.
'''
i = 0
# Infinite loop
while True:
    user_input = input('Type or word here: ') # user entry
    word_len = len(user_input)
    # Check if the user wants Even or Odd chars
    even_odd_choice = input('Do you want even or odd index: ')
    # Verification about the EVEN/ODD entry
    # While even or odd not typed, it will maintain asking for the odd or even
    if even_odd_choice not in ['even','odd']:
        even_odd_choice = input('Do you want even or odd index: ')
    else:    
        # Loop for each choice
        if even_odd_choice.lower() == 'even': # Condition for even index
            for i in range(word_len): # For loop to show each char
                if i%2 == 0: # Condition to guarantee if the index is even
                    print(user_input[i]) # Show the str equivalent the index
        else: # CONDITION FOR ODD NUMBERS
            for i in range(word_len):
                if i%2 != 0:
                    print(user_input[i])
