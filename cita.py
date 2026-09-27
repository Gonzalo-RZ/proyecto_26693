class Cita:
    def __init__(self, codigo, paciente, medico, fecha):
        self._codigo = codigo
        self._paciente = paciente
        self._medico = medico
        self._fecha = fecha
        self._estado = "programada"  # programada | atendida | cancelada

    @property
    def codigo(self):
        return self._codigo

    @property
    def paciente(self):
        return self._paciente

    @property
    def medico(self):
        return self._medico

    @property
    def fecha(self):
        return self._fecha

    @property
    def estado(self):
        return self._estado

    def cancelar(self):
        # RF07: no se puede cancelar una cita ya atendida
        if self._estado == "atendida":
            raise ValueError("No se puede cancelar una cita ya atendida.")
        self._estado = "cancelada"

    def marcar_atendida(self):
        self._estado = "atendida"

    def __str__(self):
        return (f"[{self.codigo}] {self.paciente.nombre} con {self.medico.nombre} "
                f"el {self.fecha} - Estado: {self.estado}")
