'''
    Uma loja de produtos eletronicos com vendas regulares opta por contratar uma equipe p/ organização de um
sistema de gerenciamento de vendas. Seu desafio será elaborar um algoritmo que, a partir de dados de entrada
fornecidos pelo usuario, calcule o valor da venda de um produto, exibindo uma saida em video contendo o código
do produto, o nome, a quantidade comprada, o valor unitario e o valor total.

        Input:
            Main variables
                * Nome_produto
                * valor_produto
                * código_produto
            Secondary
                * product_quantity
        Output:
            Output list
                * Nome_produto
                * Valor_produto
                * Cod_produto
                * Quantidade comprada
                * Valor Unitario
                * Valor total
'''
# Importing libraries
import random as rd

# Functions initializing 
def product_enroll(name,value):
    """Create a dictionary with a name and value from a specific product, and returns a dictionary
    with product Name, Value and Code.
    Args:
        name (str): String value representing the product's name 
        value (float): floating number representing the product's value

    Returns:
        {code: "","Name":"","Value":0.0}: A dictionary that contains some informations about a product
    """
    return {'code':code_generator(),
            'Name': name,
            'Value': value}

def code_generator():
    """
    Generate a key-value for a specific product type
    Returns:
        _type_: _description_
    """
    code = "" # Code is a string to concatenate every number from 0 to 9
    for _ in range(5):
        code += str(rd.randint(0,9))
    return code

# Variables
product_name = "" # Every product has a name
product_value = 0.0 # Every product has its value
product_list = [] # List to be used as data base


# Product enrollment
for _ in range(2):
    product_name = input('Type the name of the item: ') # Get the product name
    product_value = float(input('Type the value of the item: ')) # Get the product value
    product_list.append(product_enroll(product_name,product_value)) # Add the product into a "database"
print(product_list)
