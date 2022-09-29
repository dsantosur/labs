def imprimirCalificacion(Calificación):
    if (Puntuacion >= 0.9 and Puntuacion <= 1.0):
         Calificación = "sobresaliente"
    elif(Puntuacion >= 0.8 and Puntuacion <0.9):
         Calificación = "notable"
    elif(Puntuacion >= 0.7 and Puntuacion < 0.8):
          Calificación = "bien"
    elif(Puntuacion >= 0.6 and Puntuacion < 0.7):
          Calificación = "suficiente"
    elif(Puntuacion >=0 and Puntuacion < 0.6):
          Calificación = "Insuficiente"
    else:
        Calificación = "No definido"
    return Calificación 



try:
    Puntuacion = float(input("Ingrese la puntuación (0.01 - 1.00): "))
    Calificación = imprimirCalificacion(Puntuacion)
    print("La calificación de su puntuación es: ", Calificación)
except:
    print("Error, puntuación solamente acepta números")


