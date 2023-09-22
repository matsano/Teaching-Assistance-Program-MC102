def main():

    Y = float(input("Digite um numero positivo: "))
    x = Y / 2

    for i in range(1, 20):
        x = x - (x**2 - Y) / (2 * x)

    print (x)

main()
