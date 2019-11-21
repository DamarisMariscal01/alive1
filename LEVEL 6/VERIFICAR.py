#Inputs
print("CONSTRASEÑA, VERIFICAR")
contra = int(input("Dime la contaseña para poder acceder: "))


#Proceso
while contra != 1234:
    print("")
    print ("Vuelve a intentarlo :)")
    contra = int(input("Dime la contaseña para poder acceder: "))

print("La contraseña está correcta :)")
