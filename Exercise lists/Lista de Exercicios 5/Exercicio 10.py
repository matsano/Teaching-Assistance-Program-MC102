def separar_em_quadrados(matriz):
    quadrados = []
    quadrado = []

    for n in range(3):
        for i in range(3):
            minimo = 3*n
            maximo = 3*(n+1)
            for j in range(minimo, maximo):
                quadrado.append(matriz[i][j])
        quadrados.append(quadrado.copy())
        quadrado.clear()

    for n in range(3):
        for i in range(3, 6):
            minimo = 3*n
            maximo = 3*(n+1)
            for j in range(minimo, maximo):
                quadrado.append(matriz[i][j])
        quadrados.append(quadrado.copy())
        quadrado.clear()

    for n in range(3):
        for i in range(6, 9):
            minimo = 3*n
            maximo = 3*(n+1)
            for j in range(minimo, maximo):
                quadrado.append(matriz[i][j])
        quadrados.append(quadrado.copy())
        quadrado.clear()
        
    return quadrados

def separar_em_linhas(matriz):
    linhas = []
    linha = []
    
    for i in range(9):
        for j in range(9):
            linha.append(matriz[i][j])
        linhas.append(linha.copy())
        linha.clear()

    return linhas

def separar_em_colunas(matriz):
    colunas = []
    coluna = []

    for i in range(9):
        for j in range(9):
            coluna.append(matriz[j][i])
        colunas.append(coluna.copy())
        coluna.clear()

    return colunas

def regra_quadrado(matriz):
    quadrados = separar_em_quadrados(matriz)
    for i in range(len(quadrados)):
        quadrados[i].sort()
        for j in range(9):
            if j+1 != quadrados[i][j]:
                return False
    return True

def regra_linha(matriz):
    linhas = separar_em_linhas(matriz)
    for i in range(len(linhas)):
        linhas[i].sort()
        for j in range(9):
            if j+1 != linhas[i][j]:
                return False
    return True
        
def regra_coluna(matriz):
    colunas = separar_em_colunas(matriz)
    for i in range(len(colunas)):
        colunas[i].sort()
        for j in range(9):
            if j+1 != colunas[i][j]:
                return False
    return True

def solucao(mat):

    if regra_quadrado(mat) and regra_linha(mat) and regra_coluna(mat):
        return True
    else:
        return False
