while True:
    cpf = input("digite seu cpf:")
    if len(cpf) == 14 or len(cpf) == 11:
        break
    else:
        print("Numeros insuficientes")

if "-" in cpf or "." in cpf:
    divide_cpf = cpf.split("-")
    #Pegando os dois ultimos digitos
    digito_verificacao = divide_cpf[1]

    #pegando os nove primeiros digitos
    digitos_contagem = divide_cpf[0].split(".")
    digitos_contagem = "".join(digitos_contagem)
else:
    digitos_contagem = cpf

#PRIMEIRO DIGITO
#Multiplicação e soma
i = 10
Soma_digitos_cont = 0
for t in digitos_contagem:
    t = int(t)
    Soma_digitos_cont = Soma_digitos_cont +(t*i)
    i -= 1

num_final =(Soma_digitos_cont*10)%11
num_final = 0 if (Soma_digitos_cont*10)%11 > 9 else num_final

#SEGUNDO DIGITO
digitos_contagem_2 = digitos_contagem + str(num_final)

i = 11
Soma_digitos_cont_2 = 0
for t in digitos_contagem_2:
    t = int(t)
    Soma_digitos_cont_2 = Soma_digitos_cont_2+(t*i)
    i -= 1

num_final_2 =(Soma_digitos_cont_2*10)%11
num_final_2 = 0 if num_final_2 > 9 else num_final_2


#COMPARANDO NUMERO
cpf_validado = digitos_contagem_2 + str(num_final_2)

if "-" in cpf or "." in cpf:
    cpf_passado_usuario = digitos_contagem + digito_verificacao
else:
    cpf_passado_usuario = cpf

if cpf_passado_usuario == cpf_validado:
    print("cpf valido")
else:
    print("cpf invalido")
    print(f"cpf_validado {cpf_validado}")
    print(f"cpf_passado {cpf_passado_usuario}")

