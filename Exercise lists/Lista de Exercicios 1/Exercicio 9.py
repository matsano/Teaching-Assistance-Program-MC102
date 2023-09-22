def main():

    sexo = input("Digite o sexo (M ou F): ")
    idade = int(input("Digite a idade: "))
    tempoContribuicao = int(input("Digite o tempo de contribuicao (em anos): "))

    if sexo == "M" and idade >= 65 and tempoContribuicao >= 10:
        aposentavel = True
    elif sexo == "M" and idade >= 63 and tempoContribuicao >= 15:
        aposentavel = True
    elif sexo == "F" and idade >= 63 and tempoContribuicao >= 10:
        aposentavel = True
    elif sexo == "F" and idade >= 61 and tempoContribuicao >= 15:
        aposentavel = True
    else:
        aposentavel = False

    if aposentavel:
        print("Aposentavel")
    else:
        print("Nao Aposentavel")

main()
