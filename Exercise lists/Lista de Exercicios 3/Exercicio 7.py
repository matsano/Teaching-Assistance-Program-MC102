def main():

    n = int(input("Digite o tamanho dos vetores: "))
    vetor1 = []
    vetor2 = []
    produtoInterno = 0

    for i in range(n):
        vetor1.append(float(input("Digite um numero para o vetor 1: ")))
    for i in range(n):
        vetor2.append(float(input("Digite um numero para o vetor 2: ")))

    for i in range(n):
        produtoInterno += (vetor1[i] * vetor2[i])

    print("Vetor 1: ", end = "")
    for i in range(n-1):
        print(vetor1[i], end = " ")
    print(vetor1[n-1])

    print("Vetor 2: ", end = "")
    for i in range(n-1):
        print(vetor2[i], end = " ")
    print(vetor2[n-1])

    print("Produto interno =", produtoInterno)

main()
