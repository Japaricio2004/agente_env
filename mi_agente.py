"""
mi_agente.py — Aquí defines tu agente.
╔══════════════════════════════════════════════╗
║  ✏️  EDITA ESTE ARCHIVO                      ║
╚══════════════════════════════════════════════╝

Tu agente debe:
    1. Heredar de la clase Agente
    2. Implementar el método decidir(percepcion)
    3. Retornar: 'arriba', 'abajo', 'izquierda' o 'derecha'

Lo que recibes en 'percepcion':
───────────────────────────────
percepcion = {
    'posicion':       (3, 5),          # Tu fila y columna actual
    'arriba':         'libre',         # Qué hay arriba
    'abajo':          'pared',         # Qué hay abajo
    'izquierda':      'libre',         # Qué hay a la izquierda
    'derecha':        None,            # None = fuera del mapa

    # OPCIONAL — brújula hacia la meta.
    # No es percepción real del entorno, es información global.
    # Usarla hace el ejercicio más fácil. No usarla es más realista.
    'direccion_meta': ('abajo', 'derecha'),
}

Valores posibles de cada dirección:
    'libre'  → puedes moverte ahí
    'pared'  → bloqueado
    'meta'   → ¡la meta! ve hacia allá
    None     → borde del mapa, no puedes ir

Si tu agente retorna un movimiento inválido (hacia pared o
fuera del mapa), simplemente se queda en su lugar.
"""

from entorno import Agente
import random


class MiAgente(Agente):

    def __init__(self):
        super().__init__(nombre="Mi Agente")
        self.visitadas = set()
        self.ultima_pos = None

    def al_iniciar(self):
        self.visitadas.clear()
        self.ultima_pos = None

    def decidir(self, percepcion):

        movimientos = self.ACCIONES
        pos_actual = percepcion["posicion"]

        self.visitadas.add(pos_actual)

        direccion_vertical, direccion_horizontal = percepcion.get(
            'direccion_meta', (None, None)
        )

        # 1. META inmediata
        for mov in movimientos:
            if percepcion[mov] == 'meta':
                return mov

        mejor_mov = None
        mejor_utilidad = float("-inf")

        for mov in movimientos:

            if percepcion[mov] != 'libre':
                continue

            utilidad = 0

            # acercarse a la meta
            if mov == direccion_vertical:
                utilidad += 5
            if mov == direccion_horizontal:
                utilidad += 5

            # costo de movimiento
            utilidad -= 1

            # calcular nueva posición
            fila, col = pos_actual
            

            if mov == "arriba":
                nueva_pos = (fila - 1, col)
            elif mov == "abajo":
                nueva_pos = (fila + 1, col)
            elif mov == "izquierda":
                nueva_pos = (fila, col - 1)
            elif mov == "derecha":
                nueva_pos = (fila, col + 1)

            # evitar loops (pero no exagerado)
            if nueva_pos in self.visitadas:
                utilidad -= 2

            # evitar retroceder inmediato
            if nueva_pos == self.ultima_pos:
                utilidad -= 3

            if utilidad > mejor_utilidad:
                mejor_utilidad = utilidad
                mejor_mov = mov

        # guardar última posición
        self.ultima_pos = pos_actual

        if mejor_mov:
            return mejor_mov

        # fallback anti-bloqueo
        libres = [m for m in movimientos if percepcion[m] == 'libre']
        if libres:
            return random.choice(libres)

        return 'abajo'