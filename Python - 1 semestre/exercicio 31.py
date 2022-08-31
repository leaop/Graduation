import random
print("I know how to double the value of any number between one and hundred")
number = random.randint(1,100)
print(f"For example: {number}")
class Minha_Classe:
    def dobrar(number):
        return(number*2)
B = Minha_Classe.dobrar(number)
print(f"The double is:{B}")