print("Programa que cree un array o lista llamado datos de 10 enteros, que inicialice los elementos del array o lista con el doble de su índice, y por último que nos enseñe el contenido del array o lista.")
numeros = []
for i in range(10):
    numeros.append([])   

for i in range(10):
    numeros[i] = i*2

for i in range(10):
    print(numeros[i], end=" ")

input()