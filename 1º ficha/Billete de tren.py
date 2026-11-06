print("Programa que determina el precio de un billete de tren")
print("======================================================")
print("Introduce la distancia en km")
km=int(input())
print("Introduce los días afuera")
d=int(input())
total=km*0.25
if d>7 and km>800: 
    total= total-(total*0.30)
    print("El total es de: ",total)
else:
    print("El total es de: ",total)
input()