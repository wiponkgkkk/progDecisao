'''
5) Desenvolver um programa que pergunte 4 notas escolares de um aluno e exiba mensagem informando que o
aluno foi aprovado se a média escolar for maior ou igual a 5. Se o aluno não foi aprovado, indicar uma
mensagem informando essa condição. Apresentar junto com a mensagem de aprovação ou reprovação o valor
da média obtida pelo aluno.
'''

# Inputs

num1 = float(input("Me informe sua nota: "))
num2 = float(input("Me informe sua nota: "))
num3 = float(input("Me informe sua nota: "))
num4 = float(input("Me informe sua nota: "))

# Cálculos

media = ((num1 + num2 + num3 + num4) / 4)

# Condições e Prints

if ( num1 + num2 + num3 + num4 / 4 ) >= 5:
    print(f"Parabéns você foi aprovado sua média foi {media:.2f}")
else:
    print(f"Infelzimente você foi reprovado o valor de sua média foi {media:.2f}")
