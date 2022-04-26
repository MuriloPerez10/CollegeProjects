# ==== calculadora de IMC ====
nome = "BOB"
idade = 20
altura = 1.76
maior_de_idade = idade > 18
peso = 58
imc = peso/(altura**2)

#Podemos escrevr a string de tres formas diferente inves dessa forma que usamos
# print("ola ", nome , "voce tem " , idade , "anos \n seu Imc e " ,imc )
# == FORMA 1 ==
print(f'ola {nome} voce tem {idade} anos e seu IMC é {imc:.2f}')
# == FORMA 2 ==
print('ola {} voce tem {} anos e seu IMC é {:.2f}'.format(nome,idade,imc))
# == FORMA 3 ==
print('ola {n} voce tem {i} anos e seu IMC é {im:.2f}'.format(n=nome,i=idade,im=imc))