"""
persistencia.py - Almacenamiento en archivos de texto (TEMA 05).
"""
import os
from entidades import ExpedientePolicial


class RepositorioArchivo:
    """Clase 4: guarda y recupera los expedientes en un archivo TXT."""

    ENCABEZADO = "# ID;DNI;NOMBRE;TRAMITE;ESTADO;FECHA"

    def __init__(self, ruta: str):
        self.ruta = ruta

    def guardar(self, expedientes: list) -> None:
        carpeta = os.path.dirname(self.ruta)
        if carpeta:
            os.makedirs(carpeta, exist_ok=True)
        with open(self.ruta, "w", encoding="utf-8") as archivo:
            archivo.write(self.ENCABEZADO + "\n")
            for exp in expedientes:
                archivo.write(exp.a_linea() + "\n")

    def cargar(self):
        """Devuelve (lista de expedientes, cantidad de líneas dañadas)."""
        expedientes, danadas = [], 0
        try:
            with open(self.ruta, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    if not linea.strip() or linea.startswith("#"):
                        continue
                    exp = ExpedientePolicial.desde_linea(linea)
                    if exp is None:
                        danadas += 1
                    else:
                        expedientes.append(exp)
        except FileNotFoundError:
            pass                      # primera ejecución: aún no hay archivo
        return expedientes, danadas

    def exportar_texto(self, ruta_destino: str, contenido: str) -> None:
        with open(ruta_destino, "w", encoding="utf-8") as archivo:
            archivo.write(contenido)
