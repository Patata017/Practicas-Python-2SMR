print("Programa que crea un cuadrado magico de orden nxn, donde n es un numero impar")

n = int(input("Introduce un numero impar: "))

cuadrado = []
for i in range(n):
    fila = []
    for j in range(n):
        fila.append(0)
    cuadrado.append(fila)

# 1.- El nº 1 se coloca en la casilla justo debajo de la central.
num = 1
i = n // 2
j = n // 2
cuadrado[i][j] = num

# 2.- Cuando se coloca un nº n en la casilla (i,j) el n+1 se coloca en la (i+1, j+1).
while num < n * n:
    num += 1
    i += 1
    j += 1

    # 4.- Si al calcular los índices de una casilla se sale de los límites del cuadrado:
    # índice > N - 1 --> índice = 0
    # índice < 0 --> índice = N - 1
    if i > n - 1:
        i = 0
    if j > n - 1:
        j = 0
    if i < 0:
        i = n - 1
    if j < 0:
        j = n - 1

    # 3.- Si al ir a rellenar una casilla está ocupada se rellena la (i+1, j-1), a partir de la ocupada.
    if cuadrado[i][j] != 0:
        i += 1
        j -= 1

        # Se vuelve a comprobar límites
        if i > n - 1:
            i = 0
        if j > n - 1:
            j = 0
        if i < 0:
            i = n - 1
        if j < 0:
            j = n - 1

    cuadrado[i][j] = num

print("\nCuadrado magico de orden", n)
for i in range(n):
    for j in range(n):
        print(cuadrado[i][j], end=" ")
    print()