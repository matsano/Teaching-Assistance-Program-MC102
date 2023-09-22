def main():

    string1 = input("Digite uma string: ")
    string2 = input("Digite uma string: ")

    for i in range(len(string1)):
        if string1[i] in string2:
            string2 = string2.replace(string1[i], "")

    print(string2)

main()
