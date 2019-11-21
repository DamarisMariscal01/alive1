#Inputs
print ("Conversión de calificaciones")
calificacioon = float(input("Dime la calificación que sacó el alumno para convertirlo a calificación en USA: "))

#Proceso
if calificacioon > 9:
    print ("El/La alumn@ sacó A+ de calificación")
elif calificacioon >= 8 and calificacioon <= 9:
    print ("El/La alumn@ sacó A de calificación")
elif calificacioon <= 8 and calificacioon >= 7:
    print ("EL/La alumn@ sacó B de calificación")
elif calificacioon < 7 and calificacioon >= 6:
    print ("El/La alumn@ sacó C de calificación")
else:
    print ("El/La alumn@ sacó D de calificación")
