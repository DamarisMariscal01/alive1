#Inputs
materia = 1
materia1 = 1
materia2 = 1
materia3 = 2
edad = 0
contador = 1
contador1 = 1
contador2 = 1
contador3 = 1


#Proceso
while contador <=10:
    contador += 1
    print ("")
    edad = int(input("Dime tu edad: "))
    print ("1) Español")
    print ("2) Inglés")
    print ("3) Francés")
    materia = int(input("Dime el numero de lo que estás estudiando: "))

    if materia1 == 1:
        materia1 += 1
    elif materia2 == 2:
        materia2  += 1
    else:
        materia3 += 1


    if edad <= 10:
        contador1 += 1
    if edad > 10 and edad < 20:
        contador2 += 1
    elif edad <= 20:
        contador3 += 1
else:
    print ("ERROR")


print ("El número de personas que tienen menos de 10 años es: " , contador1)
print ("El número de personas que tienen más de 10 y menos de 20 años es: " , contador2)
print ("El número de personas que tienen más de 10 años es: " , contador3)
print("")
print ("El número de personas que estudian español es: " , materia1)
print ("EL número de personas que estudian matemáticas es: " , materia2)
print ("El número de personas que estudian francés es de: " , materia3)
