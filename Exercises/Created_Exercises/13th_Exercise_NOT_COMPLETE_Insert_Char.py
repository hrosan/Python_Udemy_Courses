'''
Try to insert a char during the iteration when the iteration hit a blanck space
'''

# While loop
while True:
    # User input data
    user_input = input('Insert a char string')
    blank_space = " " # Comparison
    i = 0 # Starts with 0
    check_string = ""
    while i < len(user_input):
        check_string = user_input[i] # check string receiving the actual number
        if check_string == " ":
            user_input[i] = user_input[i]+"*" # * concatenation
        i += 1 # Iterator
    print(f'{user_input}')