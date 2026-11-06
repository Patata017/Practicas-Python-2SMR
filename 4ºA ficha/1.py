print(" Programa que calcula la suma de todos los elementos de un  array o lista de dimensión 10, así como su media aritmética y cual es valor máximo y mínimo")
numeros = []
for i in range(10):
    numeros.append([])

print("números") 

for i in range(10):
    numeros[i] = int(input("Ingrese el número"))

mayor = 0
menor = 0
s = 0

for i in range(10):
    s = s + numeros[i]
    m = s / 10

    if numeros[i] > mayor:
        mayor = numeros[i]

    if numeros[i] < menor :
        menor = numeros[i]

    print(numeros[i], end=" ")

print("\nEl número mayor es:", mayor)
print("El número menor es:", menor)
print("La suma de los números es:", s)
print("La media aritmética es:", m)
input()