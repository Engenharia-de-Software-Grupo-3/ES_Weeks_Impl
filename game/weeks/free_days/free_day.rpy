label free_day_start:
    scene black
    "Hoje é um dia livre. O que fazer?"
    python:
        toJava = False
        libraryJava = False
        toRuby = False
        libraryRuby = False
        toPython = False
        libraryPython = False
        toLua = False
        libraryLua = False
        energy = 4
    while True:
        scene intro with dissolve
        show freeDay_menu_box
        $ freeDChoice = None
        $ energyScreen = "{b}{color=#ffae00}{size=95}" + str(energy) + "{/size}{/color}"
        call screen free_day_menu
        if freeDChoice == -1: # Sair
            "Não faça hoje, o que pode ser feito depois de amanhã."
            return
        elif freeDChoice == 0: # VER INVENTARIO
            call inventory
        elif freeDChoice == 1: # USAR ENERGÉTICO
            if itens_estado[0] <= 0:
                "Você não possui nenhum Energético ⚡"
            else:
                $ energy = 4
                $ itens_estado[0] -= 1
                "Java way of Life..."
                mc "Yeeeaahhhh mothafu-"
                "Sua energia foi restaurada ao máximo."
        else: # USA ENERGIA
            if energy <= 0:
                mc "Cara, não estou com vontade hoje."
                mc "Talvez amanhã..."
            else:
                call expression freeDChoice


screen free_day_menu:
    image "images/botoes, caixas e etc/energy icon.png":
        xalign 0.95
        yalign 0.6
        zoom 0.15
    text energyScreen:
        xalign 0.91
        yalign 0.60
    vbox:
        spacing 1
        xalign 0.91
        yalign 0.875
        xmaximum 400
        style_prefix 'battle'
        textbutton "▶ Ver Inventário" action [SetVariable('freeDChoice', 0), Return()]
        textbutton "▶ Usar Energético" action [SetVariable('freeDChoice', 1), Return()]
        textbutton ""
        textbutton "◀ Finalizar dia" action [SetVariable('freeDChoice', -1), Return()]
    frame:
        xalign 0.5
        yalign 0.55
        textbutton "Mercado Haskell" at center action [SetVariable('freeDChoice', "shop"), Return()]
    frame:
        xalign 0.3
        yalign 0.2
        textbutton "Pescar no Lago" at center action [SetVariable('freeDChoice', "toFish"), Return()]
    frame:
        xalign 0.8
        yalign 0.33
        textbutton "Estudar na Biblioteca" at center action [SetVariable('freeDChoice', "toLibrary"), Return()]
    frame:
        xalign 0.55
        yalign 0.12
        textbutton "Visitar Python" at center action [SetVariable('freeDChoice', 'toPython'), Return()]
    frame:
        xalign 0.63
        yalign 0.865
        textbutton "Visitar Java" at center action [SetVariable('freeDChoice', 'toJava'), Return()]
    frame:
        xalign 0.27
        yalign 0.8
        textbutton "Visitar Ruby" at center action [SetVariable('freeDChoice', 'toRuby'), Return()]
    frame:
        xalign 0.2
        yalign 0.44
        textbutton "Visitar Lua" at center action [SetVariable('freeDChoice', 'toLua'), Return()]
    
