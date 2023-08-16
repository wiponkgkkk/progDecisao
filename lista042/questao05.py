'''
5. Fazer um algoritmo que pergunte a sigla de um estado brasileiro (UF -> Unidade Federativa), e ao final,
informe na tela se o estado inserido está ou não na região Sudeste.
'''

# Input

estado = input("Informe a sigla de um estado brasileiro: ")

# Condições e Prints

if estado == 'ES' or estado == 'MG' or estado == 'RJ' or estado == 'SP':
    print("O estado inserido está na Região Sudeste")
else:
    print("O estado inserido não está na Região Sudeste")