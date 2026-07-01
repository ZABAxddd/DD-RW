label debug:

    stop music fadeout 1.0
    scene bg club_day2 with dissolve_scene_full

    show monika 1a zorder 2 at t11

    call bucle
    
    return


label bucle:

    menu:

        m "Que funcion deberiamos comenzar a probar"
        

        "Prueba de poema.txt":
            call prueba_poematxt

        "Cambiar fondo de pantalla":

            m "Cambiando...{w=3}{nw}"
            $ hellopc()

            menu:
                m "Deseas cambiar el fondo de pantalla por defecto?"
                "si":
                    $ restorepc()
                    return

                "no":
                    return

            jump bucle
        
        "Llenar el escritorio de iconos":

            m "Añadiendo...{w=3}{nw}"
            $ destroydesktop()

            menu:
                m "¿Borramos los iconos?"
                "si":
                    $ goodbyeicons()
                    return
                "no": 
                    return
            jump bucle
        "Mover ventana del juego con el Mouse":
            call cursortest

        "Salir":
            return


    return 
# Explicacion de uso:
    # $ hellopc() : Permite cambiar el fondo de pantalla del dispositivo
    # $ restorepc() : Permite restaurar el fondo de pantalla del dispositivo al que tenia por defecto#



label prueba_poematxt:
    
    m "Es hora de que escribas un poema para mí."
    
    $ crear_txt_desktop()
    
    
    m "Acabo de dejar un archivo en tu escritorio con instrucciones."
    m "Pero recuerda mover 'poema.txt' justo por...{w=3}{nw}"
    $ opengamebase()
    m "Aqui, en mi carpeta raiz"
    m "Sigue las instrucciones que debes seguir"
    m "Te estare esperando"

label esperar_poema:
    m "¿Ya está listo el poema en la carpeta del juego?"
    
    menu:
        "Sí, ya lo escribí.":
            # La función evalúa y salta automáticamente a los labels de abajo
            $ checar_poema() 
        "Aún no.":
            m "Te estaré esperando."
            jump esperar_poema


label label_no_existe:
    m "no esta y poema en la carpeta"
    m "Revisa bien"
    jump esperar_poema

label label_en_blanco:
    m "el poema esta en blanco, escribe tu poema tonto"
    jump esperar_poema

label label_falta_argumento:
    m "falta argumentar mas"
    jump esperar_poema

label label_sin_monika:
    m "esta mal tu poema, no estoy incluida"
    jump esperar_poema

label label_poema_perfecto:
    m "¡Oh, es un poema perfecto!"
    m "Me encanta."
    return


######################################################

label cursortest:

    m "La ventana está normal en el centro."
    
    $ windows_follow_cursor()
    
    m "Ahora la ventana se ha pegado a tu cursor y lo seguirá por todo el escritorio."
    m "¡Intenta escapar!"
    
    $ windows_unfollow_cursor()
    
    "La ventana se ha soltado y vuelve a comportarse de forma normal."