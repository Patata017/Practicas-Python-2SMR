print("Programa que sume los cuadrados de los números terminados en 9, de entre los 100 que le pediremos al usuario.")
s=0
for i in range(1, 11):
    n=int(input("Escribe un número"))
    if n%10==9:
        s=s+n**2
        i=i+1
print("La suma de los cuadrados es de: ",s)
input()