# Tarea: Trabajo con Archivos de Texto en Python

# Escritura de Archivo de Texto

# Abrimos/creamos el archivo "my_notes.txt" en modo escritura ("w")
archivo = open("my_notes.txt", "w")

# Escribimos al menos tres líneas de notas personales
archivo.write("Nota 1: Estoy aprendiendo a manejar archivos en Python.\n")
archivo.write("Nota 2: Hoy practique escritura y lectura de archivos.\n")
archivo.write("Nota 3: Con este ejercicio estoy mejorando mis habilidades.\n")

# Cerramos el archivo después de escribir
archivo.close()

# Lectura de Archivo de Texto
# Abrimos el archivo en modo lectura ("r")
archivo = open("my_notes.txt", "r")

print("Contenido del archivo my_notes.txt:\n")

# Leemos línea por línea usando readline()
linea = archivo.readline()  # primera línea
while linea:  # mientras haya contenido
    print(linea.strip())  # imprime quitando saltos extra
    linea = archivo.readline()  # lee la siguiente línea

# Cierre del archivo
archivo.close()
