'''
OBJETIVO: O usuário pode digitar 10 palavras da prefrência dele,mas não pode ser um númerico,
depois o algoritimo irá mostra na tela todas a palavras digitadas
'''

#8 Ordene uma lista de 10 palavras recebidas pela pessoa, as palavras serão digitadas uma por vez.
i = []
c = 0
while True:
    palavra = input("Escreva uma palavra: ")

    #Vaidação se a palavra digitada não tem um número
    if palavra.isnumeric() == True:
        print("Por favor Escreva uma palavra e não um numero")
    else:
        i.append(palavra)

        if c > 8:
            break
    c += 1
Cont =  0
while (Cont<10):
    print(i[Cont])
    Cont+=1