label toLibrary:
    scene black with fade
    if libraryJava and libraryLua and libraryPython and libraryRuby:
        mc "Por que eu quero ir tantas vezes na biblioteca?"
        mc "Talvez eu precise de ajuda..."
        return
    menu:
        "Quem gostaria de chamar?"
        "Java" if not libraryJava:
            python:
                libraryJava = True
                javaLoveCounter += 1
                chosen = javaPC
                character = jav
                sprite0 = 'java 2'
                sprite1 = 'java'
                sprite2 = 'java 8'
                chosenFala1 = "Bastante prudente priorizar os estudos."
                chosenFala2 = "Se importa de eu lhe acompanhar?"
                livro1 = "Orientação a Objetos"
                skill1 = javaHitS
                livro2 = "Java Como Programar"
                skill2 = javaDefUpS
        "Lua" if not libraryLua:
            python:
                libraryLua = True
                luaLoveCounter += 1
                chosen = luaPC
                character = lua
                sprite0 = 'lua 2'
                sprite1 = 'lua 3'
                sprite2 = 'lua 7'
                chosenFala1 = "Uau, quem diria que você convidaria justo eu para isso."
                chosenFala2 = "É, acho que um estudo em grupo não faz mal de vez em quando."
                livro1 = "Programando em Lua"
                skill1 = luaHitS
                livro2 = "Game development with Lua"
                skill2 = luaAtkPlusS
        "Python" if not libraryPython:
            python:
                libraryPython = True
                pythonLoveCounter += 1
                chosen = pythonPC
                character = pyt
                sprite0 = 'pyth'
                sprite1 = 'pyth 13'
                sprite2 = 'pyth 12'
                chosenFala1 = "Vamos lá! Pode contar comigo."
                chosenFala2 = "Próxima batalha será moleza."
                livro1 = "Python Fluente"
                skill1 = pythonHitS
                livro2 = "Fundamentos de Python"
                skill2 = pythonCureS
        "Ruby" if not libraryRuby:
            python:
                libraryRuby = True
                rubyLoveCounter += 1
                chosen = rubyPC
                character = rub
                sprite0 = 'ruby'
                sprite1 = 'ruby 3'
                sprite2 = 'ruby 4'
                chosenFala1 = "Não sei se vou conseguir ajudar muito"
                chosenFala2 = "Mas adoraria estudar com você."
                livro1 = "Eloquent Ruby"
                skill1 = rubyHitS
                livro2 = "Ruby on Rails Tutorial"
                skill2 = rubyLuckUpS
        "Pensando melhor...":
            return
    $ energy -= 1
    scene biblioteca with dissolve
    show expression sprite1 with dissolve
    character "[chosenFala1]"
    show expression sprite2
    character "[chosenFala2]"
    $ chosen.levelUp()
    while (True):
        scene biblioteca with dissolve
        "Vocês estão estudando..."
        menu:
            "O que fazer:"
            "Conhecer [chosen.name] melhor":
                call .curriculo from _call_toLibrary_curriculo
            "Ver conteúdo":
                call .estudar from _call_toLibrary_estudar
            "Revisar e sair":
                show expression sprite2 with dissolve
                character "Foi um encontro muito produtivo. Obrigado por chamar."
                return
label .curriculo:
    show expression sprite0 with dissolve
    mc "Sinto que quero te conhecer melhor..."
    hide expression sprite0
    show expression sprite1
    character "Claro, vou pegar meu currículo do PET."
    hide expression sprite1 with moveoutright
    mc "Espera. Não foi isso q..."
    $ age = str(renpy.random.randint(18,21))
    show expression sprite1 at right with moveinright
    python: 
        nome = "Name: " + chosen.name
        tipo = "Type: " + chosen.type.name
        idade = "Age: " + age
        if not chosen.skill_set[0] is None:
            skill00 = " - " + chosen.skill_set[0].name
        else:
            skill00 = ""
        if not chosen.skill_set[1] is None:
            skill01 = " - " + chosen.skill_set[1].name
        else:
            skill01 = ""
        if not chosen.skill_set[2] is None:
            skill02 = " - " + chosen.skill_set[2].name
        else:
            skill02 = ""
        if not chosen.skill_set[3] is None:
            skill03 = " - " + chosen.skill_set[3].name
        else:
            skill03 = ""
    show screen characterCurriculo with dissolve
    character "Aqui está."
    hide expression sprite1
    show expression sprite0 at right
    mc "..."
    mc "Obrigado, [chosen.name]."
    hide screen characterCurriculo
    return
