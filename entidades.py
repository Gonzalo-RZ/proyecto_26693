"""
entidades.py
------------
TEMA02 (Funciones y modularidad) y TEMA04 (Cadenas de caracteres).

Contiene las clases del dominio: Ciudadano y ExpedientePolicial.
Se usa encapsulamiento (atributos con guion bajo + propiedades) y
métodos propios de cada clase, tal como exige el requerimiento de
"mínimo 3 clases con métodos, llamadas dentro del MAIN".
"""

import re
from datetime import datetime


class Ciudadano:
    """Representa a la persona que presenta el trámite ante la comisaría."""

    def __init__(self, dni: str, nombre_completo: str):
        self._dni = dni
        # TEMA04: se usa .strip() y .upper() (métodos de cadenas) para
        # normalizar el nombre antes de guardarlo.
        self._nombre_completo = nombre_completo.strip().upper()

    # ---- Propiedades (encapsulamiento) ----
    @property
    def dni(self) -> str:
        return self._dni

    @property
    def nombre_completo(self) -> str:
        return self._nombre_completo

    # ---- Métodos de validación (parámetros por valor) ----
    @staticmethod
    def validar_dni(dni: str) -> bool:
        """DNI peruano: exactamente 8 dígitos numéricos."""
        return dni.isdigit() and len(dni) == 8

    @staticmethod
    def validar_nombre(nombre: str) -> bool:
        """
        Corrección aplicada tras el Desafío 6 (CP-05):
        solo letras (con tildes y ñ) y espacios, y al menos dos
        palabras (apellidos y nombres).
        """
        patron = r"^[A-Za-zÁÉÍÓÚáéíóúÑñ]+(\s[A-Za-zÁÉÍÓÚáéíóúÑñ]+)+$"
        return bool(re.match(patron, nombre.strip()))

    def __str__(self):
        return f"{self._dni} - {self._nombre_completo}"


class ExpedientePolicial:
    """Representa el expediente/trámite registrado en mesa de partes."""

    TIPOS_TRAMITE = {
        1: "Denuncia",
        2: "Pérdida de Documentos",
        3: "Citación Policial",
        4: "Garantías Personales",
    }

    ESTADOS = ("EN PROCESO", "ATENDIDO", "CANCELADO")

    def __init__(self, numero: int, ciudadano: Ciudadano, tipo_tramite: int):
        self._numero = numero
        self._ciudadano = ciudadano
        self._tipo_tramite = tipo_tramite
        self._estado = "EN PROCESO"
        self._fecha_registro = datetime.now().strftime("%d/%m/%Y %H:%M")

    # ---- Propiedades ----
    @property
    def numero(self) -> int:
        return self._numero

    @property
    def ciudadano(self) -> Ciudadano:
        return self._ciudadano

    @property
    def tipo_tramite_texto(self) -> str:
        return self.TIPOS_TRAMITE.get(self._tipo_tramite, "Desconocido")

    @property
    def tipo_tramite(self) -> int:
        return self._tipo_tramite

    @property
    def estado(self) -> str:
        return self._estado

    @estado.setter
    def estado(self, nuevo_estado: str):
        if nuevo_estado in self.ESTADOS:
            self._estado = nuevo_estado

    @property
    def fecha_registro(self) -> str:
        return self._fecha_registro

    # ---- Validación del tipo de trámite (corrección CP-06) ----
    @staticmethod
    def validar_tipo_tramite(opcion: int) -> bool:
        return opcion in ExpedientePolicial.TIPOS_TRAMITE

    # ---- Representación para listado y persistencia ----
    def generar_cargo(self) -> str:
        """Genera el cargo de recepción. Corrección CP-14: texto 100% en español."""
        return (
            f"--------------------------------------------\n"
            f"CARGO DE RECEPCIÓN - MESA DE PARTES PNP PAYET\n"
            f"--------------------------------------------\n"
            f"N° de Expediente : {self._numero:04d}\n"
            f"DNI              : {self._ciudadano.dni}\n"
            f"Ciudadano        : {self._ciudadano.nombre_completo}\n"
            f"Tipo de trámite  : {self.tipo_tramite_texto}\n"
            f"Fecha de registro: {self._fecha_registro}\n"
            f"Estado           : {self._estado}\n"
            f"--------------------------------------------\n"
            f"Conserve este cargo para la verificación oficial.\n"
        )

    def a_linea_archivo(self) -> str:
        """Serializa el expediente en una línea de texto (ver persistencia.py)."""
        return (
            f"{self._numero}|{self._ciudadano.dni}|"
            f"{self._ciudadano.nombre_completo}|{self._tipo_tramite}|"
            f"{self._estado}|{self._fecha_registro}"
        )

    @staticmethod
    def desde_linea_archivo(linea: str) -> "ExpedientePolicial":
        """Reconstruye un ExpedientePolicial desde una línea leída del archivo."""
        numero, dni, nombre, tipo, estado, fecha = linea.strip().split("|")
        ciudadano = Ciudadano(dni, nombre)
        exp = ExpedientePolicial(int(numero), ciudadano, int(tipo))
        exp._estado = estado
        exp._fecha_registro = fecha
        return exp

    def fila_listado(self) -> str:
        """
        Corrección CP-15: se usa un ancho fijo (ljust) para que los
        nombres largos no desalineen la tabla del listado.
        """
        return (
            f"{self._numero:<6}{self._ciudadano.dni:<12}"
            f"{self._ciudadano.nombre_completo:<32}"
            f"{self.tipo_tramite_texto:<22}{self._estado:<12}"
        )
