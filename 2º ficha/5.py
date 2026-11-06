print("Programa que dado un número y un porcentaje nos pida: la cantidad a pagar quitado dicho porcentaje.  Este proceso se repetirá N veces")
N = int(input("¿Cuántas veces quieres repetir la operación? "))
for i in range(N):
    cantidad = float(input("Introduce la cantidad: "))
    porcentaje = float(input("Introduce el porcentaje a quitar: "))
    descuento = cantidad * porcentaje / 100
    pago_final = cantidad - descuento
    print("La cantidad final a pagar es:", pago_final)