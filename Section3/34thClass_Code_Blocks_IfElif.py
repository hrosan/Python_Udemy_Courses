'''
if, elif, and else are used to create conditional statements.
These statements allow your program to make decisions based on certain conditions.
'''
# example of how to use if, elif, and else:

entrada = input('Informe um valor: ') # entrada de valores, retorna uma string
x = int(entrada) # transforma a entrada em um valor inteiro
if x > 10: # primeira condicional, x maior que 10
    print("x is greater than 10")
elif x < 10: # segunda condicional, x menor que 10
    print("x is less than 10")
else: # terceira condicional
    print("x is equal to 10")
# Note that the elif statement is optional and you can have as many of them as you need to test additional conditions.
