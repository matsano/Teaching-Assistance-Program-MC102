def main():

    marguerita = "1 - Pizza Marguerita"
    calabresa = "2 - Pizza Calabresa"
    pepperoni = "3 - Pizza Pepperoni"
    mussarela = "4 - Pizza Mussarela"

    print(marguerita, calabresa, pepperoni, mussarela, sep = '\n')
    numero = int(input("Digite um numero de 1 a 5: "))

    while numero != 5:
        if numero == 1:
            print(marguerita)
        elif numero == 2:
            print(calabresa)
        elif numero == 3:
            print(pepperoni)
        else:
            print(mussarela)
        numero = int(input("Digite um numero de 1 a 5: "))

main()
