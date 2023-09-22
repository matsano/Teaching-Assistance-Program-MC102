def main():

    n = int(input("Digite o tamanho da sequencia: "))
    sequencia = []
    numero1 = 0
    numero2 = 0
    numerosEncontrados = False
    
    for i in range(n):
        sequencia.append(int(input("Digite um numero inteiro para a sequencia: ")))

    C = int(input("Digite um numero inteiro: "))
    for i in range(n):
        for j in range(n):
            if i != j:
                if sequencia[i] * sequencia[j] == C:
                    numero1 = sequencia[i]
                    numero2 = sequencia[j]
                    numerosEncontrados = True

    print("Lista =", sequencia)
    print("C =", C)
    if numerosEncontrados:
        if numero1 >= numero2:
            print("Resultado:", numero2, "e", numero1)
        else:
            print("Resultado:", numero1, "e", numero2)
    else:
        print("Resultado: nao existe tais numeros")

main()
