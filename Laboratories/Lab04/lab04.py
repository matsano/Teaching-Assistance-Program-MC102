###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Avatar
# Nome: Matheus Santos Sano
# RA: 222370
###################################################

# Inicialização das variáveis
water = 0
fire = 0
earth = 0
air = 0

# Leitura da sequência de treinamento
habilidade = input()
while habilidade != "X":
    P = int(input())
    if habilidade == "W":
        water += P
        fire -= P/2
        if fire < 0:
            fire = 0
    elif habilidade == "F":
        fire += P
        water -= P/2
        if water < 0:
            water = 0
    elif habilidade == "E":
        earth += P
        air -= P/2
        if air < 0:
            air = 0
    else:
        air += P
        earth -= P/2
        if earth < 0:
            earth = 0
    habilidade = input()

# Impressão das informações de saída
print("Pontuacao Final")
print("Agua: {:.1f}".format(water))
print("Terra: {:.1f}".format(earth))
print("Fogo: {:.1f}".format(fire))
print("Ar: {:.1f}".format(air))

if water > 0 and earth > 0 and fire > 0 and air > 0:
    print("Treinamento realizado com sucesso.")
else:
    print("Realize mais treinamentos.")
