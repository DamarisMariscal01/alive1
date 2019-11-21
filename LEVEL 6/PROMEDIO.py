#Inputs
contador = 1
total2 = 0
total3 = 0

#Proceso
while contador <= 10:
    total1 = float(input("Dime el promedio del alumno:" ))
    contador += 1
    total2 += total1
    total3 = total2 / 10
print ("Este es el promedio que sacaron los alumnos: " , total3)
