'''
3) Desenvolver um programa que pergunte um número, e apresente como resposta se o referido número é par ou
é ímpar.
'''

# Input

num = int(input("Escolha um número: "))

# Cálculos

num1 = num%2

# Condições e Prints

if (num1 == 1):
    print("é impar")

else:
    print("é par")