def factorial(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

n=int(input("Ingrese un numero para calcular su factorial: "))
print("El factorial de",n,"es:",factorial(n))
