'''
2. Fazer um algoritmo que peça um número, e ao final, informe se o número está abaixo de 1000, entre 1000 e
5000, ou acima de 5000

'''


# Inputs

num = int(input("Informe um número: "))

# Condições e Prints

if num < 1000:
    print("O numero informado está abaixo de 1000")
elif num > 1000 and num < 5000:
    print("O número informado está entre 1000 e 5000")
else:
    print("O número informado está acima de 5000")