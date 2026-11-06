print("Función que nos diga si un número es capicúa. Hay que hacerlo utilizando otra función llamada “Invertir” a la que pasamos un número y lo devuelve con los dígitos en orden inverso, por ejemplo le pasamos 45651 y devuelve 15654")
def invertir(n):
    ninv = 0
    noriginal = n
    while n != 0:
        r = n % 10
        ninv = ninv * 10 + r
        n = n//10
    return ninv

def capicua(inv):
    ninv = invertir(n)
    if noriginal == ninv:
        return True
    else:
        return False

n = int(input("Introduce un número: "))
noriginal = n
inv = invertir(n)
if capicua(inv) == True:
    print("El número es capicúa")
else:
    print("El número no es capicúa")