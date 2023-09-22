'''
Um erro ocorre no loop do while, no qual ele entra no loop quando n = 1 e
multiplica o fatorial por zero. Para corrigir esse erro pode-se colocar a
subtracao "n = n - 1" após a atualizacao da variavel "fatorial", assim,
esta nao sera zerada.
Outro erro se consiste no fato do ultimo print nao estar dentro do else. Sendo
assim, ele sera sempre executado.
Um outro erro eh nao considerar o fatorial de zero igual a 1.
'''


def main():

    valor = int(input("Digite um numero: "))
    fatorial = n = valor

    if n > 0:
        n = n - 1
        while n > 0:
            fatorial = fatorial * n
            n = n - 1

        print("O fatorial de", valor, "eh igual a:", fatorial)
    elif n == 0:
        print("O fatorial de 0 eh igual a: 1")
    else:
        print("Nao existe fatorial de", valor)

main()
