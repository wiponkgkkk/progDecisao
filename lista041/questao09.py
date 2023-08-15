'''
9) Desenvolver um programa que pergunte um número e exiba a informação de que ele é positivo, negativo ou
nulo.
'''

# Input

num = int(input("Informe um número: "))

# Condições e Prints

if num > 0:
    print("O número é positivo")
elif num == 0:
    print("O número é nulo")
else:
    print("O número é negativo")