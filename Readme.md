# Mesa de Partes Digital - Comisaría PNP Payet (v2.1)

Sistema de escritorio en Python para el registro, búsqueda, ordenamiento
y cancelación de expedientes de trámites (denuncia, pérdida de
documentos, citación policial y garantías personales).

## Corrección de validaciones tras pruebas (Desafío 6 → v2.1)

| # | Error detectado (v2.0) | Corrección aplicada (v2.1) |
|---|---|---|
| 1 | Se permitía registrar el mismo trámite dos veces para el mismo DNI | `verificar_registro()` bloquea duplicados EN PROCESO |
| 2 | El nombre aceptaba números y símbolos | `Ciudadano.validar_nombre()` con expresión regular |
| 3 | Un tipo de trámite inválido se guardaba como "Trámite General" | `ExpedientePolicial.validar_tipo_tramite()` solo acepta 1-4 |
| 4 | Un mismo DNI podía registrarse con otro nombre | `verificar_registro()` valida identidad por DNI |
| 5 | El cargo de recepción tenía una línea en inglés | `generar_cargo()` 100% en español |
| 6 | El listado se desalineaba con nombres largos | `fila_listado()` usa ancho fijo (ljust) |

## Estructura del proyecto

```
proyecto_26693/
├── main.py          # Menú principal (estructuras de control, TEMA01)
├── entidades.py      # Clases Ciudadano y ExpedientePolicial (TEMA02, TEMA04)
├── gestion.py         # Clase GestorExpedientes: CRUD, ordenamientos,
│                       # persistencia y recursividad (TEMA03, TEMA05, TEMA07)
├── demo_temas.py       # Demostración de métodos de cadena y arreglos
│                        # paralelos (TEMA04, TEMA06)
├── data/
│   └── expedientes.txt # Persistencia de datos (TEMA05)
└── README.md
```

## Ejecución

```bash
python main.py
```

## Equipo (Grupo 5)

- Tazaico Ruiz, Gonzalo Mathias
- Catalino Valentín, Xiomara Cielo
- Carlos Corzo, Esteban Antonio
- Valencia Saucedo, Eddy Jeanpiere

Docente: Mg. Calderón Aquiño, Cinthia
