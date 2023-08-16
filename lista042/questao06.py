'''
6. Fazer um algoritmo que pergunte o ano de nascimento de uma pessoa e o ano atual. Ao final o algoritmo
deverá exibir na tela a idade da pessoa. Porém, se o usuário inserir o ano de nascimento com valor maior
que o ano atual, o cálculo de idade não deverá ser feito, e então deverá surgir a seguinte mensagem na tela:
“Dados inseridos estão incorretos”.
'''

# Inputs

idade = int(input("Informe seu ano de nascimento: "))
idade2 = int(input("Informe o ano atual: "))

# Cálculos

idade3 = idade2-idade

#Condições e Prints

if idade > idade2:
    print("Dados inseridos estão incorretos")
else:
    print(f"Você tem {idade3} anos")

