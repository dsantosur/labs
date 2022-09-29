minimo = 0
maximo = 0
primerNumero = True
while True:
        numero = input("Ingrese un número: ")
        if (numero == "salir"):
            break

        if(primerNumero):
            minimo = int(numero)
            maximo = minimo
            primerNumero = False
        else:
            if(int(numero)>maximo):
                maximo = int(numero)
            if(int(numero)<minimo):
                minimo = int(numero)


        print("Maximo", maximo)
        print("Minimo", minimo)
