decision = 0
while decision != 2:
    div1 = 0
    div2 = 0
    contador = 1
    #PROCESO
    while contador <= 10:
        edad = int(input("Dime la edad del beisbolista (Sólo se puede de 15 a 20 años): "))
        if edad >= 15 and edad <= 17:
            div1 += 1
        elif edad >= 18 and edad <= 20:
            div2 += 1
        else:
            print ("ERROR :|")
        contador += 1
    print ("La cantidad de beisbolistas que están en la división 1 es: " , div1)
    print ("La cantidad de beisbolistas que están en la división 2 es: " , div2)
    print ("")
    decision = int(input("¿Quieres volver a ejecutar el programa 1=Si/2=No: "))
