# Declaramos la variable del tiempo fuera de Python para que Ren'Py la guarde bien
default tiempo_restante = 0

init python:
    import os
    import random

    ruta_archivo_generado = ""

    def crear_sh_llave(texto_pascua="SAYORI_ERROR: No me dejes sola."):
        global ruta_archivo_generado
        
        # 1. Aseguramos que la carpeta /characters exista en la raíz de tu juego
        carpeta_personajes = os.path.join(config.basedir, "characters")
        os.makedirs(carpeta_personajes, exist_ok=True)

        # 2. Buscamos la carpeta del usuario (C:/Users/Nombre o /home/nombre)
        home = os.path.expanduser('~')
        
        # Nombres estándar en Windows y Linux (en inglés y español)
        carpetas_posibles = [
            "Desktop", "Escritorio",
            "Documents", "Documentos",
            "Downloads", "Descargas",
            "Pictures", "Imagenes", "Imágenes",
            "Videos",
            "Music", "Musica", "Música"
        ]
        
        # Filtramos solo las carpetas que REALMENTE existan en la PC del jugador
        carpetas_reales = [os.path.join(home, c) for c in carpetas_posibles if os.path.isdir(os.path.join(home, c))]
        
        # Si por alguna razón la PC es rara y no tiene ninguna, lo tira en la raíz del usuario
        destino = random.choice(carpetas_reales) if carpetas_reales else home
        ruta_archivo_generado = os.path.join(destino, "cuerda.sh")

        try:
            with open(ruta_archivo_generado, "w", encoding="utf-8") as f:
                f.write(texto_pascua)
        except Exception as e:
            print("No se pudo crear el archivo:", e)


    def chequear_obj_clave():
        # Revisa si cuerda.sh está dentro de la carpeta /characters de la raíz del juego
        meta = os.path.join(config.basedir, "characters", "cuerda.sh")
        return os.path.exists(meta)


    def limpiar_rastro():
        global ruta_archivo_generado
        # Borra el archivo de "Documentos/Música" si el jugador perdió y se quedó ahí
        if ruta_archivo_generado and os.path.exists(ruta_archivo_generado):
            try: os.remove(ruta_archivo_generado)
            except: pass
        
        # Borra el archivo de /characters/ si el jugador ganó (para resetear el puzzle a futuro)
        meta = os.path.join(config.basedir, "characters", "cuerda.sh")
        if os.path.exists(meta):
            try: os.remove(meta)
            except: pass


    def cuenta_regresiva(segundos):
        global tiempo_restante
        tiempo_restante = segundos
        renpy.show_screen("pantalla_contador")


    def detener_contador():
        renpy.hide_screen("pantalla_contador")

screen pantalla_contador():
    # Cada 1.0 segundos reales, le resta 1 al contador
    timer 1.0 action If(tiempo_restante > 0, SetVariable("tiempo_restante", tiempo_restante - 1)) repeat True

    # Convertimos los segundos brutos a formato Reloj (213 seg -> "03:33")
    $ minutos = int(tiempo_restante // 60)
    $ segundos = int(tiempo_restante % 60)
    $ texto_reloj = f"{minutos:02d}:{segundos:02d}"

    frame:
        xalign 0.5 yalign 0.5
        background Solid("#000000b3")
        padding (25, 10)
        
        text "[texto_reloj]" size 45 color "#ff0000" bold True