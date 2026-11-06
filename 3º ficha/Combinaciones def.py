def factorial (número):
    f=1
    for i in range(1, número+1):
        f=f*i
    return f 
m=int(input("Introduce el número de elementos"))
n=int(input("Introduce cuantos cogemos"))
fm= factorial(m)
fn=factorial(n)
fmn=factorial(m-n)

c=fm/(fn*fmn)
print("Las combinaciones de ",m," elemnetos tomados de ",n,"en ",n," son ",c)
input()