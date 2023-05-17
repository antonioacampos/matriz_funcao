def print_matriz(L, matriz):
    linhas = L[0]
    colunas = L[1]
    contacol = 0
    contalinha = 0
    i = 0
    print(f"A organização dos números em matriz {linhas} x {colunas} é:") 
    while contalinha < linhas:
        while contacol < colunas:
            print(matriz[i], end=' ')
            i += 1
            contacol += 1
        contalinha += 1
        contacol = 0
        print()

def soma_linhas(L, matriz):
    linhas = L[0]
    colunas = L[1]
    contacol = 0
    contalinha = 0
    i = 0
    somalinha = 0
    print("A soma das linhas dessa matriz é:")
    while contalinha < linhas:
        while contacol < colunas:
            somalinha += matriz[i]
            i += 1
            contacol += 1
        print(somalinha, end=' ')
        somalinha = 0
        contalinha += 1
        contacol = 0
        print()

def soma_colunas(L, matriz):
    linhas = L[0]
    colunas = L[1]
    contacol = 0
    contalinha = 0
    somacoluna = 0
    colunassomadas = 0
    print("A soma das colunas dessa matriz é:")
    while colunassomadas < colunas:
        for i in range (colunassomadas, len(matriz), colunas):
            somacoluna += matriz[i]
        print(somacoluna)
        somacoluna = 0
        colunassomadas += 1

#############################################################
L = list(map(int, input().split()))
matriz = list(map(int, input().split()))
print_matriz(L, matriz)
print()
soma_linhas(L, matriz)
print()
soma_colunas(L, matriz)
