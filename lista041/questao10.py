'''
10) Desenvolver um programa que pergunte dois números inteiros, e apresente como resultado se o segundo
número informado é ou não um divisor do primeiro número informado.
'''

# Input

num1 = int(input("Informe um número inteiro: "))
num2 = int(input("Informe um número inteiro: "))

# Cálculos

div = num2 % num1

# Condições e Prints

if div == 0:
    print(f"{num2} é divisor de {num1}")
else:
    print(f"{num2} não é divisor de {num1}")