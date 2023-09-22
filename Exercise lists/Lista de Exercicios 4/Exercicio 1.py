def main():

    string = input("Digite uma string: ")

    for i in range(len(string)-1, -1, -1):
        if i != 0:
            print(string[i], end = "")
        else:
            print(string[i])

main()
