print("Programa para determinar si un número es par o impar")
print("Escribe el número")
x=int(input())
if x==0: print("El número es 0")
else:
    d=x%2
if d==0: print("El número es par")
else: 
    print("El número es impar")
input()