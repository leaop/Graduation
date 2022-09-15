#tentativa
#algoritmo que armazene, efetua a soma e apresente o resultado
"""
def soma_meses(janeiro, fevereiro):
    assert len(janeiro) == len(fevereiro), "escrita"
    assert len(janeiro[0]) == len(fevereiro[0]), "escrita"
    l = len(janeiro)
    c = len(janeiro[0])

    soma = []
    for i in range(l):
        linha = []
        soma.append(linha)
        for j in range(c):
            celula = janeiro[i][j] + fevereiro[i][j]
            linha.append(celula)
    return soma
def main():
    janeiro = [
      [40,30,45],
      [90, 95, 90],
      [32, 3, 8],
      [23, 33, 33]
    ]
    fevereiro = [
      [0, 35, 10],
      [1, 32, 30],
      [1, 3, 0],
      [0, 3, 9]
    ]
    soma = soma_meses(janeiro, fevereiro)
    print(soma)
"""
#curso em video de python deu melhor as dicas

# função responsável por somar duas matrizes
# Parâmetros: matriz A e matriz B que serão somadas.
# Obs.: as matrizes são quadradas, ou seja possuem a mesma quantidade de
# linhas e colunas
def somarMatrizes(matrizJaneiro, matrizFevereiro):
    matriz_soma = [] # matriz vazia que receberá o resultado da soma
    quant_linhas = len(matrizJaneiro) # variável que armazena a quantidade de linhas de uma matriz
    quant_colunas = len(matrizJaneiro[0]) # variável que armazena a quantidade de colunas de uma matriz
    # laço de repetição para acessar as linhas das matrizes,
    # em que i executa de 0 até a quantidade de linhas
    for i in range(quant_linhas):
        matriz_soma.append([])
        # laço de repetição para acessar as colunas das matrizes
        for j in range(quant_colunas):
            # soma a primeira posição da matriz A com a primeira posição da Matriz B
            soma = matrizJaneiro[i][j] + matrizFevereiro[i][j]
            # armazena o resultado na matriz resultado
            matriz_soma[i].append(soma)
    return matriz_soma

# Função responsável por apresentar a matriz para o usuário
# Parâmetros: matriz que se deseja apresentar e a quantidade de linhas
def mostraMatriz(matriz, linhas):
    # laço de repetição em que i executa de 0 até o tamanho da matriz
    # e utiliza o valor de i para acessar a posição na matriz
    for i in range(linhas): 
        print(matriz[i][:])

if __name__ == "__main__":
    # cria a matriz do primeiro mês
    matrizJaneiro=[[40,90,32,23], [30,95,3,33], [45,90,8,33]]
    # cria a matriz do segundo mês
    matrizFevereiro=[[0,1,1,0], [35,32,3,3],[10,30,0,9]]
    # chama a função de somar matrizes passando por parâmetro as duas matrizes
    # criadas e armazena o resultado na matriz auxiliar
    matrizResult=somarMatrizes(matrizJaneiro, matrizFevereiro)
    # chama a função de mostrar matriz, em que deseja-se apresentar a matriz resultado
    mostraMatriz(matrizResult, len(matrizResult))