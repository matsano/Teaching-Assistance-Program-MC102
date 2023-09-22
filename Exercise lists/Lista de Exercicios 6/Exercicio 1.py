def media(v, tamanho):
    if len(v) == 0:
        return 0
    else:
        return v[len(v)-1] / tamanho + media(v[:-1], tamanho)
