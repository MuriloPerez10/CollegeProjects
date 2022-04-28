"""
Dentro do laço de repetição temos a possbilidade de usar
a expressão ELSE para que faça alguma coisa que voce queira no momento que
o laço se tornar falso, por Exemplo

contador = 1
acumulador = 1
while(contador<10):
    print(contador, acumulador)
    acumulador += contador
    contador+=1
else:
    print('o laço aponto como falso e posso fazer alguma coisa agora')
    contador = 0
    while(contador<2):
        print("criei outro laço")
        contador+=1

print('\n \n aqui o programa acaba')
"""


"""
#aqui vemos o funcionamento de um WHILE padrão

i = 0
while(i<=100):
    print(i)
    i += 1
    if (i == 33):
        break
"""
"""
#laços interligados, ou seja um teremos um laço de outro
x = 0
y = 0

while(x<2):
    y = 0
    while(y<5):
        print(f"o X esta no numero {x} e o Y está {y}")
        y +=1
    x+=1
print("acabou")
"""

#A quase calculadora
print(30*'=',"Bem vinda a quase uma calculadora",30*'=','\n')
while True:
    n1 = input("digite um número: ")
    n2 = input("digite um número: ")
    operador = input("digite um operador:")

    # A função isnumeric() verifica se a string so possue numeros
    if not n1.isnumeric() or not n2.isnumeric():
        print('Por favor digite um numero ou operador desejado')
        continue

    n1 = int(n1)
    n2 = int(n2)

    if operador == '+':
        print(n1 + n2)
    elif operador == '-':
        print(n1 - n2)
    elif operador == '*':
        print(n1 * n2)
    elif operador == '/':
        print(n1 + n2)

    sair = input("deseja sair da calculadora? Sim[s]/Não[n]: ")
    if sair == 's' or sair == 'S':
        break

print('obrigado por usar nossa caluladora')

