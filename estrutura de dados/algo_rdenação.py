import random

sta = random.sample(range(1,100), 42)
print(sta)
n = len(sta)
min = sta[0]
#para o i no tamanho da lista
for i in range(n):
    #andando na lista, quero verificar se algum valor é menor do que oq eu conheço por minimo
    if sta[i] < min:
        #achando esse vai ser o meu novo minimo
        min = sta[i]
print(min)
#printei mas nao alterei
#Desenvolvendo um programa de ordenação por seleção
def selection_sort(sta):
    #posso determinar as variáveis ou ir direto
    for j in range(len(sta)-1):
        min_index = j
        for i in range(j, len(sta)):
            #antes estava só interessado em saber qual era o minimo
            #agora a.selection_sorttenho q me preocupar com o index, por isso a variavel index foi criada
            if sta[i] < sta[min_index]:
                min_index = i
        #vamos verificar se quem está na posição 0 é maior do que o minimo
        if sta[j] > sta[min_index]:
            aux = sta[j]#ponteiro
            sta[j] = sta[min_index]#ponteiro.cabeca
            sta[min_index] = aux#ponteiro.proximo


