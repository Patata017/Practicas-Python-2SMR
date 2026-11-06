print("Programa que crea dos matrices: A de 3x4 y B de 4x3")

A = []
for i in range(3):
    fila = []
    for j in range(4):
        char = input("Introduce el carácter: ")
        fila.append(char)
    A.append(fila)

print("Matriz original (A):")
for i in range(3):
    for j in range(4):
        print(A[i][j], end=" ")
    print()

B = []
for j in range(4):
    for i in range(3):
        fila.append(A[i][j])
    B.append(fila)

print("Matriz transpuesta (B):")
for i in range(4):
    for j in range(3):
        print(B[i][j], end=" ")
    print()

input()