#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 9 - Jogos Olímpicos
# Nome: Matheus Santos Sano
# RA: 222370
#####################################################

# Leitura da primeira linha
N, O, P, B = [int(x) for x in input().split()]

# Leitura e processamento das provas
pontuacao_paises = {}
esportes_ouro = {}

for i in range(N):
    podio = input().split(" ")
    esportes_ouro[podio[0]] = podio[1]
    for i in range(1, 4):
        if podio[i] not in pontuacao_paises:
            pontuacao_paises[podio[i]] = 0
        if i == 1:
            pontuacao_paises[podio[i]] += O
        elif i == 2:
            pontuacao_paises[podio[i]] += P
        else:
            pontuacao_paises[podio[i]] += B

# Impressão da saída
paises = sorted(pontuacao_paises.keys())
melhor_pontuacao = max(pontuacao_paises.values())

for pais in paises:
    if pontuacao_paises[pais] == melhor_pontuacao:
        print(pais, melhor_pontuacao)
        for (esporte, vencedor) in esportes_ouro.items():
            if vencedor == pais:
                print(esporte)