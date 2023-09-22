###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 12 - Busca em Imagens
# Nome: Matheus Santos Sano
# RA: 222370
###################################################

def criar_matriz(matriz_original):
    nova_matriz = []
    i = 0
    while i < len(matriz_original):
        linha = []
        j = 0
        while j < len(matriz_original[0]):
            linha.append(0)
            j += 1
        nova_matriz.append(linha)
        i += 1
    return nova_matriz

def flip_horizontal(imagem_original):
    nova_imagem = criar_matriz(imagem_original)
    for x in range(len(imagem_original)):
        for y in range(len(imagem_original[0])):
            y_linha = len(imagem_original[0]) - (1 + y)
            nova_imagem[x][y_linha] = imagem_original[x][y]
    return nova_imagem

def flip_vertical(imagem_original):
    nova_imagem = criar_matriz(imagem_original)
    for x in range(len(imagem_original)):
        x_linha = len(imagem_original) - (1 + x)
        for y in range(len(imagem_original[0])):
            nova_imagem[x_linha][y] = imagem_original[x][y]
    return nova_imagem

def rotacao_90(imagem_original):
    nova_imagem = []
    for i in range(len(imagem_original[0])):
        linha = []
        for j in range(len(imagem_original)):
            linha.append(imagem_original[j][i])
        nova_imagem.append(linha)
    return flip_horizontal(nova_imagem)

def rotacao_180(imagem_original):
    return rotacao_90(rotacao_90(imagem_original))

def matriz_contida(matriz_A, matriz_B):
    contido = False
    for inicio_linha in range(0, len(matriz_A)-(len(matriz_B)-1)):
        for inicio_coluna in range(0, len(matriz_A[0])-(len(matriz_B[0])-1)):
            nova_matriz = []
            linha = 0
            for i in range(inicio_linha, inicio_linha+len(matriz_B)):
                if matriz_B[linha] == matriz_A[i][inicio_coluna:inicio_coluna+len(matriz_B[0])]:
                    nova_matriz.append(matriz_A[i][inicio_coluna:inicio_coluna+len(matriz_B[0])])
                    linha += 1
                else:
                    break
            if nova_matriz == matriz_B:
                contido = True
                break
        if contido:
            break
    return contido

# leitura da imagem A
_ = input() #P2 - linha a ser ignorada

m_A, n_A = [int(x) for x in input().split()]

_ = input() #255 - linha a ser ignorada

A = []
for i in range(n_A):
    linha = [int(x) for x in input().split()]
    A.append(linha)

# leitura da imagem B
_ = input() #P2 - linha a ser ignorada

m_B, n_B = [int(x) for x in input().split()]

_ = input() #255 - linha a ser ignorada

B = []
for i in range(n_B):
    linha = [int(x) for x in input().split()]
    B.append(linha)

# verificar padrao Original
if matriz_contida(A, B):
    print("Original: Contido")
else:
    print("Original: Nao contido")

# verificar Flip horizontal
if matriz_contida(A, flip_horizontal(B)):
    print("Flip horizontal: Contido")
else:
    print("Flip horizontal: Nao contido")

# verificar Flip vertifical
if matriz_contida(A, flip_vertical(B)):
    print("Flip vertical: Contido")
else:
    print("Flip vertical: Nao contido")

# verificar Rotacao 90
if matriz_contida(A, rotacao_90(B)):
    print("Rotacao 90: Contido")
else:
    print("Rotacao 90: Nao contido")

# verificar Rotacao 180
if matriz_contida(A, rotacao_180(B)):
    print("Rotacao 180: Contido")
else:
    print("Rotacao 180: Nao contido")
