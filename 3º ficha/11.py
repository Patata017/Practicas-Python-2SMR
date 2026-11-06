print("función que nos devuelva el salario de un trabajador, recibiendo un número de horas dado, y un salario por hora. Las horas que superen las 40 semanales, se pagarán al doble de las normales")
def calcular_salario(horas_trabajadas, salario_por_hora):
    if horas_trabajadas > 40:
        horas_normales = 40
        horas_extra = horas_trabajadas - 40
        salario_total = (horas_normales * salario_por_hora) + (horas_extra * salario_por_hora * 2)
    else:
        salario_total = horas_trabajadas * salario_por_hora
    return salario_total

horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))
salario_por_hora = float(input("Ingrese el salario por hora: "))
salario = calcular_salario(horas_trabajadas, salario_por_hora)
print("El salario total es: ",salario)
input()