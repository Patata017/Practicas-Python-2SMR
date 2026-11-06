print("Programa que calcula la suma de los divisores de cada número introducido por teclado. Termina cuando el número es negativo o 0")
s=0
n=int(input("Escribe un número"))
cd=0
for i in range (1, n+1):
        if n%i==0:
            cd=cd+1
            s=s+i
print(n," tiene ",cd," divisores y la suma de todos ellos es: ",s)
input()