def main():

    numero1 = float(input("Digite um numero: "))
    numero2 = float(input("Digite um numero: "))
    operacao = input("Digite um operador artimetico (+, -, *, /): ")

    if operacao == "+":
        resultado = numero1 + numero2
    elif operacao == "-":
        resultado = numero1 - numero2
    elif operacao == "*":
        resultado = numero1 * numero2
    elif operacao == "/":
        resultado = numero1 / numero2

    print("Resultado =", resultado)

main()
