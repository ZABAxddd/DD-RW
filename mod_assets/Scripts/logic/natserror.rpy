init python:
    import os
    import shutil
    import random

    # Defino los archivos requeridos y la variable global para rastrear las rutas generadas.
    archivos_natsuki = ["cupcake.png", "manga.png", "spider.png", "beach.png"]
    rutas_creadas = []

    def obtener_carpetas_sistema():
        # Extraigo el directorio principal del usuario operativo.
        ruta_base = os.path.expanduser('~')
        directorios_posibles = ["Documents", "Videos", "Pictures", "Downloads", "Music", "Desktop"]
        carpetas_validas = []
        
        # Filtro las carpetas reales existentes en el sistema operativo actual.
        for dir_nombre in directorios_posibles:
            ruta_completa = os.path.join(ruta_base, dir_nombre)
            if os.path.exists(ruta_completa):
                carpetas_validas.append(ruta_completa)
                
        return carpetas_validas

    def despedazar_natsuki():
        global rutas_creadas
        rutas_creadas = []
        
        carpetas_disp = obtener_carpetas_sistema()
        # Barajo los directorios para garantizar una distribución impredecible.
        random.shuffle(carpetas_disp)
        
        dir_origen = os.path.join(config.gamedir, "mod_assets", "sprites")
        
        # Asigno cada archivo a una carpeta diferente del sistema mediante iteración directa.
        for index, archivo in enumerate(archivos_natsuki):
            ruta_destino = os.path.join(carpetas_disp[index], archivo)
            ruta_origen = os.path.join(dir_origen, archivo)
            
            if os.path.exists(ruta_origen):
                shutil.copy(ruta_origen, ruta_destino)
                rutas_creadas.append(ruta_destino)

    def verificar_archivos_natsuki():
        # Escaneo el directorio characters en la raíz del juego para comprobar el progreso.
        dir_characters = os.path.join(config.basedir, "characters")
        faltantes = []
        
        for archivo in archivos_natsuki:
            ruta_char = os.path.join(dir_characters, archivo)
            if not os.path.exists(ruta_char):
                faltantes.append(archivo)
                
        return faltantes

    def limpiar_archivos_natsuki():
        # Ejecuto una purga de los archivos en las rutas temporales del sistema.
        for ruta in rutas_creadas:
            if os.path.exists(ruta):
                try:
                    os.remove(ruta)
                except Exception:
                    pass
        
        # Ejecuto una purga en la carpeta characters para reiniciar el entorno para futuras ejecuciones.
        dir_characters = os.path.join(config.basedir, "characters")
        for archivo in archivos_natsuki:
            ruta_char = os.path.join(dir_characters, archivo)
            if os.path.exists(ruta_char):
                try:
                    os.remove(ruta_char)
                except Exception:
                    pass

# Configuro la interfaz del cronómetro y el rastreador de archivos.
screen pantalla_rescate_natsuki():

    use gestor_audio_cronometro(tiempo_natsuki)

    $ minutos = tiempo_natsuki // 60
    $ segundos = tiempo_natsuki % 60
    $ tiempo_formateado = "{:02d}:{:02d}".format(minutos, segundos)
    
    # Invoco la validación en tiempo real para actualizar la interfaz.
    $ archivos_faltantes = verificar_archivos_natsuki()
    
    # Proceso el decremento de tiempo y la validación de victoria/derrota simultáneamente.
    timer 1.0 action If(tiempo_natsuki > 0 and len(archivos_faltantes) > 0, true=SetVariable("tiempo_natsuki", tiempo_natsuki - 1), false=If(len(archivos_faltantes) == 0, true=Return("exito"), false=Return("tiempo_agotado"))) repeat True
    
    vbox:
        align (0.5, 0.1)
        text "[tiempo_formateado]" size 45 color "#ff0000" bold True xalign 0.5
        
    vbox:
        align (0.5, 0.4)
        spacing 15
        text "¡Devuelve las partes de Natsuki a la carpeta {b}characters{/b}!" size 30 color "#ffffff" outlines [(2, "#000", 0, 0)] xalign 0.5
        
        # Despliego dinámicamente el nombre de los archivos que aún no han sido recuperados.
        for archivo in archivos_faltantes:
            text "[archivo]" size 28 color "#ff5555" outlines [(1, "#000", 0, 0)] xalign 0.5

