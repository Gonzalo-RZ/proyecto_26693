"""
main.py
-------
Sistema de escritorio para procesos de efectuación de denuncias
Comisaría PNP Payet, Lima 2026 - Versión v2.1 (corregida)

Punto de entrada del sistema. Aquí se instancian y llaman los métodos
de las 3 clases del proyecto: Ciudadano, ExpedientePolicial (entidades.py)
y GestorExpedientes (gestion.py), tal como exige la consigna.

TEMA01: control de versiones (ver README/GitHub) y estructuras de
control secuencial / condicional / repetitiva (todo este archivo).
"""

from entidades import Ciudadano
from gestion import GestorExpedientes


def mostrar_menu():
    print("\n==================================================")
    print(" MESA DE PARTES DIGITAL - COMISARÍA PNP PAYET v2.1")
    print("==================================================")
    print("1. Registrar trámite")
    print("2. Buscar por DNI")
    print("3. Listar expedientes")
    print("4. Ordenar expedientes (burbuja por N°)")
    print("5. Cancelar expediente")
    print("6. Demo recursividad (factorial y conteo)")
    print("0. Salir")
    print("--------------------------------------------------")


def leer_opcion_entero(mensaje: str):
    """Estructura condicional de validación: evita que el programa truene
    si el usuario ingresa texto donde se espera un número (CP-13)."""
    valor = input(mensaje)
    if not valor.strip().lstrip("-").isdigit():
        return None
    return int(valor)


def registrar(gestor: GestorExpedientes):
    print("\n--- Registro de trámite ---")
    print("Tipos de trámite: 1) Denuncia  2) Pérdida de Documentos  "
          "3) Citación Policial  4) Garantías Personales")

    dni = input("Ingrese su código de estudiante o DNI: ")
    if not Ciudadano.validar_dni(dni):
        print("❌ DNI inválido. Debe tener 8 dígitos numéricos.")
        return

    nombre = input("Ingrese nombres y apellidos: ")
    tipo = leer_opcion_entero("Ingrese el tipo de trámite (1-4): ")
    if tipo is None:
        print("❌ Debe ingresar un número de opción válido.")
        return

    ok, resultado = gestor.registrar_expediente(dni, nombre, tipo)
    if ok:
        expediente = resultado
        print(f"\n✅ Expediente N° {expediente.numero:04d} guardado correctamente.")
        print(expediente.generar_cargo())
    else:
        print(f"❌ {resultado}")


def buscar(gestor: GestorExpedientes):
    print("\n--- Búsqueda por DNI ---")
    dni = input("Ingrese el DNI a buscar: ")
    resultados = gestor.buscar_por_dni(dni)
    if not resultados:
        print("No se encontraron expedientes asociados a ese DNI.")
        return
    for exp in resultados:
        print(exp.generar_cargo())


def listar(gestor: GestorExpedientes):
    print("\n--- Listado de expedientes ---")
    expedientes = gestor.listar_expedientes()
    if not expedientes:
        print("No hay expedientes registrados.")
        return
    encabezado = f"{'N°':<6}{'DNI':<12}{'NOMBRE':<32}{'TRÁMITE':<22}{'ESTADO':<12}"
    print(encabezado)
    print("-" * len(encabezado))
    for exp in expedientes:
        print(exp.fila_listado())


def ordenar(gestor: GestorExpedientes):
    print("\n--- Expedientes ordenados (Método Burbuja, por N°) ---")
    ordenados = gestor.ordenar_burbuja_por_numero()
    for exp in ordenados:
        print(exp.fila_listado())

    print("\n--- Expedientes ordenados (Método Selección, por nombre) ---")
    ordenados_nombre = gestor.ordenar_seleccion_por_nombre()
    for exp in ordenados_nombre:
        print(exp.fila_listado())


def cancelar(gestor: GestorExpedientes):
    print("\n--- Cancelar expediente ---")
    numero = leer_opcion_entero("Ingrese el N° de expediente a cancelar: ")
    if numero is None:
        print("❌ Valor numérico inválido.")
        return
    ok, mensaje = gestor.cancelar_expediente(numero)
    print(("✅ " if ok else "❌ ") + mensaje)


def demo_recursividad(gestor: GestorExpedientes):
    print("\n--- Demo de recursividad (TEMA07) ---")
    n = leer_opcion_entero("Ingrese un número para calcular su factorial: ")
    if n is None or n < 0:
        print("❌ Debe ingresar un número entero positivo.")
        return
    print(f"{n}! = {GestorExpedientes.factorial(n)}")
    print(f"Cantidad de expedientes (conteo recursivo): "
          f"{gestor.contar_expedientes_recursivo()}")


def main():
    gestor = GestorExpedientes()

    # TEMA01: estructura de control repetitiva (menú principal).
    opcion = -1
    while opcion != 0:
        mostrar_menu()
        opcion = leer_opcion_entero("Seleccione una opción: ")

        # TEMA01: estructura de control condicional (ramas del menú).
        if opcion == 1:
            registrar(gestor)
        elif opcion == 2:
            buscar(gestor)
        elif opcion == 3:
            listar(gestor)
        elif opcion == 4:
            ordenar(gestor)
        elif opcion == 5:
            cancelar(gestor)
        elif opcion == 6:
            demo_recursividad(gestor)
        elif opcion == 0:
            print("\nSaliendo del sistema. ¡Hasta pronto!")
        else:
            print("❌ Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
