print("Programa que nos pida un número y dice si es múltiplo de otro ")
print("Escribe un número")
n=int(input())
print("Escribe el múltiplo que quieres comprobar")
m=int(input())
if n==0: print("El número es 0")
else: r=n%m
if r==0: 
    print(n, " Es múltiplo de ",m)
else: 
    print(n, " No es múltiplo de ",m)
input()