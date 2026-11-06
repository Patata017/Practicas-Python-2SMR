print("Programa que puede leer las calificaciones de una clase de informática y contar el número total de aprobados (5 o más de 5) y el de notables (7 y 8).")
cantidad = int(input("Introduce el número de alumnos: "))
aprobados = 0
notables = 0
for i in range(cantidad):
    nota = float(input("Introduce la nota: "))
    if nota >= 5:
        aprobados = aprobados + 1
    if nota >= 7 and nota < 9:
        notables = notables + 1
print("Total de aprobados:", aprobados)
print("Total de notables:", notables)