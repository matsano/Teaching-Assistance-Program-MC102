def main():

    n = int(input("Digite o tamanho da primeira sequencia: "))
    m = int(input("Digite o tamanho da segunda sequencia, maior ou igual ao da primeira: "))
    sequencia1 = []
    sequencia2 = []
    resultado = 0

    for i in range(n):
        sequencia1.append(int(input("Digite um numero inteiro para a sequencia 1: ")))
    for i in range(m):
        sequencia2.append(int(input("Digite um numero inteiro para a sequencia 2: ")))

    for i in range(m-2):
        if sequencia1[0] == sequencia2[i]:
            if sequencia1[1] == sequencia2[i+1]:
                if sequencia1[2] == sequencia2[i+2]:
                    resultado += 1

    print("Primeira sequencia: ", end = "")
    for i in range(n-1):
        print(sequencia1[i], end = " ")
    print(sequencia1[n-1])

    print("Segunda sequencia: ", end = "")
    for i in range(m-1):
        print(sequencia2[i], end = " ")
    print(sequencia2[n-1])

    print("Resultado:", resultado)

main()
