print("función llamada Digito, que nos diga si un carácter es uno de los dígitos decimales.")
def digito(c):
    if c >= '0' and c <= '9':
        return True
    else:
        return False
    
c=input("Introduce un caracter")
if digito(c):
    print("El caracter", c, "es un dígito decimal.")
else:
    print("El caracter", c, "no es un dígito decimal.")
input()