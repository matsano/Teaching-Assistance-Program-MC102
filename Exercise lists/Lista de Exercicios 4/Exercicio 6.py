def removerCaractere(c, string):
    posicao = string.find(c)
    string = list(string)
    del string[posicao]
    return "".join(string)
    
def main():

    palavra1 = input("Digite uma palavra: ")
    palavra2 = input("Digite uma palavra: ")
    palavraEncontrada = ""

    for i in palavra1:
        if i in palavra2:
            palavraEncontrada += i
            palavra2 = removerCaractere(i, palavra2)
        else:
            break
    
    if palavraEncontrada == palavra1:
        print("Anagramas!")
    else:
        print("Nao sao anagramas!")

main()
