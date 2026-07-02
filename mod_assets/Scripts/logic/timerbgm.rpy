screen gestor_audio_cronometro(tiempo_actual):
# Obtengo la pista actual en formato texto. Si no hay nada, devuelve "None".
    $ pista_actual = str(renpy.music.get_playing("music"))

    # # 1. Si el tiempo se agota, detenemos el canal de música inmediatamente
    # if tiempo_actual <= 0:
    #     if pista_actual != "None":
    #         timer 0.01 action Stop("music")

    # 2. Lógica de sincronización cuando quedan 20 segundos o menos
    if tiempo_actual <= 20 and "countdown_scary.ogg" not in pista_actual:
        # Al restar el tiempo actual a 20, si el reloj marca 20, el punto de inicio es 0.0 (inicio original).
        # Si el tiempo salta a 10s por penalización, el punto de inicio será 10.0, manteniéndose sincronizado.
        $ punto_inicio = 20 - tiempo_actual
        $ punto_inicio = max(0.0, punto_inicio) # Seguridad contra valores extraños
        
        # Construyo la directiva nativa con el nuevo punto de inicio calculado
        $ pista_sincronizada = "<from {}>mod_assets/sfx/countdown_scary.ogg".format(punto_inicio)
        
        # Ejecuto la pista de tensión
        timer 0.01 action Play("music", pista_sincronizada, loop=False)

    # 3. Lógica para mantener el BGM normal si el tiempo es mayor a 20 segundos
    elif tiempo_actual > 20 and "countdown.ogg" not in pista_actual:
        timer 0.01 action Play("music", "mod_assets/sfx/countdown.ogg", loop=True)
