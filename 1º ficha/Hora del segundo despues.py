print("Programa que da la hora exacta del siguiente segundo que se le de")
print("=================================================================")
print("Introduce la hora")
h=int(input())
print("Introduce los minutos")
m=int(input())
print("Introduce los segundos")
s=int(input())
s=s+1
if s>=60:
    s=s-60
    m=m+1
    if m>=60:
        m=m-60
        h=h+1
        if h>=24:
            h=h-24
print ("La hora exacta es: ",h,":",m,":",s,)
input()
