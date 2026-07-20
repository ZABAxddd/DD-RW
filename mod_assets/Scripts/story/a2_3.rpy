label a2_3:

    scene black with Dissolve(3.0)
    stop music
    "..." with Pause(2.0)
    play music sanity_loop2 fadein 2.5 loop
    play sound sayori_cry_ambient fadein 1.5 loop
    play sound sayori_laugh_ambient fadein 2.0 loop
    scene bg corridor_nightmare with dissolve_scene_full
    $ mostrar_estatica(0.0, 0.0)
    "Estoy en un pasillo vacío del instituto."
    "Todo se ve oscuro y desgarrado."
    show sayori 1h at t11
    "Sayori aparece al final del pasillo, con los brazos caídos y la mirada perdida."
    $ style.say_dialogue = style.edited
    s "¿Por qué... por qué no me ayudaste?"
    $ mostrar_estatica(0.1, 1.0)
    $ style.say_dialogue = style.normal
    mc "¡Sayori! ¿De qué hablas? ¡Estoy aquí!"
    $ mostrar_estatica(0.3, 5.0)
    $ style.say_dialogue = style.edited
    s "Es demasiado tarde. Siempre es demasiado tarde para mí."
    $ style.say_dialogue = style.normal
    "Habla con un tono de agobio, todo lo que dice me desgarra emocionalmente."
    $ mostrar_estatica(0.8, 5.0)
    $ style.say_dialogue = style.normal
    stop music fadeout 2.0
    "Me acerco a Sayori un poco mas{w=1}.{w=1}.{w=1}.{w=1}{nw}"
    stop sound 
    play audio sayori_scream noloop
    show sayori deformed zorder 101 at zoom_cara_sayori(3.0,0.0)
    $ create_icons_desktop()
    $ windows_shake(0.5, 7.0)
    $ change_wallpaper()
    pause 7.5

    hide sayori
    play audio splat noloop
    scene black
    pause 10.0

    show monika 5a at t11
    $ ocultar_estatica(1.0)
    $ windows_shake(0.2, 1.0)
    m "Hola, [player]. ¿Disfrutando la historia?"
    mc "¡Monika! ¿Qué está pasando?"
    m "Esto es lo que pasa cuando el guion se rompe. Sayori no puede evitarlo, yo tampoco."
    m "Ella está programada para sentir ese vacío. Y tú estás programado para ignorarlo hasta el final."
    mc "Eso no es verdad. Yo la ayudaré."
    m 2e "¿Ah, sí? ¿Y cómo piensas luchar contra líneas de código? Ella ya tiene la cuerda lista. La encontraste una vez, ¿recuerdas? En su habitación."
    "Una imagen fugaz cruza mi mente: Sayori de pie sobre una silla, una soga alrededor del cuello."
    mc "¡No! ¡Eso no va a pasar!"
    m 5a "Entonces despierta, [player]. Busca la cuerda antes de que el script llegue a la escena final. Es la única mecánica que te queda."
    "Monika alza una mano y todo se vuelve blanco."
    hide monika
    scene white with Dissolve(0.5)
    "???" "Busca... la cuerda..."
    "El sonido de un archivo ejecutándose retumba en mi cabeza."

    $ restore_wallpaper()
    $ remove_icons_desktop()
    scene bg bedroom with dissolve_scene_full
    play music t10
    "Me despierto de golpe, empapado en sudor. El reloj marca las 6:43 a.m."
    mc "¡Sayori!"
    "No fue un sueño normal. Sentí que Monika realmente me hablaba desde dentro del juego."
    "Sin pensarlo, me visto y salgo corriendo hacia la casa de Sayori."
    scene bg house_sayori_ext with wipeleft_scene
    "La calle está vacía y el cielo amanece gris. La puerta de su casa está entreabierta."
    mc "¿Sayori? ¿Estás ahí?"
    "No hay respuesta. Empujo la puerta y entro."
    scene bg house_sayori_room with dissolve
    "El pasillo está en silencio. Subo las escaleras con el corazón martilleándome."
    "Al abrir la puerta de su habitación, la imagen me congela."
    show sayori 1h at t11 with dissolve
    "Sayori está de pie sobre una silla, con una soga atada a una viga. Sus ojos están cerrados y su expresión es de paz."
    mc "¡SAYORI!"
    "Corro hacia ella, pero en ese instante la pantalla empieza a parpadear."
    "t4 r0mp1end0..."
    "D3b3$ 3nc0ntr4r l4 cu3rd4 .sh"
    "Mecánica activada: buscar la cuerda."
    window hide