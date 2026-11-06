print("Programa que inicializa una matriz de dos dimensiones con un valor constante k. Tanto las dimensiones como la constante deberán pedirse por teclado. Las filas y columnas no puede exceder de 20.")
matriz = []
k = int(input("Introduce el valor de la constante k: "))

filas = int(input("Introduce el número de filas (máximo 20): "))
columnas = int(input("Introduce el número de columnas (máximo 20): "))

while filas > 20 or columnas > 20:
    filas = int(input("El maximo de filas es 20: "))
    columnas = int(input("El maximo de columnas es 20: "))

for i in range(filas):
    matriz.append([])
    for j in range(columnas):
        matriz[i].append(k)

for i in range(filas):
    for j in range(columnas):
        print("%5d" % matriz[i][j], end=" ")
    print()

input()