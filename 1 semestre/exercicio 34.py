import random
print("será que consegue dizer mais rapido que eu se o numero é par ou impar?")
numero = random.randint(1,100)
print(f"o numero que escolhi foi:{numero}")
class EO:
    def parouimpar(numero):
        if numero%2==0:
            return("É par")
        else:
            return("É impar")
A = EO.parouimpar(numero)
print(A)
resp = str(input("Foi mais rapido que eu?"))
if resp in "sim":
    print("voce é rapido em")
else:
    print("um dia voce consegue")
