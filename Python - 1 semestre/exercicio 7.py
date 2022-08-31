#explique cada valor. Colocar aqui ou em PDF

a = 10
# is of type of int
b = "10"
# is of type of string (String can be declared either by using single or double quotes)
c = 10
# is the same type of 'a'

d = a
# the variable 'd' is assume the value of variable 'a'.
e = b
# the variable 'e' is assume the value of variable 'b'.
f = c
# the variable 'f' is assume the value of variable 'c'.

g = int(a)
h = int(b)
i = int(c)


j = float(a)
# the variable 'j' is assume the value of variable 'a' and changing the type of variable: interger to float.
k = int(b)
#the variable 'k' is assume the value of variable 'b' without change the type 
l = str(c)
# the variable 'l' is assume the value of variable 'c' and changing the type of variable: interger for string

m = str(10.00)
#the value being assigned to 'm' is 10.00 and the class assigned to the value is of type string
n = int(10.00)
#the value being assigned to 'n' is 10.00 and the class assigned to the value is of type int
o = float("10.00")
#the value being assigned to 'o' is 10.00 and the class assigned to the value is of type float

# At this point to the end is an output of the code. The user would be able to see the value of variable and the type
print("Valor de a: ", a)
print("Tipo de a: ", type(a))

print("Valor de b: ", b)
print("Tipo de b: ", type(b))

print("Valor de c: ", c)
print("Tipo de c: ", type(c))

print("Valor de d: ", d)
print("Tipo de d: ", type(d))

print("Valor de e: ", e)
print("Tipo de e: ", type(e))

print("Valor de f: ", f)
print("Tipo de f: ", type(f))

print("Valor de g: ", g)
print("Tipo de g: ", type(g))

print("Valor de h: ", h)
print("Tipo de h: ", type(h))

print("Valor de i: ", i)
print("Tipo de i: ", type(i))

print("Valor de j: ", j)
print("Tipo de j: ", type(j))

print("Valor de k: ", k)
print("Tipo de k: ", type(k))

print("Valor de l: ", l)
print("Tipo de l: ", type(l))

print("Valor de m: ", m)
print("Tipo de m: ", type(m))

print("Valor de n: ", n)
print("Tipo de n: ", type(n))

print("Valor de o: ", o)
print("Tipo de o: ", type(o))
