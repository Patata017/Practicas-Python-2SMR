print("Programa que calcula la nota media de A alumnos de una clase, que tiene B asignaturas cada uno. Y decir cual es el mejor")
media=0
mayorm=0
alum=int(input("Introduce el nº de alumnos"))
asig=int(input("Introduce el nº de asignaturas"))
for i in range (1, alum+1):
    suma=0
    nombre=input("Introduce el nombre del alumno")
    for j in range(1, asig+1):
        print("Introduce la nota del anumno",i," y la asignatura nº ",j)
        nota=int(input())
        suma=suma+nota
    media=suma/asig
    print("La media del alumno es: ",media)
    if media>mayorm:
        mayorm=media
        nombre_mejor=nombre
print("El alumno con mejor media es: ",nombre_mejor, "con una media de: ",mayorm)
input()