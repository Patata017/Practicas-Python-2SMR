print("Programa que pone las notas en forma alfanumérica")
nota = float(input("Introduce la nota: "))
if nota < 5:
    print("I")
elif nota < 6:
    print("S")
elif nota < 7:
    print("B")
elif nota < 9:
    print("N")
elif nota >= 9:
    print("Sob")
input()