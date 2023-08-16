'''
4. Fazer um algoritmo que peça um número de 1 a 7, e ao final, informe o dia da semana (por extenso)
correspondente ao número que foi inserido. Informar também a mensagem “número inválido” quando o
número inserido não corresponder à um dia da semana.
'''

# Inputs

dia = int(input("Informe um número de 1 a 7: "))

# Condições e Prints

if dia == 1:
    print("Segunda-Feira")
elif dia == 2:
    print("Terça-Feira")
elif dia == 3:
    print("Quarta-Feira")
elif dia == 4:
    print("Quinta-Feira")
elif dia == 5:
    print("Sexta-Feira")
elif dia == 6:
    print("Sabádo")
elif dia == 7:
    print("Domingo")
else:
    print("Número inválido")