print("Programa que lee una frase y determina si es un palíndromo")

frase = input("Dime una frase: ")

es = "s"
inicio = 0
l = len(frase)
final = l - 1
while (es == "s") and (inicio <= 1//2):

    while frase[inicio] == " ":
        inicio += 1
    while frase[final] == " ":
        final -= 1
    if frase[inicio] == frase[final]:
        inicio += 1
        final -= 1
    else:
        es = "n"

if es == "s":
    print("La frase es un palíndromo.")
else:
    print("La frase no es un palíndromo.")

input()