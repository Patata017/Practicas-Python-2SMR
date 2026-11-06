print("Subprograma que encuentre el mayor de dos enteros y el menor de dos números enteros")
def primera_potencia_mayor_que(n1, n2):
    mayor = 0
    menor = 0
    if n1 > n2:
        mayor = n1
        menor = n2
    else:
        mayor = n2
        menor = n1

    return mayor, menor

n1 = int(input("Introduce el primer número entero: "))
n2 = int(input("Introduce el segundo número entero: "))
may, men = primera_potencia_mayor_que(n1, n2)
print("El mayor es:", may)
print("El menor es:", men)
input()