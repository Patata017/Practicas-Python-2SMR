print("Rellenar dos arrays o listas  y obtener otro array o lista con los elementos de las dos tablas sumados elemento a elemento")
numeros1 = []
numeros2 = []   
numeros3 = []
for i in range(7):

    numeros1.append([])
    numeros2.append([])
    numeros3.append([])

for i in range(7):

    numeros1[i] = int(input("Introduce el número del primer array: "))
    print("--------------------------------------------------------")
    numeros2[i] = int(input("Introduce el número del segundo array: "))
    numeros3[i] = numeros1[i] + numeros2[i]

print("El array resultante es: ")

for i in range(7):

    print(numeros3[i], end=" ")

input()