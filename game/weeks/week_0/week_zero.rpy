label semana_0:
    call .battle
    return
label .battle:
    python:
        normal.advantages = []
        normal.disadvantages = []
        math.advantages = [theo]
        math.disadvantages = [analy]
        theo.advantages = [analy]
        theo.disadvantages = [math]
        analy.advantages = [math]
        analy.disadvantages = [theo]

init -5 python:
    import copy
    import random

init python:
    # Player
    player_name = None
    player_type = None

    # School
    school_name = 'Sem-Nome-Definido'

    #Flags
    grupoPythonRuby = False
    grupoJavaLua = False

    #EventsCounter
    pythonEventsCounter = 0
    javaEventsCounter = 0
    rubyEventsCounter = 0
    luaEventsCounter = 0
        
    #LoveCounters
    pythonLoveCounter = 0
    javaLoveCounter = 0
    rubyLoveCounter = 0
    luaLoveCounter = 0

    # Battle Status Conditions Functions
    def poison_effect(afflicted, battleState, battlePhase):
            if afflicted == 'player':
                dmg = battleState.player_hp * 0.0625
                battleState.player_hp = max(0, battleState.player_hp - dmg)
                renpy.say('', '[battleState.player_name] is hurt by calculation!')
            elif afflicted == 'enemy':
                hp = ((battleState.enemy_team_current_stats)[0]).enemy_hp
                dmg = hp * 0.0625
                ((battleState.enemy_team_current_stats)[0]).enemy_hp = max(0, hp - dmg)
                renpy.say('', '[((battleState.enemy_team_current_stats)[0]).enemy_name] is hurt by being calculated!')

    def paralys_effect(afflicted, battleState, battlePhase):
            paralysed = (renpy.random.randint(1, 100) <= 40)
            if afflicted == 'player' and paralysed and battlePhase.is_player_turn() and not battlePhase.player_attack_blocked:
                battlePhase.player_attack_blocked = True
                renpy.say('', "[battleState.player_name] is shocked by the question! It can't move!")
            elif afflicted == 'enemy' and paralysed and battlePhase.is_enemy_turn() and not battlePhase.enemy_attack_blocked:
                battlePhase.enemy_attack_blocked = True
                renpy.say('', "[((battleState.enemy_team_current_stats)[0]).enemy_name] is shocked by the answer! It can't move!")
    
    def confusion_effect(afflicted, battleState, battlePhase):
            confused = (renpy.random.randint(1, 100) <= 40)
            if afflicted == 'player' and battlePhase.is_player_turn() and not battlePhase.player_attack_blocked:
                renpy.say('', 'Ambiguous question leaves [battleState.player_name] confused!')
                if confused:
                    battlePhase.player_attack_blocked = True
                    dmg = 25 * (battleState.player_atk / battleState.player_res)
                    battleState.player_hp = max(0, battleState.player_hp - dmg)
                    renpy.say('', 'It hurt itself in its confusion!')
            elif afflicted == 'enemy' and battlePhase.is_enemy_turn() and not battlePhase.enemy_attack_blocked:
                saida = 'Ambiguous answer leaves ' + ((battleState.enemy_team_current_stats)[0]).enemy_name + ' confused!'
                renpy.say('', saida)
                if confused:
                    enemy = (battleState.enemy_team_current_stats)[0]
                    battlePhase.enemy_attack_blocked = True
                    dmg = 25 * (enemy.enemy_atk / enemy.enemy_res)
                    ((battleState.enemy_team_current_stats)[0]).enemy_hp = max(0, enemy.enemy_hp - dmg)
                    renpy.say('', 'It hurt itself in its confusion!')
    
    # Battle Passives Functions
    def pythonPassiveF_(battleState, battlePhase):
        if battlePhase.phase == 2 and battlePhase.is_enemy_turn() and not battlePhase.player_attack_hit:
            battlePhase.enemy_attack_blocked = True
            renpy.say("", "IndentationError: expected an indented block")
            saida = 'Enemy ' + ((battleState.enemy_team_current_stats)[0]).enemy_name + " used " + battlePhase.enemy_skill.name + "."
            renpy.say("", saida)
            battlePhase.enemy_attack_blockedMsg = "[battleState.player_name] IndentationError made it miss."

    def javaPassiveF_(battleState, battlePhase):
        if (battleState.turn % 2) == 1:
            renpy.say("", "[battleState.player_name]'s Coffe Compiler")
            battleState.player_luck = battleState.player_luck * 1.1
            renpy.say("", "[battleState.player_name]'s Speed rose!")

    def rubyPassiveF_(battleState, battlePhase):
        if battlePhase.is_enemy_turn() and renpy.random.randint(1, 100) <= 15:
            battlePhase.enemy_attack_blocked = True
            renpy.say("", "[battleState.player_name]'s Cute Face!")
            saida = 'Enemy ' + ((battleState.enemy_team_current_stats)[0]).enemy_name + " used " + battlePhase.enemy_skill.name + "."
            renpy.say("", saida)
            battlePhase.enemy_attack_blockedMsg = battleState.player_name + " Cute Face made it miss."

    def luaPassiveF_(battleState, _):
        target_type = analy
        keys = battleState.type_boost_dictionare.keys()
        if not target_type in keys:
            battleState.type_boost_dictionare[target_type] = 2
        else:
            battleState.type_boost_dictionare[target_type] += 2
        renpy.say("", "[battleState.player_name]'s Controller is a Table!")
        saida = "[battleState.player_name]'s " + target_type.name + " efficiency increased!"
        renpy.say("", saida)

    def tcPassiveF_(battleState, _):
        enemy = (battleState.enemy_team_current_stats)[0]
        eType = enemy.enemy_type
        eTypeName = eType.name
        eTypeStr = (eType.advantages)[0].name
        saida = "This is a " + eTypeName + " question. Its weak against " + eTypeName + ' attacks and strong against ' + eTypeStr + "."
        pyt(saida)

    def calculusPassiveF_(battleState, _):
        if (battleState.turn % 4) == 1: 
            condition = calculating
            battleState.player_status_condition_dictionare[condition] = 2
            renpy.say("", "[battleState.enemy_team_name] Without Calculator!")
            saida = battleState.player_name + "'s was affected by " + condition.name + "!"
            renpy.say("", saida) 

    def edaPassiveF_(battleState, _):
        if battleState.current_stage.upper() == "BATTLE_BEGIN":
            renpy.say("", "[battleState.enemy_team_name]  is exerting its Sort Algorithm!")
        if battleState.current_stage.upper() == "BEFORE_MENU" and ((battleState.turn % 3) == 0):
            random.shuffle(battleState.player_skill_set)
            # random.shuffle(battleState.player_items)

    # Battle Attack Patterns F.
    def attackPattern(battleState):
        return 0

    def attackPattern2(battleState):
        if (battleState.turn % 3) == 0:
            return 1
        else:
            return 0


        
