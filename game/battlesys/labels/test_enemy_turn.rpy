init python:

    import unittest
    from unittest.mock import MagicMock

    from .enemy_turn import bp_enemy_turn, enemy_calculate_manager, enemy_hit_manager

    class TestEnemyTurn(unittest.TestCase):

        def setUp(self):
            self.battleState = MagicMock()
            self.battleState.player_hp = 100
            self.battleState.original_player = MagicMock()
            self.battleState.original_player.hp = 100
            self.battleState.enemy_team_current_stats = [{}, {}, {}]
            self.battleState.enemy_team_current_stats[0].enemy_hp = 100
            self.battleState.enemy_team_current_stats[0].original_enemy = MagicMock()
            self.battleState.enemy_team_current_stats[0].original_enemy.hp = 100
            self.battlePhase = MagicMock()
            self.battlePhase.current_stage = 'Turn_start'
            self.battlePhase.phase = 1
            self.battlePhase.enemy_skill = MagicMock()
            self.battlePhase.enemy_skill.name = 'Test Skill'
            self.battlePhase.enemy_attack_blocked = False
            self.battlePhase.enemy_attack_blockedMsg = None
            self.battlePhase.enemy_attack_hit = False
            self.battlePhase.enemy_attack_hitOnce = False
            self.inLoop = True

        def test_bp_enemy_turn(self):
            with unittest.mock.patch('builtins.print') as mock_print:
                bp_enemy_turn(self.battleState, self.battlePhase)

            self.assertEqual(self.battlePhase.current_stage, 'Effect_hit')
            mock_print.assert_called_with("Enemy [enemy_name] used Test Skill.")

        def test_enemy_calculate_manager_hit(self):
            effect = MagicMock()
            effect.accurace = 100
            effect.class_name = 'Status_effect'
            effect.target = 1
            effect.target_status = 'HP'
            effect.operator = '-'
            effect.value = 10
            self.battlePhase.enemy_last_effect_used = None
            self.battlePhase.enemy_attack_hit = False
            self.battlePhase.enemy_last_effect_used = None
            self.battlePhase.enemy_last_effect_used = None
            self.battlePhase.enemy_last_effect_used = None

            with unittest.mock.patch('renpy.random.randint') as mock_randint:
                mock_randint.return_value = 50
                enemy_calculate_manager(effect, self.battleState, self.battlePhase)

            self.assertEqual(self.battlePhase.enemy_last_effect_used.target, 'player')
            self.assertEqual(self.battlePhase.enemy_last_effect_used.value, 5)
            self.assertTrue(self.battlePhase.enemy_attack_hit)

        def test_enemy_calculate_manager_miss(self):
            effect = MagicMock()
            effect.accurace = 0
            effect.class_name = 'Status_effect'
            effect.target = 1
            effect.target_status = 'HP'
            effect.operator = '-'
            effect.value = 10
            self.battlePhase.enemy_last_effect_used = None
            self.battlePhase.enemy_attack_hit = False
            self.battlePhase.enemy_last_effect_used = None
            self.battlePhase.enemy_last_effect_used = None
            self.battlePhase.enemy_last_effect_used = None

            with unittest.mock.patch('renpy.random.randint') as mock_randint:
                mock_randint.return_value = 50
                enemy_calculate_manager(effect, self.battleState, self.battlePhase)

            self.assertIsNone(self.battlePhase.enemy_last_effect_used)
            self.assertFalse(self.battlePhase.enemy_attack_hit)

        def test_enemy_hit_manager_hit(self):
            self.battlePhase.enemy_attack_hit = True
            self.battlePhase.enemy_attack_hitOnce = False

            with unittest.mock.patch('builtins.print') as mock_print:
                enemy_hit_manager(self.battlePhase)

            self.assertTrue(self.battlePhase.enemy_attack_hitOnce)
            mock_print.assert_not_called()

        def test_enemy_hit_manager_miss(self):
            self.battlePhase.enemy_attack_hit = False
            self.battlePhase.enemy_attack_hitOnce = False

            with unittest.mock.patch('builtins.print') as mock_print:
                enemy_hit_manager(self.battlePhase)

            self.assertFalse(self.battlePhase.enemy_attack_hitOnce)
            mock_print.assert_called_with("It missed.")