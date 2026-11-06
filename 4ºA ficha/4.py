print("Rellenar un array o lista y obtener otro con los pares  y otro con los  impares")
np = 0
ni = 0
numeros = []
pares = [] 
impares = []
for i in range(10):
    numeros.append([])   
    pares.append([])
    impares.append([])

for i in range(10):
    numeros[i] = int(input("Introduce un número: "))
    if numeros[i] % 2 == 0:
        pares[np] = numeros[i]
        np += 1
    else:
        impares[ni] = numeros[i]
        ni += 1

print("El array de pares es: ")

for i in range(np):
    print(pares[i], end=" ")

print("\nEl array de impares es: ")

for i in range(ni):
    print(impares[i], end=" ")

input()