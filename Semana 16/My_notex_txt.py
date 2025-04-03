# Escritura de Archivo de Texto
# Abrimos el archivo en modo 'w' para escribir (se creará si no existe)
with open('my_notes.txt', 'w') as file:
    # Escribimos tres líneas de notas personales
    file.write("1. Aprender y dominar estructuras de datos es fundamental para escribir código más eficiente.\n")
    file.write("2. La programación orientada a objetos ayuda a organizar mejor el código y facilitar su mantenimiento.\n")
    file.write("3. Siempre que escriba código, debo hacer un esfuerzo por optimizar su rendimiento y evitar redundancias.\n")

# Lectura de Archivo de Texto con readline()
# Abrimos el archivo en modo 'r' para leer su contenido
with open('my_notes.txt', 'r') as file:
    # Leer línea por línea usando readline()
    line = file.readline()  # Lee la primera línea
    while line:  # Mientras haya contenido en la línea
        print(line.strip())  # Imprimir la línea sin saltos extra
        line = file.readline()  # Leer la siguiente línea

# El archivo se cierra automáticamente al salir del bloque 'with'
