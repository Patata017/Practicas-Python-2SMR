print("Programa desglose billetes")
print("===========================")
print("Introduce una cantidad de euros")
eu=int(input())
r500 = eu % 500
r200 = r500 % 200
r100 = r200 % 100
r50 = r100 % 50
r10 = r50 % 10
r5 = r10 % 5
b500 = eu // 500
b200 = r500 // 200
b100 = r200 // 100
b50 = r100 // 50
b10 = r50 // 10 
b5 = r10 // 5
print("Serían Billetes de 500; ",b500, " billetes de 200: ",b200, " billetes de 100",b100, " billetes de 50: ",b50, " billetes de 10: ",b10, " billetes de 5: ",b5, " monedas de 1: ",r5 )
