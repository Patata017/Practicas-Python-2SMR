n=int(input("Escribe número de elementos"))
m=int(input("Escrube cuantos cogemos"))
fm=1 
for i in range(1,m+1):
    fm=fm*i
fn=1
for i in range(1,n+1):
    fn=fn*i
fmn=1
for i in range(1,m-n+1):
    fmn=fmn*i
c=fm/(fn*fmn)
print("Las combinaciones de ",m," elemnetos tomados de ",n,"en ",n," son ",c)