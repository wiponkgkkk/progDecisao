'''
11) Desenvolver um programa que pergunte um número inteiro de 3 algarismos e apresente como resultado
somente o algarismo das centenas.
'''

# Input

num = int(input("Informe um número de 3 algarismos: "))

# Condições e Input

if num > 99:
    print(int(num * 10 / 10))