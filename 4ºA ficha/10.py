print("Matriz 10x10 con las filas pares a 1 y las impares a 0")
matriz = []

for i in range(10):
    matriz.append([])
    for j in range(10):
        matriz[i].append([])

for i in range(10):
    for j in range(10):
        if i % 2 == 0:
            matriz[i][j] = 1
        else:
            matriz[i][j] = 0

for i in range(10):
    for j in range(10):
        print("%5d" % matriz[i][j], end=" ")
    print()
input()