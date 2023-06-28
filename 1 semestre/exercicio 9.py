"""
1- Crie ao menos 3 listas com pelo menos 5 itens em cada lista.

2- Imprima no console o valor do item na posição de índice 3 da sua primeira lista;

3- Substitua o valor do item na posição de índice 3 da sua primeira lista pelo valor do item na posição também 3, mas da sua segunda lista.

4- Imprima no console o novo valor do item na posição de índice 3 da sua primeira lista;
"""
g= 'guilherme'
n=10
f=2.1
c=2+5j
b=True
lista=[g, n, f, c, b]
lista2=['amanda', 'guilherme', 'ana beatriz', 'vitor', 'sara']
lista3=lista+lista2

print(lista[3])
lista[3]=[lista2[3]]
print(lista[3])
