# --- 1. DEFINICIÓN DE LA ESTÁTICA ANIMADA ---
# Intercalamos las 4 imágenes rápidamente (cada 0.05 segundos) para simular el ruido.
image estatica_tv:
    "bg/noise1.jpg"
    0.05
    "bg/noise2.jpg"
    0.05
    "bg/noise3.jpg"
    0.05
    "bg/noise4.jpg"
    0.05
    repeat

# --- 2. DEFINICIÓN DEL TRANSFORM ATL ---
# Este bloque se encarga de realizar la transición suave usando linear y alpha.
transform transicion_estatica(opacidad_objetivo, tiempo_transicion):
    linear tiempo_transicion alpha opacidad_objetivo

# --- 3. FUNCIONES DE PYTHON ---
# Funciones para llamar el efecto fácilmente.
init python:
    def mostrar_estatica(opacidad=0.5, tiempo=1.0):
        # Muestra la estática animada en la capa 100
        renpy.show("estatica_tv", at_list=[transicion_estatica(opacidad, tiempo)], zorder=100)

    def ocultar_estatica(tiempo=1.0):
        # Interpola el alpha hasta 0.0
        renpy.show("estatica_tv", at_list=[transicion_estatica(0.0, tiempo)], zorder=100)


#######


transform zoom_cara_sayori(zoom_level=2.0, tiempo=1.0):
    # Anchor (0.5, 0.22) es la coordenada exacta de la cara en tu imagen.
    # Align (0.5, 0.5) asegura que esa coordenada esté en el centro de la pantalla.
    anchor (0.5, 0.22)
    align (0.5, 0.5)
    yoffset 250
    linear tiempo zoom zoom_level

# Transform para volver a la posición normal
transform reset_sayori(tiempo=0.5):
    linear tiempo zoom 1.0 anchor (0.5, 1.0) align (0.5, 1.0)