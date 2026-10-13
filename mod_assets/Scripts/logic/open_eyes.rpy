# ---------------------------------------------------------------------------
# open_eyes.rpy  -  Transición "abrir los ojos" para Ren'Py 8.x
#
# Uso (copia este archivo dentro de la carpeta game/ de tu proyecto):
#
#     scene bg club_festival with open_eyes          # velocidad normal (~4.5 s)
#     scene bg club_festival with open_eyes(1.5)     # 1.5x más rápido
#     scene bg club_festival with open_eyes(0.7)     # más lento
#
# Qué hace:
#   - Empieza en negro (ojos cerrados).
#   - Los párpados se abren de a poco, con bordes suaves.
#   - Parpadea dos veces (uno completo y uno a medias) mientras "despierta".
#   - La imagen empieza muy desenfocada, brillante y desaturada, y se va
#     enfocando poco a poco con un leve zoom hacia atrás.
#
# No necesita imágenes externas: los párpados se generan por código.
# Usa blur y matrixcolor, así que requiere el renderizador GL (el normal).
# ---------------------------------------------------------------------------

init -1 python:

    # --- Medidas de los párpados (se adaptan a la resolución del juego) -----
    EO_W = config.screen_width
    EO_H = config.screen_height
    EO_STEPS = 24                                   # franjas del borde suave
    EO_STEP = max(1, int(EO_H * 0.09) // EO_STEPS)  # alto de cada franja (px)
    EO_SOFT = EO_STEP * EO_STEPS                    # alto total del borde suave

    EO_TOP_ANCHOR = EO_H / float(EO_H + EO_SOFT)    # ancla = borde del párpado superior
    EO_BOT_ANCHOR = EO_SOFT / float(EO_H + EO_SOFT) # ancla = borde del párpado inferior

    EO_CLOSED = -0.01                               # ojos cerrados (los párpados se solapan)
    EO_OPEN = 0.5 + EO_SOFT / float(EO_H)           # ojos abiertos (párpados fuera de pantalla)

    def eo_make_lid(top):
        """Crea un párpado negro con el borde difuminado (superior o inferior)."""
        parts = []

        if top:
            # Bloque sólido arriba, franjas que se desvanecen hacia abajo.
            parts.append(Solid("#000", xsize=EO_W, ysize=EO_H))
            for i in range(EO_STEPS):
                t = (i + 0.5) / EO_STEPS
                a = 1.0 - t * t * (3.0 - 2.0 * t)
                color = "#000000%02x" % int(a * 255)
                parts.append(Transform(Solid(color, xsize=EO_W, ysize=EO_STEP), ypos=EO_H + i * EO_STEP))
        else:
            # Franjas que se desvanecen hacia arriba, bloque sólido abajo.
            for i in range(EO_STEPS):
                t = (i + 0.5) / EO_STEPS
                a = t * t * (3.0 - 2.0 * t)
                color = "#000000%02x" % int(a * 255)
                parts.append(Transform(Solid(color, xsize=EO_W, ysize=EO_STEP), ypos=i * EO_STEP))
            parts.append(Transform(Solid("#000", xsize=EO_W, ysize=EO_H), ypos=EO_SOFT))

        return Fixed(*parts, xsize=EO_W, ysize=EO_H + EO_SOFT)

    def eo_y(side, g):
        """Posición vertical (fracción de pantalla) del borde de cada párpado.
        side 0 = superior, side 1 = inferior. g = apertura (0 = cerrado)."""
        if side == 0:
            return 0.5 - g
        return 0.5 + g

    def eo_color(brightness, saturation):
        """Brillo + saturación para el efecto de ojos recién abiertos."""
        return BrightnessMatrix(brightness) * SaturationMatrix(saturation)

define eo_lid_top = eo_make_lid(True)
define eo_lid_bottom = eo_make_lid(False)


# ---------------------------------------------------------------------------
# La transición. "speed" > 1 la acelera, "speed" < 1 la hace más lenta.
# Duración base: 4.5 segundos.
# ---------------------------------------------------------------------------
transform open_eyes(speed=1.0, *, new_widget=None, old_widget=None):

    delay (4.5 / speed)

    # Fondo negro (lo que se ve detrás de los bordes desenfocados).
    contains:
        Solid("#000")

    # La escena nueva, desenfocada y brillante que se va enfocando.
    contains:
        new_widget
        align (0.5, 0.5)
        zoom 1.06
        blur 30.0
        matrixcolor eo_color(0.4, 0.55)

        parallel:
            ease (4.4 / speed) zoom 1.0

        parallel:
            ease (4.4 / speed) matrixcolor eo_color(0.0, 1.0)

        parallel:
            pause (0.6 / speed)
            ease (1.0 / speed) blur 22.0
            linear (0.3 / speed) blur 20.0
            ease (0.25 / speed) blur 24.0      # parpadeo: se desenfoca un poco
            pause (0.15 / speed)
            ease (0.8 / speed) blur 12.0
            ease (0.2 / speed) blur 14.0       # medio parpadeo
            ease (1.1 / speed) blur 0.0

    # Párpado superior.
    contains:
        eo_lid_top
        anchor (0.0, EO_TOP_ANCHOR)
        ypos eo_y(0, EO_CLOSED)
        pause (0.6 / speed)
        ease (1.0 / speed) ypos eo_y(0, 0.06)       # primera rendija
        linear (0.3 / speed) ypos eo_y(0, 0.07)
        ease (0.25 / speed) ypos eo_y(0, EO_CLOSED) # parpadeo completo
        pause (0.15 / speed)
        ease (0.8 / speed) ypos eo_y(0, 0.22)       # se abre más
        ease (0.2 / speed) ypos eo_y(0, 0.12)       # medio parpadeo
        ease (1.1 / speed) ypos eo_y(0, EO_OPEN)    # ojos totalmente abiertos

    # Párpado inferior (mismo movimiento, en espejo).
    contains:
        eo_lid_bottom
        anchor (0.0, EO_BOT_ANCHOR)
        ypos eo_y(1, EO_CLOSED)
        pause (0.6 / speed)
        ease (1.0 / speed) ypos eo_y(1, 0.06)
        linear (0.3 / speed) ypos eo_y(1, 0.07)
        ease (0.25 / speed) ypos eo_y(1, EO_CLOSED)
        pause (0.15 / speed)
        ease (0.8 / speed) ypos eo_y(1, 0.22)
        ease (0.2 / speed) ypos eo_y(1, 0.12)
        ease (1.1 / speed) ypos eo_y(1, EO_OPEN)
