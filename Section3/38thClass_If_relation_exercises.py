# INSERIR DOIS VALORES E MOSTRAR QUAL DOS VALORES É MAIOR

primeiro_valor = int(input('Digite um valor: ')) # Inserir o primeiro valor
segundo_valor = int(input('Digite um segundo valor: ')) # Inserção do segundo valor

# COMPARATIVOS
comparativo1 = primeiro_valor > segundo_valor # PRIMEIRO MAIOR QUE SEGUNDO
comparativo2 = primeiro_valor < segundo_valor # PRIMEIRO MENOR QUE SEGUNDO
comparativo3 = primeiro_valor == segundo_valor # PRIMEIRO IGUAL AO SEGUNDO

if(comparativo1): # Se comparativo1 for Verdadeiro
    print(f'{primeiro_valor} é o maior')
elif(comparativo2): # Se comparativo2 for verdadeiro
    print(f'{segundo_valor} é o maior')
else:
    print(f'{primeiro_valor} e {segundo_valor} são iguais')