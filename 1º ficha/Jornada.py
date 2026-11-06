print("Programa que calcula la jornada")
print("Introduce si el turno es diurno o nocturno: ")
turno = input()
print("Introduce si es domingo o no S/N: ")
D = input()
print("Introduce el número de horas: ")
Horas = float(input())
if D == "S":
    if turno == "diurno":
        Total = Horas * (50 + 20)
        print("El total es de:", Total)
    elif turno == "nocturno":
        Total = Horas * (80 + 20)
        print("El total es de:", Total)
elif D == "N":
    if turno == "diurno":
        Total = Horas * 50
        print("El total es de:", Total)
    elif turno == "nocturno":
        Total = Horas * 80
        print("El total es de:", Total)
input()