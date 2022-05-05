'''
For in em Python
Iterando com strings
Função range(start=0, stop, step=1) -> retorna numeros em sequeço do
parametro stop
step = igual o numero de indices a seguir EX: 2 = pular de 2 em 2
'''

#Aqui temos uma função padrao com range()
for n in range(2,10): #começa em 2 e vai contando até o número 10
    print(n)

print(30*'-')

#Aqui temos uma função reversa com range()
for b in range(30,2,-5): # começa no 30 e vai descendo ate 2 pulando 5 em 5
    print(b)

print(30*'-')

#podemos usar o For in para adquir a quantidade especifca de indices
word = 'python'
NewWord = ''
for qn in word:
    print(qn) # podendo montar o programa de interação
    NewWord+=qn
print(NewWord)
