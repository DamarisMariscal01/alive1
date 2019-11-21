#Inputs
print ("Descuentos")
cProductos = float(input("Dime la cantidad de productos que compraste: "))
pProductos = float(input("Dime el precio del artículo que compraste: "))

#Proceso
precioTotal = cProductos * pProductos
total = precioTotal
descuento = 0

if precioTotal > 5000:
    descuento = precioTotal * 0.15
    total = precioTotal - descuento
elif precioTotal > 3000:
    descuento = precioTotal * 0.1
    total = precioTotal - descuento
elif precioTotal > 1000:
    descuento = precioTotal * 0.05
    total = precioTotal - descuento
else:
    print("Debe comprar más cosas para aplicarle descuento :(")


print ("Este es el descuento que se te aplicó: " , descuento)
print ("Este es el total a pagar: " , total)
