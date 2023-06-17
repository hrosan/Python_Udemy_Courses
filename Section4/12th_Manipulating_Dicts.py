pessoa = {
    'name': "Henrique", 'surname': 'Rosan',
    'address':[{
        'street': 'minha rua', 'number': 123},
        {'street': 'minha rua2', 'number': 456}]
}

for key in pessoa:
    print(key) # Output each key inside DICT
    print(pessoa[key]) # Each value inside each key

# acessing the Dict inside adress
print(pessoa['address']) 
# Output [{'street': 'minha rua', 'number': 123}, {'street': 'minha rua2', 'number': 456}]
print(pessoa['address'][1])
# Output {'street': 'minha rua2', 'number': 456}
print(pessoa['address'][0])       
# Output {'street': 'minha rua', 'number': 123}
# ------------------------------------------------------------- #
# Acessing each dict inside Adress dicts
print(pessoa['address'][0]['street']) # Output > minha rua
print(pessoa['address'][0]['number']) # Output > 123

# Acquiring a dict's key 
print(pessoa.get('address'[0]))
# Output > minha rua, 123
student_scores = {'John': 85, 'Emily': 92, 'James': 78}

# Get the score for 'John'
john_score = student_scores.get('John')
print(john_score)  # Output: 85

# Get the score for 'Alice' (key not found)
alice_score = student_scores.get('Alice')
print(alice_score)  # Output: None

# Get the score for 'Alice' with a default value
alice_score = student_scores.get('Alice', 0)
print(alice_score)  # Output: 0