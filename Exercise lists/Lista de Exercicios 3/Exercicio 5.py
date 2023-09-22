def main():

    n = int(input("Digite o tamanho da primeira sequencia: "))
    m = int(input("Digite o tamanho da segunda sequencia: "))
    sequencia1 = []
    sequencia2 = []
    resultado = []
    resposta = []

    for i in range(n):
        numero = int(input("Digite um numero inteiro para a sequencia 1: "))
        sequencia1.append(numero)
        resultado.append(numero)
    for i in range(m):
        numero = int(input("Digite um numero inteiro para a sequencia 2: "))
        sequencia2.append(numero)
        resultado.append(numero)

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
