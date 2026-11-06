print("Programa que da la factura")
print("Introduce el precio")
p=int(input())
print("Introduce las unidades a comprar")
u=int(input())
total=p*u*1.16
if total>500:
    total=total*0.95
print("El total es de: ",total)
input()