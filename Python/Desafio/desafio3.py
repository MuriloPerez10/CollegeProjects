import math

print(20*'=','calcule a area de qualquer circulo',20*'=')
raio = float(input('Digite o numero do raio: '))

conta = (raio * math.pi)**2
print(f'a área do circulo possui {conta:.2f}')