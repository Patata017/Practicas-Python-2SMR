print("Programa que compara dos cadenas de caracteres caracter por caracter.")

cadena1 = input("Introduce la primera cadena de caracteres: ")
cadena2 = input("Introduce la segunda cadena de caracteres: ")

l1 = len(cadena1)
l2 = len(cadena2)

if l1 != l2:
    print("Las cadenas tienen longitudes diferentes y no se pueden comparar.")
else:
    c = True
    for i in range(l1):
        if cadena1[i] != cadena2[i]:
            print("Las cadenas son diferentes.")
            print("Difieren en la posición", i + 1)
            c = False

    if c == True:
        print("Las cadenas son iguales.")

input()