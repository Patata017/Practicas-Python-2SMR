print("Programa que calcula independientemente la suma y el producto  de los números pares e impares comprendidos entre 1 y 200.")
sumaPares = 0
sumaImpares = 0
productoPares = 1
productoImpares = 1
for i in range(1, 201):
    if i % 2 == 0:
        sumaPares = sumaPares + i
        productoPares = productoPares * i
    else:
        sumaImpares = sumaImpares + i
        productoImpares = productoImpares * i
print("La suma de los pares es: ", sumaPares)
print("El producto de los pares es: ", productoPares)
print("La suma de los impares es: ", sumaImpares)
print("El producto de los impares es: ", productoImpares)
input()