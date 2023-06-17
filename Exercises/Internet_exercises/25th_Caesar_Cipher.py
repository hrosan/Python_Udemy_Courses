''' You'll code up a function to compute a Caesar cipher on text input. For this problem, 
you're free to use any part of the Python standard library to do the transform.

Hint: There's a function in the 'str' class that will make this task much easier!

Caesar Cipher (caesar.py)

A Caesar cipher is a simple substitution cipher in which each letter of the plain text is 
substituted with a letter found by moving n places down the alphabet. For example, assume the 
input plain text is the following:
                            abcd xyz
If the shift value, n, is 4, then the encrypted text would be the following:
                            efgh bcd
You are to write a function that accepts two arguments, a plain-text message and a number of 
letters to shift in the cipher. The function will return an encrypted string with all letters 
transformed and all punctuation and whitespace remaining unchanged.

Note: You can assume the plain text is all lowercase ASCII except for whitespace and 
punctuation.
'''
import string as strg # Importing string library

# importing ascii letter
main_word = "jklmn"
ascii_letters = strg.ascii_lowercase
mascara = ascii_letters[len(main_word):]+ascii_letters[:len(main_word)] 
            # ghijklmnopqrstuvwxyz + abcdef > depending on len(main_word)
print(mascara) # Output: ghijklmnopqrstuvwxyzabcdef
tran_word = str.maketrans(ascii_letters,mascara) # len(ascii_letters) == len(mascara)
print(tran_word) # Output: \/
'''
The maketrans() function is a method available in Python's str class. It is used to create a 
translation table that can be used with the translate() method to perform character-level 
replacements or transformations in a string.
The maketrans() function takes two arguments: x and y. Both x and y should be strings of equal 
length. Each character in x is mapped to the character at the corresponding index in y.
'''
x = main_word.translate(tran_word)
print(x) # Output - Translated word 
'''
Once you have the translation table, you can use it with the translate() method to perform the 
actual translation or replacement on a string. The translate() method takes the translation 
table as an argument.
'''
