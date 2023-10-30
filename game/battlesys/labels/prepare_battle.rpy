label prepare_tutorial_battle:
    play music "audio/battle.mp3"
    python:
        # Battle_state
        battleState = Battle_state(pythonTutorialPC, icEnemyTeam)
    scene battle_wall with dissolve
    "Battle Begin!"
    show player_box
    show enemy_box
    call show_fighters
    show screen hp_bars_1v1 onlayer master
    $ battleState.current_stage = "Battle_begin"
    call check_passive_time_beforeBP
    call turn_start
    $ teste0_Acertos = str(battleState.getEnemysDefeated())
    $ teste0_Nota = str(round(battleState.getTestGrade(), 2))
    return