print("Programa porra futbol ")
import os
tabla=[]
tamano=3
for i in range(tamano):
    tabla.append([])
    for j in range(tamano):
        tabla[i].append("")

for i in range(tamano):
    for j in range(tamano):
        tabla[i][j]=""

continuar="s"
while continuar=="s" or continuar=="S":
    os.system("cls")
    nombre=input("Ingrese el nombre del jugador: ")
    print("resultados ya introducidos: ")
    for i in range(tamano):
        print("%12d"%i,end="")

    for i in range (tamano):
        print("\n",i,end="")
        for j in range(tamano):
            print("%12s"%tabla[i][j],end="")
        print()

    print("Elige un resultado: ")
    gl=int(input("Goles local: "))
    gv=int(input("Goles visitante: "))
    tabla[gl][gv]=nombre
    continuar=input("Desea continuar? (s/n): ")

os.system("cls")
print("Di el resultado final: ")
gl=int(input("Goles local: "))
gv=int(input("Goles visitante: "))
if tabla[gl][gv]!="":
    print("El ganador es: ",tabla[gl][gv])
else:
    print("No hay ganador")

    print()