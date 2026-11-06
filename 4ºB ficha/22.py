print("Programa con una Función que se le pasa una frase (se lee en otro programa o en el principal) y devuelve el número de vocales y de consonantes que tiene")

def contar(frase):
    vocales = "aeiouAEIOU"
    num_vocales = 0
    num_consonantes = 0
    len_frase = len(frase)
    for i in range(len_frase):
        if frase[i] in vocales:
            num_vocales += 1
        else:
            num_consonantes += 1
    return num_vocales, num_consonantes

frase = input("Introduce una frase sin caracteres especiales:")
while frase == "":
    frase = input("La frase no puede estar vacía ni puede tener caracteres especiales:")
vocales, consonantes = contar(frase)
print("La frase tiene", vocales, "vocales y", consonantes, "consonantes.")
input()