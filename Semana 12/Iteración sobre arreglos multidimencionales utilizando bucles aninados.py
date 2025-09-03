#Primera dimensión = Ciudades
["Quito", "Guayaquil", "Loja"]

#Segunda dimensizn
["4 semanas"]

#Tercera dimensión = Días de la semana
["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sábado", "Domingo"]

#Inicia la matriz 3D con los valores

Temperaturas = [

    [ #Quito
        [16, 20, 18, 16, 21, 20, 16], #semana 1
        [18, 19, 16, 19, 17, 20, 17], #semana 2
        [20, 21, 17, 18, 19, 16, 21], #semana 3
        [18, 17, 16, 18, 20, 19, 17]  #semana 4

    ],
    [ #Guayaquil
        [30, 28, 27, 25, 30, 32, 24], #semana 1
        [32, 28, 29, 27, 30, 28, 26], #semana 2
        [28, 27, 25, 28, 30, 27, 24], #semana 3
        [32, 29, 30, 28, 26, 27, 25]  #semana 4
    ],
    [ #Cuenca
        [17, 16, 14, 15, 13, 17, 16], #semana 1
        [14, 15, 18, 19, 17, 14, 19], #semana 2
        [13, 15, 26, 13, 14, 16, 17], #semana 3
        [17, 18, 19, 15, 16, 14, 18]  #semana 4
    ]
]

#Se calcula la temperatura promedio semana de ciudad
ciudades = ["Quito", "Guayaquil", "Cuenca"]
dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

for i in range(len(Temperaturas)):  # Recorrer ciudades
    print(f"\nCiudad: {ciudades[i]}")
    suma_ciudad = 0
    total_dias_ciudad = 0

    for j in range(len(Temperaturas[i])):  # Recorrer semanas
        print(f"  Semana {j + 1}:")
        suma_semana = 0
        for k in range(len(Temperaturas[i][j])):  # Recorrer días
            temp = Temperaturas[i][j][k]
            suma_semana += temp
            suma_ciudad += temp
            total_dias_ciudad += 1
            print(f"    {dias[k]}: {temp}°C")

        promedio_semana = suma_semana / len(Temperaturas[i][j])
        print(f"    ➡ Promedio semana {j + 1}: {promedio_semana:.2f}°C")

    # Promedio general de toda la ciudad
    promedio_ciudad = suma_ciudad / total_dias_ciudad
    print(f"\n  Promedio general en {ciudades[i]}: {promedio_ciudad:.2f}°C")