print("Programa que hace la serie de Fibonacci")
n=int(input("Escribe hasta que número de la serie de Fibonacci quieres"))
f=0 
n1=0
n2=1
if n == 0:
    print(n1)
elif n == 1:
    print(n1)
    print(n2)
else:
    print(n1)
    print(n2)
    while f != n-1:
        a=n1+n2
        print(a)
        n1=n2
        n2=a
        f=f+1
input()