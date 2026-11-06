print("Programa que calcula los múltiplos de 5 comprendidos entre 1 y N, donde N es un valor introducido por teclado.")
N=int(input("Escribe el valor final hasta donde contara"))
c=0
for i in range(1, N+1):
    if 5 % i == 0:
        print(i," Es múltiplo de 5")
        c=c+1
print("Entre 1 y ",N," hay ",c," múltiplos de 5 ")
input()