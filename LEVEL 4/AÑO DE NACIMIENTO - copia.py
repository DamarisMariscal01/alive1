#Input
"""year = int(input ("Dime tu año de nacimiento: "))

#Proceso
edad = 2019 - año

print ("Esta es la edad aproximada que tienes: " , edad)
"""
#Funciones
def calcularEdad (year):
    edad = 2019 - year
    return edad
print ("Esta es la edad aproximada que tiene alguien que nació en 1999: " , calcularEdad (1999))
print ("Esta es la edad aproximada que tiene alguien que nació en 2007: " , calcularEdad (2007))
