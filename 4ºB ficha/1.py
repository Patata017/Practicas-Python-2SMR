print("Programa que calcula la letra del DNI")

#DNI/23 = Resto

dni = int(input("Introduce tu número de DNI (sin letra): "))
resto = dni % 23
letras = "TRWAGMYFPDXBNJZSQVHLCKE"
letra_dni = letras[resto]
print("La letra correspondiente al DNI", dni, "es:", letra_dni)
input()
