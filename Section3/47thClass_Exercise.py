'''
Peça ao usuario p/ digitar - Nome, e idade
Se ambos forem digitados, exiba:
    Nome
    Nome invertido
    Se o nome contém espaços
    Quantidade de letras no nome
    A primeira letra do seu nome
    A ultima letra do seu nome
Se nada for digitado, envie a msg "Você deixou campos vazios"
'''
# Informações pessoais
nome_completo = 'Henrique' #input('Informe seu nome:')
idade = 29 # input('Informe sua idade:')

# Check de informações
nome_vazio = nome_completo=="" # compara se o nome completo está vazio
idade_vazia = idade=="" # compara se a idade está vazia


if(nome_vazio or idade_vazia): # Verifica as condições se existe input vazio
    print("Desculpe você deixou campos vazios")
elif not(nome_vazio and idade_vazia): # Verifica as condições de não vazio
    int_idade = int(idade) # Transformando idade em inteiro
    print(f'Seu nome é: {nome_completo}')
    print(f'Seu nome invertido é: {nome_completo[::-1]}')
    if " " in nome_completo:
        print('Você digitou espaços em seu nome completo')
    else:
        print('Você não digitou espaços em seu nome!')
    comprimento_nome = len(nome_completo)
    print(f'Seu nome tem {comprimento_nome} caracteres')
    print(f'A primeira letra do seu nome é {nome_completo[0:1:1]}') # Mostra a primeira letra do nome
    #It takes the last letter inside the string and goes to lenght-2 just taking the last letter 
    print(f'A ultima letra do seu nome é {nome_completo[comprimento_nome:comprimento_nome-2:-1]}')