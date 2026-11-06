print("Programa que ordena un array o lista de 10 números en orden creciente por el método de la burbuja.")
numeros = []
for i in range(10):
    num = int(input("Introduce el número: "))
    numeros.append(num)

len_numeros = len(numeros)

for i in range(len_numeros - 1):
    for j in range(len_numeros - 1 - i):
        if numeros[j] > numeros[j + 1]:
            aux = numeros[j]          
            numeros[j] = numeros[j+1] 
            numeros[j+1] = aux

print("Los números ordenados en orden creciente son:")
for num in numeros:
    print(num, end=" ")

input()