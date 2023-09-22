def teste(a, b, n):
    if a**2 + b**2 == n:
        return True
    else:
        return False

def pitagorico(n):
    for i in range(1, n):
        for j in range(1, n):
            if i**2 + j**2 == n:
                return True
    return False
