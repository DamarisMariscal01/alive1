import string

# constantes
abecedario = string.ascii_lowercase

def posicion_letra(letra):
    for pos in range(len(abecedario)):
        if letra == abecedario[pos]:
            return pos

#inputs
letra1 = str(input("Dame una letra del abecedario: "))
letra2 = str(input("Dame otra letra del abecedario: "))


if posicion_letra(letra1) > posicion_letra(letra2):
    print ("La letra 1 es menor a la letra 2, es decir, no están ordenadas.")
else:
    print ("La letra 1 es mayor a la letra 2, es decir, están ordenadas.")
