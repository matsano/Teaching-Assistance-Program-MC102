def divisores(n):
    divisores = []
    
    for i in range(2, n+1):
        if n % i == 0:
            divisores.append(i)
            
    return divisores

def menor_base_log(n):
    b = 0
    divisores_n = divisores(n)

    for i in range(len(divisores_n)):
        k = 1
        while divisores_n[i] ** k <= n:
            if divisores_n[i]**k == n:
                b = divisores_n[i]
                break
            k += 1
        if b != 0:
            break
    return b
