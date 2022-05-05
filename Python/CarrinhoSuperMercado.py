'''
OBJETIVO: Criar um sistema de Carrinho de super mercado, onde o usuário possa colocar
itens no carrinho, sem um número limite, e no fim mostrar quantos itens ele tem no carinho
'''

#Mercado
carrinho = []
saida = ''
print(5*'=','Bem vindo ao mercado seu Zé, fique a vontade para suas compras',5*'=')

while True:
    #adição de itens n lista
    iten = input('Fale um iten para colocar no carrinho: ')
    carrinho.append(iten)
    #validação de saida
    saida = input('deseja encerrar sua compra S[Sim]/N[Não]')
    if saida == 's' or saida == 'S':
        break

print(f'no seu carrinho tem {len(carrinho)}')
