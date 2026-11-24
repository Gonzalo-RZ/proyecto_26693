"""
utilidades.py - Funciones reutilizables del sistema (TEMA 02, 04 y 07).

Aquí se concentran las funciones que NO pertenecen a una sola clase:
validaciones, tratamiento de cadenas, algoritmos de ordenamiento,
lectura segura de datos y funciones recursivas.
"""
import re

# ----------------------------------------------------------------------
# TEMA 04: cadenas de caracteres
# ----------------------------------------------------------------------
PATRON_NOMBRE = r"^[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+(?: [A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+)+$"


def normalizar_nombre(texto: str) -> str:
    """Quita espacios sobrantes (strip/split/join) y pasa a MAYÚSCULAS."""
    return " ".join(texto.split()).upper()


def validar_dni(dni: str) -> bool:
    """El DNI debe tener exactamente 8 dígitos numéricos."""
    return len(dni) == 8 and dni.isdigit()


def validar_nombre(nombre: str) -> bool:
    """Solo letras (con tildes y ñ) y espacios; mínimo apellido y nombre."""
    return bool(re.match(PATRON_NOMBRE, " ".join(nombre.split())))


def separar_apellidos_nombres(nombre: str):
    """Devuelve (primer apellido, resto) usando split()."""
    partes = normalizar_nombre(nombre).split(" ")
    return partes[0], " ".join(partes[1:])


def enmascarar_dni(dni: str) -> str:
    """Oculta los 4 dígitos centrales (protección de datos personales)."""
    return dni[:2] + "****" + dni[-2:]


# ----------------------------------------------------------------------
# TEMA 02 y 06: lectura de datos reutilizable (se usa desde varios menús)
# ----------------------------------------------------------------------
def leer_texto(mensaje: str) -> str:
    return input(mensaje).strip()


def leer_entero(mensaje: str):
    """Devuelve un entero o None si el usuario no escribió un número."""
    try:
        return int(input(mensaje).strip())
    except ValueError:
        return None


# ----------------------------------------------------------------------
# TEMA 03: ordenamientos (reutilizables para cualquier lista)
# El parámetro 'lista' se pasa "por referencia": se ordena la misma lista.
# 'clave' es una función que indica por qué campo se compara.
# ----------------------------------------------------------------------
def burbuja(lista: list, clave) -> None:
    n = len(lista)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if clave(lista[j]) > clave(lista[j + 1]):
                lista[j], lista[j + 1] = lista[j + 1], lista[j]


def seleccion(lista: list, clave) -> None:
    n = len(lista)
    for i in range(n - 1):
        menor = i
        for j in range(i + 1, n):
            if clave(lista[j]) < clave(lista[menor]):
                menor = j
        if menor != i:
            lista[i], lista[menor] = lista[menor], lista[i]


# ----------------------------------------------------------------------
# TEMA 07: recursividad
# ----------------------------------------------------------------------
def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("El factorial no está definido para negativos")
    if n <= 1:                      # caso base
        return 1
    return n * factorial(n - 1)     # caso recursivo


def factorial_iterativo(n: int) -> int:
    if n < 0:
        raise ValueError("El factorial no está definido para negativos")
    resultado = 1
    for k in range(2, n + 1):
        resultado *= k
    return resultado


def potencia(base: int, exponente: int) -> int:
    if exponente < 0:
        raise ValueError("Solo exponentes enteros no negativos")
    if exponente == 0:              # caso base
        return 1
    return base * potencia(base, exponente - 1)


def sumatoria(n: int) -> int:
    """1 + 2 + ... + n"""
    if n < 0:
        raise ValueError("n debe ser no negativo")
    if n == 0:
        return 0
    return n + sumatoria(n - 1)


def contar_recursivo(valores: list, objetivo, indice: int = 0) -> int:
    """Cuenta cuántas veces aparece 'objetivo' recorriendo la lista con recursión."""
    if indice >= len(valores):      # caso base: se acabó la lista
        return 0
    coincide = 1 if valores[indice] == objetivo else 0
    return coincide + contar_recursivo(valores, objetivo, indice + 1)


def buscar_binaria_recursiva(ids: list, objetivo: int, bajo: int, alto: int) -> int:
    """Búsqueda binaria recursiva sobre IDs ordenados. Devuelve la posición o -1."""
    if bajo > alto:                 # caso base: no existe
        return -1
    medio = (bajo + alto) // 2
    if ids[medio] == objetivo:      # caso base: encontrado
        return medio
    if ids[medio] < objetivo:
        return buscar_binaria_recursiva(ids, objetivo, medio + 1, alto)
    return buscar_binaria_recursiva(ids, objetivo, bajo, medio - 1)
