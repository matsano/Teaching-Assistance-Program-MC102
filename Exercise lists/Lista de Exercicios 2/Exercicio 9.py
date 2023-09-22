def main():

    C = int(input("Digite um numero inteiro positivo: "))
    x1 = x2 = x3 = 0
    solucoes = []

    while x1 <= C:
        x2 = 0
        while x2 <= C:
            x3 = 0
            while x3 <= C:
                if x1 + x2 + x3 == C:
                    solucoes.append(x1)
                    solucoes.append(x2)
                    solucoes.append(x3)
                x3 += 1
            x2 += 1
        x1 += 1

    for i in range(0, len(solucoes), 3):
        print("x1 =", solucoes[i], end = " ")
        print("x2 =", solucoes[i+1], end = " ")
        print("x3 =", solucoes[i+2])

main()
