cantidad = int(input("¿Cuántos números quieres sumar?"))

suma = 0

for i in range(cantidad):
    print("Introduce un número:")
    n = float(input())
    suma = suma + n

print("La suma total es:", suma)
