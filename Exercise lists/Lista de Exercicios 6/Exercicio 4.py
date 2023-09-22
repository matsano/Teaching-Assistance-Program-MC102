def somatorio(n):
    if n == 1:
        return 1
    else:
        return 1/n + somatorio(n-1)
