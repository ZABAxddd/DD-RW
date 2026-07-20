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



# --- CÓDIGO CORREGIDO PARA REN'PY 8.3.4+ ---
init python:
    renpy.register_shader("custom.sombra_gradiente", variables="""
        varying vec2 v_tex_coord;
    """, fragment_300="""
        // fragment_300 se ejecuta DESPUÉS de que Ren'Py cargó el sprite en pantalla
        // v_tex_coord.y va de 0.0 (arriba, la cabeza) a 1.0 (abajo, el torso)
        float gradiente = mix(0.10, 0.65, v_tex_coord.y);
        
        // Multiplicamos los colores de la imagen por el degradado
        gl_FragColor.rgb *= gradiente;
    """)

# Tu transform limpio, exactamente como querías usarlo
transform shadow:
    shader "custom.sombra_gradiente"


# --- FILTRO CRT RETRO CORREGIDO (Sin cajas negras) ---
init python:
    renpy.register_shader("custom.crt_retro", variables="""
        varying vec2 v_tex_coord;
        uniform sampler2D tex0;
    """, fragment_300="""
        // 1. Curvatura de pantalla
        vec2 cc = v_tex_coord - 0.5;
        float dist = dot(cc, cc);
        vec2 uv = v_tex_coord + cc * dist * 0.08; 
        
        // Si sale de los límites de la imagen, devuelve transparente, NO negro.
        if (uv.x < 0.0 || uv.x > 1.0 || uv.y < 0.0 || uv.y > 1.0) {
            gl_FragColor = vec4(0.0);
        } else {
            
            // 2. Efecto Croma
            float separacion = 0.003; 
            float r = texture2D(tex0, uv - vec2(separacion, 0.0)).r;
            float g = texture2D(tex0, uv).g;
            float b = texture2D(tex0, uv + vec2(separacion, 0.0)).b;
            
            // EXTRAEMOS LA TRANSPARENCIA ORIGINAL
            float a = texture2D(tex0, uv).a;
            
            // 3. Viñeta
            float vignette = uv.x * uv.y * (1.0 - uv.x) * (1.0 - uv.y);
            vignette = clamp(pow(16.0 * vignette, 0.35), 0.0, 1.0); 
            
            // Aplicamos los colores multiplicados por la viñeta y restauramos el Alpha original
            gl_FragColor = vec4(r * vignette, g * vignette, b * vignette, a);
        }
    """)