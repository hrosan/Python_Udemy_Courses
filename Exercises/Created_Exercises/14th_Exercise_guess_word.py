
import os
secret_word = "gato"
correct_letter = ""
user_tries = 0
while True:

    user_input = input("Digite uma letra: ")

    # 1 Letter condition, if user type more than 1 letter he/she will type again
    if len(user_input) > 1:
        print('Digite apenas uma letra!')
        user_tries += 1
        continue
    # Showing the letter that is within the secret word
    if user_input in secret_word:
        correct_letter += user_input # accumulator
    
    writing_word = "" # Variable to accumulate the letters
    # Loop to show the word and the * for every guess
    for secret_letter in secret_word:
        # Condition to show every letter
        if secret_letter in correct_letter: # secret letter must to be a correct letter
            writing_word += secret_letter # Showing the secret word in every turn
        else:
            writing_word += "*" # Putting an * to hide a letter
    # Showinh the hidden word
    print('Written word: ', writing_word)
    # Condition to finish the game
    if writing_word == secret_word:
        os.system('cls')
        print("You win!! Congratulations")
        print('Number of tries: ', user_tries)
        user_tries = 0
    user_tries += 1
