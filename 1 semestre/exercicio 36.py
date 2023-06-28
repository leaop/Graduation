
class Vetor:
    def menor(lista):
        menor_valor = lista[0]
        for n in range(len(lista)):
            if lista[n] < menor_valor:
                menor_valor = lista[n]
        return menor_valor

minha_lista = [7, -3, 54, 99, -96, 3, 12]
A = Vetor.menor(minha_lista)
print(f"O menor valor do vetor é de :{A}")

