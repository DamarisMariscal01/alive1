#Inputs

dia = int(input("Dime el dia en el que estás: "))
mes = int(input("Dime el numero de mes en el que estás: "))

#Proceso

if mes == 2:
    if dia == 29:
        mes = mes + 1
        dia = 1
    elif dia >= 30:
        print("Febrero no tiene 30 o más de 30 días  :(")
    else:
        dia = dia + 1

elif mes < 12:
    if dia == 30:
        if mes == 12:
            mes = 1
        else:
            mes = mes + 1
            dia = 1
    else:
        dia = dia + 1
else:
    if dia == 30:
        dia = 1
        mes = 1

print("")
if dia >= 30:
    print ("No existe esa fecha")
elif mes > 12:
    print ("No esiste esa fecha")
else:
    print ("Mañana será el día: " , dia)
    print ("El mes del día de mañana es: " , mes)
