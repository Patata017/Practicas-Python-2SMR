print("Programa que dado un número y un porcentaje nos pida: la cantidad a pagar añadido dicho porcentaje. Este proceso se repetirá mientras que el usuario quiera.")
seguir = "s"
while seguir == "s":
    num = float(input("Introduce la cantidad: "))
    por = float(input("Introduce el porcentaje: "))
    total = num + (num * por / 100)
    print("Cantidad final:", total)
    seguir = input("¿Quieres hacer otra operación? (s/n): ")