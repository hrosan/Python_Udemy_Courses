'''
Interpolação básica de strings
s - strings
d e i - int
f - float
x e X - Hexadecimal (0123456789ABCDEF)
'''
nome = 'Henrique'
preço = 11.15488968
variavel = '%s, o preço é R$%.2f' %(nome, preço)
print(variavel)

hexa = 'O Hexadecimal de %d é %04x' %(1020,1020)
print(hexa)