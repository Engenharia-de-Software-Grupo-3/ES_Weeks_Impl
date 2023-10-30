label turn_start:
    while (True):
        call victory_check from _call_victory_check
        call defeat_check from _call_defeat_check
        if (victory or defeat):
            return
        call check_enemy_change from _call_check_enemy_change
        $ battleState.turn = battleState.turn + 1
        $ battleState.current_stage = 'Before_menu'
        call check_passive_time_beforeBP from _call_check_passive_time_beforeBP_5
        call battle_menu from _call_battle_menu

label victory_check:
    python:
        victory = True
        for e in battleState.enemy_team_current_stats:
            if e is not None and e.enemy_hp > 0:
                victory = False

label defeat_check:
    $ defeat = battleState.player_hp == 0

label check_enemy_change:
    python:
        enemy_change = False
        eHead_hp = (battleState.enemy_team_current_stats[0]).enemy_hp
        if eHead_hp == 0:
            for i in range(1, 6, 1):
                if (battleState.enemy_team_current_stats[i]) is not None and (battleState.enemy_team_current_stats[i]).enemy_hp > 0:
                    esi_name = (battleState.enemy_team_current_stats[0]).enemy_sprite_info.name
                    battleState.swap_enemy_head(i)
                    enemy_change = True
                    break

    if (enemy_change):
        call enemy_change from _call_enemy_change_1

    return

label check_passive_time_beforeBP:
    $ enemy = (battleState.enemy_team_current_stats)[0]
    if (battleState.check_passive_time(battleState.player_passive)):
        $ battleState.player_passive.effect(battleState, _)
    if (battleState.check_passive_time(battleState.enemy_team_passive)):
        $ battleState.enemy_team_passive.effect(battleState, _)
    return