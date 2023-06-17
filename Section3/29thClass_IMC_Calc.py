'''
Calcular o IMC de uma pessoal
'''
#Informações pessoais
nome = 'Henrique'
altura = 1.72
peso = 77.4

#Calculo do IMC
imc_calc = peso/(altura**2)

#apresentação 
print('Olá',nome, 'seu IMC é:',imc_calc,sep=" ")