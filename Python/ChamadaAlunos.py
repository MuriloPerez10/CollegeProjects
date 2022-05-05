'''
OBJETIVO: Fazer um algoritimo, onde a professora possa colocar o nome do alunos, e depois
o algoritimo colocara todos o nomes na tela e iá falar quanto alunos foram adicionados
'''

#Programa de chamada de alunos
print(5*'=','Bem-Vindo ao Programa de chamada automatica',5*'=')
alunos = []
nome = ''
while True:
    #adição do alunos na lista
    nome = input("insira o nome do aluno que deseja entrar na lista de chamada: ")
    if not nome == nome.isnumeric():
        print('Por favor insira um nome não um numero')
    else:
        alunos.append(nome)


    saida = input("Deseja adicionar mais um aluno? S[Sim]/N[Não]:")
    if saida == 'n' or saida == 'N':
        break

TotalAlunos  = len(alunos)
i = 0
print(f"você tem um total de {len(alunos)} em sua lista de chamada, \n Os alunos na lista são:")
while i<TotalAlunos:
    print(alunos[i])
    i+=1