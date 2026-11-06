print("Programa  que permita rellenar un array o lista con el  cuadrado de los 100 primeros números enteros y a continuación escribir dicho array")
numeros = []
for i in range(100):
    numeros.append([])   

for i in range(100):
    numeros[i] = i**2

for i in range(100):
    print(numeros[i], end=" ")

input()