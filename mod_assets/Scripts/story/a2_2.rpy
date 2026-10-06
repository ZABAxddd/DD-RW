label a2_2:

    $ persistent.playername = currentuser
    $ player = user 

    scene black
    show text "{size=60}El día del festival{/size}"
    with dissolve_scene_full
    
    pause 3.0
    
    hide text with dissolve_scene_full
    
    pause 3.5
    
    scene bg sayori_bedroom at night_ambient_flicker 
    
    with dissolve_scene_full


    # Perspectiva de Sayori
    $ renpy.notify("Perspectiva de Sayori")
    "Un silencio inunda mi audición."

    "Ya llevo varios minutos sin hacer nada."

    "Mi mente divagaba."

    "En el festival, en el club, en [player] y en lo feliz que debería de estar ahora."

    "Pero pese a todo, lo siento todavía."

    "Siento ese maldito cansancio."

    "Mientras mi mente se hunde en pensamientos cada vez más oscuros."

    "Por un momento, dejo de moverme…"

    "..."
    play audio sayori_lought_alone noloop
    "Suelto una pequeña risa."

    "Pero creo que estaría mintiéndome a mí misma si me dijera que es porque algo de todo esto me hiciera gracia."

    "Incrédula, me doy cuenta de mi estado actual."
    play music tsad loop fadein 1.0
    s "¿En serio?"

    "Mi sonrisa se desvanece de inmediato."

    "Bajo lentamente la mirada."

    s "Mierda."

    "¿Cuánto tiempo llevo sintiéndome así de mal?"

    "Ah, es cierto..."

    "No lo sé."

    "..."

    "Pero..."

    "Todavía quiero pasar el día con ellas..."

    "Todavía quiero pasar el día con [player]."

    "Y me quedo quieta unos minutos más mientras la silla debajo de mi se tambalea."

    "Probablemente solo tratando de entenderme a mí misma incluso en esta situación."

    "*suspiro*"

    "Me bajo cuidadosamente de la silla."

    "Miro de reojo mi habitación..."
    scene bg sayori_bedroom at night:
        easein 2.0 zoom 1.5 xalign 0.4 yalign 0.9
    "La cama está desordenada."
    
    show bg sayori_bedroom at night:
        ease 2.0 xalign 0.0 yalign 0.95
    
    "Sobre mi escritorio descansan libros y poemas, la gran mayoría están dejados a medias."
    
    scene bg sayori_bedroom_window at night_ambient_flicker:
        subpixel True
        xcenter 0.5
        ycenter 0.5
        zoom 1.0

        linear 20.0 zoom 1.6
    show night_particles 
    "Por mi ventana entraba la tenue pero fantasmal luz lunar." with Dissolve(0.8)
    

    "Y después, empiezo a actuar como si nada hubiera pasado."
    stop music fadeout 1.0
    scene black with dissolve_scene_full
    pause 3.0


    # Se corta la escena

