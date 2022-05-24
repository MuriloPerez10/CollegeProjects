def soma(lista):
    for num in lista:
        r += num
    return r


list = []
while True:
    num = input('digite um numero: ')
    if  not num.isnumeric():
        print('por favor digite um numero')
    
    list.append(num)
    button = input('deseja digitar mais algum numero? S[sim]/N[não]: ')
    if button == 'N' or button == 'n':
        break

print(soma(list))
