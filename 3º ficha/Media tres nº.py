print("Programa que mediante una funcion de tres numeros calcula su media")
def media_tres_numeros(num1, num2, num3):
    media = (num1 + num2 + num3) / 3
    return media
numero1 = float(input("Introduce el primer numero: "))
numero2 = float(input("Introduce el segundo numero: "))
numero3 = float(input("Introduce el tercer numero: "))
resultado = media_tres_numeros(numero1, numero2, numero3)
print("La media de los tres numeros es:",resultado)
input()