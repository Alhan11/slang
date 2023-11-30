import sqlite3

# Funciones para interactuar con la base de datos

def crear_tabla():
    conexion.execute('''
        CREATE TABLE IF NOT EXISTS diccionario (
            palabra TEXT PRIMARY KEY,
            significado TEXT NOT NULL
        )
    ''')
    conexion.commit()

def agregar_palabra_bd(palabra, significado):
    conexion.execute("INSERT INTO diccionario (palabra, significado) VALUES (?, ?)", (palabra, significado))
    conexion.commit()

def editar_palabra_bd(palabra, nuevo_significado):
    conexion.execute("UPDATE diccionario SET significado = ? WHERE palabra = ?", (nuevo_significado, palabra))
    conexion.commit()

def eliminar_palabra_bd(palabra):
    conexion.execute("DELETE FROM diccionario WHERE palabra = ?", (palabra,))
    conexion.commit()

def obtener_diccionario_bd():
    cursor = conexion.execute("SELECT palabra, significado FROM diccionario")
    return {row[0]: row[1] for row in cursor.fetchall()}

# Funciones del programa principal

def agregar_palabra(diccionario):
    palabra = input("Ingrese la palabra: ")
    significado = input("Ingrese el significado: ")
    
    agregar_palabra_bd(palabra, significado)
    
    diccionario[palabra] = significado
    print(f"Palabra '{palabra}' agregada correctamente.\n")

def editar_palabra(diccionario):
    palabra = input("Ingrese la palabra que desea editar: ")
    if palabra in diccionario:
        nuevo_significado = input("Ingrese el nuevo significado: ")
        
        editar_palabra_bd(palabra, nuevo_significado)
        
        diccionario[palabra] = nuevo_significado
        print(f"Significado de '{palabra}' editado correctamente.\n")
    else:
        print(f"La palabra '{palabra}' no existe en el diccionario.\n")

def eliminar_palabra(diccionario):
    palabra = input("Ingrese la palabra que desea eliminar: ")
    if palabra in diccionario:
        
        eliminar_palabra_bd(palabra)
        
        del diccionario[palabra]
        print(f"Palabra '{palabra}' eliminada correctamente.\n")
    else:
        print(f"La palabra '{palabra}' no existe en el diccionario.\n")

def ver_listado(diccionario):
    diccionario = obtener_diccionario_bd()
    
    print("\nPalabras\t\t\tSignificado")
    print("----------------------------------------")
    for palabra, significado in diccionario.items():
        print(f"{palabra}\t\t\t{significado}")
    print()

def buscar_significado(diccionario):
    palabra = input("Ingrese la palabra que desea buscar: ")
    diccionario = obtener_diccionario_bd()
    if palabra in diccionario:
        print(f"Significado de '{palabra}': {diccionario[palabra]}\n")
    else:
        print(f"La palabra '{palabra}' no existe en el diccionario.\n")

def main():
    crear_tabla()
    diccionario = obtener_diccionario_bd()
    
    while True:
        print("Seleccione una opción:")
        print("a) Agregar nueva palabra")
        print("c) Editar palabra existente")
        print("d) Eliminar palabra existente")
        print("e) Ver listado de palabras")
        print("f) Buscar significado de palabra")
        print("g) Salir")

        opcion = input("Opción: ").lower()

        if opcion == 'a':
            agregar_palabra(diccionario)
        elif opcion == 'c':
            editar_palabra(diccionario)
        elif opcion == 'd':
            eliminar_palabra(diccionario)
        elif opcion == 'e':
            ver_listado(diccionario)
        elif opcion == 'f':
            buscar_significado(diccionario)
        elif opcion == 'g':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elija una opción válida.\n")

if __name__ == "__main__":
    conexion = sqlite3.connect("diccionario.db")
    main()
    conexion.close()

    main()
