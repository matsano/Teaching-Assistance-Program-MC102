j = 1

def main():
    a = 9

    if a % 2  == 0:
        a = 2
    else:
        a = 3

    print(fun1(2,4))

    for i in range(3):
        for j in range(3):
            print(fun1(a, i+j))

def fun1(a, b):
    p = 1
    for i in range(b):
        p = p * a
    return p+j

main()
