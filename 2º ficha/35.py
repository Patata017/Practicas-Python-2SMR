print("programa 35 figurita")
f=int(input("Escribe el nº de filas"))
for i in range(1, f//2+1+1):
    print("\n", end=" ")
    for j in range(f//2+1-i):
        print(" ",end=" ")
    for k in range(i):
        print("$",end=" ")
    for l in range(1, i):
        print("$",end=" ")
for i in range(f//2, 0, -1):
    print("\n",end=" ")
    for j in range(f//2-i+1):
        print(" ",end=" ")
    for k in range(i):
        print("$",end=" ")
    for l in range(i-1):
        print("$",end=" ")
input()