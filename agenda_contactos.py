"""
Agenda de Contactos
--------------------
Programa que resuelve un problema sencillo de la vida real: guardar y
gestionar contactos (nombre y número telefónico) usando un diccionario.

Estructura de datos utilizada: diccionario (dict)
    - Clave: nombre del contacto
    - Valor: número telefónico

Funcionalidades:
    1. Agregar un contacto nuevo
    2. Mostrar todos los contactos guardados
    3. Buscar un contacto por nombre
    4. Eliminar un contacto
    5. Salir del programa
"""

# Diccionario donde se almacenan los contactos: {nombre: telefono}
agenda = {}


def agregar_contacto():
    """Solicita nombre y teléfono al usuario y los guarda en la agenda."""
    nombre = input("Ingrese el nombre del contacto: ").strip()
    telefono = input("Ingrese el número telefónico: ").strip()

    if nombre == "":
        print("El nombre no puede estar vacío.\n")
        return

    agenda[nombre] = telefono
    print(f"Contacto '{nombre}' agregado correctamente.\n")


def mostrar_contactos():
    """Muestra en pantalla todos los contactos guardados."""
    if not agenda:
        print("La agenda está vacía. No hay contactos guardados.\n")
        return

    print("\n--- Lista de contactos ---")
    for nombre, telefono in agenda.items():
        print(f"Nombre: {nombre:<20} Teléfono: {telefono}")
    print("---------------------------\n")


def buscar_contacto():
    """Busca un contacto por nombre y muestra su teléfono si existe."""
    nombre = input("Ingrese el nombre del contacto a buscar: ").strip()

    if nombre in agenda:
        print(f"{nombre} -> {agenda[nombre]}\n")
    else:
        print(f"No se encontró ningún contacto llamado '{nombre}'.\n")


def eliminar_contacto():
    """Elimina un contacto de la agenda si existe."""
    nombre = input("Ingrese el nombre del contacto a eliminar: ").strip()

    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto '{nombre}' eliminado correctamente.\n")
    else:
        print(f"No se encontró ningún contacto llamado '{nombre}'.\n")


def mostrar_menu():
    """Muestra el menú principal de opciones."""
    print("===== AGENDA DE CONTACTOS =====")
    print("1. Agregar contacto")
    print("2. Mostrar todos los contactos")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")


def main():
    """Función principal que ejecuta el ciclo del programa."""
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ").strip()
        print()

        if opcion == "1":
            agregar_contacto()
        elif opcion == "2":
            mostrar_contactos()
        elif opcion == "3":
            buscar_contacto()
        elif opcion == "4":
            eliminar_contacto()
        elif opcion == "5":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.\n")


if __name__ == "__main__":
    main()
    