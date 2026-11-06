sp=0
cp=0
sn=0
cn=0
for i in range(10):
    print("Introduce un número")
    n=int(input())
    if n>0:
        sp=sp+n
        cp=cp+1
    elif n<0:
        sn=sn+n
        cn=cn+1
mp=sp/cp
mn=sn/cn
print("La medias de pasitivos es: ",mp, " y la de negativos es de: ",mn)
input()