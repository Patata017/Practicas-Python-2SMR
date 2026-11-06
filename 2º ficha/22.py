print("Programa que lea un entero y nos muestre la suma de sus dígitos")
c=0
s=0
n=int(input("Escribe un número"))
num=n
print("Los dígitos del número son:")
while n!=0:
    d=n%10
    n=n//10
    s=s+d
print(num," tiene como suma de sus dígitos: ",s)
input()