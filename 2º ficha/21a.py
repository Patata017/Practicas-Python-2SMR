print("Programa que lea un entero y nos muestre cuantos dígitos tiene")
c=0
n=int(input("Escribe un número"))
num=n
print("Los dígitos del número son:")
while n!=0:
    n=n//10
    c=c+1
print(num,"tiene ",c, "dígitps")
input()