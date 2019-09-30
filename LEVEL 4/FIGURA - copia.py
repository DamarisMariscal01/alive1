from math import sqrt
#Inputs
"""radio = float(input ("Dime el radio que quieres para hacer la primera parte de la figura: "))
hipotenusa = float(input ("Dime la altura que quieres para la parte de abajo de la figura: "))

#Proceso
altura1 = (hipotenusa ** 2 ) - (radio ** 2)
altura2 = sqrt (altura1)
diametro = (radio * 2)
circulo = 3.14 * (radio ** 2)
medioCirculo = circulo / 2
triangulo = (diametro * altura2) / 2
figura = (medioCirculo + triangulo)


print ( f" Esta es el area de la figura: " , figura)
"""
#Funciones
def figurarara (radio , hipotenusa):
    altura1 = (hipotenusa ** 2 ) - (radio ** 2)
    altura2 = sqrt (altura1)
    diametro = (radio * 2)
    circulo = 3.14 * (radio ** 2)
    medioCirculo = circulo / 2
    triangulo = (diametro * altura2) / 2
    figura = (medioCirculo + triangulo)
    return figura
print ("Esta es el area de la figura que trazaste: " , figurarara (3,4))
print ("Esta es el area de la figura que trazaste: " , figurarara (5,7))
