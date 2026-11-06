print("Programa que calcule la media de las estaturas de los alumnos de una clase. Deducir cuantos son más altos que la media y cuántos más bajos que dicha media")
alturas = []

for i in range(10):
    alturas.append([])

for i in range(10):
    alturas[i] = float(input("Introduce la estatura del alumno en metros: "))

suma = 0

for i in range(10):
    suma = suma + alturas[i]

media = suma / 10
print("La estatura media de la clase es de:", media, "metros")

altos = 0
bajos = 0

for i in range(10):
    if alturas[i] > media:
        altos = altos + 1
    else:
        bajos = bajos + 1

print("El número de alumnos más altos que la media es de:", altos)
print("El número de alumnos más bajos que la media es de:", bajos)