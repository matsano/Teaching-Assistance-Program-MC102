def frequencias(v):
    dicionario = {}
    f1 = 0
    f2 = 0

    for i in v:
        if i in dicionario:
            dicionario[i] = dicionario.get(i) + 1
        else:
            dicionario[i] = 1

    menorFrequencia = len(dicionario)
    maiorFrequencia = 0
    for (numero, frequencia) in dicionario.items():
        if frequencia < menorFrequencia:
            menorFrequencia = frequencia
            f1 = numero
        elif frequencia > maiorFrequencia:
            maiorFrequencia = frequencia
            f2 = numero
    return (f1, f2)
