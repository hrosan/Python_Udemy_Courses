'''Return the count of a given substring from a string
Write a program to find how many times substring “Emma” appears in the given string.'''

# Infinite loop
while True:
    # variables introduction
    searched_word = '' # Word that we need to count
    word_count_times = 0
    # User input
    user_phrase = input('Input your phrase here: ') # Phrase to check
    searched_word = input('Which word do you want to count: ') # Word to be serched
    # Check the word
    word_count_times = user_phrase.count(searched_word)
    print(f'There are {word_count_times} of "{searched_word}" word')
