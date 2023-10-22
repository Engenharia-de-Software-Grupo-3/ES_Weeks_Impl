label prepare_tutorial_battle:
    play music "audio/battle.mp3"
    python:
        # Types
        normal = Type("Neutro")
        fire = Type("Analitico")
        water = Type("Matematico", [fire])
        grass = Type("Teorico", [water], [fire])

        fire.advantages.append(grass)
        fire.disadvantages.append(water)
        water.disadvantages.append(grass)

        # Create Effects
        dmg50 = Status_effect(1, 'hp', '-', 50, 100)
        selfDmg50 = Status_effect(0, 'hp', '-', 50, 100)
        selfdmg25 = Status_effect(0, 'hp', '-', 25, 100)
        heal50 = Status_effect(0, 'hp', '+', 50, 100)
        hitkill = Status_effect(1, 'hp', '*', 0, 25)
        fire_boost = Type_effect(0, fire, '+', 100)

        # Skill
        heatVision = Skill('Throw Objects', 'Sequential', fire, [dmg50, dmg50, dmg50], 0, None)
        frostBreath = Skill('Snakes, Go!', 'Sequential', water, [dmg50], 0, None)
        sunCharge = Skill('Compile', 'Sequential', grass, [fire_boost], -1, None)
        megaPunch = Skill("Feeling luck?", 'Inverted', normal, [hitkill, selfDmg50], 1, None)

        punch = Skill('Ataque pi', 'Sequential', water, [dmg50], 0, None)
        gun = Skill('Analise de colunas', 'Sequential', fire, [dmg50, dmg50], 1, None)
        burrito = Skill('Justifique', 'Sequential', grass, [dmg50], 0, None)

        # Status_conditions
        def poison_effect(afflicted, battleState, battlePhase):
            if afflicted == 'player':
                battleState.player_hp -= 25
                renpy.say('', '[battleState.player_name] is hurt by poison!')
            elif afflicted == 'enemy':
                ((battleState.enemy_team_current_stats)[0]).enemy_hp -= 25
                renpy.say('', '[((battleState.enemy_team_current_stats)[0]).enemy_name] is hurt by poison!')

        poison = Status_condition('Calculando', 'Battle_End', poison_effect, 3)
        podre = Status_condition_effect(1, '+', poison, 50)
        punch.effect_list.append(podre)

        # Passives
        def regen(battleState, y):
            battleState.player_hp = min(battleState.original_player.hp, battleState.player_hp + 67)
            renpy.say('', "[battleState.player_name]'s HP was restored by [battleState.player_passive.name]")

        def backstab(battleState, y):
            battleState.player_hp = max(0, battleState.player_hp - 69)
            renpy.say('', 'Enemy [battleState.enemy_team_passive.name] damaged [battleState.player_name]')

        underSun = Passive('Under the Sun', 'NEVER', regen)
        backstab = Passive('Backstab', 'NEVER', backstab)

        # Player
        pxy = Sprite_info("pyth battle", 0.5, 1.0, "pyth battle atk", "pyth battle dmg")
        player = Pc("Python", normal, 1000, 100, 100, 100, underSun, pxy, [heatVision, frostBreath, sunCharge, megaPunch])
        
        # Enemys
        e1xy = Sprite_info("mathEnemy", 0.5, 1.0, "mathEnemy atk", "mathEnemy dmg")
        e2xy = Sprite_info("teoricoEnemy", 0.5, 1.0, "teoricoEnemy atk", "teoricoEnemy dmg")
        e3xy = Sprite_info("analyticEnemy", 0.5, 1.0, "analyticEnemy atk", "analyticEnemy dmg")

        def attackPattern(state):
            return 0

        red = Enemy('Logaritmau', water, 500, 50, 50, 100, [punch], e1xy, attackPattern)
        yellow = Enemy('Em 1943...', grass, 500, 50, 50, 100, [burrito], e2xy, attackPattern)
        blue = Enemy('ASCII', fire, 500, 50, 50, 100, [gun], e3xy, attackPattern)

        # Enemy_team
        enemyTeam = Enemy_team("Tutorial", backstab, [red, yellow, blue, None, None, None], None)

        # Battle_state
        battleState = Battle_state(player, enemyTeam)

    scene battle_wall with dissolve
    show player_box
    show enemy_box
    call show_fighters from _call_show_fighters
    show screen hp_bars_1v1 onlayer master
    call turn_start from _call_turn_start
    $ teste0_Acertos = str(battleState.getEnemysDefeated())
    $ teste0_Nota = str(battleState.getTestGrade())
    return