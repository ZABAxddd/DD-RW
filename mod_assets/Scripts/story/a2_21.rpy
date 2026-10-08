label a2_21:
    pause 1.5
    scene black
    show text "{size=60}El día del festival{/size}"
    with dissolve_scene_full
    pause 3.0

    scene bg bedroom with dissolve_scene_full
    $ renpy.notify("Perspectiva de [player]")
    "Llegó el día del festival."

    "Esperaba ir a clases con Sayori en un día tan señalado."

    "Pero no responde al teléfono."

    "Pensé en ir a su casa a despertarla, pero quizá es demasiado."

    "En este momento, los preparativos del evento deben estar casi listos."

    "La pancarta que pintamos Yuri y yo ya se secó, así que la enrollo con delicadeza para llevármela."

    "Ella me envió un mensaje muy agradable para que no me olvide nada y yo le dije que no se preocupara."

    "Creo que me siento igual que Natsuki sobre el recital. Tiene su gracia."

    "Tengo ganas de que acabe para disfrutar del festival con Sayori y Yuri."

    "Pero, conociendo a Monika, seguro que el recital también será genial."

    "Aunque... me gustaría que Sayori también estuviera aquí."

    "Supongo que no pasa nada si llego un poquito tarde, quizás está durmiendo como una marmota otra vez."

    "La conozco desde hace muchos años, yo sé que es imposible que me sorprenda por algo así."

    "Finalmente decido esperar unos minutos más..."
    scene black with wipeleft_scene
    pause 3.0
    scene bg living with wipeleft_scene
    "Estaba a punto de darme por vencido, hasta que veo que se abre la puerta de su casa."

    "Sayori sale como un bala, tratando de arreglarse su cabello mientras intenta ponerse los zapatos."
    show sayori 4r zorder 2 at t11
    s "¡[player]!"

    "Ella alza su mano para saludarme, y la misma sonrisa de siempre se dibuja en su rostro."
    show sayori 5a zorder 2 at h11
    s "L-lo siento! ¡Me dormí más de lo que esperaba!"

    "Realmente dudo de que le preocupe haberme hecho esperar."

    "Pero es Sayori, claramente no puedo enojarme con ella solo por esto."

    "Mientras finjo clavar mi mirada en el camino a la escuela, miro de reojo a Sayori."

    "Nada fuera de lo común…"

    show sayori 4a at h11
    s "¿Vamos a ir o…?"

    "Sayori muestra su sonrisa mientras ambos caminamos rumbo al festival."

    "Ya no me acuerdo de por qué estaba un poco preocupado."

    "Lo único que necesito para pasarla bien hoy es el festival, el club y a Sayori."

    # Se corta la escena.
    scene black with dissolve_scene_full
    pause 1.5
    scene bg club_day with dissolve_scene_half
    # Aparecemos en el aula del club.

    show monika 5a zorder 2 at t11
    m "¡Sayori, [player]!"

    m "Ustedes dos son los primeros en llegar."

    m 2e "Tardaron un poco más de lo que esperaba…"

    m 5a "Pero lo importante es que al menos mantienen su compromiso."

    "Comenta Monika, mostrando su sonrisa serena de siempre."
    show sayori 5b zorder 2 at t21
    show monika 1a at t22 
    s "Sí, lamento haberme quedado dormida... MC solo estaba esperando por mí."

    "Menciona Sayori mientras ríe tímidamente."

    m 4j "Jejeje, Descuida, no tengo problema con eso."
    show monika at thide
    hide monika
    show sayori 1y at t11 
    "Miro el rostro sonrojado de Sayori, aunque una duda se planta en mi mente."
    show sayori at thide
    hide sayori
    mc "Qué extraño. Pensé que Yuri ya habría hecho acto de presencia."

    "Monika coloca unos pequeños folletos los pupitres del aula."

    "Deben ser los que contienen los folletos que vamos a recitar."

    "Al final, lo que hice fue buscar en internet un poema que podría agradarle a Monika y se lo envié."

    "Por lo tanto, es el que me toca recitar."
    show monika 4b zorder 2 at t11
    m "¿Quieren hecharle ojo a los folletos?"

    m 2a "¡Quedaron de maravilla!"

    mc "Sí, claro."

    show sayori 4r zorder 2 at t22
    show monika zorder 1 at t21
    s "¡Yo también!"
    show monika at thide
    show sayori at thide
    hide monika 
    hide sayori
    "Ambos agarramos los pequeños folletos."

    "Y mientras nos sentamos en unos pupitres para leerlos juntos, el celular de Monika empieza a vibrar."
    
    show monika 2d at t11
    m "¿Hmm?"

    "Monika saca el celular."

    show monika 1a
    "Ella esboza una sonrisa satisfecha, luego se dirige a nosotros."

    m 5a "Espérenme aquí, Natsuki y Yuri ya llegaron."

    m "Solo quieren que les ayude a subir algunas cosas."

    show sayori 1a at t22
    show monika at t21

    s "Esta bien Monika."
    show monika at t41
    show monika at thide
    hide monika
    show sayori at t11
    "Ella camina hacia la puerta, parece entusiasmada también."

    "Aunque dejando eso de lado, miro a Sayori."

    mc "¿Quieres leer aún?"

    "Ella me mira como una niña emocionada, claramente su respuesta será positiva."
    show sayori 1q at h11
    s "¡Siempre!"

    show sayori 1a
    "Sin más rodeos, le entrego dos folletos a Sayori y yo me quedo con unos tres folletos."

    "Ella tiene el mío y el de Monika."

    "Yo tengo el de Yuri, Natsuki y el de Sayori."

    "Ambos empezamos a leer los poemas detenidamente."

    "Soy sacado de mis pensamientos al escuchar a Sayori."

    s 3b "hmmm"

    s "¿Este es tuyo?"

    mc "Sí."

    s 1x "¡A ver!"
    show sayori 1o 
    "Sayori agarra el poema y empieza a leerlo."
    show sayori 1n
    "Inicialmente parece concentrada, pero poco a poco, una sonrisa empieza a dibujarse en su rostro."

    "Perfecto, presiento que no sospecha nada…"
    show sayori 2x at h11
    s "Je…"

    mc "¿Qué?"

    s 1a "Oh, no es nada."

    show sayori 1o
    "Continua leyendo y se le escapa otra risita."

    "Empiezo a sentirme un poco nervioso."

    "¿Por qué sigue leyéndolo?"

    s 4s "Ay, esto está bien bonito."

    mc "Hmmm, ¿Lo está?"

    s 3x "¡Totalmente!"

    "Lee otra parte y sigue sonriendo."

    s 3a "No sabía que podías escribir algo así."

    mc "¡O-oye! ¿Qué quieres decir con eso?"

    s 2d "Tranquilo, [player], ¡es solo un cumplido!"

    "Nuevamente, ella vuelve a posar su mirada en el poema."

    s 4s "Me gusta mucho."

    mc "M-me alegro."

    s 2o "Pero…"

    "Ella se detiene"

    mc "¿Pero qué?"

    s "Espera."

    "Ella empieza a releer una de las líneas."

    s 1f "..."

    "No. No, no, no, esa cara no me gusta."

    s 1g "Esto…"

    "Vuelve unas líneas atrás."

    s 2g "¿Tú escribiste esto?"

    mc "¿Qué quieres decir?"

    mc "Por supuesto que sí."

    mc "La pregunta ofende."

    s 2h "¿Estás seguro?"

    mc "¿Por qué no iba a estar seguro?"

    "Mierda, ¿Por qué dije que lo escribí yo?"

    s 1k "Solo…"

    "Lo mira durante unos segundos."

    s 1f "No parece tuyo."

    mc "¿¡Qué!?"

    s 1d "N-no te lo tomes a mal."

    "Ella sigue riéndose suavemente."

    s 2f "Oh, vamos [player], te conozco."

    s 1l "Es que esto es demasiado... tú no escribes así."

    "¿Cómo puede haberse dado cuenta tan rápido?"

    "Piensa en otra cosa, di algo."

    mc "Solo tengo un lado poético que nunca te he enseñado."

    s 1i "¿En serio?"

    s 1j "¿Acaso eres un poeta secreto, [player]?"

    mc "Desde siempre."
    show sayori 1q at h11
    s "Jejejeje…"

    s 2a "¡Mentiroso!"

    "Mientras ella sigue viendo el poema, parece recordar algo finalmente."

    s 2b "De hecho…"

    "Por favor... que no se de cuenta."

    s 3d "Creo que he visto esta frase antes."

    mc "¿Dónde?"

    s 1l "No estoy segura, pero..."

    "Ella piensa durante unos segundos."

    s 4a "¡Ya sé, en Reddit!"

    mc "..."

    s 1b "¿Qué?"

    mc "¿Tú tienes una cuenta en Reddit?"

    s 1l "¿Eh? Claro."

    mc "¿Tú?"

    s 1d "¿Por qué lo dices de esa manera?"

    mc "Porque pensaba que eras la ultima persona en el mundo que tendria una cuenta en... no sé, ¿Reddit?"

    s 3i "¿¡Y por qué no tendría Reddit!?"

    mc "No sé, ¿quizás porque la única vez que te he visto usando internet fue para buscar un tutorial para hacer tortillas?"

    mc "Tortillas que jamás hiciste en realidad."

    s 1l "Jejeje... eso también lo hago..."

    mc "¡Lo sabía!"

    s 1a "¡Pero lo importante es que también tengo Reddit!"

    mc "Lo cambia todo."

    s 2b "¿Qué cosas?"

    mc "Necesito saber que clase de cosas publicas ahí."

    s 1l "..."

    mc "Sayori."

    s 5a "Nada."

    mc "Ese \"nada\" ha sonado demasiado a que hay algo."

    s 4l "¡Ya dije que no hay nada!"

    mc "¿Tienes nombre de usuario?{nw}"

    s 1j "¡No!"

    mc "¡Has respondido demasiado rápido!"

    s 1f "..."

    mc "..."

    "..."

    "Antes de que pudiese hacer más preguntas, Monika entra al aula, seguida de Yuri y Natsuki."

    "Llevan consigo las pancartas y los cupcakes."
    
    show sayori 4o zorder 3 at hop(x=640,z=1.00), t44  
    show monika 5a zorder 4 at l43
    show natsuki 5g zorder 2 at l42
    show yuri 4b zorder 1 at l41
    m "¡Ya estamos aquí!"

    show monika zorder 4 at f43
    m "Ya termine de ayudarlas."
    show monika zorder 3 at t43
    show natsuki zorder 4 at f42
    n "Ugh, sigo pensando que podría haber llevado los cupcakes yo sola." 

    show monika 2b zorder 4 at f43
    show natsuki zorder 3 at t42
    m "Jejeje, supongo que solo quería asegurarme de que no hubiera un incidente en las escaleras."

    show monika at t43
    "Yuri asiente ante lo dicho por Monika."

    show sayori 3x zorder 5 at h44 
    s "¡Déjenmelo a mí!"
    show sayori at thide
    show monika at thide
    show yuri at thide
    show natsuki at thide
    
    hide sayori
    hide natsuki
    hide yuri 
    hide monika 
    
    "Sayori se levanta y camina en dirección a ellas, probablemente queriendo ayudar a decorar y tenerlo todo listo."

    mc "¡Oye Sayori! todavía no hemos terminado nuestra conversación."

    "Sayori se gira mientras me mira nerviosamente."
    show sayori 5b at t11
    s "¿Conversación? Je, ¿de qué conversación hablas?"

    mc "La de tu misteriosa cuenta de Reddit."
    show sayori 4p at h11
    s "¡[player]!"
    show sayori zorder 3 at t44
    show natsuki 2k zorder 4 at t43
    show yuri 2f zorder 2 at t42
    show monika 2d zorder 1 at t41
    
    show natsuki zorder 4 at f43
    n "Espera, ¿de verdad Sayori tiene Reddit?"
    show natsuki zorder 3 at t43
    show yuri zorder 4 at f42
    y "¿Reddit?"
    show monika 2b zorder 4 at f41
    show yuri zorder 3 at t42
    m "Vaya, eso sí que no me lo esperaba."
    show monika zorder 3 at t41
    show sayori zorder 4 at hf44
    s "¡Déjenlo ya! ¡No es para tanto!"
    show sayori at t44
    mc "Dice que no la dejemos."
    show sayori 3j at h44
    "¡No! ¡Tenemos que preparar el festival!"
    
    show sayori 1a
    show monika 2a
    show natsuki 5a
    show yuri 1a

    "Después de eso, se forma un pequeño silencio."

    "Pero no dura demasiado, ya que Natsuki suelta un pequeño sonido de protesta."
    
    show natsuki 4b zorder 5 at f43

    n "Creo que tiene razón."

    "Yuri sonríe tímidamente, está vez concediéndole la razón a Natsuki."
    
    show natsuki 4b zorder 5 at t43
    show yuri 1b zorder 6 at f42

    y "No podemos quedarnos aquí hablando todo el día."
    
    show monika 5a zorder 7 at hf41
    show yuri at t42
    m "Exactamente."
    show monika at t41
    mc "Sip, pero probablemente diría que Sayori nos ha salvado de perder toda la mañana."
    show sayori 1q zorder 8 at hf44 

    s "Ese es mi mayor talento, por fin lo reconoces."
    show sayori at t44
    "Acto seguido, Sayori me da un suave codazo juguetón."

    "Monika se pone delante de todos, mientras miraba al resto del grupo."
    show monika 5a zorder 9 at f41
    show sayori 1a
    show natsuki 5g
    show yuri 
    m "Okay, todo el mundo."

    m 1a "Ya hemos descansado suficiente."

    "Los ojos de Monika brillan con profunda determinación mientras nos mira a todos."

    m 2e "Hoy tenemos una misión."

    m "Debemos montar nuestro puesto antes de que empiece el festival."

    "Entonces, Sayori levantó el puño."

    show sayori 2r at hf44
    s "¡Entonces vamos a hacerlo!"

    show yuri zorder 10 at f42
    
    y "¡S-sí!"
    show natsuki 5j zorder 11 at f43
    n "¡Venga!"
    show monika at t41
    show sayori at t44
    show natsuki at t43
    show yuri at t42
    mc "De acuerdo."

    "Monika parecía bastante satisfecha ante todas estas respuestas, manteniendo su actitud de lideresa."
    
    show monika 5a zorder 10 at h41
    m "Perfecto, ¡pues empezemos!"
    
    show monika at thide
    show sayori at thide
    show natsuki at thide
    show yuri at thide
    
    hide yuri
    hide monika
    hide sayori
    hide natsuki
    
    scene bg club_day with wipeleft_scene

    "Y sin más preámbulos, todos nos pusimos manos a la obra."

    "Monika, está coordinando y comprobando que todo esté listo."

    "Sayori está ocupada ayudando con los panfletos y moviéndose energéticamente de un lado al otro."

    "Yuri parece colocar meticulosamente los banners y la decoración para que quede lo mejor posible."

    "Natsuki prepara las mesas para recibir a los estudiantes que vengan ansiosos de sentarse a probar sus cupcakes."

    "Y yo... Bueno, ayudo donde hace falta."

    "De todos modos…"

    "Poco a poco el ruido de los pasillos fue aumentando progresivamente."

    "Voces, canciones y pasos se mezclaban con el movimiento constante de estudiantes que iban de un lado al otro."

    "Había salido del aula para escaquearme de ayudar, y al mismo tiempo ir a mear…"

    "Pero cuando salí del club, apenas pude reconocer algunos de los pasillos que había recorrido cientas de veces."

    "Había carteles en todos lados, las puertas de las aulas estaban abiertas y se podían ver las diversas actividades que se realizaban, gente estaba moviendo mesas y sillas por los pasillos, estudiantes moviéndose de un lado al otro."

    "Okey, creo que el festival definitivamente va a comenzar dentro de nada."

    "Después de hacer lo necesario, vuelvo al aula."

    "Parece que todo está casi listo."

    mc "Oh, ¿Acaso ya han terminado?"

    m "Casi, sigo comprobando que no nos falte nada."

    n "¿No lo has comprobado demasiadas veces ya?"

    m "Je, bueno, solo quiero que todo salga bien."

    y "Pero creo que todo está preparado ya, Monika…"

    "Monika se estira, reflexionando."

    m "Hmmm, supongo que tienes razón."

    "Ella mira la hora."

    m "Está bien, tenemos una hora antes del festival."

    s "Entonces, ¿Qué hacemos ahora?"

    n "Nada. Supongo, ya hemos terminado."

    mc "Podríamos salir un rato."

    s "¿A ver el festival?"

    mc "Exactamente."

    n "Bueno, yo tampoco tengo nada mejor que hacer..."

    mc "Oh, ya veo."

    mc "¿Eso significa que vienes?"

    n "Ni te emociones, solo me apetece dar una vuelta."

    s "¡Entonces seremos 3!"

    "Yuri está sentada cerca de nosotros, tratando de concentrarse en su folleto."

    y "Y-yo... creo que me quedaré aquí."

    s "¿Seguro?"

    y "Sí... solo quiero repasar un poco antes del recital."

    n "Oh, vamos, pasear no es un crimen, puedes venir."

    y "No, en serio está bien..."

    mc "Bueno, supongo que como quieras..."

    "Sin esperar más, los tres salimos del aula, no sin antes despedirnos de Monika y Yuri."

    # Mientras tanto, Monika y Yuri:

    m "¿No ibas a quedarte?"

    "Yuri queda totalmente paralizada."

    y "Y-yo…"

    "Yuri mira hacia la puerta."

    y "Pensándolo mejor, tomar un poco de aire nunca viene mal."

    m "Claro."

    "Yuri trata de aparentar la mayor normalidad posible mientras se retira del aula también."

    m "..."

    m "Que discretos..."

    "Monika se ríe suavemente."

    # Volvemos con MC:

    "Ya fuera del aula, empezamos a caminar los 3 juntos."

    "Podemos notar como la escuela se ha transformado totalmente."

    "La cancha está llena de olores a yakisoba y tokoyaki."

    "Las aulas están convertidas en cafés o en casas embrujadas."

    "También hay actuaciones organizadas por gente de todos los años."

    "Y al igual que nosotros, también hay clubes organizando actividades para reclutar nuevos miembros."

    "Creo que hay demasiado que ver por hoy..."

    # Se corta la escena, para representar que ha pasado un buen rato.

    "La siguiente hora paso mucho más rápido de lo que esperaba."

    "Primero estuvimos dando vueltas por los distintos puestos, viendo cómo había quedado la escuela."

    "Sayori, como era de esperarse, quiso probar casi todo lo que se encontraba."

    "Hasta intentó chantajearme para que le compre un poco de comida."

    "Pero solo porque es Sayori, termine cediendo a sus caprichos."

    "Inicialmente Natsuki se quejaba de que estábamos perdiendo el tiempo."

    "Pero luego ella se separó momentáneamente de nosotros para mirar las exposiciones de arte e ilustraciones del club de manga."

    "En ese tiempo, Sayori y yo simplemente seguimos paseando y viendo demostraciones de un club deportivo."

    "Pero el tiempo se nos estaba escapando."

    "Ya había pasado casi 1 hora."

    "Tendríamos que volver pronto al recital."

    mc "Supongo que ya va siendo hora de volver."

    "Me giro hacía Sayori."

    mc "¿Vamos de una vez?"

    "Sayori asiente afirmativamente."

    "Con una pequeña sonrisa que demuestra que lo ha pasado bien pero que sabe que es hora de irse."

    s "¡Vamos!"

    s "¿Pero sabes donde está Natsuki?"

    mc "Es cierto, ¿Dónde estará?"

    "Por un momento sentí a alguien detrás de mí."

    "Pensé que podría ser Natsuki, así que me volteo lentamente."

    mc "Oh, ahí estás, Nats-"

    y "Ah, [player]..."

    "¿Qué?"

    mc "¿Yuri?"

    s "Sí~ ¡Yuri!"

    y "Sí... soy yo..."

    "Yuri parece algo avergonzada."

    y "Pensé que quizás la estarían regresando."

    mc "¿Qué estás haciendo aquí?"

    s "¡Pensábamos que te habías quedado en el aula!"

    "Yuri aparta la mirada hacia un lado, se ve tímida como siempre."

    y "Bueno... sí, supongo que eso era lo que había dicho."

    mc "Entonces... ¿Te apetece contarnos por qué saliste?"

    y "Quise ver una exposición de libros de segunda mano que estaba en uno de los pasillos."

    s "¿Libros?"

    "Yuri sonríe muy levemente."

    y "Sí... Había algunos bastante interesantes."

    mc "¿Fuiste tú sola?"

    "Yuri asiente afirmativamente."

    y "Yo... no quería molestarlos con mi presencia, además de que pensé que era una buena oportunidad para hechar un vistazo."

    s "¿Qué? ¡Jamás serías una molestia, Yuri!"

    s "¡Podrías habernos avisado!"

    y "Yo... lo sé, pero vi que ustedes la estaban pasando muy bien."

    "Sayori sonríe."

    s "Bueno, ¡La programa no! ven con nosotros!"

    "Yuri parece estar un poco más animada."

    y "Lo intentaré…"

    "Antes de decir algo más, escuchamos unos pasos acercándose por el pasillo."

    n "¡Ah!, ¿Ya están aquí?"

    "Natsuki apareció doblando la esquina y se detuvo al ver a Yuri."

    n "¿Yuri?"

    y "Natsuki."

    n "Pensaba que te habías quedado con Monika."

    y "Y yo pensaba que tú estabas con ellos."

    "Menciona Yuri, refiriéndose a mí y a Sayori."

    n "Estuve un rato, pero luego fui a ver la exposición del club de manga…"

    s "Oh, ¿Había cosas buenas?"

    n "Podría decirse que sí, habían algunas ilustraciones que estaban bastante bien."

    "Natsuki parece darse cuenta de algo."

    n "Espera, ¿ustedes dos han estado juntos todo este tiempo?"

    s "¡Sí!"

    "Natsuki sonríe naturalmente, su expresión confiada dice algo que no me gusta…"

    n "Ja, que conveniente."

    mc "¿A qué se supone que quieres llegar?"

    mc "¿Qué significa eso?"

    n "No es nada, solo calate."

    y "..."

    y "Deberíamos volver, recuerden que el recital empieza pronto."

    mc "Muy cierto…"

    "Y así, finalmente, los cuatro emprendimos el camino de vuelta al aula."

    "Después de recorrer el festival por separado, finalmente estábamos todos juntos otra vez."

    "Claro, sin contar a Monika, la cual probablemente siga en el club de literatura."

    # Se corta la escena, indicando que ha ocurrido algo de tiempo.

    "Cuando regresamos al aula, Monika ya estaba esperándonos."

    "Se alegró al vernos aparecer juntos, y en seguida quiso saber que hemos estado haciendo."

    "Tras un par de bromas, nos preparamos para el recital."

    "Al principio solo había unas cuantas personas frente a nosotros."

    "Desde luego no era la multitud que Monika había imaginado."

    "Pese a eso, solo seguimos."

    "Natsuki fue la primera en ponerse algo nerviosa."

    "Intento disimularlo fingiendo despreocupación, pero parecía pendiente de la reacción del público."

    "Aunque quizás no lo querría admitir."

    "Cuando termino de leer, pareció relajarse al escuchar varios comentarios positivos entre los espectadores."

    "Yuri parecía más concentrada, pero también más nerviosa."

    "Ella leía su poema con calma."

    "Y cuando terminó, parecía bastante aliviada. Pese a que seguía evitando el contacto visual con el público."

    "Monika era la siguiente, ella intentó mantener su seguridad habitual."

    "Aunque parecía ligeramente más callada que de costumbre."

    "Incluso ella parecía estar algo decepcionada con la cantidad de gente que había asistido."

    "Aún así, continuó como si nada y se esforzó para hacer que todo terminará de la mejor manera posible."

    "Y Sayori..."

    "Al principio parecía emocionada."

    "Al ver al público, se sintió algo nerviosa."

    "Ella no parecía haber leído en público antes."

    "Cuando terminó, sonrió con alivio."

    "Verla volver con esa expresión... Hizo que sintiera que mi corazón empezaba a latir más rápido y fuerte."

    "Después de todo... quizás este festival no había salido mal en absoluto pese a todo."

    "Definitivamente, creo que todos nos habíamos imaginado algo más grande."

    "Quizás bastante más grande."

    "Pero al menos algunas personas se quedaron para escucharnos, y por lo que pude ver, parece que lo han disfrutado."

    "Y Monika pareció recuperar al menos una parte de su entusiasmo."

    "Después de aquello, el resto del festival ocurrió mucho más rápido."

    "Natsuki se dedico a vender los cupcakes que había preparado."

    "Y poco a poco, se quedaba mirando como la gente volvía por otro."

    "Cada vez que algún alumno decía que estaban ricos, Natsuki no fingía que le importará demasiado."

    "Pero era bastante evidente de que estaba orgullosa."

    "Yuri fue a ver algunas exposiciones que aún seguían abiertas."

    "Monika se dedico a repartir los últimos panfletos."

    "Y Sayori... solo se dejaba llevar por el momento."

    "Visitamos algunos puestos de comida, para celebrar."

    "Ya que al menos el festival no había salido nada mal."

    "Desde luego el Club de Literatura no era el más popular y tampoco hubo demasiada gente..."

    "Pero los cupcakes habían gustado y hubo gente que al menos mostró interés por nuestro Club."

    "Para ser nuestro primer festival..."

    "Salió bastante bien."

    "Y, simplemente nos dedicamos a disfrutar del resto del festival."

    # Se corta la escena, cambiando a la casa de MC:

    "Cuando llegue a casa, hice lo de siempre."

    "Deje las cosas en mi habitación, cené, me duché, y me pasé el resto de la tarde sin hacer gran cosa."

    "Después de un día entero rodeado de gente necesitaba algo de comodidad."

    "Acabe sentado frente al ordenador."

    "Jugando al LOL mientras intentaba no pensar demasiado en nada."

    "Había pasado un rato, hasta que llegó una notificación."

    unk "¿Estás ocupado?"

    "Sonreí."

    mc "Depende, estoy a mitad de una partida."

    s "Entonces sí estás ocupado."

    mc "Pero podemos hablar si quieres."

    s "¡Bien!"

    "A partir de ahí, la conversación simplemente siguió."

    "Hablamos del festival, de Natsuki y sus cupcakes."

    "De Yuri y su misteriosa escapada a la exposición de libros."

    "Y de como Monika había conseguido hablar con varios estudiantes, mientras nosotros estábamos fuera."

    "Poco a poco, empezamos a hablar de cosas completamente distintas."

    "Películas, videojuegos o tonterías absurdas que habíamos visto por internet."

    "Sayori incluso volvió a sacar el tema de mi poema."

    s "Sigo sin olvidar que intentaste engañarme."

    s "Si yo no lo hubiera notado, jamás hubieses dicho que ese poema no era tuyo."

    "Sonrío al ver el mensaje."

    mc "...Vale, sí."

    s "¡Ja!"

    "La conversación continuó durante un buen rato."

    "Era extraño."

    "Nos habíamos declarado ayer."

    "Y habíamos pasado prácticamente todo el festival juntos."

    "Y aún así, parecía que ninguno de los dos tenía demasiada prisa por hablar directamente de ello."

    "A decir verdad, no me sentía incómodo."

    "Simplemente había algo distinto entre nosotros."

    "Cada mensaje parecía tener un significado ligeramente diferente."

    "Cómo si ambos fuéramos conscientes de lo que había cambiado."

    "Pero ninguno quisiera señalarlo."

    mc "¿Sabes? Una vez escuché una frase de una película."

    mc "Creo que era una frase de “Good Will Hounding.”."

    s "Ah, ¿Sí?"

    mc "Seee... creo que era de esa."

    s "No la he visto."

    mc "Hmmm, yo tampoco la recuerdo demasiado bien."

    s "Pues algún día podemos verla juntos."

    mc "Jeje, Claro."

    s "¿De qué iba?"

    "Eh...."

    mc "De un chico muy inteligente, creo."

    s "¡Suena bien!"

    s "¿Y que decía?"

    mc "Algo sobre de que tendrás momentos malos, pero ellos te harán abrir los ojos a las cosas buenas que no estabas viendo."

    "Honestamente, no pensé demasiado en lo que acababa de escribir."

    "Para mí era solo una frase, aunque Sayori tardo un poco más en responder."

    s "Sí..."

    "Después escribió de nuevo."

    s "Tiene sentido."

    "Simplemente seguí mirando la pantalla."

    mc "¿Tú qué opinas?, es un poco cursi, ¿no lo crees?"

    s "Un poquito."

    "..."

    mc "Sabía que dirías eso."

    "Está vez, ella tardó un poquito más."

    "Pero el mensaje apareció finalmente."

    s "Creo que voy a salir un rato."

    "Fruncí el ceño."

    mc "¿Ahora?"

    s "Sí, necesito aire."

    mc "¿Todo bien?"

    "La respuesta llegó casi inmediatamente."

    s "Sí :D"

    "Volví a mirar la pantalla."

    "Algo en ese mensaje me hizo dudar."

    "Pero no sé exactamente qué."

    "Era el mismo emoticono, y la misma forma de escribir se siempre."

    "Pero juro por mi madre que había algo... quizá estaba imaginándolo."

    mc "Vale... si necesitas algo, avísame escribiéndome con tú celular."

    s "Lo haré..."

    "Y entonces, dejo de responder."

    "Me quedé mirando la conversación unos segundos, quizá había dicho algo que no debía."

    "No sé qué podría haber sido, pero aquella frase..."

    "Tal vez toque un tema que no debí tocar."

    "No pude darle más vueltas, escuché unos golpes en la puerta."

    "Me levante, todavía confuso."

    mc "¿Quién podría ser?"

    "Cuando abrí, Sayori estaba ahí, ella sonreía... Una sonrisa perfectamente normal."

    s "¡Holis!"

    mc "¿Sayori?"

    s "Sip."

    "Ella se encoje de hombros."

    s "Pensé que podríamos dar una vuelta."

    "La mire durante unos segundos."

    mc "¿Ahora?"

    s "¿Por qué no?"

    "Su sonrisa se hace más grande."

    s "Hace buen tiempo."

    "Parece que no ha ocurrido nada..."

    "Pero no puedo dejar de pensar en esa conversación."

    mc "Vale..."

    "Sayori se aparto un poco de la puerta."

    s "¡Entonces vamos!"

    mc "¿A dónde?"

    s "No sé, podemos decidirlo por el camino."

    mc "Sayori... se honesta."

    mc "No tienes ningún plan, ¿Verdad?"

    s "¡Claro que tengo un plan!"

    mc "¿Cuál?"

    s "Salir."

    mc "Eso no es un plan, tontita."

    s "Jajaja, Entonces podemos iniciar por ahí, ¿de acuerdo?"

    "Cerré la puerta detrás de mí y salí con ella."

    "Durante un rato caminamos por las calles, ya oscurecidas por la hora."

    "Contabamos algunos chistes entre nosotros, hasta que doblamos por un callejón algo iluminado."

    s "Ah, espera."

    mc "¿Qué pasa?"

    s "Quiero enseñarte algo."

    "Entonces, Sayori me llevo a una pared junto a uno de los edificios."

    "Había estado allí durante el festival, aunque no le había prestado demasiada atención."

    "Era un gran panel lleno de papeles escritos a mano."

    "En la parte superior había un título:"

    "COSAS QUE QUIERO HACER DESPUÉS DE SALIR DE LA PREPARATORIA"

    mc "¿Ya lo conocías?"

    s "Sí, lo vi hace unas semanas, aunque antes no habían tantos papeles."

    "Juntos, empezamos a leer algunas de las respuestas."

    "Viajar a otro país."

    "Aprender a tocar la guitarra."

    "Viajar a Europa."

    "Aprender a cocinar algo que no sean fideos instantáneos."

    "Sayori señaló este último.*"

    s "Ese me gusta."

    mc "¿Por qué?"

    s "Porque me parece realista."

    mc "Es verdad, olvidé que tú tampoco sabes cocinar."

    s "¡Oye! ¡S-sé hacer cosas!"

    mc "¿Cómo cuáles?"

    s "...Cosas..."

    mc "Respuesta errónea."

    "Entonces, ella suelta una risa."

    s "¡No importa!"

    "Al lado del panel, había varios papeles y bolígrafos."

    "Sayori tomo uno."

    s "Podemos escribir algo."

    mc "¿Ahora?"

    s "Sí."

    mc "¿Qué se supone que tengo que poner?"

    s "Algo que quieras hacer después de graduarte."

    mc "Eso es demasiado amplio…"

    s "¡Esa es la gracia!"

    "Sayori se quedó mirando el papel."

    "Y por primera vez desde que habíamos salido, dejó de bromear."

    "Ella se quedó pensando por unos segundos, y empezó a escribir."

    "Yo, decidí tratar de mirar por encima de su hombro."

    s "¡No mires!"

    mc "Solo tenía curiosidad."

    s "La curiosidad mato al gato, ¿Recuerdas?"

    "Dice Sayori en un tono que no suena amenazante en absoluto."

    mc "¿Qué has puesto?"

    s "Bueno, ahora sí puedes mirar."

    "Ella me pasa el papel doblado."

    s "Quiero que lo leas."

    mc "Espera, antes de eso…"

    "Cogí otro papel, y escribí el mío."

    "Termine de escribir, y Sayori, al igual que yo, intentó mirar."

    s "¿Qué has puesto?"

    "Le extiendo mi papel y ella lo toma"

    mc "Quiero que ambos leamos el del otro."

    s "Oh, suena bien…"

    "Sayori sonríe suavemente."

    "Ella finalmente lee mi papel."

    mc "¿Y?"

    s "Es bonito."

    mc "¿Solo bonito?"

    s "Sip."

    mc "Honestamente esperaba algo más."

    s "Jaja, no te preocupes [player], es algo lindo de tu parte que hayas compartido esto conmigo…"

    "Tras decir esto, siento que un calor recorre mi pecho mientras mis mejillas se tiñen de rojo."

    "Sayori lo nota, pero parece no querer meterse conmigo por eso ahora."

    "Ella sonrió otra vez, y señaló mi papel."

    "¿De verdad quieres eso?"

    "Yo también termino sonriendo."

    mc "Supongo que sí."

    s "¡Entonces yo también!"

    mc "¿Uh? ¿Tú también qué?"

    "Sayori lanza una última mirada a mi papel, antes de devolverlo, aún con su enigmática sonrisa."

    s "No es nada."

    "Decidí no insistir más, en cambio, mire finalmente lo que había escrito:"

    "Ver qué clase de persona terminó siendo."

    "Me quede algunos segundos en silencio."

    mc "Este es bastante bueno."

    s "¿Lo es?"

    mc "Lo es…"

    "Sayori volvió a mirar el panel."

    s "Hay tantas cosas que todavía no sabemos…"

    mc "Supongo que sí."

    s "Podemos descubrirlas después."

    mc "¿Después de graduarnos?"

    s "Sí..."

    "Ella se giro hacía mí con una sonrisa."

    s "Y"

    "Me quede mirándola fijamente."

    mc "¿Y ahora qué?"

    "Sayori se mete las manos en los bolsillos."

    s "¡Ahora podemos buscar algo para comer!"

    mc "Debí saber que acabaríamos hablando de comida."

    s "Jeje, sé que nada de mí puede sorprenderte."

    mc "A veces creo que tienes un segundo estomago o algo así."

    "Y así, pasamos el resto del tiempo juntos."

    # Se corta la escena.

    # Pasamos a la habitación de MC, al día siguiente:

    "Amanecí un sábado."

    "Después de cenar en un sitio sencillo con Sayori, se hizo bastante tarde."

    "Ninguno de los dos dijo nada al respecto."

    "Cuando llegamos a casa y ella se quedó mirando el reloj."

    "Su expresión decía que ella ya sabía que era demasiado tarde como para volver sola a su casa."

    "Así que simplemente se quedó."

    "Yo le presté una camiseta vieja y también una manta extra."

    "Y sin mucho drama, acabó durmiendo en mi cama."

    "Yo me acomodé al borde."

    "Lo más lejos posible para no invadir su espacio, o al menos eso intenté..."

    "Cuando abrí los ojos, la luz de la mañana entraba suave por la ventana."

    "Sayori seguía profundamente dormida a mi lado."

    "Con el pelo revuelto y una expresión completamente relajada."

    "Dormía como un bebé... o como una marmota."

    "Aunque mejor dicho... Una marmota bebé."

    "Me quede mirándola más, era tan extraño verla así, tan quieta."

    "Sobretodo cuando recuerdo que está en movimiento constante, hablando o riendo, o quizás arrastrándome a alguna idea absurda."

    "Ahora solo podía escuchar su respiración densa y pausada, sin preocupaciones visibles."

    "En mi infinita amabilidad, decidí no despertarla."

    "Me levanté con cuidado, me puse una camiseta y bajé a la cocina."

    "Por alguna razón me apetecía hacer algo, y no era solo para mí."

    "Abrí la nevera, revisé lo que había y empecé a preparar el desayuno."

    "Tostadas, un par de huevos con fruta que no estuviese demasiado madura y café."

    "Nada sofisticado, pero al menos olía bastante bien."

    "Seee, estoy satisfecho..."

    "Mientras cocinaba, me dí cuenta de que estaba... bien."

    "Me sentía menos apagado, cómo si un interruptor dentro de mí se hubiese encendido después de estos días."

    "La verdad es que no recuerdo haber consumido drogas, pero me siento bastante más ligero de lo normal."

    "Y como era de esperarse, el olor de la comida hizo su trabajo."

    "Escuche pasos suaves, y al girarme."

    "Vi a Sayori asomarse por la puerta de la cocina."

    "Sus ojos seguían medio cerrados y su pelo era un auténtico desastre."

    "Llevaba mi camiseta, la cual le quedaba bastante grande."

    "Mientras se frotaba un ojo con su mano."

    s "Huele bien..."

    mc "Buenos días, Sayori. Parece que se te han pegado las sábanas."

    "Ella se acerco un poquito más, apoyándose en la encimera mientras yo terminaba de servir los platos."

    "Me miro por un breve momento, como si se diera cuenta de algo."

    s "¿De verdad eres [player]?"

    mc "¿Cómo?"

    s "Simplemente parece que de verdad estás aquí."

    "Me quedé quieto un momento, removiendo el café con la cuchara."

    "Sonrío mientras miro tranquilamente a Sayori."

    mc "¿Eso es un cumplido?"

    s "Un cumplido, creo…"

    "Sonríe un poco, aún somnolienta, pero despertando más."

    s "Parece como si... no sé ¿acaso te ha sentado bien todo esto?"

    "Me tomé mi tiempo para procesar la pregunta."

    "Le pase un plato y me senté frente a ella."

    mc "Tal vez."

    "Ella tomo un bocado, y cerró los ojos, disfrutando."

    s "Hmmm~ Eshta bueno."

    "Yo también tomo un bocado."

    mc "¿A qué shi~?"

    "Después de masticar, trago la comida de una vez."

    mc "Supongo que pasar tiempo contigo no es tan malo."

    s "Qué detallista eres, [player]."

    mc "Solo callate y come antes de que la comida se ponga fría."

    "Sayori y yo decidimos seguir comiendo tranquilamente."

    "Creo que este va a ser un buen fin de semana."

    # Se corta la escena.

    "Lunes."

    "Me desperté más temprano de lo normal. No sabía muy bien por qué.. O tal vez sí."

    "Desde el fin de semana con Sayori, mis mañanas se sentían aunque sea un poco distintas."

    "Me sentía más ligero, como si estos días con Sayori hubiesen cambiado algo en mí."

    "Las clases iniciaron sin nada especial."

    "Natsuki me lanzó un par de miradas raras en el pasillo."

    "Yuri me saludo con su usual “hola” callado."

    "Y Monika me recordó que en el club íbamos a organizar los materiales para la próxima actividad."

    "En el descanso, Sayori me encontró y me habló de un sueño absurdo que había tenido, riéndose de si misma como siempre."

    "Todo parecía en orden."

    "Demasiado en orden."

    "Cuando llegamos al club, Monika tenía una lista en la mano."

    m "Okay, ¡todo el mundo!"

    "Monika empieza a hablar en tono práctico."

    m "Necesitamos papel de colores, cinta un par de cartulinas más... y probablemente también necesitemos marcadores."

    m "El presupuesto del club no es exactamente grande, así que tendremos que organizarnos."

    "Natsuki miraba la lista con el celo fruncido."

    "Parecía estar sumando precios en voz baja, su postura era bastante tensa."

    "Sayori, estaba se gada a su lado."

    "Y se dio cuenta al momento."

    "Se inclinó hacia ella con esa naturalidad habitual."

    s "¿Te preocupa algo?"

    n "¿Eh?"

    "Natsuki levanta la mirada."

    n "No..."

    s "Oh, ¿Estás segura?"

    n "Sí..."

    s "Lo digo porque estás haciendo esa cara."

    "Natsuki suspira con frustración, parecía no tener mucha paciencia hoy"

    n "¿De qué cara estás hablando?"

    s "La que usas cuando piensas mucho en algo."

    n "No estoy pensando mucho en nada..."

    s "Jeje~, sí lo estás haciendo."

    n "¡Qué no!"

    "Sayori parpadeo un poco y luego sonrió nuevamente."

    s "Vale."

    "Natsuki se quedó callada, aún más incómoda."

    "Volvió a mirar la lista."

    n "Son bastantes cosas…"

    m "No te preocupes demasiado, podríamos comprarlo poco a poco."

    m "Incluso podríamos reutilizar parte del material del festival."

    "Dice Monika en su habitual tono pacífico."

    n "Aun así..."

    "Natsuki suspira nuevamente."

    n "Probablemente el dinero no va a alcanzar."

    "Sayori inclinó la cabeza."

    s "¿Cuánto falta?"

    n "No te debería importar…"

    s "Pero si falta poco…"

    n "Sayori."

    "El tono de Natsuki provocó que Sayori guardara silencio por un segundo."

    "Yo las observaba desde el otro lado del aula."

    "Definitivamente pude notar que había algo que estaba mal."

    "Lejos del presupuesto, Natsuki parecía estar más cansada de lo habitual."

    "Sayori volvió a mirar los números."

    s "Yo podría poner una parte."

    "Natsuki se quedó quieta."

    n "¿Q-qué?"

    s "Dinero, podría poner un poco para que no tengamos que preocuparnos tanto."

    n "No."

    s "No pasa nada."

    n "He dicho que no…"

    s "Natsuki, de verdad, no me importa…"

    n "¡Pues a mí sí!"

    "Sayori dejó de sonreír un momento."

    s "Yo… únicamente trataba de ayudar."

    n "Ya lo sé."

    "Pese a eso, Natsuki seguía intranquila."

    "Y Sayori la miraba en silencio."

    s "Entonces... ¿Por qué estás tan enfadada..?"

    "Natsuki apretó el papel entre sus dedos."

    n "Porque no necesito que me ayudes…"

    s "Natsuki, solo dije que podía poner un poco."

    n "¿No será porque te doy lástima?"

    "El aula quedó en silencio."

    "Sayori tardo en responder, su expresión mostro una mayor confusión."

    s "¿Eh? ¡Claro que no, Natsuki!"

    s "No quise hacerte sentir mal, yo solo…"

    n "¿Entonces que es?"

    s "Es porque somos amigas."

    n "No por ser amigas significa que debes ayudar en todo."

    s "Solo quería ayudar al club…"

    n "Je, claro…"

    "Natsuki soltó una risa seca, sin humor."

    n "Siempre haces lo mismo."

    mc "Natsuki..."

    "Sin embargo, Natsuki ni siquiera me miro."

    n "Siempre tienes que arreglarlo todo. Que todo tiene que estar bien contigo..."

    n "Si alguien está deprimido, simplemente sonríes. O si alguien tiene un problema, le dices que “todo estará bien”."

    n "O si algo no sale bien... intentas solucionarlo siempre."

    "Sayori permaneció completamente inmóvil."

    n "Pero no siempre funciona..."

    n "No todo se puede arreglar con una sonrisa, Sayori."

    n "No puedes ir por ahí actuando como si todo fuera fácil... ¡porque no lo es!"

    "Sayori bajo la mirada lentamente, Natsuki pareció darse cuenta de lo que salía de su boca."

    "Su expresión se suavizó por un momento."

    n "Yo..."

    "Pero el estrés podía más."

    n "¡No necesito que me tengas lástima!"

    "Sayori levantó la mirada, aún bastante relajada."

    s "Vale..."

    n "Sayori, yo no..."

    s "Está bien, Natsuki."

    "La sonrisa de Sayori ya no era la de antes, era más pequeña y educada."

    s "No pasa nada."

    n "Sí que pasa, solo quería decir qu-"

    s "Ya entendí."

    "Sayori simplemente se levantó, recogió su mochila sin prisas."

    "Se movia de forma bastante cuidadosa."

    y "Sayori... no tienes qué irte, podemos hablarlo calmadamente."

    "Natsuki, dándose cuenta de lo que había dicho, intento detenerla de igual modo."

    n "Espera, no... no era para tanto. Solo..."

    "Sayori se colgó la mochila."

    s "Natsuki."

    s "Ya dije que no pasa nada."

    m "Sayori, quédate, por favor."

    "Yuri asintió, y casi en un susurro dijo:"

    y "No te vayas así..."

    "Sayori las miro a todas un momento, después hizo una pequeña inclinación de cabeza."

    "Es que usaba cuando quería cortar una conversación sin pelear."

    s "Estoy bien, de verdad..."

    "Y entonces salió."

    "La puerta se cerró con un clic suave."

    "El silencio que dejó fue bastante pesado en el aula."

    "Yo me quedé mirando el sitio donde había estado sentada."

    "Natsuki apretaba los dientes y estaba cabizbaja."

    "Monika se llevó una mano a la sien."

    "Yuri apretaba el borde de su libro con más fuerza de lo normal."

    "Ninguno había conseguido detenerla."

    "Nos quedamos en silencio."

    "La puerta todavía estaba cerrada, pero ninguno de nosotros parecía saber que hacer con el silencio había dejado Sayori."

    mc "¿Natsuki...?"

    "Natsuki no respondió rápidamente, seguía bastante tensa."

    mc "Creo que te pasaste..."

    n "Lo sé..."

    n "¿Pero acaso lo que he dicho es mentira?"

    m "Hmmm, Natsuki, si estabas enojada, igualmente podrías haberle hablado de otra manera."

    "Monika se acerco un poco."

    n "Que sí..."

    "Yuri, tímidamente, se pone delante de nosotros para decir algo."

    y "Creo que... todos pusimos ver qué estás pasando por algo ahora mismo... ¿Estoy en lo correcto o...?"

    "Natsuki levantó la mirada hacia Yuri."

    n "¿Cómo?"

    y "Hoy te ves... ya sabes, ¿Más tensa?"

    y "Y cuando viste el precio de los materiales, parecías preocupada."

    "Natsuki volvió a bajar la mirada."

    n "Mi papá perdió su trabajo."

    "El aula se quedó en silencio nuevamente."

    mc "¿Qué?"

    "Intento procesar está información lo mejor posible."

    n "Hace unos días..."

    "Se encogió un poco de hombros, tratando de restarle la mayor importancia posible."

    n "Fue despedido, y no ha podido conseguir otro trabajo."

    m "Natsuki... No tenías porque ocultarnoslo."

    n "¡Sí tenía!"

    n "Yo... solo... no quería que nadie empezara a tratarme diferente por ello."

    "La voz de Natsuki parecía ahora más cansada que enfadada."

    n "En casa estamos intentando arreglarnoslas... tenemos que pagar las cosas de siempre, comprar comida, las facturas..."

    n "Y luego llego aquí y veo que hay que comprar un montón de cosas para una actividad..."

    "Ella observa la lista que había dejado sobre la mesa."

    n "Y sí, estoy... preocupada."

    mc "Natsuki, lamento mucho todo esto, pero concuerdo con Monika en qué podrías habérnoslo dicho."

    n "¿Qué habría cambiado?"

    n "¿Qué todos me dijeran que no me preocupara por esto?"

    n "¿Qué me dijeran que todo va a salir bien?"

    "Natsuki frunció en ceño."

    n "Y eso es lo que más me fastidia de Sayori…"

    "Monika, Yuri y yo intercambiamos miradas, los tres estamos preocupados."

    n "Siempre dice que vamos a encontrar una manera..."

    n "Y que “todo saldrá bien”."

    n "Yo sé que lo hace porque quiere ayudar, pero a veces simplemente quisiera que entendiera de una vez."

    n "Que entendiera que no todo se arregla solo por creer que todo irá sobre ruedas."

    mc "Entiendo."

    n "¿Ahora entienden por qué dije lo que dije?"

    mc "Sí..."

    mc "Pero... yo sé la clase de persona que es Sayori..."

    n "..."

    mc "Y si hay algo que te puedo asegurar, es que no es del tipo de persona que querría hacerte sentir menos por algo que no es culpa tuya."

    mc "Probablemente solo buscaba ayudarte."

    n "Sí..."

    n "Pero ese es el problema."

    mc "¿El problema?"

    n "Que sé que no lo hizo con mala intención."

    n "Yo sé que solo intentaba hacerme sentir más tranquila."

    n "Pero estaba tan harta de todo que cuando empezó a hablar de poner dinero para los materiales y ayudarme..."

    "Suspiro."

    n "Sentí que me estaba teniendo lástima."

    m "¿Y por eso explotaste de esa manera?"

    n "Sí..."

    "Se hizo un breve silencio."

    n "Pero eso no significa que me arrepienta de todo lo que he dicho o pienso..."

    n "Sigo pensando que Sayori quiere solucionarlo todo con ese optimismo excesivo."

    n "Y seguiré pensando que no siempre es necesario."

    n "Solo..."

    "Se tensa un poco al recordar lo que dijo."

    n "No tuve que decírselo de esa manera..."

    mc "Natsuki, yo... Creo que ahora veo esto de una forma distinta..."

    n "Lo sé."

    y "Creo que Sayori también entendera que estabas molesta."

    y "Pero seguramente le hizo sentir mal..."

    "Natsuki cerró brevemente los ojos."

    n "Ya me di cuenta."

    m "Creo que solo deberíamos darle más espacio y tiempo."

    mc "Sí..."

    "Miré hacia la puerta."

    mc "Pero no quiero dejarla sola, ni me sentiría tranquilo conmigo mismo..."

    n "..."

    n "Ve."

    mc "¿Eh?"

    mc "¿Estás segura? ¿crees que debería?"

    n "Sí."

    "Natsuki levantó la mirada hacia mí."

    n "Ve a buscarla."

    n "Y dile que..."

    n "Dile que lo siento..."

    "Le soy una sonrisa pequeña a Natsuki."

    mc "Lo haré..."

    mc "Se lo diré."

    n "¡P-pero no le vayas a decir que estaba totalmente equivocada y que me arrepiento de todo!"

    "Parece que ha vuelto, aunque sea por un momento, la Natsuki de siempre."

    mc "Jeje, no te preocupes, no lo haré..."

    n "Bien."

    n "Porque sigo pensando lo mismo..."

    mc "Sí sí, ya me quedo claro."

    n "Idiota."

    "Me levante de mi asiento y tomé mi mochila."

    m "[player]."

    "Me volteé a ver a Monika antes de llegar a la puerta."

    m "Ten cuidado con ella, por favor."

    mc "Lo tendré..."

    y "Por favor, asegúrate de que ella esté bien..."

    "Dice Yuri con su casual tono bajo."

    "Hago un gesto de aprobación."

    "Mire una ultima vez al aula."

    "Y entonces salí..."

    "Tenía que ir donde estaba ella."

    "Salí del aula intentando no correr."

    "Ya que no tenía ni idea de que le iba a decir cuando la viese."

    "Y pensé que caminar más lento me ayudaría a pensar en ello."

    "Sayori había salido unos minutos antes, así que probablemente ya estaría llegando a casa."

    "El camino de me hizo más corto de lo normal, y para cuando llegué, me quedé parado en la puerta de su casa."

    "Mire la puerta, levante la mano... y luego sentí como si se bajara sola."

    mc "¿Debería tocar?"

    "*suspiro*"

    "Al final podía quedarme ahí todo el día... o.... Simplemente entrar, pese a que pudiese enojarse conmigo por entrar."

    mc "¿Sayori?"

    "No hubo respuesta, entré con mucho cuidado y cerré detrás de mí, todo parecía demasiado tranquilo."

    "Avancé un poco y la vi, ella estaba sentada en el sofá, inclinada hacia adelante."

    "Los brazos apoyados sobre sus piernas."

    "La mochila olvidada a un lado."

    "Parecía estar más cansada que otra cosa."

    "Mejor dicho, es como si toda su energía para el resto del día se hubiese agotado."

    mc "Hola."

    s "¿[player]?"

    mc "Hola otra vez..."

    s "¿Qué estás haciendo aquí?"

    mc "Quise venir a verte."

    s "¿Hasta aquí?"

    mc "Sip."

    s "Debí saberlo."

    mc "Sayori..."

    s "Vale, vale..."

    "Intento sonreír, pero era una sonrisa pequeña y no la de cuando estaba realmente contenta."

    s "Bueno, te conozco, así que creo que esto tampoco se me hace tan raro de tu parte."

    "Sayori se hizo a un lado en el sofá, y palmeo un lugar al lado suyo."

    s "Sientate..."

    "Me senté junto a ella."

    "Durante unos segundos, no dijimos nada."

    "La mire de reojo, seguía con esa expresión de agotamiento."

    mc "¿Estás bien?"

    s "Es la pregunta que más me esperaba de ti."

    mc "Es que últimamente parece que siempre tengo que hacértela."

    s "Eres bastante considerado."

    mc "Hablo en serio..."

    s "Jaja, yo también."

    "Sonrió un poco, está vez parecía más auténtica su sonrisa."

    mc "Natsuki está arrepentida."

    "Su sonrisa se le bajó un poco."

    s "¿Lo está?"

    mc "Sí."

    s "¿Te dijo algo?"

    mc "Ella me pidió que te dijera cómo se siente."

    "Sayori bajó la mirada."

    s "Ya..."

    mc "Ella dijo que no quiso decirlo de esa manera..."

    s "¿Entonces que quiso decir?"

    mc "Simplemente creo que estaba muy estresada."

    s "¿Es por los materiales?"

    mc "Bueno, en parte..."

    s "¿Hay algo más? ¿Qué pasó?"

    "Me quede callado un momento, sentía incomodad, ya que Natsuki no quería que nadie más supiera de esto."

    "Pero pensé que era bueno que Sayori lo supiese."

    mc "Su padre perdió su trabajo hace unos pocos días..."

    "Sayori me miro fijamente."

    s "¿Qué?"

    mc "Lo despidieron."

    s "No sabía nada de nada..."

    mc "Ella tampoco quiso que nadie lo supiera."

    s "Oh..."

    "Sayori se quedó procesando esa información, mirando al suelo."

    s "¿Entonces por eso se encontraba de esa manera?"

    mc "Sí."

    s "Y cuando le ofrecí poner dinero..."

    mc "Ella sintió que le tenías lástima."

    s "Yo no..."

    "Ella se detiene."

    s "Yo no quise hacer eso."

    mc "Lo sé..."

    s "Solo quise ayudar."

    mc "También lo sé."

    "Sayori se abrazo un poco a su misma."

    s "Cielos, ahora me siento un poco mal."

    mc "No tienes que perdonarla pronto si no quieres, es mejor que te tomes tu tiempo."

    s "Lo sé."

    s "No voy a pretender como si no hubiera pasado nada..."

    s "Pero me alegro de saber qué estaba pasando."

    mc "¿Te encuentras mejor?"

    s "Un poquito."

    mc "¿Eso significa que puedo intentar animarte?"

    s "Estas en tu derecho de intentarlo."

    mc "¿Y que pasa si fracaso?"

    s "Tendrás que intentarlo nuevamente..."

    mc "¿Y si fracaso por segunda vez?"

    s "¡Tendrás que comprarme comida!"

    s "Soy una chica bastante exigente..."

    "Solte una carcajada, seguido de ella."

    "Durante un rato, hablamos de cualquier cosa menos de lo ocurrido."

    "De una profesora, de una película, del club y cualquier tontería que hiciera que nuestro tiempo juntos fuese menos pesado."

    "Y funcionó, un poco..."

    "Después de un rato parecía más relajada, pero todavía había algo en su cara, que no desaparecía del todo."

    mc "Sayori."

    s "¿mmm?"

    mc "¿Estás enfadada?"

    "Esta vez no sonrió."

    s "Sí..."

    "La respuesta fue bastante más directa de lo que esperaba."

    s "Estoy enfadada, y mucho."

    "Miro hacia el techo."

    s "Porque soy como cualquier persona, no soy una muñeca con pulso, [player]."

    "Su tono no era algo, muchísimo menos agresivo."

    "Pero era firme."

    s "Ahora ya sé porque Natsuki estaba así, entiendo un poco mejor lo que pasó en realidad."

    s "Entiendo que esté preocupada, incluso puedo entender que no quisiera que le tuviese lástima."

    s "También sé que no todo de mí debe agradarle."

    "Respiro hondo."

    s "Pero eso no significa que deje de dolerme lo que me dijo."

    mc "Comprendo..."

    s "Estoy enfadada, y me siento mal... Pero eso no significa que eso no esté bien."

    "Sayori me mira directamente a los ojos."

    s "Tampoco voy a hacerme la loca y olvidar lo que me dijo solo porque sé que estaba pasando por algo o porque es mi amiga."

    mc "Y no tienes por qué hacerlo."

    s "¿Pero sabes? Eso no significa que deba a tratar a Natsuki como si fuera una basura."

    "Su expresión se endurece un poco más."

    s "No planeo humillarla, y mucho menos devolverle el golpe."

    s "No porque este enfadada significa que debo convertirme en una bravucona..."

    mc "Pienso que eso dice bastante de ti."

    s "Nop."

    "Ella niega con la cabeza ante lo que he dicho."

    s "Simplemente no busco rebajarme a mí misma."

    "Me mantuve en silencio ante las palabras de Sayori"

    s "Lo que dijo estuvo mal, y en parte entiendo por qué lo dijo."

    "Yo solo asiento."

    s "Además..."

    "Su expresión se suavizó."

    s "Jamás voy a dejar de poder enfadarme."

    mc "Me alegra de que puedas hacerlo..."

    "Ella me mira ligeramente confusa."

    s "¿Enfadarme contigo?"

    mc "Nope."

    mc "El hecho de que sepas contarme todo esto."

    "Sayori me miro por unos segundos, y posteriormente apoyo su cabeza sobre mi hombro, dejándose caer. Claramente aún sigue agotada."

    s "Gracias por venir..."

    mc "No tienes que agradecerme por eso."

    s "Sí tengo."

    mc "¿Hmmm? ¿Por qué?"

    s "Porque sin ti, podría haberme quedado sola pensando demasiado..."

    "Empece a sentir un calorcito en mi pecho, sentí como mis mejillas se enrojecían."

    "Y finalmente, decidí simplemente quedarme aquí con ella."

    "Quizá eso es lo que realmente necesitamos..."

    # Se corta la escena, pasamos al día siguiente:

    "Las clases pasaron sin nada especialmente memorable."

    "Los profesores solo hablaban de cosas que olvidaríamos antes de llegar a casa."

    "Durante el descanso, Sayori parecía haber vuelto a su humor habitual, riéndose como si nada."

    "Pero ambos sabíamos que lo de ayer no había desaparecido."

    "Y no era algo fácil de borrar por solo una noche."

    "Durante el recreo, se acercó a mí inmediatamente al encontrarme frente a la multitud de estudiantes."

    s "Hola."

    mc "Hola."

    s "¿Dormiste bien?"

    mc "Más o menos."

    s "Seee, yo tampoco."

    mc "Ya veo... ¿Tienes algo que ver con lo de ayer?"

    "Sayori permaneció callada, mirando hacia el suelo, claramente pensativa."

    s "Un poco..."

    mc "Dejame adivinar, ¿Sigues molesta?"

    s "Algo así."

    "Lo dijo de forma sorpresivamente directa."

    s "Aunque me parece que ya no tanto como ayer."

    mc "Eso está bastante bien."

    s "Seguramente…"

    "Sayori metió sus manos en sus bolsillos mientras su expresión demostraba que estaba pensando y dándole muchas vueltas a algo."

    s "Estuve pensando en Natsuki."

    mc "¿Te aparece hablar con ella?"

    s "No lo sé... Yo..."

    s "Una parte de mi quiere, pero la otra parte de mi quiere que lo deje pasar y ya..."

    mc "¿A qué parte creés que deberías escuchar?"

    s "No tengo la menor idea."

    mc "Si quieres podemos esperar."

    s "¿Esperar? ¿Esperar el qué?"

    mc "A que sepas que le puedes decir."

    "Sayori me mira de reojo con una sonrisa medio cansada."

    s "Eres bastante paciente cuando quieres..."

    mc "No te acostumbres."

    s "Lo único que quiero es que esto no se quede así..."

    mc "¿Por?"

    s "Porque ella es mi amiga de todos modos, incluso cuando estoy enfadada con ella."

    s "Quizás debería hablar con ella."

    mc "Cuando quieras, siempre puedes contar con mi apoyo."

    "Sayori me mira fijamente a los ojos."

    s "¿Vas a estar ahí?"

    mc "Síp."

    s "¿Incluso si se pone raro?"

    mc "No veo por qué no."

    "Sayori soltó una pequeña risa, aunque nerviosamente"