# Defino las variables base necesarias para el flujo del evento.
default tiempo_yuri = 213
default entrada_jugador = ""
default estado_minijuego = "normal" 

# Aplico una oscilación horizontal para enfatizar el error de entrada.
transform shake_error:
    xoffset 0
    linear 0.05 xoffset -15
    linear 0.05 xoffset 15
    linear 0.05 xoffset -15
    linear 0.05 xoffset 15
    linear 0.05 xoffset 0

# Defino un efecto de pulso dinámico que expande ligeramente el elemento antes de colapsarlo y desvanecerlo.
transform pulsar_exito:
    parallel:
        easeout 0.2 zoom 1.1
        easein 0.3 zoom 0.0
    parallel:
        ease 0.5 alpha 0.0

init python:
    # Valido la contraseña introducida normalizando la cadena para asegurar precisión.
    def checar_clave_yuri(clave):
        if clave.strip().lower() == "pandemonium":
            return True
        else:
            return False

    # Establezco el punto de entrada para invocar la interfaz desde el script principal.
    def autolesiones():
        renpy.call("evento_autolesiones_label")

screen pantalla_clave_yuri():
    # Calculo el formato temporal para representar el tiempo en estructura legible.
    $ minutos = tiempo_yuri // 60
    $ segundos = tiempo_yuri % 60
    $ tiempo_formateado = "{:02d}:{:02d}".format(minutos, segundos)

    # Asigno colores de estado según la resolución del evento.
    $ color_cronometro = "#ff0000" if estado_minijuego != "exito" else "#00ff00"
    $ color_general = "#ffffff" if estado_minijuego == "normal" else ("#ff0000" if estado_minijuego == "error" else "#00ff00")


    # Restauro el estado tras el error para habilitar nuevos intentos limpios.
    if estado_minijuego == "error":
        timer 0.5 action [SetVariable("estado_minijuego", "normal"), SetVariable("entrada_jugador", "")]

    # Gestiono el decremento cíclico del temporizador.
    timer 1.0 action If(tiempo_yuri > 0 and estado_minijuego != "exito", true=SetVariable("tiempo_yuri", tiempo_yuri - 1), false=If(tiempo_yuri <= 0, true=Return("tiempo_agotado"))) repeat True

    vbox:
        if estado_minijuego == "error":
            at shake_error
        elif estado_minijuego == "exito":
            at pulsar_exito

        align (0.5, 0.1)
        text "Tiempo restante: [tiempo_formateado]" size 50 color color_cronometro outlines [(2, "#000", 0, 0)] xalign 0.5

    vbox:
        if estado_minijuego == "error":
            at shake_error
        elif estado_minijuego == "exito":
            at pulsar_exito

        align (0.5, 0.8)
        spacing 15
        text "Encuentra la clave para detenerla:" size 30 xalign 0.5 color color_general outlines [(2, "#000", 0, 0)]
        
        # Proceso la entrada de texto y el botón de confirmación.
        if estado_minijuego != "exito":
            input id "clave_input" value VariableInputValue("entrada_jugador") length 20 size 40 color color_general xalign 0.5
            textbutton "Confirmar" action Return(entrada_jugador) xalign 0.5
            key "K_RETURN" action Return(entrada_jugador)

        else:
            text "[entrada_jugador]" size 40 color color_general xalign 0.5

label evento_autolesiones_label:
    $ tiempo_yuri = 213 
    $ entrada_jugador = "" 
    $ estado_minijuego = "normal" 

label bucle_ingreso_yuri:
    call screen pantalla_clave_yuri
    
    # Evalúo la condición de fallo crítico.
    if _return == "tiempo_agotado":
        hide screen pantalla_clave_yuri
        jump ruta_mala_yuri
        
    $ resultado = checar_clave_yuri(_return)
    
    if resultado == True:
        $ estado_minijuego = "exito"
        
        # Mantengo la pantalla activa para renderizar la animación de salida.
        show screen pantalla_clave_yuri 
        pause 0.5 
        
        hide screen pantalla_clave_yuri
        jump ruta_buena_yuri
    else:
        $ estado_minijuego = "error"
        $ tiempo_yuri -= 20
        
        if tiempo_yuri <= 0:
            jump ruta_mala_yuri
        else:
            jump bucle_ingreso_yuri

label ruta_buena_yuri:

    jump a2_2beta
    return

label ruta_mala_yuri:
    "Me quedé paralizado, sin saber qué hacer..."
    "El tiempo se agotó."
    "(Ruta Mala: Yuri no sobrevivió)"
    return