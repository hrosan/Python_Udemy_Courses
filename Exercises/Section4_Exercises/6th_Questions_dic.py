
from os import system

questions = [
    {'question': 'Quanto é 2^2?',
     'options': ['3','4','2','1'],
     'answer': '4'},
     {'question': 'Quanto é 5*2?',
     'options': ['10','7','25','3'],
     'answer': '10'},
     {'question': 'Qual desses numeros é primo?',
     'options': ['15','17','25','33'],
     'answer': '17'},
     {'question': 'Quanto é 90/3 ?',
     'options': ['12','107','90','30'],
     'answer': '30'}
]

while True:
    answer = "" # Variable to get the correct answer
    chances = 2
    for quizzes in questions:
        system('cls') # Just to clean the prompt
        print(quizzes['question']) # Show the question

        for index, value in enumerate(quizzes['options']):
            print(f'{index+1})',value)

        answer = input(f'What your answer ({chances+1} chances) : ')
        while answer != quizzes['answer']:
            chances -= 1 # Reducing the chances
            answer = input(f'What your answer ({chances+1} chances): ')
            if chances == 0:
                print('You lose, try again!')
                break
            
        if answer == quizzes['answer']:
            print("You're right, go to next question!!")
    break    
    

