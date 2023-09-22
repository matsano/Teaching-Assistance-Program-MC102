#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Linha do Tempo Sagrada
# Nome: Matheus Santos Sano
# RA: 222370
#####################################################

# Leitura da matriz

matriz = []
for i in range(11):
    matriz.append(list(input()))

# Deteção dos eventos nexus
def evento_nexus(linha, coluna, matriz):
    fim_da_bifurcacao = False
    while (not fim_da_bifurcacao) and (linha != 0) and (linha != 10) and (coluna != 0) and (coluna != 49):
        if matriz[linha][coluna-1] == "+":
            matriz[linha][coluna] = "."
            coluna -= 1
        elif matriz[linha][coluna+1] == "+":
            matriz[linha][coluna] = "."
            coluna += 1
        elif matriz[linha-1][coluna] == "+":
            matriz[linha][coluna] = "."
            linha -= 1
        elif matriz[linha+1][coluna] == "+":
            matriz[linha][coluna] = "."
            linha += 1
        else:
            fim_da_bifurcacao = True
    if fim_da_bifurcacao:
        return False
    else:
        return True

bifurcacoes = {}
for i in range(50):
    if matriz[4][i] == "+":
        if evento_nexus(4, i, matriz):
            bifurcacoes[i] = "Evento Nexus"
        else:
            bifurcacoes[i] = "Instavel"
    elif matriz[6][i] == "+":
        if evento_nexus(6, i, matriz):
            bifurcacoes[i] = "Evento Nexus"
        else:
            bifurcacoes[i] = "Instavel"

for (coluna, bifurcacao) in bifurcacoes.items():
    print("Bifurcacao ", coluna, ": ", bifurcacao, sep="")
