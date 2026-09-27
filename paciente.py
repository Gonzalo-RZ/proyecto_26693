class Paciente:
    def __init__(self, codigo, nombre, edad):
        self._codigo = codigo
        self.nombre = nombre     # pasa por el setter
        self.edad = edad         # pasa por el setter
        self._historial = []     # lista de atenciones (RF05)
        self._citas = []         # lista de citas asociadas (RF04)

    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        print(f">>> VALIDANDO NOMBRE: {valor}")
        if not valor or not valor.strip():
            raise ValueError("El nombre no puede estar vacío.")
        cadena_limpia = valor.replace(" ", "")
    
        if not cadena_limpia.isalpha():
            raise ValueError("El nombre solo debe contener letras.")
        self._nombre = valor.strip().title()

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        print(f">>> VALIDANDO EDAD: {valor}")
        
        # Validación de rango: entre 1 y 119 años
        if valor <= 0 or valor >= 120:
            raise ValueError("La edad debe ser mayor a 0 y menor a 120 años.")
        self._edad = valor


    @property
    def historial(self):
        return list(self._historial)  # copia: no se expone la lista real

    @property
    def citas(self):
        return list(self._citas)

    def agregar_atencion(self, descripcion):
        self._historial.append(descripcion)

    def agregar_cita(self, cita):
        self._citas.append(cita)

    def __str__(self):
        return f"[{self.codigo}] Paciente: {self.nombre} ({self.edad} años)"
