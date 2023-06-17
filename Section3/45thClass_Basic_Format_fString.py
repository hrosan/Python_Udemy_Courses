'''
Formatação basica de strings
s - string
d - int
f - float
.<numero de digitos>f - Qtde de casas decimais
x ou X - Hexadecimal
(caractere)(><^)(quantidade)
    > Esquerda
    < Direita
    ^ centro
Sinal - + ou -
Exemplo:
    0>-100,.1f
Conversion flag - !r !s !a
'''

var = 'ABC_123'
print(f'{var}')
print(f'{var: <10}') # padding p/ esquerda
print(f'{var:-^10}') # padding p/ centro
print(f'{var:>10}') # padding p/ direita
print(f'{1452532.4589657:-,.2f}')