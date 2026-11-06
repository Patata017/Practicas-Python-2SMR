print("Programa que rellenar un array o lista de 10 elementos colocando cada elemento en su posición. Tiene que quedar ordenado")
array = []

for i in range(10):
    array.append([])

for i in range(10):
    array[i] = i
    print(array[i], end=" ")
input()