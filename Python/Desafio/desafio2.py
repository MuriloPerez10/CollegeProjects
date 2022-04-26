'''
programa para o usuario digitar um numero inteiro e informa
a ele se é par ou impar,
e fazer uma verificaçõa de o numero e um inteiro ou não
'''

"""
print(10*'=','Welcome Program verificador impar/par ' ,end=10*'=')
num = input(" \n Digite o numero a ser verificado: ")
try:
    num = int(num)
    if type(num) == int:
        if num%2 == 0:
            print(f" o número {num} é par")
        else:
            print(f"o numero {num} é impar")
except:
    print("o numero digitado não e um valor inteiro")
"""


'''
Programa que pergunta a hora para o usuário, baseando-se no horário
descrito, exiba a saudação apropriada
Bom dia (0-11), Boa tarde (12-17) e Boa noite (18-23)
'''
"""
hora = input('Olá caro usuário, você saberia me fala que horas são: ')
try:
    hora = int(hora)
    if hora >= 0 and hora <= 11:
        print('Bom Diaa caro usuário')
    elif hora >= 12 and hora < 17:
            print('Boa tarde caro usuário')
    else:
        print("Boa noite caro usuário")

except:
    print('Desculpa, nao entendi o que escreveu, tente falar a hora com numeros'
          ' por exemplo: 11')
"""

'''
Programa que pede o primeiro nome do uuario, se o nome tiver 4 letras ou menos
escreva "seu nome é curto"; se tiver entre 5 e 6 letras , escreva "seu nome e normal";
Maior que isso, "seu nome e grande"
'''

nome = input("Ola, caro usuário, sou pearl , qual é o seu primeiro nome? \n")
quanti_letras = len(nome)
if quanti_letras <= 4:
    print(f"Nossa {nome}, seu nome e muito curto")
elif quanti_letras <= 6:
    print(f"Nossa {nome}, seu nome é bem normal")
else:
    print(f"Nossa {nome}, seu nome é bem grande")