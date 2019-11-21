#Inputs
print ("El número mayor")
numero1 = float(input("Dime el primer número: "))
numero2 = float(input("Dime el segundo número: "))
numero3 = float(input("Dime el tercer número: "))

#Proceso
if numero1 > numero2 and numero3:
    print ("Número 1 es el mayor")
elif numero2 > numero3 and numero1:
    print ("Numero 2 es el mayor")
else:
    print ("Numero 3 es el mayor")
