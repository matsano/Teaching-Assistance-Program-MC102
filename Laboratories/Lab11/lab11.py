###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Fuga de Nova York
# Nome: Matheus Santos Sano
# RA: 222370
###################################################

# Leitura da matriz
# DICA: o método isnumeric() pode ser útil para determinar o fim da leitura da matriz 
matriz = []
entrada = input()
while not entrada.isnumeric():
    matriz.append(entrada.split(" "))
    entrada = input()

# Leitura das coordenadas e início do processamento
coordenadas = []
quantidade_coordenadas = int(entrada)
for i in range(quantidade_coordenadas):
    entrada = input()
    coordenadas.append(entrada.split(" "))

for i in range(len(coordenadas)):
    caminho = []
    linha = int(coordenadas[i][0])
    coluna = int(coordenadas[i][1])
    fuga_incompleta = False
    while (not fuga_incompleta) and (linha >= 0) and (linha < len(matriz)) and (coluna >= 0) and (coluna < len(matriz[0])):
        if matriz[linha][coluna] == "N":
            linha -= 1
        elif matriz[linha][coluna] == "S":
            linha += 1
        elif matriz[linha][coluna] == "O":
            coluna -= 1
        else:
            coluna += 1
        if [linha, coluna] in caminho:
            fuga_incompleta = True
        else:
            caminho.append([linha, coluna])
    
    # Impressão do resultado para cada coordenada
    if linha == -1:
        print("Fuga pelo norte.")
    elif linha == len(matriz):
        print("Fuga pelo sul.")
    elif coluna == -1:
        print("Fuga pelo oeste.")
    elif coluna == len(matriz[0]):
        print("Fuga pelo leste.")
    elif fuga_incompleta:
        print("Resgate aereo solicitado.")
