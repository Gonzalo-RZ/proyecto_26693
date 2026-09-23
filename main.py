from paciente import Paciente
from medico import Medico, filtrar_medicos_por_especialidad
from cita import Cita

pacientes = {}
medicos = {}
citas = {}
contador_citas = 0


def cargar_medicos_demo():
    """Médicos ya disponibles, uno por especialidad, para que el paciente elija."""
    datos = [
        ("M01", "Sofía Ramos", "Dermatología"),
        ("M02", "Carlos Mendoza", "Psicología"),
        ("M03", "Ana Torres", "Pediatría"),
        ("M04", "Lucía Vargas", "Ginecología"),
        ("M05", "Elena Quispe", "Obstetricia"),
        ("M06", "Pedro Salas", "Nutrición"),
        ("M07", "Luis Rojas", "Medicina General"),
        ("M08", "Marco Díaz", "Cirugía General"),
    ]
    for codigo, nombre, especialidad in datos:
        medicos[codigo] = Medico(codigo, nombre, especialidad)


def registrar_paciente():
    """RF01"""
    codigo = input("Código del paciente: ").strip()
    if codigo in pacientes:
        print("Error: código duplicado.")
        return
    nombre = input("Nombre: ").strip()
    
    try:  
        edad = int(input("Edad: ")) 
        # Aquí se crea el objeto y se dispara tu setter de nombre
        pacientes[codigo] = Paciente(codigo, nombre, edad)
        print(f"Registrado: {pacientes[codigo]}")

    except ValueError as e:
        # Unificamos ambos casos en un solo except
        if "invalid literal" in str(e):
            print("Edad no numérica.")
        else:
            print(f"Error: {e}") # <-- AQUÍ SE IMPRIMIRÁ: "Error: El nombre solo debe contener letras."



def registrar_medico():
    """RF02 (ya hay 8 cargados; esto es para sumar uno extra)."""
    codigo = input("Código del médico: ").strip()
    if codigo in medicos:
        print("Error: código duplicado.")
        return
    nombre = input("Nombre: ").strip()
    especialidad = input("Especialidad: ").strip()
    try:
        medicos[codigo] = Medico(codigo, nombre, especialidad)
        print(f"Registrado: {medicos[codigo]}")
    except ValueError as e:
        print(f"Error: {e}")


def elegir_medico():
    """Muestra la lista de médicos y devuelve el que el paciente elija."""
    lista = list(medicos.values())
    for i in range(len(lista)):
        print(f"{i + 1}) {lista[i]}")
    try:
        opcion = int(input("Elige un médico (número): "))
        return lista[opcion - 1]
    except (ValueError, IndexError):
        print("Opción no válida.")
        return None


def programar_cita():
    """RF04"""
    global contador_citas
    codigo_paciente = input("Código del paciente: ").strip()
    if codigo_paciente not in pacientes:
        print("Error: paciente no existe.")
        return
    medico = elegir_medico()
    if medico is None:
        return
    fecha = input("Fecha (dd/mm/aaaa): ").strip()
    contador_citas = contador_citas + 1
    codigo_cita = f"C{contador_citas:03d}"
    cita = Cita(codigo_cita, pacientes[codigo_paciente], medico, fecha)
    citas[codigo_cita] = cita
    pacientes[codigo_paciente].agregar_cita(cita)
    print(f"Cita creada: {cita}")


def registrar_atencion():
    """RF05"""
    codigo_cita = input("Código de la cita: ").strip()
    if codigo_cita not in citas:
        print("Error: esa cita no existe.")
        return
    cita = citas[codigo_cita]
    if cita.estado == "cancelada":
        print("Error: no se puede atender una cita cancelada.")
        return
    detalle = input("Descripción: ").strip()
    cita.marcar_atendida()
    cita.paciente.agregar_atencion(f"{cita.fecha} - {cita.medico.especialidad}: {detalle}")
    print("Atención registrada.")


def filtrar_medicos_menu():
    """RF06: mostrar médicos y permitir que el usuario elija uno."""
    lista = list(medicos.values())
    print("\n===== MÉDICOS DISPONIBLES =====")

    for i, medico in enumerate(lista, 1):
        print(f"{i}) {medico}")
    try:
        opcion = int(input("Elige un médico (número): "))
        if opcion < 1 or opcion > len(lista):
            print("Opción no válida.")
            return

        medico_elegido = lista[opcion - 1]
        print("\n===== MÉDICO SELECCIONADO =====")
        print(medico_elegido)
    except ValueError:
        print("Debes ingresar un número.")

def cancelar_cita():
    """RF07"""
    codigo_cita = input("Código de la cita: ").strip()
    if codigo_cita not in citas:
        print("Error: esa cita no existe.")
        return
    try:
        citas[codigo_cita].cancelar()
        print("Cita cancelada.")
    except ValueError as e:
        print(f"Error: {e}")


def ver_historial():
    """RF03: muestra al paciente, sus citas y sus atenciones."""
    codigo = input("Código del paciente: ").strip()
    if codigo not in pacientes:
        print("Error: paciente no existe.")
        return
    paciente = pacientes[codigo]
    print(paciente)
    print("Citas:", [str(c) for c in paciente.citas] or "sin citas")
    print("Historial:", paciente.historial or "sin atenciones")


def mostrar_menu():
    print("\n===== SISTEMA KAWSAY =====")
    print("1) Registrar paciente")
    print("2) Registrar médico")
    print("3) Programar cita")
    print("4) Registrar atención")
    print("5) Filtrar médicos por especialidad")
    print("6) Cancelar cita")
    print("7) Ver historial del paciente")
    print("8) Salir")


def menu():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            registrar_paciente()
        elif opcion == "2":
            registrar_medico()
        elif opcion == "3":
            programar_cita()
        elif opcion == "4":
            registrar_atencion()
        elif opcion == "5":
            filtrar_medicos_menu()
        elif opcion == "6":
            cancelar_cita()
        elif opcion == "7":
            ver_historial()
        elif opcion == "8":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    cargar_medicos_demo()
    menu()