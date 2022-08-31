
def my_function():
    print("Hello from function")
my_function()

def function():
    """Essa funcao mostra um 'hello world'"""
    print('hello world')
    print('ola mundo')
function()
help(function)

def teste(name):
    print('hello', name)
teste('lex')
teste(334)

def cumprimento(nome, sobrenome, idade):
    print('Olá', nome, sobrenome, 'voce tem:', idade, 'anos de idade')
cumprimento('Manoel', 'da Silva', 22)

def ola(*nomes):
    i=0
    print('Olá', end='')
    while len(nomes) > i:
        print(nomes[1], end='')
        i+=1