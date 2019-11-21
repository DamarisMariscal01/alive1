print("TRIANGULOS")
decision = 1

#Proceso
def compara (l1 , l2 , l3):
    if l1 == l2 and l1 == l3:
        return "Equilatero"
    elif l1 == l2 or l1 == l3 or l2 == l3:
        return "Isosceles"
    else:
        return "Escaleno"
while decision == 1:
    l1 = float(input("Dime la medida del lado 1: "))
    l2 = float(input("Dime la medida del lado 2: "))
    l3 = float(input("Dime la medida del lado 3: "))
    print ("El triángulo que me diste es: " , compara (l1, l2, l3))
    print ("")
    decision = int (input("¿Quieres volver a ejecutar el programa? 1=Si/2=No: " ))
if decision == 1:
    print ("Ok listo! :)")
    print ("")
else:
    print ("Regresa pronto, gracias :)")
    print ("")
