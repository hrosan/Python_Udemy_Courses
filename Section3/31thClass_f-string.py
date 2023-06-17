'''
Introdução a formatação de strings
'''

#Informações pessoais
nome = 'Henrique'
altura = 1.72
peso = 77.4

#Calculo do IMC
imc_calc = peso/(altura**2)

#apresentação 
print('Olá',nome, 'seu IMC é:',imc_calc,sep=" ")

string_exemplo = f'Olá {nome}, seu IMC é: {imc_calc:.1f}' #Aqui a string está sendo formatada
'''Uma variavel a ser alocada dentro de uma string deve estar entre chaves {}
Para o numero de casas de um numero de ponto flutuante {nome_var:.xf} | x = numero de casas
decimais'''

# EXEMPLO DE F-STRING
print(string_exemplo) # Mostra a String formatada