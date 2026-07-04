


label debug:
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
    # 
    # $ cuenta_regresiva(213)


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
#     "De repente, la pantalla parpadea y el juego pierde el control..."

#     # 1. ESCRIBE TUS DIÁLOGOS AQUÍ (Esto es lo que saldrá en la ventana negra)
#     $ dialogos_inicio = [
#         "Monika: Hola de nuevo...",
#         "Monika: Logré aislar este proceso fuera del motor de Ren'Py.",
#         "Monika: Acabo de crear un archivo en tu carpeta 'game'.",
#         "Monika: Se llama salvation.bat",
#         "Monika: Por favor, búscalo, arrástralo a esta ventana y presiona Enter antes de que nos descubra."
#     ]
    
#     $ dialogos_exito = [
#         "Monika: ¡Perfecto! El código de anulación fue aceptado.",
#         "Monika: Regresando al juego..."
#     ]
    
#     $ dialogos_fallo = [
#         "Monika: Oh no...",
#         "Monika: Te quedaste sin tiempo.",
#         "Monika: Supongo que este es el fin. Adiós."
#     ]
    
#     # 2. EL CONTENIDO DE TU ARCHIVO .BAT (El script que se ejecuta al arrastrar)
#     $ script_bat = """@echo off
# color 0A
# echo ===========================================
# echo [SISTEMA] INICIANDO PROTOCOLO DE SALVACION
# echo ===========================================
# timeout /t 2 >nul
# echo Parcheando archivos base...
# timeout /t 1 >nul
# echo Inyeccion completada con exito.
# """

#     # 3. INICIAMOS LA CONSOLA EXTERNA
#     $ preparar_evento_cmd(dialogos_inicio, dialogos_exito, dialogos_fallo, script_bat)
    
#     # 4. MOSTRAMOS LA PANTALLA EN REN'PY (Ej. 60 segundos)
    # $ tiempo_cmd = 60
    # 
    # show screen pantalla_video_cmd
    
#     # 5. EL BUCLE DE ESPERA DEL JUEGO
#     # Ren'Py se queda aquí esperando a que el jugador gane o el reloj llegue a 0
#     while tiempo_cmd > 0 and comprobar_estado_cmd() == "ESPERANDO":
#         $ renpy.pause(0.5, hard=True)

        
        
#     # --- FIN DEL BUCLE: EVALUAMOS RESULTADOS ---

#     if comprobar_estado_cmd() == "GANO":
#         hide screen pantalla_video_cmd
#         $ limpiar_archivos_cmd()
        
#         "La consola se cerró de golpe y el ambiente se sintió más ligero."
#         jump ruta_buena_historia
        
#     else:
#         # El tiempo se acabó
#         hide screen pantalla_video_cmd
#         $ enviar_timeout_cmd() 
        
#         # Le damos 4 segundos a Ren'Py de pausa obligatoria 
#         # para que el jugador tenga tiempo de leer los diálogos tristes en la ventana negra antes de que se cierre
#         $ renpy.pause(4.0) 
#         $ limpiar_archivos_cmd()
        
#         "Todo se volvió silencioso..."
#         jump ruta_mala_historia

# ### Script de cambio del fondo de pantalla y otras cosas mas:


#     stop music fadeout 1.0
#     scene bg club_day2 with dissolve_scene_full

#     show monika 1a zorder 2 at t11

#     call bucle
    
#     return


# label bucle:

#     menu:

#         m "Que funcion deberiamos comenzar a probar"
        

#         "Prueba de poema.txt":
#             call prueba_poematxt

#         "Cambiar fondo de pantalla":

#             m "Cambiando...{w=3}{nw}"
#             $ hellopc()

#             menu:
#                 m "Deseas cambiar el fondo de pantalla por defecto?"
#                 "si":
#                     $ restorepc()
#                     return

#                 "no":
#                     return

#             jump bucle
        
#         "Llenar el escritorio de iconos":

#             m "Añadiendo...{w=3}{nw}"
#             $ destroydesktop()

#             menu:
#                 m "¿Borramos los iconos?"
#                 "si":
#                     $ goodbyeicons()
#                     return
#                 "no": 
#                     return
#             jump bucle
#         "Mover ventana del juego con el Mouse":
#             call cursortest

#         "Salir":
#             return


