print("Programa que determinar de un conjunto de 100 números leídos de teclado, cuántos hay menores de 15, cuantos están entre 25 y 45 y cuántos son mayores de 50")
menores15 = 0
entre25y45 = 0
mayores50 = 0
for i in range(1, 101):
    print("Introduce un número:")
    n = float(input())
    if n < 15:
        menores15 = menores15 + 1
    elif n >= 25 and n <= 45:
        entre25y45 = entre25y45 + 1
    elif n > 50:
        mayores50 = mayores50 + 1
print("Cantidad menores de 15:", menores15)
print("Cantidad entre 25 y 45:", entre25y45)
print("Cantidad mayores de 50:", mayores50)