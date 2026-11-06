print("Programa que calcula el coste de una llamada telefónica ")
print("Introduce el tiempo de llamada")
min=int(input())
if min<= 3: 
    total=min*0.15
else:
    total=3*0.15+(min-3)*0.25
print("El total es de: ",total)   
input() 