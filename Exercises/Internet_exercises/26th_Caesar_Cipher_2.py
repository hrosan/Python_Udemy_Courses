'''you'll solve the Caesar cipher again, but this time you'll do it without using .
translate().'''

import string

def shift_n(letter, table):
    try:
        index = string.ascii_lowercase.index(letter)
        return table[index]
    except ValueError:
        return letter

def caesar(message, amount):
    amount = amount % 26
    table = string.ascii_lowercase[amount:] + string.ascii_lowercase[:amount]
    enc_list = [shift_n(letter, table) for letter in message]
    return "".join(enc_list)


message = "Chorou"
caesar_word = caesar(message.lower(),len(message))
print(caesar_word)