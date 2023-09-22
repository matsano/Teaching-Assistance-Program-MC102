def separarNumero(numero):
    numero = str(numero)
    return numero.split('.')

def obterParteInteiro(numero):
    numero = separarNumero(numero)
    return int(numero[0])

def obterParteFracao(numero):
    numero = separarNumero(numero)
    return float("0." + numero[1])

def main():

    numero = float(input("Digite um numero na base decimal: "))
    binarioInteiro = ""
    binarioFracao = ""
    inteiro = obterParteInteiro(numero)
    fracao = obterParteFracao(numero)

    while inteiro > 1:
        binarioInteiro = str(inteiro % 2) + binarioInteiro
        inteiro = inteiro // 2
    binarioInteiro = str(inteiro) + binarioInteiro
    
    casaDecimal = 0
    while fracao != 0 and casaDecimal <= 10:
        fracao *= 2
        binarioFracao += str(obterParteInteiro(fracao))
        fracao -= obterParteInteiro(fracao)
        casaDecimal += 1
    
    print(binarioInteiro + "." + binarioFracao)

main()
