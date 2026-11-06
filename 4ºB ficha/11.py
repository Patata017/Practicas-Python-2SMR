print("Contar el número de vocales de una frase. ")

frase = input("Introduce una frase: ")

num_vocales = 0

l= len(frase)
for i in range(l):
    if frase[i] in "aeiouAEIOU":
        num_vocales += 1
print("Número de vocales: ", num_vocales)
input()