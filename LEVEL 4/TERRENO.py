#Input
a = int(input ("Dime la medida del lado A: "))
b = int(input ("Dime la medida del lado B: "))
c = int(input ("Dime la medida del lado C: "))

#Proceso
actualizarA = a - c
triangulo = (actualizarA * b) / 2
rectangulo = (b * c)
terreno = rectangulo + triangulo

print ("Esta es la medida de tu terreno: " , terreno)
