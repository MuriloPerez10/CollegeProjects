'''
Formatando valores com modificadores

:s - texto (string)
:d - Inteiros (int)
:f - Numeros de ponto flutuante (float)
:.(numero)f - Quantidade de casas decimais (float)
:(caractere) (> ou < ou ^) (quantidade) (tipo - s, d ou f)

> - Esquerda
< - Direita
^ -  Centro
'''

# :(caractere) (> ou < ou ^) (quantidade) (tipo - s, d ou f)
#ele ira colocar carcteres ao redor da palvara podendo ser usado de duas formas
nome = ' BANANA'
var = 100
#forma mais recomendada
nome_formatado = '{:=^50}'.format(nome) #com strings
Var_formatado = '{:-^50}'.format(var) #com numeros
print(nome_formatado)
print(Var_formatado)
#outra forma
print(f'{nome:#^50}')
print(f'{var:*^50}')

#Mechendo com indices
nome_formatado = '{1:@^50} {0:$^50}'.format(nome, var) # posição 1 = var e posiçao 0 = nome
print(nome_formatado)


#modificando o tamanho da letra
print(70*'-', '\n Mechendo com indices \n',70*'-')

print(nome.lower()) # Tudo minusculo
print(nome.upper()) # Tudo maiusculo
print(nome.title()) # Letras  iniciais maiusculas

#acessando um indice especifico de uma string
print(70*'-', '\n acessando um indice especifico de uma string \n',70*'-')

print(nome[2])
print(nome[2:6]) #pegando uma parte do codigo (fatiamento)
print(nome[-1]) #Usando -1 você tem acesso ao ultimo Carac.

