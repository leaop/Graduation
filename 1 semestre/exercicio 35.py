import random
number = random.randint(1,100)
class Class:
    def fatorial(number):
        if number == 1:
            return 1
        resultado = number*Class.fatorial(number-1)
        return resultado
print(number)
C = Class.fatorial(number)
print(C)
