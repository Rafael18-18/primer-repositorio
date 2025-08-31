# Programa 2: Ordenación de Arreglo Multidimensional

matriz = [
    [4, 7, 9],
    [1, 5, 3],
    [8, 2, 6]
]

# Función para ordenar una fila usando Bubble Sort
def bubble_sort_fila(matriz, fila):
    n = len(matriz[fila])
    for i in range(n - 1):
        for j in range(n - i - 1):
            if matriz[fila][j] > matriz[fila][j + 1]:
                # Intercambio de elementos
                matriz[fila][j], matriz[fila][j + 1] = matriz[fila][j + 1], matriz[fila][j]
    return matriz

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Fila a ordenar (ejemplo: la fila 1 → segunda fila)
fila_a_ordenar = 2
matriz_ordenada = bubble_sort_fila(matriz, fila_a_ordenar)

# Mostrar la matriz con la fila ordenada
print(f"\nMatriz con la fila {fila_a_ordenar} ordenada:")
for fila in matriz_ordenada:
    print(fila)
