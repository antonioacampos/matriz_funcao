def print_matriz(L, matriz):
    linhas = L[0] #Define quantas linhas terá a matriz
    colunas = L[1] #Define quantas colunas terá a matriz
    contacol = 0 #contador de colunas
    contalinha = 0 #contador de linhas
    i = 0
    print(f"A organização dos números em matriz {linhas} x {colunas} é:") 
    while contalinha < linhas:
        while contacol < colunas:
            print(matriz[i], end=' ') #imprime cada linha de uma vez, respeitando o limite de colunas
            i += 1
            contacol += 1
        contalinha += 1
        contacol = 0
        print()

def soma_linhas(L, matriz):
    linhas = L[0] #Define quantas linhas terá a matriz
    colunas = L[1] #Define quantas colunas terá a matriz
    contacol = 0 #contador de colunas
    contalinha = 0 #contador de linhas
    i = 0
    somalinha = 0
    print("A soma das linhas dessa matriz é:")
    while contalinha < linhas:
        while contacol < colunas: #soma cada linha de uma vez, respeitando o número de colunas
            somalinha += matriz[i] #adiciona o elemento da linha à soma
            i += 1
            contacol += 1
        print(somalinha, end=' ') #imprime a soma da linha
        somalinha = 0 #reseta os contadores
        contalinha += 1 #conta quantas linhas já foram somadas
        contacol = 0
        print()

def soma_colunas(L, matriz):
    linhas = L[0] #Define quantas linhas terá a matriz
    colunas = L[1] #Define quantas colunas terá a matriz
    contacol = 0 #contador de colunas
    contalinha = 0 #contador de linhas
    somacoluna = 0
    colunassomadas = 0
    print("A soma das colunas dessa matriz é:")
    while colunassomadas < colunas:
        for i in range (colunassomadas, len(matriz), colunas): #soma os elementos de cada coluna, de acordo com o número de colunas
            somacoluna += matriz[i]
        print(somacoluna)
        somacoluna = 0
        colunassomadas += 1 #conta quantas colunas já foram somadas

#############################################################
L = list(map(int, input().split()))
matriz = list(map(int, input().split()))
print_matriz(L, matriz)
print()
soma_linhas(L, matriz)
print()
soma_colunas(L, matriz)
