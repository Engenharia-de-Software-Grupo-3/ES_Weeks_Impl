init python:

    # Test Battle Status Conditions Functions
    def test_poison_effect():
        battleState = type('', (), {})()
        battleState.player_hp = 100
        battleState.player_name = 'Player'
        battleState.enemy_team_current_stats = [type('', (), {})()]
        (battleState.enemy_team_current_stats)[0].enemy_hp = 100
        (battleState.enemy_team_current_stats)[0].enemy_name = 'Enemy'
        poison_effect('player', battleState, type('', (), {'is_player_turn': lambda self: True, 'player_attack_blocked': False})())
        assert battleState.player_hp < 100
        poison_effect('enemy', battleState, type('', (), {'is_enemy_turn': lambda self: True, 'enemy_attack_blocked': False})())
        assert (battleState.enemy_team_current_stats)[0].enemy_hp < 100

    def test_paralys_effect():
        battleState = type('', (), {})()
        battleState.player_name = 'Player'
        battleState.enemy_team_current_stats = [type('', (), {})()]
        (battleState.enemy_team_current_stats)[0].enemy_name = 'Enemy'
        battlePhase = type('', (), {'is_player_turn': lambda self: True, 'player_attack_blocked': False, 'is_enemy_turn': lambda self: True, 'enemy_attack_blocked': False})()
        paralys_effect('player', battleState, battlePhase)
        assert battlePhase.player_attack_blocked
        paralys_effect('enemy', battleState, battlePhase)
        assert battlePhase.enemy_attack_blocked

    def test_confusion_effect():
        battleState = type('', (), {})()
        battleState.player_name = 'Player'
        battleState.player_atk = 10
        battleState.player_res = 10
        battleState.player_hp = 100
        battleState.enemy_team_current_stats = [type('', (), {})()]
        (battleState.enemy_team_current_stats)[0].enemy_name = 'Enemy'
        (battleState.enemy_team_current_stats)[0].enemy_atk = 10
        (battleState.enemy_team_current_stats)[0].enemy_res = 10
        (battleState.enemy_team_current_stats)[0].enemy_hp = 100
        battlePhase = type('', (), {'is_player_turn': lambda self: True, 'player_attack_blocked': False, 'is_enemy_turn': lambda self: True, 'enemy_attack_blocked': False})()
        confusion_effect('player', battleState, battlePhase)
        assert battlePhase.player_attack_blocked
        confusion_effect('enemy', battleState, battlePhase)
        assert battlePhase.enemy_attack_blocked

    # Test Battle Passives Functions
    def test_pythonPassiveF_():
        battleState = type('', (), {})()
        battleState.turn = 1
        battlePhase = type('', (), {'phase': 2, 'is_enemy_turn': lambda self: True, 'player_attack_hitOnce': False, 'enemy_skill': type('', (), {'name': 'Skill'})})()
        pythonPassiveF_(battleState, battlePhase)
        assert battlePhase.enemy_attack_blocked

    def test_javaPassiveF_():
        battleState = type('', (), {})()
        battleState.player_name = 'Player'
        battleState.player_luck = 1
        javaPassiveF_(battleState, type('', (), {}))
        assert battleState.player_luck > 1

    def test_rubyPassiveF_():
        battleState = type('', (), {})()
        battleState.player_name = 'Player'
        battleState.enemy_team_current_stats = [type('', (), {})()]
        (battleState.enemy_team_current_stats)[0].enemy_name = 'Enemy'
        battlePhase = type('', (), {'is_enemy_turn': lambda self: True, 'enemy_skill': type('', (), {'name': 'Skill'})})()
        rubyPassiveF_(battleState, battlePhase)
        assert battlePhase.enemy_attack_blocked

    def test_luaPassiveF_():
        battleState = type('', (), {})()
        analy = type('', (), {})()
        battleState.type_boost_dictionare = {}
        luaPassiveF_(battleState, type('', (), {}))
        assert analy in battleState.type_boost_dictionare.keys()

    # Test Battle Passives Functions
    def test_tcPassiveF_():
        battleState = type('', (), {})()
        battleState.enemy_team_current_stats = [type('', (), {'enemy_type': type('', (), {'name': 'EnemyType', 'advantages': [type('', (), {'name': 'Advantage'})]})})]
        tcPassiveF_(battleState, type('', (), {}))
        assert renpy.get_say_count() == 1
        assert renpy.get_say(0) == "This is a EnemyType question. Its weak against EnemyType attacks and strong against Advantage."

    def test_calculusPassiveF_():
        battleState = type('', (), {'turn': 1, 'player_status_condition_dictionare': {}})
        battlePhase = type('', (), {'enemy_team_name': 'EnemyTeam'})
        calculusPassiveF_(battleState, battlePhase)
        assert battleState.player_status_condition_dictionare['calculating'] == 2
        assert renpy.get_say_count() == 2
        assert renpy.get_say(0) == ""
        assert renpy.get_say(1) == "Player's was affected by calculating!"

    def test_edaPassiveF_():
        battleState = type('', (), {'current_stage': 'battle_begin', 'player_skill_set': ['Skill1', 'Skill2', 'Skill3']})
        battlePhase = type('', (), {'turn': 3})
        edaPassiveF_(battleState, battlePhase)
        assert renpy.get_say_count() == 1
        assert renpy.get_say(0) == "EnemyTeam is exerting its Sort Algorithm!"
        battleState.current_stage = 'before_menu'
        edaPassiveF_(battleState, battlePhase)
        assert battleState.player_skill_set != ['Skill1', 'Skill2', 'Skill3']
        assert sorted(battleState.player_skill_set) == ['Skill1', 'Skill2', 'Skill3']
        assert renpy.get_say_count() == 1
    
label testes_semana_0:
    python:
        test_poison_effect()
        test_paralys_effect()
        test_confusion_effect()
        test_pythonPassiveF_()
        test_javaPassiveF_()
        test_rubyPassiveF_()
        test_luaPassiveF_()
        test_tcPassiveF_()
        test_calculusPassiveF_()
        test_edaPassiveF_()
        renpy.say("All tests passed!")
    return