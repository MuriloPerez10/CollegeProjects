import random

num1 = float(input('digite um numero inteiro: '))
num2 = float(input('digite outro numero inteiro: '))
numR = float(input('digite outro numero Real: '))

print('a) o produto entre o dobro do primeiro e a metade do segundo')
Dobro = (num1*2)
m = num2/2
print(random.randrange(m,Dobro))

print('b) a soma entre o triplo do primeiro e o terceiro.')
soma = (num1*3)+numR
print(soma)

print('c) o terceiro elevado ao cubo.')
print(numR**3)