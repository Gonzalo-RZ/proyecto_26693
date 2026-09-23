class Medico:
    ESPECIALIDADES_VALIDAS = {
        "Dermatología", "Psicología", "Pediatría", "Ginecología",
        "Obstetricia", "Nutrición", "Medicina General", "Cirugía General",
    }

    def __init__(self, codigo, nombre, especialidad):
        self._codigo = codigo
        self.nombre = nombre
        self.especialidad = especialidad  # pasa por el setter (RF06)

    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor or not valor.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = valor.strip().title()

    @property
    def especialidad(self):
        return self._especialidad

    @especialidad.setter
    def especialidad(self, valor):
        valor = (valor or "").strip().title()
        if valor not in Medico.ESPECIALIDADES_VALIDAS:
            raise ValueError(
                f"Especialidad no reconocida. Use una de: "
                f"{', '.join(sorted(Medico.ESPECIALIDADES_VALIDAS))}"
            )
        self._especialidad = valor

    def __str__(self):
        return f"[{self.codigo}] Dr(a). {self.nombre} - {self.especialidad}"


def filtrar_medicos_por_especialidad(medicos, especialidad):
    """Función pura (paradigma funcional, RD03): no modifica la lista
    original, siempre da la misma salida para la misma entrada."""
    especialidad = (especialidad or "").strip().title()
    return list(filter(lambda m: m.especialidad == especialidad, medicos))