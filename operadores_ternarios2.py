'''
Crie um programa que pergunte a idade do usuário e em seguida informe se
este usuário é menor de idade ou maior de idade.
'''

# Inputs

idade = int(input("Informe a sua idade:"))

# Condições e Prints
#lógica do op ternário2:
#var = resultado_verdadeiro if teste_condicional else resultado_falso


resposta = "maior de idade" if idade >= 18 else "menor de idade"
print("Você é", resposta)