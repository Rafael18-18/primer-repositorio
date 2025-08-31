# Programa 1: Búsqueda en Arreglo Multidimensional

matriz = [
    [4, 7, 9],
    [1, 5, 3],
    [8, 2, 6]
]

# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):            # Recorre filas
        for j in range(len(matriz[i])):     # Recorre columnas
            if matriz[i][j] == valor:
                return (i, j)  # Devuelve la posición (fila, columna)
    return None

# Valor a buscar
valor_buscar = 6

resultado = buscar_valor(matriz, valor_buscar)

# Mostrar resultados
print("Matriz:")
for fila in matriz:
    print(fila)

if resultado:
    print(f"\nEl valor {valor_buscar} se encontró en la posición: fila {resultado[0]}, columna {resultado[1]}")
else:
    print(f"\nEl valor {valor_buscar} no se encontró en la matriz.")
