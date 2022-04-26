'''
* Crair variáveis para nome (str), idade (int),
* altura (float) e peso (float) de uma pessoa
* Criar variável com o no atual (int)
* Obter o ano de nascimento da pessoa (baseando na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto co todos os valores na tela usando F-string (com as chaves)
'''

nome = "mario"
ano_nasciment = 2002
altura = 1.75
peso = 59.50
ano = 2022
imc = peso/altura**2
idade = ano - ano_nasciment

print(f" Olá seu {nome} , o senho nasceu no ano de {ano_nasciment} entao voce tem {idade} anos de idade, tem o peso {peso} e {altura} de altura \n Seu IMC e {imc:.1f}")