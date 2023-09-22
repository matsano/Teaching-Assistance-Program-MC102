###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 13 - Ordenação de Panquecas
# Nome: Matheus Santos Sano
# RA: 222370
###################################################


# Dada uma sequência de números de inteiros, gera
# uma string representando a pilha de panquecas
def str_panquecas(lista):
    return(" ".join(map(str, lista)))

def posicao_correta(lista):
    maior = max(lista)
    posicao = lista.index(maior)
    parte_lista = lista[posicao:len(lista)]
    if parte_lista == sorted(parte_lista):
        return True
    else:
        return False

def primeira_inversao(lista, posicao):
    lista1 = lista[0:posicao+1]
    lista2 = lista[posicao+1:len(lista)]
    lista1.reverse()
    return lista1 + lista2

panquecas = [int(x) for x in input().split()]
if panquecas == sorted(panquecas):
    print("Panquecas ja ordenadas")
else:
    panquecas_restantes = panquecas.copy()
    panquecas_ordenadas = []
    while panquecas != sorted(panquecas):
        if not posicao_correta(panquecas_restantes):
            maior_panqueca = max(panquecas_restantes)
            print("Posicionando a panqueca", maior_panqueca)
            posicao_maior = panquecas_restantes.index(maior_panqueca)
            if posicao_maior != 0:
                panquecas_restantes = primeira_inversao(panquecas_restantes, posicao_maior)
                print("Primeira inversao:", str_panquecas(panquecas_restantes + panquecas_ordenadas))
            panquecas_restantes.reverse()
            print("Segunda inversao:", str_panquecas(panquecas_restantes + panquecas_ordenadas))
        panquecas_ordenadas.append(panquecas_restantes[-1])
        panquecas_ordenadas.sort()
        panquecas_restantes.pop(-1)
        panquecas = panquecas_restantes + panquecas_ordenadas
