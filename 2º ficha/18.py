print("18.	Programa que lea números hasta que se escriba el cero, y después indique si se ha dado alguna vez el mismo número dos veces consecutivas.")
anterior = None
repetido = False
n = int(input("Introduce un número (0 para terminar): "))
while n != 0:
    if n == anterior:
        repetido = True
    anterior = n
    n = int(input("Introduce un número (0 para terminar): "))
if repetido:
    print("Se repitió un número consecutivamente.")
else:
    print("No hubo números consecutivos iguales.")