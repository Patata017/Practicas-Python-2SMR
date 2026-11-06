print("Programa que pide N números y sume los que son pares por una parte y los impares por otra.")
N = int(input("¿Cuántos números vas a introducir? "))
sp = 0
si = 0
for i in range(N):
    n = int(input("Introduce un número: "))
    if n % 2 == 0:
        sp += n
    else:
        si += n
print("Suma de pares:", sp)
print("Suma de impares:", si)