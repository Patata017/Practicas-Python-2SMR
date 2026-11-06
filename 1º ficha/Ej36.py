print("Programa que dados 10 números enteros, visualizar la suma de los números pares de la lista, cuántos son impares, y cuál es la media aritmética de todos.")
Pares=0
Impares=0
Media=0
s_total=0
for i in range(1, 11):
    N=int(input("Escribe un número"))
    s_total=s_total+N
    if N % 2 == 0:
        print(N," Es par")
        Pares=Pares+N
    else:
        print(N," Es impar")
        Impares=Impares+N
Media= s_total/10
print("La suma de los pares es: ",Pares)
print("La suma de los impares es: ",Impares)
print("La media de todos los número es de: ",Media)
input()