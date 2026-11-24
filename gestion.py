"""
gestion.py
----------
Clase GestorExpedientes: concentra la lógica de negocio.
Cubre: TEMA03 (arreglos/CRUD/ordenamiento), TEMA04 (arreglos paralelos
y búsqueda), TEMA05 (persistencia en archivo), TEMA07 (recursividad).
"""

import os
from entidades import Ciudadano, ExpedientePolicial

ARCHIVO_DATOS = os.path.join(os.path.dirname(__file__), "data", "expedientes.txt")


class GestorExpedientes:
    """Administra la lista de expedientes en memoria y su persistencia."""

    def __init__(self):
        # TEMA03: arreglo (lista) principal de objetos ExpedientePolicial.
        self._expedientes = []
        self._siguiente_numero = 1
        self.cargar_desde_archivo()

    # ------------------------------------------------------------------
    # TEMA03 - CRUD
    # ------------------------------------------------------------------
    def verificar_registro(self, dni: str, nombre: str, tipo_tramite: int):
        """
        Corrección aplicada tras el Desafío 6:
        - CP-04: bloquea un trámite duplicado EN PROCESO con el mismo DNI.
        - CP-07: bloquea un DNI ya registrado con un nombre distinto.
        Retorna (ok: bool, mensaje: str).
        """
        for exp in self._expedientes:
            if exp.ciudadano.dni == dni and exp.estado == "EN PROCESO":
                if exp.tipo_tramite == tipo_tramite:
                    return False, (
                        f"Ya existe el expediente N° {exp.numero:04d} EN PROCESO "
                        f"con el mismo DNI y trámite."
                    )
                if exp.ciudadano.nombre_completo != nombre.strip().upper():
                    return False, (
                        "El DNI ya está registrado con otro nombre. "
                        "Verifique la identidad."
                    )
        return True, "OK"

    def registrar_expediente(self, dni: str, nombre: str, tipo_tramite: int):
        """
        Crea (Create) un nuevo expediente aplicando todas las validaciones
        corregidas. Retorna (ok: bool, mensaje_o_expediente).
        """
        if not Ciudadano.validar_dni(dni):
            return False, "DNI inválido. Debe tener 8 dígitos numéricos."

        if not Ciudadano.validar_nombre(nombre):
            return False, (
                "El nombre solo puede tener letras y espacios, "
                "e incluir apellidos y nombres."
            )

        if not ExpedientePolicial.validar_tipo_tramite(tipo_tramite):
            return False, "Tipo de trámite inválido. Seleccione una opción entre 1 y 4."

        ok, mensaje = self.verificar_registro(dni, nombre, tipo_tramite)
        if not ok:
            return False, mensaje

        ciudadano = Ciudadano(dni, nombre)
        expediente = ExpedientePolicial(self._siguiente_numero, ciudadano, tipo_tramite)
        self._expedientes.append(expediente)
        self._siguiente_numero += 1
        self.guardar_en_archivo()
        return True, expediente

    def buscar_por_dni(self, dni: str):
        """Read: TEMA04 - búsqueda lineal por DNI (arreglo paralelo simulado)."""
        resultados = [e for e in self._expedientes if e.ciudadano.dni == dni]
        return resultados

    def listar_expedientes(self):
        return list(self._expedientes)

    def cancelar_expediente(self, numero: int):
        """Delete (lógico): cambia el estado a CANCELADO."""
        for exp in self._expedientes:
            if exp.numero == numero:
                if exp.estado == "CANCELADO":
                    return False, f"El expediente N° {numero:04d} ya estaba cancelado."
                exp.estado = "CANCELADO"
                self.guardar_en_archivo()
                return True, f"Expediente N° {numero:04d} cancelado correctamente."
        return False, f"No existe un expediente con el número {numero}."

    # ------------------------------------------------------------------
    # TEMA03 - Ordenamientos
    # ------------------------------------------------------------------
    def ordenar_burbuja_por_numero(self):
        """Método Burbuja ascendente por N° de expediente."""
        datos = list(self._expedientes)
        n = len(datos)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if datos[j].numero > datos[j + 1].numero:
                    datos[j], datos[j + 1] = datos[j + 1], datos[j]
        return datos

    def ordenar_seleccion_por_nombre(self):
        """Método Selección ascendente por nombre del ciudadano."""
        datos = list(self._expedientes)
        n = len(datos)
        for i in range(n - 1):
            idx_menor = i
            for j in range(i + 1, n):
                if datos[j].ciudadano.nombre_completo < datos[idx_menor].ciudadano.nombre_completo:
                    idx_menor = j
            datos[i], datos[idx_menor] = datos[idx_menor], datos[i]
        return datos

    # ------------------------------------------------------------------
    # TEMA04 - Arreglos paralelos (código, nombre, precio) - demo
    # requerido por el sílabo como ejemplo independiente del dominio.
    # ------------------------------------------------------------------
    @staticmethod
    def demo_arreglos_paralelos():
        codigos = ["P001", "P002", "P003"]
        nombres = ["Laptop", "Mouse", "Teclado"]
        precios = [2500.0, 50.0, 80.0]

        salida = []
        for i in range(len(codigos)):
            salida.append(f"{codigos[i]}: {nombres[i]};{precios[i]}")
        return salida

    @staticmethod
    def buscar_en_arreglos_paralelos(nombre_buscado: str):
        codigos = ["P001", "P002", "P003"]
        nombres = ["Laptop", "Mouse", "Teclado"]
        precios = [2500.0, 50.0, 80.0]
        for i in range(len(nombres)):
            if nombres[i].lower() == nombre_buscado.lower():
                return codigos[i], nombres[i], precios[i]
        return None

    # ------------------------------------------------------------------
    # TEMA05 - Persistencia de datos (archivo de texto)
    # ------------------------------------------------------------------
    def guardar_en_archivo(self):
        os.makedirs(os.path.dirname(ARCHIVO_DATOS), exist_ok=True)
        with open(ARCHIVO_DATOS, "w", encoding="utf-8") as f:
            for exp in self._expedientes:
                f.write(exp.a_linea_archivo() + "\n")

    def cargar_desde_archivo(self):
        if not os.path.exists(ARCHIVO_DATOS):
            return
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as f:
            for linea in f:
                if linea.strip():
                    exp = ExpedientePolicial.desde_linea_archivo(linea)
                    self._expedientes.append(exp)
                    if exp.numero >= self._siguiente_numero:
                        self._siguiente_numero = exp.numero + 1

    # ------------------------------------------------------------------
    # TEMA07 - Recursividad
    # ------------------------------------------------------------------
    @staticmethod
    def factorial(n: int) -> int:
        """Ejemplo clásico de recursividad (TEMA07)."""
        if n <= 1:
            return 1
        return n * GestorExpedientes.factorial(n - 1)

    def contar_expedientes_recursivo(self, lista=None) -> int:
        """Cuenta los expedientes usando recursividad en lugar de len()."""
        if lista is None:
            lista = self._expedientes
        if not lista:
            return 0
        return 1 + self.contar_expedientes_recursivo(lista[1:])

    def buscar_por_dni_recursivo(self, dni: str, indice: int = 0):
        """Búsqueda recursiva por DNI (alternativa recursiva a buscar_por_dni)."""
        if indice >= len(self._expedientes):
            return None
        if self._expedientes[indice].ciudadano.dni == dni:
            return self._expedientes[indice]
        return self.buscar_por_dni_recursivo(dni, indice + 1)
