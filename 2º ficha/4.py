print("Programa que puede pasar Fahrenheit-Celsius o al reves")
m=input("Elije Celsius o Fahrenheit C / F")
while m == "c" or m == "C":
    tempC = int(input("Escribe tu temperatura de Celsius"))
    tempF = (tempC * 9/5) + 32
    print("La temperatura que escribiste en Celsius es igual a ",tempF," en Fahrenheit")
    m = "x"
while m == "f" or m == "F":
    tempF = int(input("Escribe tu temperatura de Fahrenheit"))
    tempC = (tempF - 32) * 5 / 9
    print("La temperatura que escribiste en Fahrenheit es igual a ",tempC," en Celsius")
    x = "x"
input()