print("¿Cuántos números quieres introducir?")
N = int(input())
sumaTotal = 0
sumaPos = 0
sumaNeg = 0
contPos = 0
contNeg = 0
print("Introduce un número:")
num = float(input())
mayor = num
menor = num
sumaTotal = sumaTotal + num
if num > 0:
    sumaPos = sumaPos + num
    contPos = contPos + 1
elif num < 0:
    sumaNeg = sumaNeg + num
    contNeg = contNeg + 1
for i in range(2, N + 1):
    print("Introduce un número:")
    num = float(input())
    sumaTotal = sumaTotal + num
    if num > 0:
        sumaPos = sumaPos + num
        contPos = contPos + 1
    elif num < 0:
        sumaNeg = sumaNeg + num
        contNeg = contNeg + 1
    if num > mayor:
        mayor = num
    if num < menor:
        menor = num
mediaTotal = sumaTotal / N
if contPos > 0:
    mediaPos = sumaPos / contPos
else:
    mediaPos = 0
if contNeg > 0:
    mediaNeg = sumaNeg / contNeg
else:
    mediaNeg = 0
print("La media aritmética total es:", mediaTotal)
print("La media aritmética de los positivos es:", mediaPos)
print("La media aritmética de los negativos es:", mediaNeg)
print("El mayor es:", mayor)
print("El menor es:", menor)