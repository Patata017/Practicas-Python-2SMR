print("Programa que escribe del 1 al 100")
for n in range(1,101):
    cd=0
    i=2
    while cd==0 and i<=n//2:
        if n%i==0:
            cd=cd+1
        i=i+1
    if cd==0:
        print(n," es primo")
input()