###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Fórmula 1
# Nome: Matheus Santos Sano
# RA: 222370
###################################################

# Leitura de dados
t = float(input())
dist_a = int(input())
vel_a = float(input())
t_pit_stop = float(input())
dist_b = int(input())
vel_b = float(input())

# Cálculo do tempo total gasto para realizar o pit stop
t_a = 3.6 * (dist_a / vel_a)
t_b = 3.6 * (dist_b / vel_b)
t_total = t_a + t_pit_stop + t_b

# Impressão da resposta
if t_total < t:
    print(True)
else:
    print(False)
