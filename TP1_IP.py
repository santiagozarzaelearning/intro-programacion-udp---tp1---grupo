#Trabajo Practico Grupal - Introduccion a la informatica
#Intregrantes: Alejo Seyler, Athos Ferracci, Ornela Zanella y Santiago Zarza.

capacidad_total = 0

#Variables 
max_habitaciones = -1 
ciudad_max_hab = "" #Se va a acutalizar con el nombre de la ciudad

#10 hoteles de la cadena por ende:
for i in range(1, 11):
    print("Hotel numero:"i)
    ciudad = input("Ingrese el nombre de la ciudad:")

    capacidad = int(input("Ingrese la capacidad total del hotel con respecto a los huespedes:"))
    habitaciones = int(input("Ingrese la cantidad de habitaciones:"))
    huespedes_mes = int(input("ingrese la cantidad de huespedes en un mes:"))

#Sumamos la capacidad a la capacidad total de la cadena.
    capacidad_total += capacidad

    #Calculamos el porcentaje de ocupacion del hotel

    if capacidad > 0:
        porcentaje_ocupacion = (huespedes_mes * 100) / capacidad
    else:
        #En caso de que alguien ponga 0 por error , evitamos la division por 0
        porcentaje_ocupacion = 0

    print("Porcentaje de ocupacion del hotel en ", ciudad, ":" ,round(porcentaje_ocupacion, 2), "%")

    #Redefinimos el valor del hotel con maximas habitaciones
    if habitaciones > max_habitaciones:
        max_habitaciones = habitaciones
        ciudad_max_hab = ciudad

    print() #Linea en blanco solo por estetica para la salida

    #Cuando terminamos de cargar los datos de los 10 hoteles, mostramos los resultados.
print("Capacidad total de la cadena de hoteles:", capacidad_total, "huespedes")
       
print("La ciudad con mayor cantidad de habitaciones es:", ciudad_max_hab, "con", max_habitaciones, "habitaciones")

 