print("Programaque lee dos valores numéricos distintos X e Y y determina cual es el mayor dejando el resultado en una tercera variable de nombre Z")
print("==============================================================================================================")
print("Introduce el valor de X")
x=int(input())
print("Introduce el valor de Y")
y=int(input())
if x<y: z=y
elif x>y: z=x
print("El número mayor es: ", z)
input()