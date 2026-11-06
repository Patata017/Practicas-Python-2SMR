matriz = []

for i in range(3):
    matriz.append([])
    for j in range(6):
        matriz[i].append([])

for i in range(3):
    for j in range(6):
        print("Da número para fila", i, "columna", j)
        matriz[i][j] = int(input())

for i in range(3):
    for j in range(6):
        print("%5d" % matriz[i][j], end=" ")
    print()

pos = 0
neg = 0
cero = 0

for i in range(3):
    for j in range(6):
        if matriz[i][j] == 0:
            cero += 1
        elif matriz[i][j] > 0:
            pos += 1
        else:
            neg += 1
            
print("Cantidad de números positivos:", pos)
print("Cantidad de números negativos:", neg)
print("Cantidad de ceros:", cero)
input()