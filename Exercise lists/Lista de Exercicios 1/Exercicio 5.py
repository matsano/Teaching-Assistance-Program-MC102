def main():

    a = float(input("Digite o valor do lado do triangulo: "))
    b = float(input("Digite o valor do lado do triangulo: "))
    c = float(input("Digite o valor do lado do triangulo: "))

    if a != b and a != c and b != c:
        print("Triangulo escaleno")
    elif a == b == c:
        print("Triangulo equilatero")
    else:
        print("Triangulo isoceles")

    s = (a + b + c)/2
    area = (s*(s-a)*(s-b)*(s-c))**(1/2)
    print("A =", area)

main()
