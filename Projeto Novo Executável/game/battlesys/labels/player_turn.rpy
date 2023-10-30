label bp_player_turn:
    # Start--------------------------------------------------------------------------------------
    $ battlePhase.current_stage = 'Turn_start'
    $ battlePhase.phase += 1
    # CHECK PASSIVES, HP = 0, ENEMY_HP = 0
    call check_passive_time from _call_check_passive_time_4
    if (battleState.player_hp == 0 or ((battleState.enemy_team_current_stats)[0]).enemy_hp == 0):
        return
    # CHECK NEG_STATS 
    call check_status_condition from _call_check_status_condition_4
    if (battleState.player_hp == 0 or ((battleState.enemy_team_current_stats)[0]).enemy_hp == 0):
        return
    # Effect_calculator
    $ skill = battlePhase.player_skill
    if battlePhase.player_attack_blocked:
        $ inLoop = False
        if battlePhase.player_attack_blockedMsg /= "":
            "[battlePhase.player_attack_blockedMsg]"
    else:
        python:
            enemy = (battleState.enemy_team_current_stats)[0]
            # Get skill info
            superEffective = 1
            if skill.type == enemy.enemy_type:
                superEffective = superEffective * 2
            if skill.type in enemy.enemy_type.advantages:
                superEffective = superEffective * 0.5
            effect_list = skill.effect_list
            effect_list_size = len(effect_list)
            is_sequential = (skill.effect_sequence.upper() == 'SEQUENTIAL')
            i = 0
            if (i == effect_list_size):
                inLoop = False
            else:
                inLoop = True
        '[battleState.player_name] used [skill.name].'
    while (inLoop):
        $ effect = effect_list[i]
        $ battlePhase.player_attack_hit = False
        # Effect_calculate------------------------------------------------------------
        $ battlePhase.current_stage = 'Effect_calculate'
        call player_calculate_manager from _call_player_calculate_manager
        # CHECK PASSIVES, HP = 0, ENEMY_HP = 0
        call check_passive_time from _call_check_passive_time_5
        if (battleState.player_hp == 0 or ((battleState.enemy_team_current_stats)[0]).enemy_hp == 0):
            return
        # CHECK NEG_STATS
        call check_status_condition from _call_check_status_condition_5
        if (battleState.player_hp == 0 or ((battleState.enemy_team_current_stats)[0]).enemy_hp == 0):
            return
        # Effect_hit-----------------------------------------------------------------
        $ battlePhase.current_stage = 'Effect_hit'
        call player_hit_manager from _call_player_hit_manager
        # CHECK PASSIVES, HP = 0, ENEMY_HP = 0
        call check_passive_time from _call_check_passive_time_6
        if (battleState.player_hp == 0 or ((battleState.enemy_team_current_stats)[0]).enemy_hp == 0):
            return
        # CHECK NEG_STATS
        call check_status_condition from _call_check_status_condition_6
        if (battleState.player_hp == 0 or ((battleState.enemy_team_current_stats)[0]).enemy_hp == 0):
            return
        # Check in loop
        $ i += 1
        if (i == effect_list_size):
            $ inLoop = False
        elif (((not battlePhase.player_attack_hit) and is_sequential) or (battlePhase.player_attack_hit and (not is_sequential))):
            $ inLoop = False
        else:
            $ inLoop = True
    # End turn -----------------------------------------------------------------------------------
    if battlePhase.phase == 2:
        $ battlePhase.current_stage = 'Battle_end'
        # CHECK PASSIVES
        call check_passive_time from _call_check_passive_time_7
        # CHECK NEG_STATS
        call check_status_condition from _call_check_status_condition_7
        return
    else:
        call bp_enemy_turn from _call_bp_enemy_turn_1

    return
        

label player_calculate_manager:
    python:
        # [target, stats, operator, value]
        hit = (renpy.random.randint(1, 100) <= (effect.accurace + battleState.accurace_boost))
        battlePhase.player_attack_hit = hit
        if (hit):
            player_effect_dict = {0: 'player', 1: 'enemy'}
            battlePhase.player_last_effect_used = copy.copy(effect)
            # Alvo verdadeiro
            battlePhase.player_last_effect_used.target = player_effect_dict[effect.target]
            if effect.class_name == 'Status_effect':
                # if deals demage to enemy -> calcular total damage 
                if (effect.target == 1 and effect.target_status.upper() == 'HP' and effect.operator == '-'):
                    inicial_damage = effect.value
                    player_attack = battleState.player_atk
                    enemy_defense = ((battleState.enemy_team_current_stats)[0]).enemy_res
                    player_type_boost = battleState.get_player_typeBoost(skill.type)
                    enemy_type_resistance = battleState.get_enemyHead_typeBoost(skill.type)
                    resistance_value = min(2, max(0.1, 1 + ((player_type_boost - enemy_type_resistance) * 0.25)))
                    crit = (renpy.random.randint(0, 500) < (battleState.player_luck))
                    if crit:
                        crit_value = 2
                    else:
                        crit_value = 1
                    final_damage = inicial_damage * (player_attack / enemy_defense) * superEffective * crit_value * resistance_value
                    battlePhase.player_last_effect_used.value = final_damage

    return

label player_hit_manager:
    if (not hit):
        if (not battlePhase.player_attack_hitOnce):
            narrator "It missed."
    else: 
        python:
            battlePhase.player_attack_hitOnce = True

            effect = battlePhase.player_last_effect_used
            playerName = battleState.player_name
            enemy_name = ((battleState.enemy_team_current_stats)[0]).enemy_name
            if effect.class_name == 'Status_effect':
                if (effect.target == 'enemy' and effect.target_status.upper() == 'HP' and effect.operator == '-'):
                    renpy.call('damage_scene')
                else:
                    s = effect.target_status.lower()
                    renpy.call(s + "_effect_scene")
            elif effect.class_name == 'Type_effect':
                renpy.call('type_effect_scene')
            elif effect.class_name == 'Status_condition_effect':
                renpy.call('status_condition_effect_scene')
    return

label check_passive_time:
    $ enemy = (battleState.enemy_team_current_stats)[0]
    if (battlePhase.check_passive_time(battleState.player_passive)):
        $ battleState.player_passive.effect(battleState, battlePhase)
    if (battlePhase.check_passive_time(battleState.enemy_team_passive)):
        $ battleState.enemy_team_passive.effect(battleState, battlePhase)
    return

label check_status_condition:
    python: 
        enemy = (battleState.enemy_team_current_stats)[0]
        playerStatusTrigged = battlePhase.check_statusCondition_time(battleState.player_status_condition_dictionare)
        enemyStatusTrigged = battlePhase.check_statusCondition_time(enemy.status_condition_dictionare)
        for sp in playerStatusTrigged:
            sp.effect('player', battleState, battlePhase)
        for se in enemyStatusTrigged:
            se.effect('enemy', battleState, battlePhase)
    return


