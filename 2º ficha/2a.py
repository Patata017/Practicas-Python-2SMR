print("Programa que decide si un número es primo o no")
n=int(input("Escribe un número"))
p=0
i=2
while p==0 and i<n:
    if n % i == 0:
        p=p+1
    i=i+1
if p==0:
    print("Primo")
else:
    print("No Primo")
input()