def main():

    n = int(input("Digite o tamanho da primeira sequencia: "))
    m = int(input("Digite o tamanho da segunda sequencia: "))
    sequencia1 = []
    sequencia2 = []
    resultado = []
    resposta = []

    for i in range(n):
        sequencia1.append(int(input("Digite um numero inteiro para a sequencia 1: ")))
    for i in range(m):
        sequencia2.append(int(input("Digite um numero inteiro para a sequencia 2: ")))

    for i in range(m):
        for j in range(n):
            if sequencia1[j] == sequencia2[i]:
                resultado.append(sequencia1[j])
    resultado.sort()
    for i in resultado:
        if i not in resposta:
            resposta.append(i)

    print("Primeira sequencia: ", end = "")
    for i in range(n-1):
        print(sequencia1[i], end = " ")
    print(sequencia1[n-1])

    print("Segunda sequencia: ", end = "")
    for i in range(m-1):
        print(sequencia2[i], end = " ")
    print(sequencia2[m-1])

    print("Resultado:", resposta[0], end = " ")
    for i in range(1, len(resposta)):
        if i == len(resposta) - 1:
            print(resposta[i])
        else:
            print(resposta[i], end = " ")

main()
