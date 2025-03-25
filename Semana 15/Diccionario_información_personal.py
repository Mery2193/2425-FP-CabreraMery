# Crear un diccionario con información ficticia sobre una persona
informacion_personal = {
    "nombre": "María López",
    "edad": 28,
    "ciudad": "Esmeraldas",
    "profesion": "Diseñadora Gráfica"
}

# Acceder al valor de la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "Ambato"

# Agregar una nueva clave-valor que represente el "telefono"
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0987654321"

# Eliminar la clave "edad" del diccionario
informacion_personal.pop("edad", None)

# Imprimir el diccionario resultante
print("Diccionario final:", informacion_personal)
