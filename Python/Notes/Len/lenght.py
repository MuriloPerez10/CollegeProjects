#checagem de quantidade de caracteres
print('Digite uma palavra com 6 caracteres\n')
usuario = input('digite qualquer coisa: ')
quanidade = len(usuario)

if quanidade >= 6:
    print(f"'{usuario}' tem {quanidade} de carcteres parabens")
else:
    print(f"você falhou, ficou faltando {6 - len(usuario)} caracteris")
