label battle_menu:
    while (True):
        show battle_menu_box
        $ battle_choice = None
        call screen battle_main_menu
        hide battle_menu_box
        if battle_choice == 'Fight':
            $ battlePhase = Battle_phase()
            call battle_skill_menu from _call_battle_skill_menu
            if (skill_i != -1):
                call start_battle_phase from _call_start_battle_phase
                return
        elif battle_choice == 'Item':
            if (not broughtItem or (bItem[0] == False and bItem[1] == False and bItem[2] == False and bItem[3] == False)):
                "You dont have any items."
            else:
                call battle_item_menu from _call_battle_item_menu
        elif battle_choice == 'Enemies':
            call battle_change_menu from _call_battle_change_menu
        else:
            narrator "No! There's no running from a battle!"

label battle_item_menu:
    show battle_menu_box
    $ item_i = -1
    call screen battle_item_menu
    hide battle_menu_box
    if item_i == -1:
        pass
    elif item_i == 0:
        $ battleState.player_hp = min(battleState.original_player.hp, battleState.player_hp + 150)
        "[player_name]'s HP was restored."
        $ bItem[0] = False
    elif item_i == 1:
        python:
            condition = calculating
            keys = battleState.player_status_condition_dictionare.keys()
            if not condition in keys:
                renpy.say('', '[player_name] is not affected by [condition.name]!')
            else:
                battleState.player_status_condition_dictionare.pop(condition)
                renpy.say('', '[player_name] is no longer affected by [condition.name]!') 
            bItem[1] = False 
    elif item_i == 2:
        python:
            condition = shocked
            keys = battleState.player_status_condition_dictionare.keys()
            if not condition in keys:
                renpy.say('', '[player_name] is not affected by [condition.name]!')
            else:
                battleState.player_status_condition_dictionare.pop(condition)
                renpy.say('', '[player_name] is no longer affected by [condition.name]!') 
            bItem[2] = False 
    elif item_i == 3:
        python:
            condition = confused
            keys = battleState.player_status_condition_dictionare.keys()
            if not condition in keys:
                renpy.say('', '[player_name] is not affected by [condition.name]!')
            else:
                battleState.player_status_condition_dictionare.pop(condition)
                renpy.say('', '[player_name] is no longer affected by [condition.name]!') 
            bItem[3] = False 
    return

label battle_skill_menu:
    show battle_menu_box
    python:
        skills = battleState.player_skill_set
        if skills[0] is not None:
            button0 = ("- " + skills[0].name.upper())
        if skills[1] is not None:
            button1 = ("- " + skills[1].name.upper())
        if skills[2] is not None:
            button2 = ("- " + skills[2].name.upper())
        if skills[3] is not None:
            button3 = ("- " + skills[3].name.upper())
        skill_i = -1
    call screen battle_skill_menu
    hide battle_menu_box
    return

label start_battle_phase:
    python:
        player_speed = battleState.player_luck
        player_skill_choice = (battleState.player_skill_set)[skill_i]
        enemy_speed = ((battleState.enemy_team_current_stats)[0]).enemy_luck
        skill_i = ((battleState.enemy_team_current_stats)[0]).enemy_attack_pattern(battleState)
        enemy_skill_choice = (((battleState.enemy_team_current_stats)[0]).enemy_skill_set)[skill_i]
        battlePhase.attack_order(player_speed, player_skill_choice, enemy_speed, enemy_skill_choice)
    # call battle_turn_1st_attack
    if (battlePhase.fst_attacker.upper() == 'PLAYER'):
        call bp_player_turn from _call_bp_player_turn_1
    else:
        call bp_enemy_turn from _call_bp_enemy_turn
    $ eHead_hp = (battleState.enemy_team_current_stats[0]).enemy_hp
    if eHead_hp == 0:
        $ enemy_name = ((battleState.enemy_team_current_stats)[0]).enemy_name
        narrator "[enemy_name] fainted!"
    $ battleState.status_condition_downgrade(battleState.player_name)
    return

label battle_change_menu:
    show battle_menu_box
    python:
        i = -1
        enemy0 = battleState.enemy_team_current_stats[0]
        enemy1 = battleState.enemy_team_current_stats[1]
        enemy2 = battleState.enemy_team_current_stats[2]
        enemy3 = battleState.enemy_team_current_stats[3]
        enemy4 = battleState.enemy_team_current_stats[4]
        enemy5 = battleState.enemy_team_current_stats[5]

        if enemy0 is not None:
            button0 = ("★ " + enemy0.enemy_name.upper())
        if enemy1 is not None:
            button1 = ("• " + enemy1.enemy_name.upper())
        if enemy2 is not None:
            button2 = ("• " + enemy2.enemy_name.upper())
        if enemy3 is not None:
            button3 = ("• " + enemy3.enemy_name.upper())
        if enemy4 is not None:
            button4 = ("• " + enemy4.enemy_name.upper())
        if enemy5 is not None:
            button5 = ("• " + enemy5.enemy_name.upper())

    call screen battle_enemy_menu
    hide battle_menu_box
    if not i == -1: 
        $ esi_name = (battleState.enemy_team_current_stats[0]).enemy_sprite_info.name
        $ battleState.swap_enemy_head(i)
        call enemy_change from _call_enemy_change
    return