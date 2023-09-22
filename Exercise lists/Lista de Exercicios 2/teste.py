x = 5
y = 0

while True:
    y = (x % 2) + 10 * y
    x = x // 2
    print("x =", x, "y =", y)
    if x == 0:
        break

while y != 0:
    x = y % 100
    y = y // 10
    print("x =", x, "y =", y)
