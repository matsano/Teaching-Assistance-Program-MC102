######################################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Vacinação CoronaVac
# Nome: Matheus Santos Sano
# RA: 222370
######################################################################

# Leitura do número de meses

N = int(input())

# Processamento de cada mês

D2 = 0
D1 = 0
D2A = 0
D1A = 0
for i in range(N):
    vacinas = int(input())
    if D1A != 0 and vacinas != 0:
        if vacinas >= D1A:
            D2A += D1A
            D2 += D1A
            vacinas -= D1A
            D1 -= D1A
            D1A = 0
        else:
            D2A += vacinas
            D2 += vacinas
            D1A -= vacinas
            D1 -= vacinas
            vacinas = 0
    if D1 != 0 and vacinas != 0:
        if vacinas >= D1:
            D2 += D1
            vacinas -= D1
            D1 = 0
        else:
            D2 += vacinas
            D1 -= vacinas
            D1A += D1
            vacinas = 0
    D1 += vacinas
    vacinas = 0

# Impressão da saída

print("Pessoas completamente imunizadas:", D2)
print("Pessoas imunizadas com uma dose:", D1)
print("Pessoas com atraso na segunda dose:", D2A)
print("Pessoas esperando segunda dose com atraso:", D1A)
