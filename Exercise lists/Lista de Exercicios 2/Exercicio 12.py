def main():

    n = int(input("Digite um numero: "))

    for i in range(1, n+1):
        for j in range(i-1):
            print(j + 1, end = " ")
        print(i)

main()
