print("11.	Programa que pida un número “NUM”· al usuario por teclado, y lea ese número de números y calcula lo siguiente")
num = int(input("Introduce el número: "))
sp = 0
pi = 1
cm = 0
sm = 0
sr = 0
cr = 1000
for i in range(num):
    n = int(input("Introduce un número: "))
    if n % 2 == 0:
        sp += n
    else:
        pi *= n
    if n % 15 == 0:
        sm += n
        cm += 1
if cm > 0:
    mm = sm / cm
else:
    mm = 0
for x in range(num, num + 1000):
    sr += x
mr = sr / cr
print("Suma pares:", sp)
print("Producto impares:", pi)
print("Media múltiplos de 15:", mm)
print("Media rango:", mr)
