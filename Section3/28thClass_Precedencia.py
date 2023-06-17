'''
Para calculos matematicos existe uma precedencia nos calculos que é
    1. (n + m) - PARENTESIS
    2. ** - EXPONENCIAÇÃO
    3. * / // % - MULTIPLICAÇÃO E OPERADORES DE DIVISÃO
    4. + - - SOMA E SUBTRAÇÃO
'''
n1 = int(3)
n2 = float(4.25)
exp = int(3)
div = float(5.25)

# EXEMPLO
conta_1 = (1+5)*3/4**2 # SIMPLES
print(conta_1)

# Exemplo 2
conta_2 = 2*n1*(n2+n1/div)**exp
print(conta_2)