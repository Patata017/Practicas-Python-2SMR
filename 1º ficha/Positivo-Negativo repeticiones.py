print("¿Cuántas veces quieres repetir la operación?")
veces = int(input())

for i in range(veces):
    print("Introduce un número:")
    n = float(input())
    if n > 0:
        print("El número es positivo")
    elif n < 0:
        print("El número es negativo")
    else:
        print("El número es cero")
