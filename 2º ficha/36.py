print("Programa 36 figurita")
filas = int(input("Filas: "))
cols = int(input("Columnas: "))
for i in range(filas):
    if i % 2 == 0:
        c='.'
    else:
        c='+'
    for j in range(cols):
        print(c, end="")
        if c == '+':
            c='.'
        else:
            c='+'
    print()
input()