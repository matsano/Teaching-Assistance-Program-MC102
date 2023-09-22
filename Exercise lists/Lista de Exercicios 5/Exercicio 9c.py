def verifica(mat):
    resposta = []
    semSaidas = []
    semEntradas = []

    for i in range(len(mat)):
        semSaidas.append(True)
    for i in range(len(mat)):
        semEntradas.append(True)

    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j] == 1:
                semSaidas[i] = False

    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[j][i] == 1:
                semEntradas[i] = False

    for i in range(len(mat)):
        if semEntradas[i] and semSaidas[i]:
            resposta.append(True)
        else:
            resposta.append(False)

    return resposta
