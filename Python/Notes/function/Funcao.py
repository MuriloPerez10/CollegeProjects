

#podemos colocar um valor padrão nos parametros caso nao seja inserido algun valor como parametros
#caso use uma função onde nao use todos os parametros, o programa irá dar um erro
from ast import arg


def soma(a = 0,b = 2):
    resultado = a + b
    print(a,b,resultado)
#exemplo de uso de parametro padrão
soma()
#tambem podemos mudar a ordem de aparição dos parametros
soma(b = 12,a = 1)

#ultilizamos o 'return' para retornar um valor, Caso nao use ele,  função irá retornar 'none'

# o parametr *args(podendo ser qualquer palavra junto do *, muitos escripits usam o args para seguir padrão) usada para ter um limite ilimitados de itens para o parametros
#OBS: Usando o args voce cria uma tupla(uma lista que nao pode ser modificada)

#No parametro de **kwargs(mesma coisa do args, podemos usar qualquer nome desde que tenha ** na frente do nome, mas o padrão da comunidade e o **kwargs), ele te a mesma função do args, so que funciona com parametro com valores padrões.
def func(*args,**kwargs):
    print(args[0])# se não especificar a colocação, o esultado sai como uma tupla
    print(kwargs)

var = func('banana','maça','ovo',name='murilo',last_name='perez')
print(var)

#OBS: e possivel mudar variavel dentro de um escopo local(dentro da função) para a variavel Global 
# ====ATENÇÂO ISSO NÃO É RECOMENDADO A SE FAZER====
def GlobalEX():
    global var #mudando o valor da variavel no escopo global
    var = 1

