
def VerificaçaoDigito(x):
    r = 11-(x%11)
    if r>9:
        r = 0
    return r



print(25*'=','alidador de CPF',25*'=')
multplicaçao = []

cpf = input('Por Favor inisira o seu cpf, sem os pontos: ')

#validação se so tem numericos
if not cpf.isnumeric:
    print('por favor inserir apenas numeros')

d = list(cpf)
#Transformação em inteiros e separção dos dois ultimos digitos
cpf_antigo,numeros_cpf , digitos_cpf,multplicaçao = [],[],[],[]
i = 0 
while i <= 10:
    t = int(d[i])
    if i >= 9:
        digitos_cpf.append(t)
    else:
        numeros_cpf.append(t)
    i+=1

# Multplicação do valores e soma de verificação
i = 10
for c in numeros_cpf:
    multplicaçao.append(c*i)
    i-=1

soma = sum(multplicaçao)
digito1 = VerificaçaoDigito(soma) #primeiro digito

#juntando o primeiro digito com a lista dos num do cpf
numeros_cpf.append(digitos_cpf[0])

# Multplicação do valores e soma de verificação
i = 11
multplicaçao1 = []
for c in numeros_cpf:
    multplicaçao1.append(c*i)
    i-=1

soma1= sum(multplicaçao1)
digito2 = VerificaçaoDigito(soma1)

#juntando o primeiro digito com a lista dos num do cpf
numeros_cpf.append(digitos_cpf[1])

#comparação de vericidade
i = 0 
while i <= 10:
    t = int(d[i])
    cpf_antigo.append(t)
    i+=1
"""
if numeros_cpf == cpf_antigo:
    print('seu cpf e valido')
else:
    print('seu cpf está invalido')
"""
print(cpf_antigo)
print(numeros_cpf)