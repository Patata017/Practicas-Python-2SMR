print("Programa que pasa un número a binario")
n=int(input("Escribe un número"))
num = n
b = 0
p = 1
while num != 0:
    r = n % 2
    b = b + r * p
    p = p * 10
    num = num // 2 
print("El número en binario es: ",b)
input()