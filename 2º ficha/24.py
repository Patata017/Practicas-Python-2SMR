print("Programa que pida un número al usuario, lo eleve al cubo y sume los dígitos del resultado. La salida será SI, si esa suma es igual al número, y NO en otro caso")
c=0
s=0
n=int(input("Escribe un número"))
num=n
n=n**3
print("Los dígitos del número son:")
while n!=0:
    d=n%10
    n=n//10
    s=s+d
if s==num:
    print("SI")
else:
    print("NO")
input()