def main():

    n = int(input("Digite o tamanho da primeira sequencia: "))
    m = int(input("Digite o tamanho da segunda sequencia: "))
    sequencia1 = []
    sequencia2 = []
    posicao = 0

    for i in range(n):
        sequencia1.append(int(input("Digite um numero inteiro para a sequencia 1: ")))
    for i in range(m):
        sequencia2.append(int(input("Digite um numero inteiro para a sequencia 2: ")))

    primeiraSequencia = sequencia1.copy()
    segundaSequencia = sequencia2.copy()

    while segundaSequencia != []:
        while (segundaSequencia[0] > primeiraSequencia[posicao]) and (posicao < len(primeiraSequencia)):
            posicao += 1
        primeiraSequencia.insert(posicao, segundaSequencia[0])
        segundaSequencia.pop(0)
        

    print("Primeira sequencia: ", end = "")
    for i in range(n-1):
        print(sequencia1[i], end = " ")
    print(sequencia1[n-1])

    print("Segunda sequencia: ", end = "")
    for i in range(m-1):
        print(sequencia2[i], end = " ")
    print(sequencia2[m-1])

    print("Resultado:", primeiraSequencia[0], end = " ")
    for i in range(1, len(primeiraSequencia)):
        if i == len(primeiraSequencia) - 1:
            print(primeiraSequencia[i])
        else:
            print(primeiraSequencia[i], end = " ")

main()
