contador = 0
suma = 0
primerNumero = True
while True:
    try:
        numero = input("Ingrese un numero: ")
        if (numero == "fin"):
            break
        contador = contador + 1
        suma = suma + int(numero)

    except:
        print("Dato erróneo")

print("contador", contador)
print("suma", suma)
print("promedio", suma/contador)
