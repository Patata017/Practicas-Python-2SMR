print("Programa que pide un número entero y nos diga si el número es capicúa")
ninv = 0
n=int(input("Escribe un número"))
noriginal = n
while n != 0:
    r = n % 10
    ninv = ninv * 10 + r
    n= n//10
print("El número inverso es: ",ninv)
if noriginal == ninv:
    print("El número es capicúa")
else:
    print("El número no es capicúa")
input()