import time

def caixa(linhas, colunas):

    colunas = 1 + colunas * 3
    # Cria a matriz preenchida com espaços
    matriz = [[" " for _ in range(colunas)] for _ in range(linhas)]

    # Preenche as bordas superior e inferior
    for j in range(1, colunas - 1):
        matriz[0][j] = "‾"
        matriz[linhas - 1][j] = "‾"

    # Preenche as bordas laterais
    for i in range(1, linhas - 2):
        matriz[i][0] = "|"
        matriz[i][colunas - 1] = "|"

    # Define os quatro cantos
    matriz[0][0] = "⌈"
    matriz[0][colunas - 1] = "⌉"
    matriz[linhas - 2][0] = "⌊"
    matriz[linhas - 2][colunas - 1] = "⌋"
    
    return matriz


def mostrar_caixa(caixa):
    for linha in caixa:
        print("".join(linha))
    print("\n\n")


def grao(caixa):
    for linha in range(len(caixa)):
        if linha == 1:
            meio = round(len(caixa[linha])/2)
            caixa[linha][meio] = "*"
            mostrar_caixa(caixa)
        if linha > 1 and linha < len(caixa)-1:
            caixa[linha-1][meio] = " "
            caixa[linha][meio] = "*"
            time.sleep(1)
            mostrar_caixa(caixa)

def rotar(caixa):
    for i in range(len(caixa)):
        for j in range(len(caixa[i])):
            if caixa[i][j] == "*":
                caixa[i][0] == "*"
                caixa[i][j] == " "
    mostrar_caixa(caixa)

box = caixa(8, 6)
mostrar_caixa(box)
grao(box)
rotar(box)