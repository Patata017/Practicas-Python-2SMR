print("Programa que escriba todos los múltiplos de 3 que estén comprendidas entre dos cantidades leídas del teclado.")
a = int(input("Introduce el primer número: "))
b = int(input("Introduce el segundo número: "))
for n in range(a, b + 1):
    if n % 3 == 0:
        print(n)