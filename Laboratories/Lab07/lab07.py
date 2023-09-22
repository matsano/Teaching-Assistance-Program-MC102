###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Vacinação AstraZeneca
# Nome: Matheus Santos Sano
# RA: 222370
###################################################

# Leitura dos dados

N = int(input())

# Listas dos números de vacinados com a primeira e segunda dose em cada mês

D1 = []
D2 = []
for i in range(N):
    D1.append(0)
    D2.append(0)

# Lista do número de vacinas devolvidas em cada mês

X = []
for i in range(N):
    X.append(0)

# Processamento dos dados

vacinas = []
for i in range(N):
    vacinas.append(int(input()))

for i in range(N):
    if i-3 >= 0:
        D2[i] = D1[i-3]
        vacinas[i] -= D1[i-3]
    if i+3 <= N-1:
        if vacinas[i+3] >= vacinas[i]:
            D1[i] = vacinas[i]
            vacinas[i] = 0
        else:
            D1[i] = vacinas[i+3]
            vacinas[i] -= vacinas[i+3]
    else:
        D1[i] = vacinas[i]
        vacinas[i] = 0
    X[i] = vacinas[i]

# Impressão do uso das vacinas mês a mês

for i in range(N):
    print("Mes " + str(i+1) + ":")
    print("Vacinados com a primeira dose:", D1[i])
    print("Vacinados com a segunda dose:", D2[i])
    print("Vacinas devolvidas:", X[i])

# Impressão do resumo final

print("Total:")
print("Vacinados apenas com a primeira dose:", sum(D1)-sum(D2))
print("Vacinados com as duas doses:", sum(D2))
print("Vacinas devolvidas:", sum(X))