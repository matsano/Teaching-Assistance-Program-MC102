def main():

    n = int(input("Digite um numero: "))

    for i in range(n):
        print("* " * i, end = "")
        if i == n - 1:
            print("+")
        else:
            print("+ ", end = "")
            print("* " * (n - i - 2), end = "")
            print("*")

main()
