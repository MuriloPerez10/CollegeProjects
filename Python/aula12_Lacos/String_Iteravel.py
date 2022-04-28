# indices
# 0123445...2
"""
O programa esta pegando cada indice da frase e fazendo o tratamento e
remontando a frase
"""
frase = "A aranha arranha a rã."
quantidade_letras = len(frase)
contador = 0
nova_frase = ''
letra_user = input('insira ume letra a ser maiuscula: ')

while(contador<quantidade_letras):
    letra = frase[contador]
    print(letra,contador)
    if letra == letra_user:
        nova_frase+= letra_user.upper()
    else:
        nova_frase+=letra
    contador += 1

print(nova_frase)
