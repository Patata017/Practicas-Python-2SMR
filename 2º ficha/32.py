print("Programa 32 figurita")
f=int(input("Escribe el nº de filas"))
c=int(input("Escribe el nº de columnas"))
for i in range(1, f+1):
    print("\n", end=" ")
    for j in range(1, c+1):
        print("&",end=" ")
input()