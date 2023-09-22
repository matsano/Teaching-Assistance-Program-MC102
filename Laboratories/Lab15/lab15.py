###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 15 - Fuga de Nova York II
# Nome: Matheus Santos Sano
# RA: 222370
###################################################

def clonar_matriz(matriz):
    matriz_clonada = []
    for i in matriz:
        matriz_clonada.append(i.copy())
    return matriz_clonada

'''
Dada uma matriz e a posição (x,y), realiza a 
verificação de é possível realizar a fuga da cidade
ou se é necessário o resgate aéreo.
'''
def fuga(matriz, x, y):
    if matriz[x][y] == "N":
        return False
    elif x == 0 or x == (len(matriz)-1) or y == 0 or y == (len(matriz[0])-1):
        return True
    elif matriz[x][y] == ".":
        return False
    elif matriz[x][y] == "H":
        matriz[x][y] = "."
        return fuga(matriz, x, y-1) or fuga(matriz, x, y+1)
    elif matriz[x][y] == "V":
        matriz[x][y] = "."
        return fuga(matriz, x-1, y) or fuga(matriz, x+1, y)
    elif matriz[x][y] == "T":
        matriz[x][y] = "."
        return  fuga(matriz, x, y-1) or fuga(matriz, x, y+1) or fuga(matriz, x-1, y) or fuga(matriz, x+1, y)

# Leitura de dados

matriz = []    
linha = input()
while not(linha.isnumeric()):
  matriz.append(linha.split())
  linha = input()
n = int(linha)

# Verifica se é preciso realizar a fuga da cidade
# ou solicitar o resgate aéreo para cada posição

for i in range(n):
    mapa = clonar_matriz(matriz)
    coordenada = [int(x) for x in input().split()]
    if fuga(mapa, coordenada[0], coordenada[1]):
        print("Fuga da cidade realizada.")
    else:
        print("Resgate aereo solicitado.")
