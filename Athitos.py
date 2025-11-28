#   Variables
contHuespedesTotales = 0
mayorCantHabitacionesTotales = 0
ciudadMasHabitaciones = ""
#   Logica
#   Se tienen q ingresar los datos de las 10 filiales
for i in range(10):
    filial = str(input("Ingrese la ciudad donde se encuentra la filial: "));

    capTotal = int(input("Ingrese la capacidad diaria total de la filial: "));
#   Sumo la capacidad total de esta filial a la variable contadora
    contHuespedesTotales += capTotal
#   Calculo la capacidad mensual de la filial
    capTotalMensual = capTotal * 30

    cantHabitaciones = int(input("Ingrese la cantidad de habitaciones de la filial: "));
#   Verifico si esta filial tiene la mayor cantidad de habitaciones
    if cantHabitaciones > mayorCantHabitacionesTotales:
        mayorCantHabitacionesTotales = cantHabitaciones
        ciudadMasHabitaciones = filial

    cantHuespedesMes = int(input("Ingrese la cantidad de huespedes por mes de la filial: "));
#   Calculo el porcentaje de ocupacion mensual de la filial, en el resultado redondeo a 2 decimales
    porcentajeOcupacion = (cantHuespedesMes * 100) / capTotalMensual
    print("El porcentaje de ocupacion mensual del hotel en ", filial, " es del: ", round(porcentajeOcupacion, 2), "%")

#   Resultados
print("La cantidad total de huespedes que puede alojar toda la cadena de hoteles es: ", contHuespedesTotales);
print("La ciudad con mayor cantidad de habitaciones es: ", ciudadMasHabitaciones, " con ", mayorCantHabitacionesTotales, " habitaciones.");