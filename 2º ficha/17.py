print("Programa que lee N caracteres y contabiliza el número de veces que se repite la letra a, e, i, o, u.")
n=int(input("Introduce el nº de caracteres que vas a escribir"))
ca=ce=ci=co=cu=0
for i in range(n):
    c=input("Introduce carácter")
    match c:
        case _ if c=='a': ca==ca+1
        case _ if c=='e': ce==ce+1
        case _ if c=='i': ci==ci+1
        case _ if c=='o': co==co+1
        case _ if c=='u': cu==cu+1

print(" a: ",ca)
print(" e: ",ce)
print(" i: ",ci)
print(" o: ",co)
print(" u: ",cu)
print("Total de vocales: ", ca+ce+ci+co+cu)
input()