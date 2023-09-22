def main():

    n = int(input("Digite a quantidade de numeros: "))
    numeros = []
    somatorio = 0

    for i in range(n):
        numeros.append(float(input("Digite um numero real: ")))

    media = sum(numeros) / len(numeros)
    for i in range(n):
        somatorio += (numeros[i] - media) ** 2
    variancia = somatorio / (n - 1)
    desvioPadrao = variancia ** (1/2)

    print(desvioPadrao)

main()
