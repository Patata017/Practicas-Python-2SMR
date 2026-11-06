print("Programa que calcula los múltiplos de 4 comprendidos entre 4 y N, donde N es un valor introducido por teclado.")
N=int(input("Escribe el valor final hasta donde contara"))
c=0
for i in range(4, N+1, 4):
    print(i," Es múltiplo de 4")
    c=c+1
print("Entre 4 y ",N," hay ",c," múltiplos de 4 ")
input()