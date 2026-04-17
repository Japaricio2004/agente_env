"""
main.py — Ejecuta tu agente en el Grid World.

Uso:
    python main.py

Configuración:
    Modifica las variables de abajo para cambiar el mapa.
"""

from entorno import GridWorld
from mi_agente import MiAgente

# ── Configuración del mapa ───────────────────────
FILAS     = 8        # Alto del mapa (ejemplo: 8)
COLUMNAS  = 12       # Ancho del mapa (ejemplo: 12)
SEMILLA   = 123      # Cambia la semilla para otro mapa
PAREDES   = 0.25     # Porcentaje de paredes (0.0 a 0.40)
VELOCIDAD = 0.10     # Segundos entre pasos (más bajo = más rápido)
MAX_PASOS = 60       # Máximo de pasos antes de rendirse
# ─────────────────────────────────────────────────

# Crear el mundo
mundo = GridWorld(
    filas=FILAS,
    columnas=COLUMNAS,
    semilla=SEMILLA,
    porcentaje_paredes=PAREDES,
)

# Mostrar mapa en consola
mundo.mostrar_mapa()

# Crear tu agente
agente = MiAgente()

# Ejecutar con animación
resultado = mundo.animar(agente, max_pasos=MAX_PASOS, velocidad=VELOCIDAD)
print(f"\nResultado: {resultado}")