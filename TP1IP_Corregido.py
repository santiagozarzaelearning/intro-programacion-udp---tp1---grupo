cantHuespedesTotal = 0
ciudadMasHabitaciones = ""
cantHabitacionesMas = 0
for i in range (1 , 3):
    print("Hotel numero:",i)
    nombreCiudadFilial = str(input("Ingrese el nombre de la ciudad de la filial: "))
    capacidadTotalFilial = int(input("Ingrese la capacidad total de la filial: "))
    cantHabitaciones = int(input("Ingrese la cantidad de habitaciones: "))
    cantHuespedesMes = int(input("Ingrese la cantidad de huespedes por mes: "))
    # Validaciones 
    while capacidadTotalFilial <= 0 or cantHabitaciones <= 0 or cantHuespedesMes <= 0:
        print("Error: Los valores ingresados no pueden ser menores o iguales a cero")
        capacidadTotalFilial = int(input("Ingrese la capacidad total de la filial: "))
        cantHabitaciones = int(input("Ingrese la cantidad de habitaciones: "))
        cantHuespedesMes = int(input("Ingrese la cantidad de huespedes por mes: "))

    # N1 La cantidad total de huéspedes que puede alojar toda la cadena de hoteles.
    cantHuespedesTotal += capacidadTotalFilial
    # N2 El porcentaje de ocupación de cada hotel.
    cantHuespedesDiarios = cantHuespedesMes / 30  # Promedio de huespedes por día
    porcentajeOcupacion = int((cantHuespedesDiarios/capacidadTotalFilial) * 100)
    # N3 El nombre de la ciudad con mayor cantidad de habitaciones.
    if cantHabitaciones >= cantHabitacionesMas:
        if cantHabitaciones > cantHabitacionesMas:
            cantHabitacionesMas = cantHabitaciones
            ciudadMasHabitaciones = nombreCiudadFilial
        else:
            if cantHabitaciones == cantHabitacionesMas:
                ciudadMasHabitaciones = ciudadMasHabitaciones + ", " + nombreCiudadFilial
    

    print("El porcentaje de ocupacion diario del hotel de la ciudad de", nombreCiudadFilial, "es:", porcentajeOcupacion, "%")
    print()  # Salto de linea para mejor estetica
print("La cantidad total de huespedes que puede tener toda la cadena de hoteles es: ", cantHuespedesTotal)
print("La ciudad con mayor cantidad de habitaciones es: ", ciudadMasHabitaciones)