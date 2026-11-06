def producto_de_los_pares_comprendidos_entre_dos_numeros(num1, num2):
    producto = 1
    for i in range(num1, num2 + 1):
        if i % 2 == 0:
            producto = producto * i
    return producto

def media_aritmetica_impares_comprendida_entre_dos_numeros(num1, num2):
    suma = 0
    contador = 0
    for i in range(num1, num2 + 1):
        if i % 2 == 1:
            suma = suma + i
            contador = contador + 1
    media = suma / contador
    return media

def suma_de_los_primos(num1, num2):
    sp = 0
    for i in range(num1, num2 + 1):
        if primo(i):
            sp = sp + i
    return sp

def primo(num):
    for i in range(1, num + 1):
        if num % i == 0 and i != 1 and i != num:
            return False

def valor_factorial_del_mayor_de_dos_numeros(num1, num2):
    factorial = 1
    for i in range(1, num2 + 1):
        factorial = factorial * i
    return factorial

num1 = int(input("Introduce el primer numero: "))
while num1 < 0:
    num1 = int(input("Introduce un numero positivo: "))
num2 = int(input("Introduce el segundo numero: "))
while num2 < num1:
    num2 = int(input("Introduce un numero mayor o igual que el primero: "))
print("El producto de los numeros pares comprendidos entre", num1, "y", num2, "es:", producto_de_los_pares_comprendidos_entre_dos_numeros(num1, num2))

print("La media aritmetica de los numeros impares comprendidos entre", num1, "y", num2, "es:", media_aritmetica_impares_comprendida_entre_dos_numeros(num1, num2))

print("La suma de los numeros primos comprendidos entre", num1, "y", num2, "es:", suma_de_los_primos(num1, num2))

print("El valor factorial del mayor de los dos numeros es:", valor_factorial_del_mayor_de_dos_numeros(num1, num2))

input()