print("programa 33 figurita")
f=int(input("Escribe el nº de filas"))
for i in range(1, f+1):
    print("\n", end=" ")
    for p in range(f-i):
        print(" ",end=" ")
    for j in range(i):
        print("$",end=" ")
input()