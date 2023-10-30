label prepare_tutorial_battle:
    play music "audio/battle.mp3"
    python:
        # Battle_state
        battleState = Battle_state(pythonTutorialPC, icEnemyTeam)
    scene battle_wall with dissolve
    "Battle Begin!"
    show player_box
    show enemy_box
    show screen hp_bars_1v1 onlayer master
    call show_fighters
    $ battleState.current_stage = "Battle_begin"
    call check_passive_time_beforeBP
    call turn_start
    $ teste0_Acertos = str(battleState.getEnemysDefeated())
    $ teste0_Nota = str(round(battleState.getTestGrade(), 2))
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
    "Battle Begin!"
    show player_box
    show enemy_box
    show screen hp_bars_1v1 onlayer master
    call show_fighters
    $ battleState.current_stage = "Battle_begin"
    call check_passive_time_beforeBP
    call turn_start
    $ teste1_Acertos = str(battleState.getEnemysDefeated())
    $ teste1_Nota = str(round(battleState.getTestGrade(), 2))
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
    "Battle Begin!"
    show player_box
    show enemy_box
    show screen hp_bars_1v1 onlayer master
    call show_fighters
    $ battleState.current_stage = "Battle_begin"
    call check_passive_time_beforeBP
    call turn_start
    $ teste2_Acertos = str(battleState.getEnemysDefeated())
    $ teste2_Nota = str(round(battleState.getTestGrade(), 2))
    return

label prepare_java_battle:
    play music "audio/battle.mp3"
    scene battle_wall with dissolve
    $ battleState = Battle_state(javaPC, obmEnemyTeam)
    "Battle Begin!"
    show player_box
    show enemy_box
    show screen hp_bars_1v1 onlayer master
    call show_fighters
    $ battleState.current_stage = "Battle_begin"
    call check_passive_time_beforeBP
    call turn_start
    $ testeOBM_Acertos = str(battleState.getEnemysDefeated())
    $ testeOBM_Nota = round(battleState.getTestGrade(), 2)
    return