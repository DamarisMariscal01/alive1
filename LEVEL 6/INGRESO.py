contador = 1
total2 = 0

#Proceso
while contador <= 7:
    total1 = float(input("Escribe lo que ganaste hoy: "))
    contador += 1
    total2 += total1
print ("Esto es lo que ganaste en la semana: " , total2)
