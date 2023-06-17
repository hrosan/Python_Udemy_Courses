'''
Criar uma função que calcule a multiplicação de numeros passados p/ ela
'''
def multiplicacao(*args):
    acc = 1 # acumulador
    print(args)
    try:
        for item in args:
            acc *= item
        return acc
    except TypeError:
        num, *a = args
        for item in num:
            acc *= item
        return acc

numeros = 1,2,3,4,5
x = multiplicacao(*numeros)
y = multiplicacao(numeros) #
print(x,y)