"""
Sistema de Préstamos de Equipos
--------------------------------
Aplicación para gestionar inventario, préstamos y devoluciones de equipos de cómputo.
Utiliza diccionarios, listas y tuplas para almacenar la información.
"""

import datetime

# Estructura principal del sistema:
# equipos = {
#     "nombre_equipo": {
#         "disponible": True/False,
#         "prestamos": [(usuario, fecha), ...]
#     }
# }

equipos = {}  # Diccionario vacío para almacenar los equipos


def mostrar_equipos():
    """
    Muestra en pantalla todos los equipos registrados y su estado actual.
    """
    if not equipos:
        print("\n--- No hay equipos registrados en el sistema ---")
        return

    print("\n--- Lista de Equipos ---")
    for nombre, datos in equipos.items():
        estado = "Disponible" if datos["disponible"] else "Prestado"
        print(f"- {nombre}: {estado}")
    print("------------------------")


def registrar_prestamo():
    """
    Registra un nuevo préstamo de un equipo disponible.
    Solicita el nombre exacto del equipo y el nombre del usuario.
    Guarda la información en una tupla (usuario, fecha) y actualiza el estado.
    """
    if not equipos:
        print("\nNo hay equipos registrados. Por favor, agregue equipos primero.")
        return

    print("\n--- Registrar Préstamo ---")
    # Mostrar solo los equipos disponibles (opcional, pero el enunciado pide mostrar todos)
    mostrar_equipos()

    equipo = input("\nIngrese el nombre exacto del equipo a prestar: ").strip()
    if equipo not in equipos:
        print(f"Error: El equipo '{equipo}' no existe en el sistema.")
        return

    if not equipos[equipo]["disponible"]:
        print(f"Error: El equipo '{equipo}' ya está prestado actualmente.")
        return

    usuario = input("Ingrese el nombre del usuario que realiza el préstamo: ").strip()
    if not usuario:
        print("Error: El nombre del usuario no puede estar vacío.")
        return

    # Obtener fecha actual o solicitarla al usuario
    fecha = input("Ingrese la fecha del préstamo (DD/MM/AAAA) o presione Enter para usar hoy: ").strip()
    if not fecha:
        fecha = datetime.datetime.now().strftime("%d/%m/%Y")

    # Crear tupla inmutable con los datos del préstamo
    prestamo = (usuario, fecha)

    # Agregar a la lista de préstamos del equipo
    equipos[equipo]["prestamos"].append(prestamo)

    # Cambiar estado a no disponible
    equipos[equipo]["disponible"] = False

    print(f"\nPréstamo registrado exitosamente. Equipo '{equipo}' prestado a {usuario} el {fecha}.")


def devolver_equipo():
    """
    Marca un equipo como devuelto.
    Cambia el estado del equipo a disponible si está prestado.
    """
    if not equipos:
        print("\nNo hay equipos registrados.")
        return

    print("\n--- Devolver Equipo ---")
    equipo = input("Ingrese el nombre exacto del equipo a devolver: ").strip()
    if equipo not in equipos:
        print(f"Error: El equipo '{equipo}' no existe en el sistema.")
        return

    if equipos[equipo]["disponible"]:
        print(f"El equipo '{equipo}' ya está disponible (no está prestado).")
        return

    # Cambiar estado a disponible
    equipos[equipo]["disponible"] = True
    print(f"Equipo '{equipo}' devuelto correctamente y ahora está disponible.")


def ver_historial():
    """
    Muestra el historial completo de préstamos de todos los equipos.
    Para cada equipo, lista los préstamos realizados (usuario y fecha).
    """
    if not equipos:
        print("\nNo hay equipos registrados.")
        return

    print("\n--- Historial de Préstamos ---")
    for nombre, datos in equipos.items():
        print(f"\nEquipo: {nombre}")
        prestamos = datos["prestamos"]
        if prestamos:
            print("  Préstamos realizados:")
            for i, (usuario, fecha) in enumerate(prestamos, 1):
                print(f"    {i}. Usuario: {usuario}, Fecha: {fecha}")
        else:
            print("  Sin préstamos registrados.")
    print("\n-----------------------------")


def agregar_equipo():
    """
    Agrega un nuevo equipo al inventario.
    Verifica que no exista previamente y lo inicializa como disponible con lista de préstamos vacía.
    """
    print("\n--- Agregar Nuevo Equipo ---")
    nombre = input("Ingrese el nombre del nuevo equipo: ").strip()
    if not nombre:
        print("Error: El nombre del equipo no puede estar vacío.")
        return

    if nombre in equipos:
        print(f"El equipo '{nombre}' ya existe en el sistema.")
        return

    # Agregar el equipo con estado disponible y lista vacía de préstamos
    equipos[nombre] = {
        "disponible": True,
        "prestamos": []
    }
    print(f"Equipo '{nombre}' agregado exitosamente al inventario.")


def menu():
    """
    Función principal que muestra el menú interactivo y gestiona las opciones.
    Se repite hasta que el usuario elige salir.
    """
    while True:
        print("\n" + "=" * 40)
        print("   SISTEMA DE PRÉSTAMOS DE EQUIPOS")
        print("=" * 40)
        print("1. Ver equipos disponibles")
        print("2. Registrar préstamo")
        print("3. Devolver equipo")
        print("4. Ver historial de préstamos")
        print("5. Agregar nuevo equipo")
        print("6. Salir del programa")
        print("=" * 40)

        opcion = input("Seleccione una opción (1-6): ").strip()

        if opcion == "1":
            mostrar_equipos()
        elif opcion == "2":
            registrar_prestamo()
        elif opcion == "3":
            devolver_equipo()
        elif opcion == "4":
            ver_historial()
        elif opcion == "5":
            agregar_equipo()
        elif opcion == "6":
            print("\n¡Gracias por usar el Sistema de Préstamos de Equipos! Hasta luego.")
            break
        else:
            print("\nOpción no válida. Por favor, ingrese un número del 1 al 6.")

        # Pausa para que el usuario pueda leer los resultados antes de continuar
        input("\nPresione Enter para continuar...")


# Punto de entrada del programa
if __name__ == "__main__":
    # Opcional: Agregar algunos equipos de ejemplo para pruebas iniciales
    # (Se pueden comentar o eliminar para empezar desde cero)
    equipos_ejemplo = {
        "Laptop Dell XPS": {"disponible": True, "prestamos": []},
        "Proyector Epson": {"disponible": True, "prestamos": []},
        "Tableta Wacom": {"disponible": False, "prestamos": [("Ana García", "15/03/2025")]},
    }
    equipos.update(equipos_ejemplo)  # Cargar datos de ejemplo

    menu()