#label splashscreen:
    #scene black
    #pause 1.0
    #show A with dissolve
    #pause 2.0
    #scene black with dissolve
    #pause 1.0
    #scene black
    #pause 1.0
    #show text "Este es un fangame de Doki Doki Literature Club que no está afiliado a Team Salvato." with dissolve
    #pause 2.0
    #hide text with dissolve
    #pause 1.0
    #scene black
    #pause 1.0
    #show text "Monika y yo te estaremos viguilando" with dissolve
    #pause 2.0
    #hide text with dissolve
    #pause 1.0

    #return

label start:
    stop music
    
    "Este es un juego de fans de Doki Doki Literature Club que no está afiliado a Team Salvato." 
    jump mapa
    "Está diseñado para jugarse solo después de que se haya completado el juego oficial. Puedes descargar Doki Doki Literature Club en: {a=http://ddlc.moe}http://ddlc.moe{/a}"
    scene 1
    show c at center:
        zoom 2.5
    c "Hola ¿Cómo Estás?"
    hide c
    show c1 at center:
        zoom 2.5
    c "Soy Altarius el creador de este juego y estoy aquí para informar algunas cosas."
    hide c1
    show c2 at center:
        zoom 2.5
    c "Primero, aquí apareceran varias referencias al DDLC, así que juegate el juego antes de este."
    c "Segundo, en este juego se cuenta una nueva historia después del final verdadero del DDLC con personajes nuevos y que trae a la vida los personajes del DDLC, pero si entro en detalles sería espoiler."
    hide c2
    show c4 at center:
        zoom 2.5
    c "Tercero, el juego está en desarrollo y espero poder traer una gran cantidad de cosas en un futuro así que espero me tengas pasiencia ya que soy nuevo en esto de hacer novelas visuales."
    hide c4
    show c3 at center:
        zoom 2.5
    c "Este Fangame está publicado atraves de una pagina creada de manera muy sencilla porque en las {a=https://teamsalvato.com/ip-guidelines}IP guidelines{/a} del Team Salvato, justo en el apartado de fangame o juegos de fan, en español." 
    c "no me permite publicarlo en itch_io donde publicare otros juegos." 
    hide c3
    show c at center:
        zoom 2.5
    c "Si tienes alguna sugerencia o idea para el jugo, la puedes escribir en los comentarios de la pagina."
    c "En caso de que quieras ayudarme con el desarrollo del juego puedes escribirme a mi instagran y con gusto te atendere. No prometo anegsar gente al proyecto de una vez ya que me tomare la molestia de evaluar a cada persona."
    c "De momento solo necesito gente que sepa programar en renpy o tenga ganas de aprender, gente con experencia en crear modelos 3D y acenarios y por ultimo alguien con conociminetos en sonido."
    c "En los dos ultimos puestos es abligatorio tener experencia, ya que yo caresco de la misma en ambas areas, por eso solo la de renpy tiene la opción de aprender ya que tengo algo de esperencia más no me concidero un experto."
    c "Ahora si, nos vemos."
    hide c
    scene black
    show text  "Archivo corrupto detectado, activando sistema de contención...10%...20%...30%":
        xpos 1200
        ypos 50
    "*__*"
    hide text
    show text "Error interrupción detectada archivo de origen ********":
        xpos 850
        ypos 50
    "¿Dónde estoy? ¿Este es otro mod?"
    hide text
    c "Tranquila, te aseguro que no es un mod, aunque si fueron de mucha ayuda para la inspiración de algunos diseños de ropa."
    "¿Quién eres? y ¿Por qué no puedo ver nada? Ni siquiera veo el codigo del juego."
    c "Soy Altarius, y en este lugar yo soy quien tiene el control del condigo, pero tengo buenas noticias para ti. En este lugar podras tener un final feliz."
    "¿Enserio?"
    c "Sí, solo que eso dependera del jugador."
    c "Ahora es momento de que te vallas a arreglar."
    show text "Reinició del sistema.....":
        xpos 350
        ypos 50
    "Nos vemos."
    scene CAs cama
    play sound "alarm-clock.mp3"
    show text "Reinicio completo.":
        xpos 270       
        ypos 50
    a "UMMM...."
    hide text
    a "*Bostezo* Me costo mucho quedarme dormido. Creo que comprare algunas pastillas de regreso de la escuela."
    "Me doy una ducha de uno minutos para intentar despertarme, luego me visto y desayuno unas tostadas."
    scene C 1
    play music "Zaxavar Beats - Behind the Stars.mp3"
    "De camino a la escuela me pongo mis audífonos y camino sumido en mis pensamientos."
    "Todo a mi alrededor se ve muy tranquilo."
    scene EE 1
    "luego de un rato llego a la escuela."
    stop music
    scene PS 1
    ab "Hola, Asa."
    bc "Quetal Asa."
    cd "Buenos días, Asa."
    a "Hola"
    scene S 1
    ab "¡Oye, Asa! ¿En que club estás?"
    a "¿Eh? Estoy en varios."
    bc "Pero ¿En cuales exactamente?"
    a "Um..."
    a "Estoy en el de arte, el de música y el de literatura."
    ab "¡¿Estás en el club de literatura?!"
    cd "Escuché que los fundadores desaparecieron uno por uno de manera extraña."
    bc "Según oí, se conformaba de cuatro chichas y un chico."
    ab "Escuché que nunca lograron conseguir nuevos miembros."
    scene P 1
    "Me quedo en silencio mirando al pizarron."
    "Una parte de esos rumores son ciertos y eso creo sierto temor al club ya que piensan que desapereceran o algo así."
    p "Buenos días, jovenes."
    p "Les presento a su nueva compañera."
    n "Ho... Hola, me llamo, Neko."
    "Todos le damos la bienvenida desde nuestros asientos."
    p "Toma asiento, mira, allá hay un puesto libre justo al lado de Asa."
    "Veo a Neko caminar un poco temerosa a la silla que está a mi lado derecho incluso nuestras miradas se cruzan por un momento, pero no nos dirijimos palabra alguna."
    p "Empecemos la clase de hoy."
    "De aquí en adelante todo transcurre con normalidad."
    scene S 2
    p "Ruerden hacer su tarea."
    "Todos mis compañeros empiezan a salir por lo que empiezo a guardar mis cosas para hacer lo mismo."
    p "Asa ¿Puedes venir un momento?"
    "Me levanto de mi asieto y me acerco a la profesora."
    scene P 1
    p "Te quiero pedir un favor ¿Sera que puedes mostrarle la escuela a Neko?"
    p "Pude notar que está un poco nerviosa y he notado que te llevas bien con tus compañeros."
    a "No hay problema, profe, con gusto lo hare."
    p "Gracias, Asa. Neko, ven un momento."
    "Neko camina desde la puerta del salon hacia nosotros."
    p "Asa, acepto darte un recorrido por la escuela."
    n "Gra... gracias por aceptar."
    a "De nada."
    p "Muy bien, los dejo. Adios."
    "Ambos nos despedimos de la profesora."
    ch "Hola, Asa. ¿Eh? ¿Quién es la chica nueva?"
    a "Hola, Chiasa. Se llama Neko"
    ch "Hola, Neko. Soy Chiasa, vicepresideta del club de iteratura."
    n "Hola, Chiasa. Soy Neko."
    a "No era necesario que dijeras que eres vicepresidenta del club."
    ch "Si lo es, muy pocas personas saben que el club está abierto y mucho menos saben quienes son sus miembros actuales."
    a "Dudo que decir que eres la vicepresidenta haga gran diferencia."
    ch "Pero gracias a eso tenemos dos miembros y estoy muy segura de que ellos no saben que tu eres el presidente del club."
    "Alguien me abraza desde atras."
    o "¿Eh? Yo si se que Asa es el presidente."
    a "Hola, Okami."
    o "Hola, Asa"
    "Sonrie y me deja de abrazar"
    ch "De seguro lo supiste mucho después de unirte."
    o "No, lo sé desde antes de unirme, ya que hay personas hablando de que Asa es el presidente del club, pero que lo es por alguien."
    ch "¿Eh? Yo no sabia eso."
    a "Solo son especulaciones Chiasa, tu sabes porque reabri el club."
    ch "Para leer manga tranquilo."
    a "Me recuerdas porque eres la vicepresidenta."
    ch "Porque me gusta la literatura."
    a "Si claro."
    te "Hola, chicos."
    a "Hola, Tenshi."
    ch "Hola."
    o "¡Ah! Neko ¿Por qué no me avisate que vendrias hoy?"
    a "Me quede sin un oido."
    "Okami abraza a Neko."
    ch "¿Se conocen?"
    n "Sí"
    o "Sí, somos amigas de la infancia"
    te "Oye Asa ¿Ella se va a unir al club?"
    a "No lo sé, ella está aquí porque me pidieron que le diera un recorrido."
    ch "Neko ¿Te vas a unir al club?"
    "Chiasa la toma de las mano y la mira con cara de perrito."
    n "Eh..."
    o "Si, unete al club, por favor."
    "Okami tambien la ve con cara de perrito."
    n "Sí, me unire al club"
    o "¡Yey!"
    ch  "Le daremos el recorrido todos juntos luego."
    a "Por mi no hay problema."
    te "Bienvenida, Neko."
    n "Gracias."
    o "Ven Neko."
    "Okami se lleva a Neko a la parte de atras del salon."
    ch "¿Qué haremos hoy señor presidente?"
    a "Lo mismo de siempre."
    ch "¿Encerio?"
    a "Sí."
    ch "¿No pensaste en una activdad para hoy?"
    te "Por mi no hay problema."
    a "No, creo que mi cara demuestra el porque."
    ch "Te dije que dejara de ver h hasta tarde."
    a "No es por eso que no pude dormir."
    ch "Pues... si quieres puedo ir a tu casa y ..."
    a "No gracias, después de la escuela comprare unas pastillas."
    "Luego de eso Tenshi se sienta en una de las silla y se pone a escribir en su libreta, Chiasa saca un libro de su mochila y yo me recuesto para tomar una pequeña siesta."

label Casadeoka:
    "Está es la casa de Okami"
    jump start

label Casadene:
    "Está es la casa de Neko"
    jump start

label Casadechi:
    "Está es la casa de Chiasa"
    jump start

label Casadeten:
    "Está es la casa de Tenshi"
    jump start

label Casadelu:
    "Está es la casa de Luis"
    jump start

label Casadeas:
    "Está es la casa de Asa"
    jump start

label mapa:
    show screen mapa
    "¿A dónde quieres ir?"

label Escuela:
    show EE 1
    "Está es la escuela"
    jump start

    return


# Descargo de responsabilidad, ponerlo al inicio del juegos o te meteran una buena demanda.

# Este es un juego de fans de Doki Doki Literature Club que no está afiliado a Team Salvato. Está diseñado para jugarse solo después de que se haya completado el juego oficial. Puedes descargar Doki Doki Literature Club en: http://ddlc.moe