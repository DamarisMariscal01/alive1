#Inputs
print ("Resta absoluta")
n1 = float(input("Dime el primer número: "))
n2 = float(input("Dime el segundo numero: "))

#Proceso
if n1 < 0:
    valorAbsoluto1 = n1 * (-1)
    n1 = valorAbsoluto1
elif n2 < 0:
    valorAbsoluto2 = n2 * (-1)
    n2 = valorAbsoluto2
#Resta
if n1 > n2:
    restaN1 = n1 - n2
    print ("El resultado de la resta absoluta es: " , restaN1)
else:
    restaN2 = n2 - n1
    print ("El resultado de la resta absoluta es: " , restaN2)
