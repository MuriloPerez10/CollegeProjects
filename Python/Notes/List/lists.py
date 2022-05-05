"""
as istas tem diversas funções importantes dentro de sistema, como a capacidade
de conseguir guardar um numero infinito de variaveis
"""


list1 = [1,2,3,3]
list2 = [4,5,6,4]
#cosguimo concatenar as listas de duas formas
#primeira forma usando +
list3 = list1+list2
print(list3)
#segunda maneira usando a função EXTEND()
list1.extend(list2)
print(list1)

#para adicionarmos valoroes usamos a função APPEND()
list1.append(10)
print(list1)

#Para inserimos valores em lugares especificos usamos o INSERT(posição,valor)
list2.insert(0, 'banana')
print(list2)

#Para removermos o ultimo valor de uma lista utilizamos POP()
list1.pop()
print(list1)

#para deletarmos um valor especifico utilizamos o del(lista[posiçãp])
del(list1[:3])
print(list1)

#usamos o Min() e o Max() para mostra o menor e o maior valo da lista
print(min(list1))
print(max(list1))

#Usamos o Range(start,stop,step) Para construir lista, pois elas são obj. iteraveis
l4 = list(range(1,10))
print(l4)