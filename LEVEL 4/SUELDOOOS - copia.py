#Inputs
"""sueldoMeses = float(input ("Escribe el sueldo que recibes mensualmente: "))

#Proceso
quincena = 0.15 * 2
ahorroMes = sueldoMeses * quincena
sueldoAhorrado = ahorroMes * 12

print ("Este es el dinero que te ahorras en un año: " , sueldoAhorrado)
"""
#Funciones
def sueldooos (sueldoMeses):
    quincena = 0.15 * 2
    ahorroMes = sueldoMeses * quincena
    sueldoAhorrado = ahorroMes * 12
    return sueldoAhorrado
print ("Este es el dinero 1 que te ahorras en un año: " , sueldooos (325))
print ("Este es el dinero 2 que te ahorras en un año: " , sueldooos (999))
