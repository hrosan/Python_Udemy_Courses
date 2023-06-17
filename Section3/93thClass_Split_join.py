import os
os.system('cls')
frase = 'Uma frase qualquer que podemos escrever aqui'
lista_palavras = frase.split(" ") # Break the phrase every time space occurs
print(lista_palavras)

frase = "**".join(lista_palavras)
print(frase)