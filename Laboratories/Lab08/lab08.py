###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Emparelhamento de Primers
# Nome: Matheus Santos Sano
# RA: 222370
###################################################

# Leitura de dados

dna = input()
primer = input()

# Verificação da ligação dos primers na fita
primer = primer[::-1]
sequencia = ""
posicao = 0
posicoes = []

for i in range(1, len(primer)-1):
    if primer[i] == "A":
        sequencia = sequencia + "T"
    elif primer[i] == "T":
        sequencia = sequencia + "A"
    elif primer[i] == "G":
        sequencia = sequencia + "C"
    else:
        sequencia = sequencia + "G"

while posicao != -1:
    posicao = dna.find(sequencia)
    if posicao != -1:
        posicoes.append(posicao)
        dna = list(dna)
        dna[posicao] = "X"
        dna = "".join(dna)

# Impressão da saída do programa
if len(posicoes) != 0:
    for i in range(len(posicoes)):
        print("Ligacao na posicao", posicoes[i])
else:
    print("Nenhuma ligacao")