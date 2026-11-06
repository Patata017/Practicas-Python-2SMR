print("Primera cadena de caracteres")

frase = input("Introduce una frase: ")

print(frase)

l = len(frase)

for i in range(l):
    print(frase[i], end=' ')

print()
print(frase[5])