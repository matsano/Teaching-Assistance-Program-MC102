###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - O Porteiro do Castelo
# Nome: Matheus Santos Sano
# RA: 222370
###################################################

# Leitura de dados

sequencia = [int(i) for i in input().split()]

# Rotacoes circulares

menor_valor = min(sequencia)
sequencia_ordenada = sequencia.copy()
sequencia_ordenada.sort()
while sequencia[0] != menor_valor:
    sequencia.append(sequencia[0])
    del sequencia[0]

# Verificacao de senha

if sequencia == sequencia_ordenada:
    print("Klift, Kloft, Still, a porta se abriu")
else:
    print("Senha incorreta")