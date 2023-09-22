###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Cartões de Crédito
# Nome: Matheus Santos Sano
# RA: 222370
###################################################

# Leitura de dados
score = int(input())
idade = int(input())
saldo = float(input())
salario= float(input())

# Verificação se o cartão de crédito será concedido ou não
if score < 300:
    cartao = False
elif score >= 300 and score < 600:
    if idade < 30:
        cartao = False
    else:
        if salario < 3000:
            cartao = False
        else:
            if saldo < 7000:
                cartao = False
            else:
                cartao = True
else:
    if idade >= 50:
        cartao = True
    else:
        if salario >= 2000:
            cartao = True
        else:
            if saldo >= 5000:
                cartao = True
            else:
                cartao = False

if cartao:
    print("Cartao concedido")
else:
    print("Cartao nao concedido")
