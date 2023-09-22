def main():

    n = int(input("Digite a quantidade de numeros: "))
    intervalo0_25 = 0
    intervalo26_50 = 0
    intervalo51_75 = 0
    intervalo76_100 = 0

    for i in range(n):
        numero = int(input("Digite um numero: "))
        if numero >= 0 and numero <= 25:
            intervalo0_25 += 1
        elif numero >= 26 and numero <= 50:
            intervalo26_50 += 1
        elif numero >= 51 and numero <= 75:
            intervalo51_75 += 1
        elif numero >= 76 and numero <= 100:
            intervalo76_100 += 1

    print("[0,25]:", intervalo0_25)
    print("[26,50]:", intervalo26_50)
    print("[51,75]:", intervalo51_75)
    print("[76,100]:", intervalo76_100)

main()
