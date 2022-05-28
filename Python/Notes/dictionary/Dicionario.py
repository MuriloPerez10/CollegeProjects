"""======== DICIONARIO EM PYTHON ========"""
import copy
#Dicionários são iguais a lista, só que com eles e possível mudar o nome do índice, invés do padrão numeral.

#Podemos os dicionários em casos como, criar uma lista de contatos, onde conseguimos identificar cada índice pelo nome, assim nos trazendo o valor correspondente ao nome.
#podemos criar a lista de varias formas
# jeito padrão(usado pela comunidade)
d1 = {
    'murilo':'1234-4561',
    'laura':'5555-555',
    'Evee':'9595-9696'
}
#Declarando a o Dicionário
d2 = dict(murilo='1234-5678',laura='5555-5555',Evee='9595-9696')

#Usando a função construtora dict()
#Através dela conseguimos transformar uma lista ou tupla em um dicionário
# ======== ATENÇÃO ====> so cnseguimos montar caso aja dados duplos como no exmplo abaixo
lista = [('murilo','1234-4561'),
    ('laura','5555-555'),
    ('Evee','9595-9696')]
d3 = dict(lista)

#Nos dicionários e possível criar filhos dentro deles, olhe o exemplo abaixo
cliente = {
    'cliente1' : { #criação do dicionario dentro do dicionario
        'nome':'Murilo',
        'sobrenome':'Perez'
    },
    'cliente2' : { 
        'nome':'Laura',
        'sobrenome':'Silva'
    },
}
#para acessar o itens
#print('diconarios filhos = ',cliente['cliente2']['sobrenome'])


# Caso queria uma copia para em uma variável do dicionário, recomendasse que use a função .copy() -> para se ter uma copia rasa(Referencia de valores) da sua lista, onde a variavel que recebeu essa copia possa modificar um valor do dicionario sem que modifique o dicionario root
d4 = {1:'a', 2:'b', 3:'c', 4:'d',5:['murilo','perez']}
'''v = d4.copy() # copia de referenca
v[5][0] = 'banana'
print(v)
print(d4) #aqui podemos ver que ele altero o dicionario filho
''' 

# para que essa situação não aconteça usamos a função deepcopy() ou copia profunda da biblioteca copy
v = copy.deepcopy(d4) #fazendo a copia do dicionario, por completo
v[5][0] = 'banana' 
#teste para ver se o filho na dicionario root teve o filho modificado tambem como no v
print(v) # aqui podemos ver que a alteração so ocorreu no v, graça o deepcopy()
print(d4)

# ===== FUNÇÔES COM DICIONARIOS =======

d4.update() #adiciona um valo ao dicionario
d4.pop() #exclui um indice especifico por completo 
#tambebom podemos usr o del para deletear um indice especifico
del d4[1]
#d4.popitem() #exclui o ultimo indice
print(d4)