def desvioPadrao(v):
    variancia = sum(v)**2 / len(v)

    for i in range(len(v)):
        v[i] = v[i] ** 2

    variancia = sum(v) - variancia
    variancia = variancia / (len(v) - 1)

    return variancia ** (1/2)
