def main():

    x = int(input("x = "))
    y = int(input("y = "))

    y = x - y
    x = x - y
    y = x + y

    print("x =", x)
    print("y =", y)

main()
