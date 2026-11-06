print("Subprograma que realiza la serie de Fibonacci debolviendo solo el numero en la posición ")
def fibonacci(n):
    ult = 1
    penul = 0
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(1, n):
            f = ult + penul
            penul = ult
            ult = f
        return f
n=int(input("Introduce un número"))

f=fibonacci(n)
print("El número en la posición", n, "de la serie de Fibonacci es:", f)
input()