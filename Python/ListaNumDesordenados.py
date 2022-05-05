'''
OBJETIVO: Faz com que o usuário escolha de dez números inteiros
em ordem aleatorio e depois o algoritimo irá falar qual o maior e qual o menor
'''

#5 De uma lista de dez números desordenados, encontre e mostre o maioi = []
contador = 0
while True:
    num = input("Fale um numero: ")
    #validação se o que foi escrito é realmete um número
    if not num.isnumeric() == True:
        print("Por favor insira um numero")
    else:
        num = int(num)

        i.append(num)
        contador += 1

        if contador == 10:
            break

print(f"o maior numero da lista d numeros citado é {max(i)}")
print(f"o menor numero da lista d numeros citado é {min(i)}")