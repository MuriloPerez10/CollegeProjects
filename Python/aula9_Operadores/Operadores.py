'''
Operadores realacionais
> < >= <= != == ===
-------------------------------------
Operadores condiocionais
IF ELIF ELSE
-------------------------------------
Operadores Lógicos
and, or, not in e not in

--> AND <---
(true and true) = true
(true and falso) = false

---> OR <---
(true and false) = true

---> NOT (INVERSE) <---
ele inverte o valor verdadeiro
a = 10  b = 11
( not b > a ) = false

---> IN ( Contém ) <---
nome = "banana"
if "a" in nome:
    print(true)

'''
'''
var1 = 10
var2 = 20

if var1<var2 or var2==20:
    print("verdadeiro")
else:
    print('falso')
'''
#Pograma para Verificar se pessoa pode ou nao beber
'''
bebida = input('Ola boa noite o que gostaria de tomar? \n')
idade = input('quantos anos o senhor tem? \n')
idade = int(idade)

if idade >= 18:
    print(f'Bom, uma {bebida} saindo ')
else:
    print(f'desculpe, o senhor nao pode ingerir bebeidas alcoolicas, pois voce tem {idade} anos')
'''

n1 = 0
n2 = 0

if n1 != n2:
    print('true')
else:
    print('false')


