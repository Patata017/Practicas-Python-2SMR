print("Programa que nos pida un N números que estén comprendidos entre -10 y 10  y si no que nos digan que están fuera de rango y pida otro. Si están en el rango que nos diga cual es positivo y cual es negativo.")
N = int(input("¿Cuántos números quieres introducir?"))
for i in range(N):
    num = int(input("Introduce un número entre -10 y 10: "))
    while num < -10 or num > 10:
        print("Fuera de rango, introduce otro:")
        num = int(input())
    if num > 0:
        print("El número es positivo")
    elif num < 0:
        print("El número es negativo")
    else:
        print("El número es cero")
input()