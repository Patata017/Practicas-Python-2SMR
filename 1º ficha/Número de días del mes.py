print("Programa que dado el nombre de un mes y si el año es o no bisiesto, deducir el número de días del mes.")
print("Introduce el mes")
mes=input()
print("¿El año es bisiesto? Introduce S/N:")
b=input()
if mes == "enero" or mes == "marzo" or mes == "mayo" or mes == "julio" or mes == "agosto" or mes == "octubre" or mes == "diciembre":
    print("El mes tiene 31 días")
elif mes == "abril" or mes == "junio" or mes == "septiembre" or mes == "noviembre":
    print("El mes tiene 30 días")
elif mes == "febrero":
    if b == "S":
        print("El mes tiene 29 días")
    else:
        print("El mes tiene 28 días")
input()