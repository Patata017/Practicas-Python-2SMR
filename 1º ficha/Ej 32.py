print("Programa que nos pida un número y  nos diga si es positivo o negativo  y además lo realice hasta que le introduzcamos que no queremos más veces.")
continuar = 'S'
while continuar == 'S' or continuar == 's':
    num = float(input("Introduce un número: "))
    if num > 0:
        print("El número es positivo")
    elif num < 0:
        print("El número es negativo")
    else:
        print("El número es cero")
    continuar = input("¿Quieres introducir otro número? (S/N): ")
input()