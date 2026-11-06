print("Programa que visualice el número más grande, el más pequeño y la media  de una serie de N números leídos de teclado. N se leerá al principio y debe ser > 0 para realizar el proceso.")
N = int(input("Introduce N (mayor que 0): "))
if N > 0:
    primero = int(input("Introduce un número: "))
    mayor = primero
    menor = primero
    suma = primero
    for i in range(N - 1):
        n = int(input("Introduce un número: "))
        if n > mayor:
            mayor = n
        if n < menor:
            menor = n
        suma += n
    media = suma / N
    print("Mayor:", mayor)
    print("Menor:", menor)
    print("Media:", media)
else:
    print("N no es válido.")