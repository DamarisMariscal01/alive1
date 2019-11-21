#Inputs
contador = 1
total2 = 0
total3 = 0
alumnos = int(input("Dime la cantidad de alumnos que tienes: "))
#Proceso
while contador <= alumnos:
    total1 = float(input("Dime el promedio del alumno: " ))
    contador += 1
    total2 += total1
    total3 = total2 / alumnos
print ("Este es el promedio que sacaron los alumnos: " , total3)
