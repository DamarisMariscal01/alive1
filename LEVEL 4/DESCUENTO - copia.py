#Input
"""compra = int(input ("Dime el precio total de tu compra: "))

#Proceso
descuento = compra - (compra * 0.15)

print ("Este es el total a pagar con el descuento incluido: " , descuento)
"""
#Funciones
def descuentoss (compra):
    descuento = compra - (compra * 0.15)
    return descuento
print ("Este es el descuento obtenido en tu compra 1: " , descuentoss (453))
print ("Este es el descuento obtenido en tu compra 2: " , descuentoss (734))
