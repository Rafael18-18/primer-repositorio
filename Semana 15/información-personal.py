# 1. Crear el diccionario inicial
informacion_personal = {
    "nombre": "Alberto Dominguez",
    "edad": 30,
    "ciudad": "Quito",
    "profesion": "Ingeniero"
}
print("Paso 1 - Diccionario inicial:")
print(informacion_personal)
# {'nombre': 'Alberto Dominguez'
# 'edad': 30
# 'ciudad': 'Quito'
# 'profesion': 'Ingeniero'}

# 2. Modificar la ciudad
informacion_personal["ciudad"] = "Guayaquil"
print("\nPaso 2 - Ciudad modificada:")
print(informacion_personal)
# {'nombre': 'Alberto Dominguez'
# 'edad': 30
# 'ciudad': 'Guayaquil'
# 'profesion': 'Ingeniero'}

# 3. Agregar una nueva clave-valor que represente la profesion
informacion_personal["profesion_secundaria"] = "Docente"
print("\nPaso 3 - Profesión secundaria agregada:")
print(informacion_personal)
# {'nombre': 'Alberto Dominguez'
# 'edad': 30
# 'ciudad': 'Guayaquil'
# 'profesion': 'Ingeniero'
# 'profesion_secundaria': 'Docente'}

# 4. Verificar y agregar teléfono si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0998765432"
print("\nPaso 4 - Teléfono agregado (si no existía):")
print(informacion_personal)
# {'nombre': 'Alberto Dominguez', 'edad': 30
# 'ciudad': 'Guayaquil', 'profesion': 'Ingeniero'
# 'profesion_secundaria': 'Docente'
# 'telefono': '0998765432'}

# 5. Eliminar la edad
del informacion_personal["edad"]
print("\nPaso 5 - Edad eliminada:")
print(informacion_personal)
# {'nombre': 'Alberto Dominguez'
# 'ciudad': 'Guayaquil'
# 'profesion': 'Ingeniero'
# 'profesion_secundaria': 'Docente'
# 'telefono': '0998765432'}

# 6. Diccionario final
print("\nDiccionario final:")
print(informacion_personal)
