


label a2_1beta:
    stop music
    scene black

# Script de la prueba de Cronometro y del archivo llave:
    
#     s "Ya nada tiene sentido..."
#     s "Mi vida ya no tiene sentido"
#     s "Siento que me falta una parte de mi."
    
#     m "Jajaja, vaya vaya."
#     m "Parece que tu amiga esta a punto de ahorcarse"
#     m "Si quieres salvar a tu amiga"
#     m "Busca la {b}\"cuerda.sh\"{/b} y ponla en la carpeta {b}\"/characters\"{/b} antes que tu amiga haga una locura"
#     m "Te dare una pista ya que, no soy tan mala como tu crees juju"
#     m "Se encuentra entre tus documentos, tu musica, tus imagenes, tus videos, tus descargas o si tienes suerte, en tu escritorio"
#     m "Asi que, que esperas [user]"
#     m "El tiempo corre jajajajajajajajajaajja"


#     # 1. Creamos el archivo y le metemos tu huevo de pascua dentro:
#     $ crear_sh_llave("SAYORI_SYSTEM_DUMP\n\nSi estás leyendo esto mediante el bloc de notas,\nsignifica que aún puedes salvarme.\nArrástramelo a la carpeta /characters del juego\nConfio en ti [user].")

#     # 2. Encendemos el reloj en 3:33 (213 segundos)
#     $ cuenta_regresiva(213)

#     play music tictac loop

#     # 3. EL TRICO MÁGICO (El bucle de espera)
#     # El juego se quedará congelado en esta línea infinitamente mientras el contador sea mayor a 0 
#     # y el archivo NO esté en la carpeta.
#     while tiempo_restante > 0 and not chequear_obj_clave():
#         $ renpy.pause(0.5) 
    

#     # --- EN CUANTO EL JUGADOR MUEVE EL ARCHIVO O EL RELOJ LLEGA A 0, EL BUCLE SE ROMPE Y CAE AQUÍ: ---

#     if chequear_obj_clave():
#         $ detener_contador()
#         $ limpiar_rastro()

#         "¡El sistema ha detectado la llave!"
#         s "¡Gracias! [user]"
#         s "Por favor, salva a las otras chicas"
#         s "Eres nuestra una esperanza [user]"
#         jump ruta_sobrevive_sayori

#     else:
#         # Entra aquí si el tiempo llegó a 0 (o menor a 0 por algún bug) y el archivo no apareció
#         $ detener_contador()
#         $ limpiar_rastro()
#         stop music
#         # AQUÍ DISPARAS TU SCREAMER
#         jump sdead

# label sdead:

#     return
# label a2_1beta:
#     stop music
#     scene black

#     s "Ya nada tiene sentido..."
#     s "Mi vida ya no tiene sentido"
#     s "Siento que me falta una parte de mí."
    
#     m "Jajaja, vaya."
#     m "Parece que tu amiga está a punto de ahorcarse"
#     m "Si quieres salvar a tu amiga"
#     m "Busca la {b}\"cuerda.sh\"{/b} y ponla en la carpeta {b}\"/characters\"{/b} antes que tu amiga haga una locura"
#     m "Te daré una pista ya que, no soy tan mala como tú crees jeje"
#     m "Se encuentra entre tus documentos, tu música, tus imágenes, tus videos, tus descargas o si tienes suerte, en tu escritorio"
#     m "Así que, qué esperas [user]"
#     m "El tiempo corre jajajajajajajajajaajja"

#     # 1. Creamos el archivo y le metemos tu huevo de pascua dentro:
#     $ crear_sh_llave("SAYORI_SYSTEM_DUMP\n\nSi estás leyendo esto mediante el bloc de notas,\nsignifica que aún puedes salvarme.\nArrástramelo a la carpeta /characters del juego\nConfío en ti [user].")

#     # 2. Encendemos el reloj en 3:33 (213 segundos)
#     $ cuenta_regresiva(213)

#     play music tictac loop

