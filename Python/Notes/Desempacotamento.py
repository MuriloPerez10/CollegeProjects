'''
Desmpacotamento
'''

lista = ['bana','maça','uva',1,2,3,5]
# conseguimos desempacotar itens direto em variavei
#quando não desempacotamos todos o itens, pegando os itens q nos interassa
#utilizamos *var para criar uma lista alternativa para os itens nao designados para var
#Usamos *_ para mostrar para os dev mostrando q o q esta contido nessa parte não e importante
n1, n2 , n3, *_ = lista

print(*_)