'''
4) Desenvolver um programa que pergunte um valor numérico inteiro e faça a exibição desse valor caso seja
divisível por 4 e 5. Não sendo divisível por 4 e 5, o programa deverá exibir a mensagem “Valor não é divisível por
4 e 5”.
'''

# Inputs

num = int(input("Me informe um valor: "))

# Cálculos

num1 = num % 4 and 5

# Condições e Prints

if ( num1 == 0 ):
    print(f"{num} é divisivel por 4 e 5.")
else:
    print(f"{num} não é divisivel por 4 e 5.")