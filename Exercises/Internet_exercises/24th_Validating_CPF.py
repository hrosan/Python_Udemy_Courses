'''
Create a program that validate a CPF number:
Ex: 746.824.890-70

How it works
O número de um CPF tem 9 algarismos e mais dois dígitos verificadores, 
que são indicados após uma barra. Logo, um CPF tem 11 algarismos. 
O número do CPF é escrito na forma ABCDEFGHI/JK ou diretamente como ABCDEFGHIJK, 
onde os algarismos não podem ser todos iguais entre si.

O J é chamado 1° dígito verificador do número do CPF.
O K é chamado 2° dígito verificador do número do CPF.

Primeiro Dígito
Para obter J multiplicamos A, B, C, D, E, F, G, H e I pelas constantes correspondentes:

A	B	C	D	E	F	G	H	I
x10	x9	x8	x7	x6	x5	x4	x3	x2
 O resultado da soma, 10A + 9B + 8C + 7D + 6E + 5F + 4G + 3H + 2I, é dividido por 11.

 Analisamos então o RESTO dessa divisão:

 Se for 0 ou 1, o dígito J é [0] (zero). Se for 2, 3, 4, 5, 6, 7, 8, 9 ou 10, o dígito J é 
 [11 - RESTO]

Segundo Dígito
Já temos J. Para obter K multiplicamos A, B, C, D, E, F, G, H, I e J pelas constantes 
correspondentes:

A	B	C	D	E	F	G	H	I	J
x11	x10	x9	x8	x7	x6	x5	x4	x3	x2
O resultado da soma, 11A + 10B + 9C + 8D + 7E + 6F + 5G + 4H + 3I + 2J, é dividido por 11.

Verificamos então o RESTO dessa divisão:

Se for 0 ou 1, o dígito K é [0] (zero). Se for 2, 3, 4, 5, 6, 7, 8, 9 ou 10, o dígito K é 
[11 - RESTO].
'''
import os, time, random

while True:
    os.system('cls') # Clear the prompt
    # Defining the variables
    CPF_number = "" # It starts as string because the ways it can be written

    # Getting the CPF number and Treating errors
    try:
        # Getting the CPF number
        for i in range(9):
            CPF_number += str(random.randint(0,9))
        if CPF_number.isnumeric() == False: # Getting error from alphabetic entry and symbols
            raise TypeError ("Invalid Input detected") # Raising Type error
        elif len(CPF_number) != 9: # Error about CPF lenght
            raise IndexError
    except TypeError as CPF_with_Aplhabetics_ASCII:
        print("Your Entry has Alphabetics or ASCII elements: ",CPF_number)
        time.sleep(5) # Wait 5 seconds until return to the init
    except IndexError as CPF_Index_Error:
        print(f"Your entry has a lenght of {len(CPF_number)} is different from expected (9 elements)")
        time.sleep(5) # Wait 5 seconds until return to the init
    
    # Calculating the J number from ABCDEFGHI-JK
    j_iterator = 10
    acc_j_num = 0
    rest_j = 0
    j = 0
    for number in CPF_number:
        acc_j_num += int(number)*j_iterator # Multiplicating and adding
        j_iterator -= 1
    j = 0 if acc_j_num%11 == (0 or 1) else 11-(acc_j_num%11)
    # Concatenating J with our CPF
    CPF_number += str(j)
    # Calculating the K from ABCDEFGHI-JK
    k_iterator = 11
    acc_k_num = 0
    rest_k = 0
    k = 0
    for number in CPF_number:
        acc_k_num += int(number)*k_iterator
        k_iterator -= 1
    k = 0 if acc_k_num%11 == (0 or 1) else 11-(acc_k_num%11)
    CPF_number +=str(k)
    print(f"Your CPF number is {CPF_number}")
    time.sleep(10)