label .estudar:
    scene black with fade
    show book with dissolve
    while True:
        "O que estudar..."
        $ libraryChoice = None
        call screen libraryMenu
        call learnAbility(chosen, libraryChoice) from _call_learnAbility
        menu:
            'Continuar?'
            "Sim":
                pass
            "Não":
                return
    return

label learnAbility(character, skill):
    "Este livro contém a habilidade [skill.name]."
    "[skill.text]"
    "Gostaria de aprender esta habilidade?"
    menu:
        "Gostaria de aprender esta habilidade?"
        'Aprender [skill.name]':
            if skill in character.skill_set:
                "[character.name] já possui esta habilidade."
                pass
            elif None in character.skill_set:
                "[character.name] aprendeu [skill.name]"
                python:
                    for i in range(0, 5):
                        if character.skill_set[i] is None:
                            character.skill_set[i] = skill
                            break
            else:
                "[character.name] quer aprender [skill.name]."
                "Mas [character.name] já conhece quatro habilidades..."
                menu:
                    "Gostaria de trocar uma habilidade por [skill.name]?"
                    "Substituir habilidade":
                        menu: 
                            "Substituir habilidade..."
                            "[character.skill_set[0].name]":
                                $ sI = 0
                            "[character.skill_set[1].name]":
                                $ sI = 1
                            "[character.skill_set[2].name]":
                                $ sI = 2
                            "[character.skill_set[3].name]":
                                $ sI = 3
                        $ saida = character.skill_set[sI].name
                        "[character.name] esqueceu [saida]"
                        $ character.skill_set[sI] = skill
                        "[character.name] aprendeu [skill.name]"
                    "Pensando melhor...":
                        pass
        'Pensando melhor...':
            pass
    return

screen characterCurriculo:
    image "images/curriculo.png":
        xalign 0.5
        yalign 0.5
    vbox:
        xalign 0.561
        yalign 0.15
        spacing 30
        text nome at left
        text idade at left
        text tipo at left
    vbox:
        xalign 0.44
        yalign 0.45
        spacing 30
        text "• Abilities:" at left
        text skill00 at left
        text skill01 at left
        text skill02 at left
        text skill03 at left

screen libraryMenu:
    style_prefix 'battle'
    vbox:
        xalign 0.25
        yalign 0.5
        spacing 15
        textbutton "▶ Fundamentos de Matemática" at left action [SetVariable('libraryChoice', genericMathS), Return()]
        text "   →"
        text "   →"
        textbutton "▶ Análise de Sistemas" at left action [SetVariable('libraryChoice', genericAnalyS), Return()]
        text "   →"
        text "   →"
        textbutton "▶ Teoria da Computação" at left action [SetVariable('libraryChoice', genericTheoS), Return()]
        text "   →"
        text "   →"
        textbutton "▶ Inteligência Artificial" at left action [SetVariable('libraryChoice', analyBoostS_), Return()]
        text "   →"
        text "   →"
        textbutton "▶ Processar Linguagem Natural" at left action [SetVariable('libraryChoice', theoBoostS_), Return()]
        text "   →"
        text "   →"    
    vbox:
        xalign 0.74
        yalign 0.5
        spacing 15
        textbutton "▶ Técnicas de Algoritmos" at left action [SetVariable('libraryChoice', mathBoostS_), Return()]
        text "   →"
        text "   →"
        textbutton "▶ A Verdade Relativa" at left action [SetVariable('libraryChoice', confusedPlusS_), Return()]
        text "   →"
        text "   →"
        textbutton "▶ A Técnica do Chute" at left action [SetVariable('libraryChoice', luckKick), Return()]
        text "   →"
        text "   →"
        textbutton "▶ [livro1]" at left action [SetVariable('libraryChoice', skill1), Return()]
        text "   →"
        text "   →"
        textbutton "▶ [livro2]" at left action [SetVariable('libraryChoice', skill2), Return()]
        text "   →"
        text "   →"

