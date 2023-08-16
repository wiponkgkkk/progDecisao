'''
10. Fazer um algoritmo que pergunte o nome do aluno, e as notas das provas 1 e 2. Deverá ser exibida na tela
como resposta a média do aluno, e se ele está aprovado, reprovado ou em prova final. Estas condições
devem seguir as regras da tabela abaixo:
Média Situação
Abaixo de 3,0 Reprovado
Entre 3,0 e 6,9 Prova Final
A partir de 7,0 Aprovado
'''

# Inputs

nome = input("Informe seu Nome: ")
nota1 = float(input("Informe sua nota na prova 1: "))
nota2 = float(input("Informe sua nota na prova 2: "))

# Calculos

media = nota1 + nota2 / 2

# Condições e Prints

if media < 3.0:
    print("Você está reprovado")
elif media > 3.0 and media < 6.9:
    print("Você está de prova final")
else:
    print("Você está aprovado")

