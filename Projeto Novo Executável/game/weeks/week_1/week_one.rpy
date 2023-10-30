label semana_1:
    call .intro from _call_semana_1_intro
    $ d = 1
    while d <= 3:
        $ dia = 'semana1_dia' + str(d)
        call expression dia from _call_expression_1
        $ d = d + 1
    
    call free_day_start from _call_free_day_start
    call free_day_start from _call_free_day_start_1
    call free_day_start from _call_free_day_start_2
    return
label .intro:
    show black
    scene intro with dissolve
    mc "A gigantesca academia se eleva sobre todos os outros prédios na barulhenta área urbana."
    mc "É como se ela existisse no centro do mundo inteiro."
    mc "A Academia [school_name] recolhe estudantes de todas as áreas que pode encontrar" 
    mc "Funcionais, Orientados a Objetos, Lógicos; qualquer paradigma de linguagem, se mostrar potencial o suficiente, tem seu lugar aqui." 
    mc "É uma instituição do mais alto prestígio que o país pode oferecer" 
    mc "Seu esplendor é rivalizado apenas pelos boatos e mistérios que circulam-a todo semestre." 
    mc "E, por isso, Linguagens de Programação ao redor do globo lutam pela oportunidade de estudarem nesses corredores." 
    mc "Os estudantes que saem são vistos como figuras excepcionais, quase míticas aos olhos de alguns" 
    mc "Como nobres e realeza de tempos de outrora, imortalizados nos anais da história e fóruns do StackOverflow…" 
    mc "Então como foi que eu vim parar aqui?"
    return