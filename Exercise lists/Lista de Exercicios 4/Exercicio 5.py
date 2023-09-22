def main():

    palavra1 = input("Digite uma palavra: ")
    palavra2 = input("Digite uma palavra: ")
    palavraEncontrada = ""
    posicao = 0

    for i in palavra2:
        if i == palavra1[posicao]:
            palavraEncontrada += i
            posicao += 1

    if palavraEncontrada == palavra1:
        print(palavra1, "eh uma subsequencia de", palavra2)
    else:
        print(palavra1, "nao eh uma subsequencia de", palavra2)

main()
