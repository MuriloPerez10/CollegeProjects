'''
Entrada de dados
'''

nome = input("qual seu nome? \n")
AnoNas = input('qual o ano que você nasceu? \n')
#Para trasnformar basta mudar o tipo de str para tipo int
idade = 2022 - int(AnoNas)

print(f'O usuario se chama {nome} rla é uma {type(nome)}')
print(f'O usuario se chama {nome} tem a idade igual a {idade}')

