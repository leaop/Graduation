
import random
name = input("Hello, whats your name? ")
number = random.randint(0,20)
print("Let's try our conexion on math")
try:
    print('block try')
    x=int(input('try a number: '))
    y=number
    z=x/y
except ZeroDivisionError:
    print("Exception with block ZeroDivisionError")
    print("Division by zero not allowed")
# Observe que o tipo Exception que eh generico vem depois de ZeroDivisionError, senão não entraria no especifico ZeroDivisionError
except Exception:
    print("Something wrong happened")
else:
    print("block de else")
    print("Result = ", z)
finally:
    print("Block, life will continue, finally block")
    x=0
    y=0
print ("Code out of try, except, else and block finally." )


