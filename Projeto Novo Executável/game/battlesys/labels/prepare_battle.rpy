label prepare_tutorial_battle:
    play music "audio/battle.mp3"
    python:
        # Battle_state
        battleState = Battle_state(pythonTutorialPC, icEnemyTeam)
        broughtItem = False
    scene battle_wall with dissolve
    "Battle Begin!"
    show player_box
    show enemy_box
    show screen hp_bars_1v1 onlayer master
    call show_fighters from _call_show_fighters
    $ battleState.current_stage = "Battle_begin"
    call check_passive_time_beforeBP from _call_check_passive_time_beforeBP
    call turn_start from _call_turn_start
    python:
        teste0_Acertos = str(battleState.getEnemysDefeated())
        teste0_Nota = str(round(battleState.getTestGrade(), 2))
    return

label prepare_battle_1:
    play music "audio/battle.mp3"
    scene battle_wall with dissolve
    menu:
        "Choose your partner:"
        "Java":
            $ partner = javaPC
        "Python":
            $ partner = pythonPC
        "Ruby":
            $ partner = rubyPC
        "Lua":
            $ partner = luaPC
    $ battleState = Battle_state(partner, calculusEnemyTeam)
    $ broughtItem = True
    $ bItem = [True, True, False, False]
    "Your partner brought items!"
    "Battle Begin!"
    show player_box
    show enemy_box
    show screen hp_bars_1v1 onlayer master
    call show_fighters from _call_show_fighters_1
    $ battleState.current_stage = "Battle_begin"
    call check_passive_time_beforeBP from _call_check_passive_time_beforeBP_1
    call turn_start from _call_turn_start_1
    python:
        teste1_Acertos = str(battleState.getEnemysDefeated())
        teste1_Nota = str(round(battleState.getTestGrade(), 2))
        if battleState.getTestGrade() > 5:
            if partner == pythonPC: 
                pythonLoveCounter += 3
            if partner == javaPC: 
                javaLoveCounter += 3
            if partner == rubyPC: 
                rubyLoveCounter += 3
            if partner == luaPC: 
                luaLoveCounter += 3
        else:
            if partner == pythonPC: 
                pythonLoveCounter -= 1
            if partner == javaPC: 
                javaLoveCounter -= 1
            if partner == rubyPC: 
                rubyLoveCounter -= 1
            if partner == luaPC: 
                luaLoveCounter -= 1
    return

label prepare_battle_2:
    play music "audio/battle.mp3"
    scene battle_wall with dissolve
    menu:
        "Choose your partner:"
        "Java":
            $ partner = javaPC
        "Python":
            $ partner = pythonPC
        "Ruby":
                $ partner = rubyPC
        "Lua":
            $ partner = luaPC
    $ battleState = Battle_state(partner, edaEnemyTeam)
    $ broughtItem = True
    $ bItem = [True, True, True, True]
    "Your partner brought items!"
    "Battle Begin!"
    show player_box
    show enemy_box
    show screen hp_bars_1v1 onlayer master
    call show_fighters from _call_show_fighters_2
    $ battleState.current_stage = "Battle_begin"
    call check_passive_time_beforeBP from _call_check_passive_time_beforeBP_2
    call turn_start from _call_turn_start_2
    python:
        teste2_Acertos = str(battleState.getEnemysDefeated())
        teste2_Nota = str(round(battleState.getTestGrade(), 2))
        if battleState.getTestGrade() > 5:
            if partner == pythonPC: 
                pythonLoveCounter += 3
            if partner == javaPC: 
                javaLoveCounter += 3
            if partner == rubyPC: 
                rubyLoveCounter += 3
            if partner == luaPC: 
                luaLoveCounter += 3
        else:
            if partner == pythonPC: 
                pythonLoveCounter -= 1
            if partner == javaPC: 
                javaLoveCounter -= 1
            if partner == rubyPC: 
                rubyLoveCounter -= 1
            if partner == luaPC: 
                luaLoveCounter -= 1
    return

label prepare_java_battle:
    play music "audio/battle.mp3"
    scene battle_wall with dissolve
    $ battleState = Battle_state(javaPC, obmEnemyTeam)
    $ broughtItem = False
    "Battle Begin!"
    show player_box
    show enemy_box
    show screen hp_bars_1v1 onlayer master
    call show_fighters from _call_show_fighters_3
    $ battleState.current_stage = "Battle_begin"
    call check_passive_time_beforeBP from _call_check_passive_time_beforeBP_3
    call turn_start from _call_turn_start_3
    $ testeOBM_Acertos = str(battleState.getEnemysDefeated())
    $ testeOBM_Nota = round(battleState.getTestGrade(), 2)
    return