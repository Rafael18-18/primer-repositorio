def calcular_promedios(temperaturas, ciudades, dias):
    """
    Calcula los promedios semanales y generales de temperatura para varias ciudades.

    :param temperaturas: Lista 3D con datos de temperaturas [ciudad][semana][día]
    :param ciudades: Lista con los nombres de las ciudades
    :param dias: Lista con los nombres de los días
    :return: Diccionario con el promedio general de cada ciudad
    """
    resultados = {}

    for i in range(len(temperaturas)):  # Recorrer ciudades
        print(f"\nCiudad: {ciudades[i]}")
        suma_ciudad = 0
        total_dias_ciudad = 0

        for j in range(len(temperaturas[i])):  # Recorrer semanas
            print(f"  Semana {j + 1}:")
            suma_semana = 0
            for k in range(len(temperaturas[i][j])):  # Recorrer días
                temp = temperaturas[i][j][k]
                suma_semana += temp
                suma_ciudad += temp
                total_dias_ciudad += 1
                print(f"    {dias[k]}: {temp}°C")

            promedio_semana = suma_semana / len(temperaturas[i][j])
            print(f"    ➡ Promedio semana {j + 1}: {promedio_semana:.2f}°C")

        # Promedio general de toda la ciudad
        promedio_ciudad = suma_ciudad / total_dias_ciudad
        resultados[ciudades[i]] = promedio_ciudad
        print(f"\n  Promedio general en {ciudades[i]}: {promedio_ciudad:.2f}°C")

    return resultados


# =====================
# Datos de ejemplo
# =====================
Temperaturas = [
    [  # Quito
        [16, 20, 18, 16, 21, 20, 16],
        [18, 19, 16, 19, 17, 20, 17],
        [20, 21, 17, 18, 19, 16, 21],
        [18, 17, 16, 18, 20, 19, 17]
    ],
    [  # Guayaquil
        [30, 28, 27, 25, 30, 32, 24],
        [32, 28, 29, 27, 30, 28, 26],
        [28, 27, 25, 28, 30, 27, 24],
        [32, 29, 30, 28, 26, 27, 25]
    ],
    [  # Cuenca
        [17, 16, 14, 15, 13, 17, 16],
        [14, 15, 18, 19, 17, 14, 19],
        [13, 15, 26, 13, 14, 16, 17],
        [17, 18, 19, 15, 16, 14, 18]
    ]
]

ciudades = ["Quito", "Guayaquil", "Cuenca"]
dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

# Llamada a la función
promedios = calcular_promedios(Temperaturas, ciudades, dias)

print("\nResumen de promedios generales:")
print(promedios)
