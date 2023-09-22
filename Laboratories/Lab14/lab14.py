#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 14 - Linha do Tempo Sagrada II
# Nome: Matheus Santos Sano
# RA: 222370
#####################################################

"""
Esta função recebe como parâmetro uma matriz, uma posição inicial 
de uma ramificação na matriz determinada pelos parâmetros linha 
e coluna. O retorno esperado para a função é um número inteiro 
indicando a quantidade de eventos nexus gerados pela ramificação.
"""
def eventos_nexus(matriz, linha, coluna):
    if matriz[linha][coluna] != "+":
        return 0
    elif linha == 0 or linha == 10 or coluna == 0 or coluna == 49:
        matriz[linha][coluna] = "."
        return 1
    matriz[linha][coluna] = "."
    soma1 = eventos_nexus(matriz, linha-1, coluna-1) + eventos_nexus(matriz, linha-1, coluna) + eventos_nexus(matriz, linha-1, coluna+1)
    soma2 = eventos_nexus(matriz, linha, coluna-1) + eventos_nexus(matriz, linha, coluna+1)
    soma3 = eventos_nexus(matriz, linha+1, coluna-1) + eventos_nexus(matriz, linha+1, coluna) + eventos_nexus(matriz, linha+1, coluna+1)
    return soma1 + soma2 + soma3

# Leitura da matriz

matriz = []
for i in range(11):
    matriz.append(list(input()))

# Deteção dos eventos nexus

for coluna in range(50):
    X = 0
    if matriz[4][coluna] == "+" or matriz[6][coluna] == "+":
        X = eventos_nexus(matriz, 4, coluna) + eventos_nexus(matriz, 6, coluna)
        print("Ramificacao {0}: {1} Eventos Nexus.".format(coluna, X))
