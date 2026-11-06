print("Programa que lee números hasta que se den 5 ceros, y escriba después la suma de los números leídos")
s=0
c=0
while c < 5:
    n = int(input("Introduce un número: "))
    if n<0:
        c=c+1
    else:
        s=s+n
print("La suma de los números leídos es:", s)
input()