print("Programa que defina una matriz de 4x4 e inicialice sus elementos con la suma de su fila más su columna")
matriz = []

for i in range(4):
    matriz.append([])
    for j in range(4):
        matriz[i].append([])

for i in range(4):
    for j in range(4):
        matriz[i][j] = i + j

for i in range(4):
    for j in range(4):
        print("%5d" % matriz[i][j], end=" ")
    print()
input()