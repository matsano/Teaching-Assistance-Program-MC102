'''
Nao faz de maneira correta, porque as condicoes estão equivocadas.
Caso o numero seja impar e maior ou igual a 100, ele entrará no primeiro else, e isso estaria errado.
Uma forma de corrigir isso, é separar as duas condicoes: se eh par ou impar, se eh < 100 ou >= 100.
'''

def main():
    
    print("Digite um numero: ")
    a = int(input())

    if a % 2 == 0:
        print("O numero eh par e ", end = '')
    else:
        print("O numero eh impar e ", end = '')

    if a < 100:
        print("menor do que 100")
    else:
        print("maior ou igual que 100")

main()
