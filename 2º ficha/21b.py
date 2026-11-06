print("Programa que lea un entero y nos muestre cuantos dígitos pares tiene")
c=0
p=0
n=int(input("Escribe un número"))
num=n
print("Los dígitos del número son:")
while n!=0:
    d=n%10
    if d!=0 and d%2==0:
        p=p+1
    n=n//10
print(num," tiene ",p," dígitos pares")
input()