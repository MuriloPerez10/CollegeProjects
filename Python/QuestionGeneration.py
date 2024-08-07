import random

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
    {
        'Pergunta': 'Quanto é 7 * 3?',
        'Opções': ['21', '24', '20', '18'],
        'Resposta': '21',
    },
    {
        'Pergunta': 'Quanto é 15 - 6?',
        'Opções': ['7', '8', '9', '10'],
        'Resposta': '9',
    },
    {
        'Pergunta': 'Quanto é 9 + 8?',
        'Opções': ['15', '17', '16', '18'],
        'Resposta': '17',
    },
    {
        'Pergunta': 'Quanto é 12 / 4?',
        'Opções': ['2', '3', '4', '5'],
        'Resposta': '3',
    },
    {
        'Pergunta': 'Quanto é 5 + 7?',
        'Opções': ['11', '12', '13', '14'],
        'Resposta': '12',
    },
    {
        'Pergunta': 'Quanto é 14 - 5?',
        'Opções': ['9', '8', '7', '6'],
        'Resposta': '9',
    },
    {
        'Pergunta': 'Quanto é 8 * 6?',
        'Opções': ['42', '48', '46', '50'],
        'Resposta': '48',
    },
    {
        'Pergunta': 'Quanto é 20 / 5?',
        'Opções': ['4', '5', '6', '3'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 11 + 9?',
        'Opções': ['20', '21', '18', '19'],
        'Resposta': '20',
    },
    {
        'Pergunta': 'Quanto é 18 - 7?',
        'Opções': ['11', '12', '13', '14'],
        'Resposta': '11',
    },
]

def faz_pergunta(list_position, chave1, chave2, chave3, acertos):
    # Imprimir a pergunta e opções
    print(f"Pergunta: {perguntas[list_position][chave1]}")
    for i, num in enumerate(perguntas[list_position][chave2]):
        print(f"{i}) {num}")
    
    # Obter a posição correta da resposta
    position_response = perguntas[list_position][chave2].index(perguntas[list_position][chave3])
    
    # Solicitar entrada do usuário
    resposta = input("Escolha uma resposta: ")

    # Corrigir a verificação se a resposta é numérica e verificar resposta correta
    if resposta.isnumeric():
        if int(resposta) == position_response:
            acertos += 1
            print("Você acertou 👍")
        else:
            print("Você errou ❌")
    else:
        print("Entrada inválida! Por favor, escolha um número.")

    return acertos

# Geração de lista com a ordem dos números
lista = []
while len(lista) < len(perguntas):
    aleatorio = random.randint(0, len(perguntas) - 1)  # Ajuste aqui
    if aleatorio not in lista:
        lista.append(aleatorio)

contador_de_acertos = 0

# Gerando as perguntas
for i in lista:
    contador_de_acertos = faz_pergunta(i, 'Pergunta', 'Opções', 'Resposta', contador_de_acertos)

print("Programa finalizado. Você acertou", contador_de_acertos, "de", len(perguntas), "perguntas.")
