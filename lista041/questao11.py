'''
11) Desenvolver um programa que pergunte um número inteiro de 3 algarismos e apresente como resultado
somente o algarismo das centenas.
'''

# Input

num = int(input("Informe um número de 3 algarismos: "))

# Condições e Input

if ( num >= 100 and num <= 999 ):
    print(f"O algarismo das centenas de {num} é" ,num // 100 )
else:
    print(f"O valor informado não possui 3 algarismos")