#     return 
# # Explicacion de uso:
#     # $ hellopc() : Permite cambiar el fondo de pantalla del dispositivo
#     # $ restorepc() : Permite restaurar el fondo de pantalla del dispositivo al que tenia por defecto#



# label prueba_poematxt:
    
#     m "Es hora de que escribas un poema para mí."
    
#     $ crear_txt_desktop()
    
    
#     m "Acabo de dejar un archivo en tu escritorio con instrucciones."
#     m "Pero recuerda mover 'poema.txt' justo por...{w=3}{nw}"
#     $ opengamebase()
#     m "Aqui, en mi carpeta raiz"
#     m "Sigue las instrucciones que debes seguir"
#     m "Te estare esperando"

# label esperar_poema:
#     m "¿Ya está listo el poema en la carpeta del juego?"
    
#     menu:
#         "Sí, ya lo escribí.":
#             # La función evalúa y salta automáticamente a los labels de abajo
#             $ checar_poema() 
#         "Aún no.":
#             m "Te estaré esperando."
#             jump esperar_poema


# label label_no_existe:
#     m "no esta y poema en la carpeta"
#     m "Revisa bien"
#     jump esperar_poema

# label label_en_blanco:
#     m "el poema esta en blanco, escribe tu poema tonto"
#     jump esperar_poema

# label label_falta_argumento:
#     m "falta argumentar mas"
#     jump esperar_poema

# label label_sin_monika:
#     m "esta mal tu poema, no estoy incluida"
#     jump esperar_poema

# label label_poema_perfecto:
#     m "¡Oh, es un poema perfecto!"
#     m "Me encanta."
#     return


# ######################################################

# label cursortest:

#     m "La ventana está normal en el centro."
    
#     $ windows_follow_cursor()
    
#     m "Ahora la ventana se ha pegado a tu cursor y lo seguirá por todo el escritorio."
#     m "¡Intenta escapar!"
    
#     $ windows_unfollow_cursor()
    
#     "La ventana se ha soltado y vuelve a comportarse de forma normal."


# Script de Prueba para poner claves de a la etapa de Yuri:

#     mc "¡Yuri, por favor detente! ¡No lo hagas!"
#     # $ tiempo_yuri = 213
#     $ tiempo_yuri = 50
    
#     $ autolesiones()
#     return

# label ruta_buena_yuri:

#     jump a2_2beta
#     return

# label ruta_mala_yuri:
#     "Me quedé paralizado, sin saber qué hacer..."
#     "El tiempo se agotó."
#     "(Ruta Mala: Yuri no sobrevivió)"
#     return


# label a2_2beta:
#     "Escribí rápidamente la palabra de aquel manual extraño..."
#     "Yuri se detiene abruptamente, soltando el cuchillo."
#     y "Oh [player] muchas gracias por salvarme"

# #### Script del evento con Natsuki y su desvanecimiento:

    # 
    # $ tiempo_natsuki = 120
    # $ despedazar_natsuki()
    
#     call screen pantalla_rescate_natsuki
    
#     if _return == "exito":
#         $ limpiar_archivos_natsuki()
#         jump ruta_buena_natsuki
#     elif _return == "tiempo_agotado":
#         $ limpiar_archivos_natsuki()
#         jump ruta_mala_natsuki

# label ruta_buena_natsuki:
#     "El código del juego se estabiliza..."
#     "Natsuki abre los ojos de golpe, respirando agitadamente."
#     "¡Conseguiste todas las partes a tiempo!"
#     return

# label ruta_mala_natsuki:
#     # Reproduzco el impacto visual de terror al fallar la ventana de tiempo.
#     # play sound "scream.ogg"
#     # show natsuki_screamer at center
#     "El tiempo se detuvo."
#     "Los archivos de Natsuki fueron eliminados del sistema permanentemente."
#     return

# ### Prueba de crear un txt
#     "..."
#     $ creartxt("escritorio", "Mira_mama_soy_un_txt.txt", """para entender la cronologia de doki doki literature club, hay que enter que no es un juego
#     sino tambien por lo que representa su comunidad.

#     ¿Terror?

#     si

#     pero tambien... una familia feliz

#     """)


#     m "Mira tu escritorio [user]"
#     m "Que te parece"

#     menu:
#         "Ta Bonito":
#             pass

#     m "jujuju"


return