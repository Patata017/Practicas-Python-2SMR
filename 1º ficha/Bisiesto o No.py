print("Programa que determina si un año es bisiesto o no")
print("Introduce el año:")
año = int(input())

if año % 4 > 0:
    print("El año no es bisiesto")
else:
    if año % 100 == 0:
        if año % 400 == 0:
            print("El año es bisiesto")
        else:
            print("El año no es bisiesto")
    else:
        print("El año es bisiesto")
input()