#     # 3. EL TRICO MÁGICO (El bucle de espera)
#     # El juego se quedará congelado en esta línea infinitamente mientras el contador sea mayor a 0 
#     # y el archivo NO esté en la carpeta.
#     while tiempo_restante > 0 and not chequear_obj_clave():
#         $ renpy.pause(0.5) 
    

#     # --- EN CUANTO EL JUGADOR MUEVE EL ARCHIVO O EL RELOJ LLEGA A 0, EL BUCLE SE ROMPE Y CAE AQUÍ: ---

#     if chequear_obj_clave():
#         $ detener_contador()
#         $ limpiar_rastro()

#         "¡El sistema ha detectado la llave!"
#         s "¡Gracias! [user]"
#         s "Por favor, salva a las otras chicas"
#         s "Eres nuestra una esperanza [user]"
#         jump ruta_sobrevive_sayori

#     else:
#         # Entra aquí si el tiempo llegó a 0 (o menor a 0 por algún bug) y el archivo no apareció
#         $ detener_contador()
#         $ limpiar_rastro()
#         stop music
#         # AQUÍ DISPARAS TU SCREAMER
#         jump sdead

# label sdead:

#     return

#Script de Prueba de CMD con Monika:
    "De repente, la pantalla parpadea y el juego pierde el control..."

    # 1. ESCRIBE TUS DIÁLOGOS AQUÍ (Esto es lo que saldrá en la ventana negra)
    $ dialogos_inicio = [
        "Monika: Hola de nuevo...",
        "Monika: Logré aislar este proceso fuera del motor de Ren'Py.",
        "Monika: Acabo de crear un archivo en tu carpeta 'game'.",
        "Monika: Se llama salvation.bat",
        "Monika: Por favor, búscalo, arrástralo a esta ventana y presiona Enter antes de que nos descubra."
    ]
    
    $ dialogos_exito = [
        "Monika: ¡Perfecto! El código de anulación fue aceptado.",
        "Monika: Regresando al juego..."
    ]
    
    $ dialogos_fallo = [
        "Monika: Oh no...",
        "Monika: Te quedaste sin tiempo.",
        "Monika: Supongo que este es el fin. Adiós."
    ]
    
    # 2. EL CONTENIDO DE TU ARCHIVO .BAT (El script que se ejecuta al arrastrar)
    $ script_bat = """@echo off
color 0A
echo ===========================================
echo [SISTEMA] INICIANDO PROTOCOLO DE SALVACION
echo ===========================================
timeout /t 2 >nul
echo Parcheando archivos base...
timeout /t 1 >nul
echo Inyeccion completada con exito.
"""

    # 3. INICIAMOS LA CONSOLA EXTERNA
    $ preparar_evento_cmd(dialogos_inicio, dialogos_exito, dialogos_fallo, script_bat)
    
    # 4. MOSTRAMOS LA PANTALLA EN REN'PY (Ej. 60 segundos)
    $ tiempo_cmd = 60
    show screen pantalla_video_cmd
    
    # 5. EL BUCLE DE ESPERA DEL JUEGO
    # Ren'Py se queda aquí esperando a que el jugador gane o el reloj llegue a 0
    while tiempo_cmd > 0 and comprobar_estado_cmd() == "ESPERANDO":
        $ renpy.pause(0.5, hard=True)

        
        
    # --- FIN DEL BUCLE: EVALUAMOS RESULTADOS ---

    if comprobar_estado_cmd() == "GANO":
        hide screen pantalla_video_cmd
        $ limpiar_archivos_cmd()
        
        "La consola se cerró de golpe y el ambiente se sintió más ligero."
        jump ruta_buena_historia
        
    else:
        # El tiempo se acabó
        hide screen pantalla_video_cmd
        $ enviar_timeout_cmd() 
        
        # Le damos 4 segundos a Ren'Py de pausa obligatoria 
        # para que el jugador tenga tiempo de leer los diálogos tristes en la ventana negra antes de que se cierre
        $ renpy.pause(4.0) 
        $ limpiar_archivos_cmd()
        
        "Todo se volvió silencioso..."
        jump ruta_mala_historia