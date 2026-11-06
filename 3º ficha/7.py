print("subprograma que me halle cual es la primera potencia en base 2 mayor que un número que pasamos como parámetro, devolviendo el valor de dicha potencia y el exponente al que está elevado.")
def primera_potencia_mayor_que(n):

    exp = 0

    while 2 ** exp <= n:
        exp = exp + 1
    return 2**exp, exp

n = int(input("Introduce un número entero positivo: "))
p,e = primera_potencia_mayor_que(n)
print("La primera potencia de 2 mayor que ",n, "es: ",p)
print("Y el valor del exponente es: ",e)
input()