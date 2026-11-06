print("Programa que determina el mayor de entre tres números")
print("Escribe el primer número")
a=float(input())
print("Escribe el segundo número")
b=float(input())
print("Escribe el tercer número")
c=float(input())
if a > b and a > c:
    print("El primer número es el mayor de los tres")
elif b > a and b > c:
    print("El segundo número es el mayor de los tres")
elif a==b and a==c and b==c:
    print("Los tres números son iguales")
else:
    print("El tercer número es el mayor de los tres")

input()