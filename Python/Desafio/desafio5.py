'''
Vamos fazer um programa para verificar quem é o assassino de um crime. Para descobrir o
assassino, a polícia faz um pequeno questionário com 5 perguntas onde a resposta só pode ser
sim ou não:
1. Mora perto da vítima?
2. Já trabalhou com a vítima?
3. Telefonou para a vítima?
4. Esteve no local do crime?
5. Devia para a vítima?
Cada resposta sim dá um ponto para o suspeito. A polícia considera que os suspeitos com 5
pontos são os assassinos, com 4 a 3 pontos são cúmplices e 2 pontos são apenas suspeitos,
necessitando de outras investigações. Valores abaixo de 2 são liberados.
No seu programa, você deve fazer essas perguntas e, de acordo com as respostas do usuário,
você vai informar como a polícia o considera.
'''

pontos = 0
print(25*'=','Bem vindo ao Jogo detetive',25*'=')
while True:
    P1 = input('Mora perto da vítima? s[Sim]/n[Não]: ')
    if P1 == 'S' or P1 == 's':
        pontos += 1
    
    P2 = input('Já trabalhou com a vítima? s[Sim]/n[Não]: ')
    if P2 == 'S' or P2 == 's':
        pontos += 1
    
    P3 = input('Telefonou para a vítima? s[Sim]/n[Não]: ')
    if P3 == 'S' or P3 == 's':
        pontos += 1
    
    P4 = input('Esteve no local do crime? s[Sim]/n[Não]: ')
    if P4 == 'S' or P4 == 's':
        pontos += 1
    
    P5 = input('Devia para a vítima? s[Sim]/n[Não]: ')
    if P5 == 'S' or P5 == 's':
        pontos += 1
    
    break

if pontos == 5:
    print('Voce é o assassino!!')
elif pontos == 4 or pontos == 3:
    print('voce tem de vir com a gente, pois e um cumplice')
elif pontos == 2:
    print('Nos acompanhe ate a delegacias, voce e suspeito')
else:
    print('Voce está liberado')