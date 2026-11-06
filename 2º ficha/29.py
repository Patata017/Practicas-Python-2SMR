print("¿Cuáles y cuántos son los números primos comprendidos entre 1 y 1000?")
c = 0
for n in range(1, 1001):
    if n > 1:
        primo = True
        for x in range(2, n):
            if n % x == 0:
                primo = False
                break
        if primo:
            print(n)
            c = c + 1
print("Total:", c)