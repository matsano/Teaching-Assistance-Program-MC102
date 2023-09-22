def main():

    unidade = input("Digite a unidade da temperatura digitada (F ou C): ")
    temperatura = float(input("Digite o valor da temperatura na unidade declarada: "))

    if  unidade == "F":
        C = (5/9) * (temperatura - 32)
        print(C, "C")
    else:
        F = (9/5) * temperatura + 32
        print(F, "F")

main()
