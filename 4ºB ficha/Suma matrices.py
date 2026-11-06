print("Programa que suma dos matrices y la guarda en una tercera matriz.")
matriz1 = []
matriz2 = []
matriz3 = []

n = int(input("Introduce el número de filas y columnas de las matrices: "))
print("Introduce los elementos de la primera matriz:")
for i in range(n):
    matriz1.append([])
    for j in range(n):
        matriz1[i].append([])

for i in range(n):
    for j in range(n):
        matriz1[i][j] = int(input("Introduce el valor"))

print("\nMatriz 1:")
for i in range(n):
    for j in range(n):
        print(matriz1[i][j], end=" ")
    print()

print("Introduce los elementos de la segunda matriz:")
for i in range(n):
    matriz2.append([])
    for j in range(n):
        matriz2[i].append([])

for i in range(n):
    for j in range(n):
        matriz2[i][j] = int(input("Introduce el valor"))

print("\nMatriz 2:")
for i in range(n):
    for j in range(n):
        print(matriz2[i][j], end=" ")
    print()

print("\nSuma de las dos matrices:")
for i in range(n):
    matriz3.append([])
    for j in range(n):
        matriz3[i].append(matriz1[i][j] + matriz2[i][j])
        print(matriz3[i][j], end=" ")
    print()