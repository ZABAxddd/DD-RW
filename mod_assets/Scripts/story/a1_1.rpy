label a1_1:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2

    python:
        try: renpy.file("../characters/monika.chr")
        except: renpy.jump("ch0_kill")

    $ restore_all_characters()
    s "¡Heeeeeeeyyy!!"
    "Veo a una chica molesta corriendo hacia mí desde la distancia, agitando los brazos en el aire como si no se diera cuenta de la atención que podría llamar."
    "Esa chica es Sayori, mi vecina y buena amiga desde que éramos niños."
    "Ya sabes, ¿ese tipo de amiga que nunca te imaginarías haciendo hoy, pero que simplemente funciona porque se conocen desde hace tanto tiempo?"
    "Solíamos caminar juntos a la escuela en días como este, pero desde que empezó la secundaria ella se quedaba dormida cada vez más a menudo, y yo me cansaba de esperar."
    "Pero si va a perseguirme de esta manera, casi me siento mejor saliendo corriendo."
    "Sin embargo, solo suspiro y me quedo parado frente al cruce peatonal y dejo que Sayori me alcance."
    $ s_name = "Sayori"
    show sayori 4p zorder 2 at t11
    s 4p "Haaahhh... haaahhh..."
    s "¡Me quedé dormida otra vez!"
    s "¡Pero esta vez te alcancé!"
    mc "Tal vez, pero solo porque decidí parar y esperarte."
    show sayori at s11
    s 5c "¿Eeehhhhh? ¡Lo dices como si hubieras pensado en ignorarme!"
    s "¡Eso es cruel, [player]!"
    mc "Bueno, si la gente te mira por actuar raro, entonces no quiero que piensen que somos novios o algo así."
    show sayori zorder 2 at t11
    s 1a "Está bien, está bien."
    s "Pero al final sí me esperaste."
    s "Supongo que no eres capaz de ser malo aunque quieras~"
    mc "Lo que tú digas, Sayori..."
    s 1q "Ehehe~"
    show sayori zorder 1 at thide
    hide sayori
    "Cruzamos la calle juntos y nos dirigimos a la escuela."
    "A medida que nos acercamos, las calles se llenan cada vez más de otros estudiantes que hacen su viaje diario."
    show sayori 3a zorder 2 at t11
    s "Por cierto, [player]..."
    s "¿Ya has decidido a qué club unirte?"
    mc "¿Un club?"
    mc "Ya te lo dije, realmente no me interesa unirme a ningún club."
    mc "Tampoco he estado buscando."
    show sayori at s11
    s 4h "¡¿Eh?! ¡Eso no es cierto!"
    s "¡Me dijiste que te unirías a un club este año!"
    mc "¿Lo hice...?"
    "Estoy seguro de que es posible que lo haya dicho, en una de nuestras muchas conversaciones donde sigo la corriente a lo que sea que ella esté divagando."
    "A Sayori le gusta preocuparse demasiado por mí, cuando yo estoy perfectamente contento con aprobar raspando y pasar mi tiempo libre con juegos y anime."
    s 4j "¡Ajá!"
    s "Estaba hablando de cómo me preocupa que no aprendas a socializar o no tengas habilidades antes de la universidad."
    s "¡Tu felicidad es muy importante para mí, sabes!"
    s "¡Y sé que eres feliz ahora, pero moriría de solo pensar en que te conviertas en un NEET en unos años porque no estás acostumbrado al mundo real!"
    s 4g "¿Confías en mí, verdad?"
    s "No me hagas seguir preocupándome por ti..."
    mc "Está bien, está bien..."
    mc "Veré algunos clubes si eso te hace feliz."
    mc "Pero no prometo nada."
    s 1h "¿Al menos me prometerás que lo intentarás un poco?"
    mc "Sí, supongo que te prometo eso."
    show sayori zorder 2 at t11
    s 4r "¡Yaay~!"
    "¿Por qué dejo que una chica tan despreocupada me sermonee?"
    "Más que eso, me sorprende que incluso haya cedido ante ella."
    "Supongo que verla preocuparse tanto por mí me hace querer tranquilizarla al menos un poco, incluso si exagera todo dentro de su cabeza."

    scene bg class_day
    with wipeleft_scene

    "El día escolar es tan común como siempre, y termina antes de que me dé cuenta."
    "Después de guardar mis cosas, miro fijamente la pared, buscando un gramo de motivación."
    mc "Clubes..."
    "Sayori quiere que revise algunos clubes."
    "Supongo que no tengo otra opción que empezar con el club de anime..."

    s "¿Holaaa?"
    show sayori 1b zorder 2 at t11
    mc "¿Sayori...?"
    "Sayori debe haber entrado al salón mientras yo estaba distraído."
    "Miro alrededor y me doy cuenta de que soy el único que queda en el aula."
    s 1a "Pensé que te vería salir del salón, pero te vi sentado aquí distraído, así que entré."
    s "Sinceramente, a veces eres peor que yo... ¡Estoy impresionada!"
    mc "No tienes que esperarme si eso te va a hacer llegar tarde a tu club."
    s 1y "Bueno, pensé que podrías necesitar algo de ánimo, así que pensé, ya sabes..."
    mc "¿Saber qué?"
    s 1a "Bueno, ¡que podrías venir a mi club!"
    mc "Sayori..."
    s 4r "¿¿Síí??"
    mc "...De ninguna manera voy a ir a tu club."
    show sayori at s11
    s 5d "¡¿Eeeehhhhh?! ¡Malvado!"
    "Sayori es la vicepresidenta del Club de Literatura."
    "No es que yo supiera que ella tuviera algún interés en la literatura."
    "De hecho, estoy 99%% seguro de que solo lo hizo porque pensó que sería divertido ayudar a empezar un nuevo club."
    "Como ella fue la primera en mostrar interés después de quien propuso el club, heredó el título de \"Vicepresidenta\"."
    "Dicho esto, mi interés en la literatura está garantizado que es incluso menor."
    mc "Sí. Voy al club de anime."
    show sayori zorder 2 at t11
    s 1g "Vamos, ¿por favor?"
    mc "¿Por qué te importa tanto, de todos modos?"
    s 5b "Bueno..."
    s "Le dije al club ayer que traería un nuevo miembro..."
    s "Y Natsuki hizo pastelitos y todo..."
    s "Ehehe..."
    mc "¡No hagas promesas que no puedas cumplir!"
    "No sé si Sayori es realmente tan cabeza hueca, o si es tan astuta como para haber planeado todo esto."
    "Dejo escapar un largo suspiro."
    mc "Está bien... Me pasaré por un pastelito, ¿de acuerdo?"
    show sayori at h11
    s 4r "¡Sí! ¡Vamos~!"

    stop music fadeout 2.0

    scene bg corridor
    with wipeleft_scene

    "Y así, hoy marca el día en que vendí mi alma por un pastelito."
    "Sigo abatido a Sayori a través de la escuela y subiendo las escaleras, una sección de la escuela que rara vez visito, ya que generalmente se usa para clases y actividades de tercer año."
    "Sayori, llena de energía, abre la puerta del aula de golpe."

    scene bg club_day
    with wipeleft
    play music t3
    show sayori 4 at l41
    s "¡Todos! ¡El nuevo miembro está aquí~!"
    mc "Te dije que no me llames 'nuevo miembro--'"
    show sayori at lhide
    hide sayori
    "¿Eh? Echo un vistazo por la sala."
    show yuri 1a zorder 2 at t11
    y "Bienvenido al Club de Literatura. Es un placer conocerte."
    y "Sayori siempre dice cosas bonitas sobre ti."
    show yuri zorder 2 at t22
    show natsuki 4c zorder 2 at t21
    n "¿En serio? ¿Trajiste a un chico?"
    n "Qué manera de matar el ambiente."
    show yuri zorder 2 at t33
    show natsuki zorder 2 at t32
    show monika 1k zorder 2 at t31
    m "¡Ah, [player]! ¡Qué agradable sorpresa!"
    m "¡Bienvenido al club!"

    jump a2_1beta