def main():

    n = int(input("Digite a quantidade numeros da sequencia: "))
    sequencia = []
    crescente = True

    for i in range(n):
        numero = float(input("Digite um numero: "))
        sequencia.append(numero)

    numeroAnterior = sequencia[0]
    for numero in sequencia:
        if numero < numeroAnterior:
            crescente = False
            break
        numeroAnterior = numero

    if crescente:
        print("Sequencia crescente")
    else:
        print("Sequencia nao crescente")

main()
