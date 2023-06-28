print("this is the program to find the total sum of numbers and the avarage between them")
print("To start I ask you a little help: put the number 1, number 2 and number 3... after that I can help you")

number1=int(input("put the first number: "))
number2=int(input("put the second number: "))
number3=int(input("put the third number: "))

print(f'The numbers you choose are: {number1}, {number2}, {number3}')
list=(number1, number2, number3)
print("The sum is:", sum(list))
print("The avarage is:", sum(list)/len(list))

#segundo o enunciado da questão o maior erro mesmo aqui foi colocar o input como int e não como float
"""
num1 = 0
num2 = 0
num3 = 0
def ler_numeros():
    global1 num1
    global1 num2
    global1 num3
    num1 = float (input("digite o primeiro numero: "))
    num2 = float (input("digite o segundo numero: "))
    num3 = float (input("digite o terceiro numero: "))
    print(fÓs numeros lidos são: {num1}, {num2}, {num3}')

def calcular_soma():
    global num1
    global num2
    global num3
    soma = num1 + num2 + num3
    print(f'A soma é: {soma}')

def calcular_media():
    global num1
    global num2
    global num3
    media = (num1 + num2 + num3) / 3
    print(f'A média é: {media}')

ler_numeros()
calcular_soma()
calcular_media()
    """