print("Posición de una cadena en otra. (LAS POSICIONES DE UN CARÁCTER EN UNA CADENA Y DECIR CUANTAS VECES APARECE)")

cadena = input("Dime la primera cadena: ")
caracter = input("Pon el caracter a buscar en la cadena: ")

l = len(cadena)

nº = 0

for i in range(l):
    if cadena[i] == caracter:
        nº += 1
        print("El carácter", caracter, "aparece en la posición", i + 1)
print("El carácter", caracter, "aparece", nº, "veces en la cadena.")

input()