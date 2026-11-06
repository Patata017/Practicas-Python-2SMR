print("Programa que lea tres números e imprima los dos números cuya diferencia sea menor")
print("Escribe el primer número")
a=float(input())
print("Escribe el segundo número")
b=float(input())
print("Escribe el tercer número")
c=float(input())
if a>b:
    difAB=a-b
else:
    difAB=b-a
if a>c:
    difAC=a-c
else:
    difAC=c-a
if b>c:
    difBC=b-c
else:
    difBC=c-b
if difAB<=difAC and difAB<=difBC:
    print("Los números cuya diferencia es menor son: ",a, "y ",b)
elif difAC<=difAB and difAC<=difBC:
    print("Los números suya diferencia es menor son: ",a, "y ",c)
else:
    print("Los números suya diferencia es menor son: ",b, "y ",c)
input()