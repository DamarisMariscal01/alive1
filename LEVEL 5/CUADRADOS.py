#Inputs
print ("Cuadrados")
n1 = float(input("Dime el primer número: "))
n2 = float(input("Dime el segundo número: "))

#Proceso
resultN1 = n1 ** 2
resultN2 = n2 ** 2
resultado = resultN1 + resultN2

if resultado > 2530:
    resta1 = resultado - 5
    print ("Este es el resutado de la suma de los números al cuadrados - 5: " , resta1)
else:
    resta2 = resultado - 3
    print("Este es el resultado de la suma de los números al cuadrado - 3: " , resta2)
