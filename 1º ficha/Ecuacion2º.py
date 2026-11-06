print("Programa que calcula una ecucacion de segundo grado")
import math
print("Introduzca el valor de a")
a = float(input())

print("Introduzca el valor de b")
b = float(input())

print("Introduzca el valor de c")
c = float(input())

d = b * b - 4 * a * c

if d < 0:
    print("No hay soluciones reales")
else:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print("Las soluciones son: x1 es igual", x1, "y x2 es igual", x2)
input()