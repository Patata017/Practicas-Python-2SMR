print("Programa que nos diga si un número es perfecto")
s=0
resp='y'
while resp=='y' or resp=='Y':
    n=int(input("Escribe un número"))
    cd=0
    for i in range (1, n):
        if n%i==0:
            cd=cd+1
            s=s+i
    if s==n:
        print(n,"Es un número perfecto")
    else:
        print(n,"No es un número perfecto")
        print("Desea continuar Y/N")
        resp=input()
input()