matriz = []
tamaño = int(input("Introduce el tamaño de la matriz"))

for i in range(tamaño):
    matriz.append([])
    for j in range(tamaño):
        matriz[i].append([])

for i in range(tamaño):
    for j in range(tamaño):
        print("Da número para fila", i, "columna", j)
        matriz[i][j] = int(input())

for i in range(tamaño):
    for j in range(tamaño):
        print("%5d" % matriz[i][j], end=" ")
    print()