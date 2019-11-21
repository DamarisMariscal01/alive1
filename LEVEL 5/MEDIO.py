#Inputs
print ("El número de en medio")
n1 = float(input("Dame el primer numero: "))
n2 = float(input("Dame el segundo numero: "))
n3 = float(input("Dame el tercer numero: "))

#Proceso
if n2 < n1 < n3:
    print ("El numero 1 es el de en medio")
elif n1 < n2 < n3:
    print ("El numero 2 es el de en medio")
else:
    print ("El numero 3 es el de en medio")
