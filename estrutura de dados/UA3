#Desafio 
#banco de dados interativo (clientes)

arq = open('arquivo.txt', 'w')
art.writelines(['Nome´, '\t', 'Telefone', '\t', 'Saldo', '\n'])
arq.close()

controle = 1
while True:
    print('Cadastro de Clientes')
    print('1-Cadastrar novo cliente:')
    print('2-Sair')
    controle = int(input('Escolha uma opção:'))
    if(controle==2):
      break
     print('--------------------------', end='\n')
     if controle==1:
       nome = input('Digite o nome do cliente:')
       telefone = input('Digite o telefone:')
       saldo = float(input('Digite o saldo (em reais):'))
       msg = [nome, '\t', telefone, '\t\t', str(saldo), '\n']
       #Abre o arquivo .txt, caso não exista o arquivo será criado
       arq = open('banco.txt', 'a')
       art.writelines(msg)
       art.close()
       
       print('-----------------', end='\n')
print('-----------------', end='\n')
print('Fim do cadastro de clientes')

