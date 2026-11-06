print("función que realice el intercambio de valores de 2 variables A y B.")
def intercambiar_valores(a, b):
    return b, a

a = int(input("Introduce el primer número entero: "))
b = int(input("Introduce el segundo número entero: "))
a, b = intercambiar_valores(a, b)
print("Después del intercambio:")
print("a =", a, "b =", b)
input()