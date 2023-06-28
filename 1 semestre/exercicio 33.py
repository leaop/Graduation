import random
number = random.randint(1,10)
number2 = random.randint(11,21)
class Change:
    def trocar(number, number2):
        return (number2, number)
print(f"A ordem original é: {number}, {number2}")
C = Change.trocar(number,number2)
print(f"pela magica do python, agora a ordem é: {C}")