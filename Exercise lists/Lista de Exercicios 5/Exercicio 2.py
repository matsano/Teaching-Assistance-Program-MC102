def soma_divisores(n):
    divisores = []
    
    for i in range(1, n):
        if n % i == 0:
            divisores.append(i)
            
    return sum(divisores)

def amigos(a, b):
    if (soma_divisores(a) == b) and (soma_divisores(b) == a):
        return True
    else:
        return False
