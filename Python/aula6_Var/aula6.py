"""
As variaveis sempre devem iniciar com letra, pode conter numeros, separar com _, letras minusculas
"""
# ==== calculadora de IMC ====
nome = "BOB"
idade = 20
altura = 1.76
maior_de_idade = idade > 18
peso = 58
imc = peso//(altura**2)

print("ola ", nome , "voce tem " , idade , "anos \n seu Imc e " ,imc )