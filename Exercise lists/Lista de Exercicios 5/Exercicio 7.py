def verificar_primalidade(n):
    i = 2
    variavel = 0

    while i < n:
        if n % i == 0:
            variavel += 1
        i += 1

    if variavel == 0:
        return True
    else:
        return False

def sanduiche_primo(n):
    menorPrimo = n
    maiorPrimo = n

    primalidade = False
    while not primalidade and menorPrimo > 1:
        if verificar_primalidade(menorPrimo):
            primalidade = True
        else:
            menorPrimo -= 1

    primalidade = False
    while not primalidade:
        if verificar_primalidade(maiorPrimo):
            primalidade = True
        else:
            maiorPrimo += 1

    return (menorPrimo, maiorPrimo)
