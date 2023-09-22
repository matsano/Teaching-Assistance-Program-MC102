def main():

    m = float(input("Digite um numero: "))
    n = float(input("Digite um numero: "))

    while n > 0:
        resto = m % n
        m = n
        n = resto

    print("MDC =", m)

main()
