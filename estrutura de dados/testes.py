#sempre com testes aleatórios
def somar_matrizes(a, b):
    """Devolve a soma das matrizes a e b"""
    assert len(a) == len(b), "escrita"
    assert len(a[0]) == len(b[0]), "Números de colunas devem ser iguais"

    m = len(a)
    n = len(a[0])

    soma = []
    for i in range(m):
        linha = []
        soma.append(linha)
        for j in range(n):
            celula = a[i][j] + b[i][j]
            linha.append(celula)
    return soma

def main():
    a = [
      [5.3, 4.0, 7.5],
      [9.0, 0.0, 9.5],
      [7.0, 6.9, 7.8]
    ]
    b = [
      [1.0, 1.0, 1.0],
      [1.0, 1.0, 1.0],
      [1.0, 1.0, 1.0]
    ]
    soma = somar_matrizes(a, b)
    print(soma)

main()