print("Programa calcula el máximo de entre un número indefinido de números positivos introducidos por teclado, sabiendo que metemos números hasta que introduzcamos uno negativo.")
n=int(input("Introduce un número positivo"))
mayor=0
if n > 0:
    while n > 0:
        if n > mayor:
            mayor = n
        n=int(input("Introduce un número"))
    print("El mayor número es: ",mayor)
if n==0:
    print("No has introducido ningun número")
else:
    print("El número es negativo")
input()