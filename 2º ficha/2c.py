print("Programa que escribe del 1 al 100")
a=0
n=2
while a<100:
    cd=0
    i=2
    while cd==0 and i<=n//2:
        if n%i==0:
            cd=cd+1
        i=i+1
    if cd==0:
        print(n," es primo")
        a=a+1
    n=n+1
input()