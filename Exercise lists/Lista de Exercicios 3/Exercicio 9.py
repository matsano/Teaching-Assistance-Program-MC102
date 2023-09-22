def saoComprimos(numero1, numero2):
    variavel = 2
    naoComprimos = False

    while variavel <= numero1 and variavel <= numero2:
        if (numero1 % variavel == 0) and (numero2 % variavel == 0):
            naoComprimos = True
            break
        variavel += 1
    return not naoComprimos

def main():

    n = int(input("Digite o tamanho da sequencia: "))
    v = []
    linhaQuadrado = []

    for i in range(n):
        v.append(float(input("Digite um numero inteiro positivo maior do que 1 para a sequencia: ")))

    for i in range(n):
        for j in range(n):
            if saoComprimos(v[i], v[j]):
                print(1, end = "")
            else:
                print(0, end = "")
            if j != n - 1:
                print(" ", end = "")
            else:
                print()

main()
