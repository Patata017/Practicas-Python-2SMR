print("Programa que intercambia las filas de una matriz")

matriz = []

for i in range(5):
    fila = []
    for j in range(5):
        fila.append(0)
    matriz.append(fila)

for i in range(5):
    for j in range(5):
        matriz[i][j] = int(input("Introduce el valor de la posición: "))

print("\nMatriz original:")
for i in range(5):
    for j in range(5):
        print(matriz[i][j], end=" ")
    print()

f1 = int(input("\nIntroduce la primera fila a intercambiar (0 a 4): "))
f2 = int(input("Introduce la segunda fila a intercambiar (0 a 4): "))

aux = matriz[f1]
matriz[f1] = matriz[f2]
matriz[f2] = aux

print("\nMatriz con filas intercambiadas:")
for i in range(5):
    for j in range(5):
        print(matriz[i][j], end=" ")
    print()