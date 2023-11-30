def agregar_palabra(diccionario):
    palabra = input("Ingrese la palabra: ")
    significado = input("Ingrese el significado: ")
    diccionario[palabra] = significado
    print(f"Palabra '{palabra}' agregada correctamente.\n")

def editar_palabra(diccionario):
    palabra = input("Ingrese la palabra que desea editar: ")
    if palabra in diccionario:
        nuevo_significado = input("Ingrese el nuevo significado: ")
        diccionario[palabra] = nuevo_significado
        print(f"Significado de '{palabra}' editado correctamente.\n")
    else:
        print(f"La palabra '{palabra}' no existe en el diccionario.\n")

def eliminar_palabra(diccionario):
    palabra = input("Ingrese la palabra que desea eliminar: ")
    if palabra in diccionario:
        del diccionario[palabra]
        print(f"Palabra '{palabra}' eliminada correctamente.\n")
    else:
        print(f"La palabra '{palabra}' no existe en el diccionario.\n")

def ver_listado(diccionario):
    print("\nPalabras\t\t\tSignificado")
    print("----------------------------------------")
    for palabra, significado in diccionario.items():
        print(f"{palabra}\t\t\t{significado}")
    print()

def buscar_significado(diccionario):
    palabra = input("Ingrese la palabra que desea buscar: ")
    if palabra in diccionario:
        print(f"Significado de '{palabra}': {diccionario[palabra]}\n")
    else:
        print(f"La palabra '{palabra}' no existe en el diccionario.\n")

def main():
    diccionario = {}
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
    main()