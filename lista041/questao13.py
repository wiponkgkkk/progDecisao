'''
13) Desenvolver um programa que pergunte 3 valores (variáveis a, b e c) e ao final apresente-os dispostos em ordem
crescente
'''

# Input

a = int(input("Informe um valor: "))
b = int(input("Informe um valor: "))
c = int(input("Informe um valor: "))

# Condições e Prints

if(a > b):
    aux = a
    a = b
    b = aux

if(a > c):
    aux = a
    a = c
    c = aux

if( b > c ):
    aux = b
    b = c
    c = aux

    print(a,b,c, sep="\n")