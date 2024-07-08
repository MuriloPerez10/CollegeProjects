print("lista de compra")

import os

lista_compra = []

while True:
    print("Seleciona uma opção:")
    botao = input("[i]nserir [a]pagar [l]istar:")

    if len(botao) > 1:    
        print("Não consegui entender o que selecionou, tente novamente")
        continue

    if botao.lower() == "i":
        valor_inserido = input("Valor: ")
        lista_compra.append(valor_inserido)

    
    if botao.lower() == "a":
        os.system('cls')
        valor_inserido = ""
        while True:
            valor_inserido = input("Digite o numero para apagar: ")
            if valor_inserido.isdigit():
                break
            else:
                print("insira um valor valido")
        valor_inserido = int(valor_inserido)
        lista_compra.pop(valor_inserido)
        
    if botao.lower() == "l":
        os.system('clear')
        for ordem, produto in enumerate(lista_compra):
            print(ordem, produto)

        
        