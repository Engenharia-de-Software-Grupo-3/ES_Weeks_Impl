init python:
    import unittest
    from unittest.mock import MagicMock

    from .player_turn import bp_player_turn, player_calculate_manager, player_hit_manager

    class TestPlayerTurn(unittest.TestCase):

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
            self.battlePhase.current_stage = ''
            self.battlePhase.phase = 0
            self.battlePhase.player_skill = MagicMock()
            self.battlePhase.player_attack_blocked = False
            self.battlePhase.player_attack_blockedMsg = ''
            self.battlePhase.player_attack_hit = False
            self.battlePhase.player_attack_hitOnce = False
            self.battlePhase.player_last_effect_used = MagicMock()

        def test_bp_player_turn(self):
            with unittest.mock.patch('builtins.print') as mock_print:
                bp_player_turn(self.battleState, self.battlePhase)

            self.assertEqual(self.battlePhase.current_stage, 'Battle_end')
            mock_print.assert_called_with("[player_name] used [skill.name].")

        def test_player_calculate_manager(self):
            effect = MagicMock()
            effect.type = ''
            effect.target = ''
            effect.class_name = ''
            effect.target_status = ''
            effect.operator = ''
            effect.value = 0
            self.battlePhase.player_last_effect_used = MagicMock()
            self.battlePhase.player_last_effect_used.target = ''
            self.battlePhase.player_last_effect_used.class_name = ''
            self.battlePhase.player_last_effect_used.target_status = ''
            self.battlePhase.player_last_effect_used.operator = ''
            self.battlePhase.player_last_effect_used.value = 0

            with unittest.mock.patch('builtins.print'):
                player_calculate_manager(effect, self.battleState, self.battlePhase)

            self.assertIsNotNone(self.battlePhase.player_last_effect_used)

        def test_player_hit_manager(self):
            hit = True

            with unittest.mock.patch('builtins.print') as mock_print:
                player_hit_manager(hit, self.battleState, self.battlePhase)

            self.assertTrue(self.battlePhase.player_attack_hitOnce)
            mock_print.assert_called_with("[player_name] took [battlePhase.player_last_effect_used.value] damage.")

        def test_player_hit_manager_missed(self):
            hit = False
            self.battlePhase.player_attack_hitOnce = False

            with unittest.mock.patch('builtins.print') as mock_print:
                player_hit_manager(hit, self.battleState, self.battlePhase)

            self.assertFalse(self.battlePhase.player_attack_hitOnce)
            mock_print.assert_called_with("It missed.")

        def test_player_hit_manager_status_effect(self):
            hit = True
            effect = MagicMock()
            effect.class_name = 'Status_effect'
            effect.target = 'enemy'
            effect.target_status = 'HP'
            effect.operator = '-'
            self.battlePhase.player_last_effect_used = effect

            with unittest.mock.patch('builtins.print') as mock_print, \
                unittest.mock.patch('renpy.call') as mock_call:
                player_hit_manager(hit, self.battleState, self.battlePhase)

            self.assertTrue(self.battlePhase.player_attack_hitOnce)
            mock_call.assert_called_with('damage_scene')
            mock_print.assert_not_called()

        def test_player_hit_manager_type_effect(self):
            hit = True
            effect = MagicMock()
            effect.class_name = 'Type_effect'
            self.battlePhase.player_last_effect_used = effect

            with unittest.mock.patch('builtins.print') as mock_print, \
                unittest.mock.patch('renpy.call') as mock_call:
                player_hit_manager(hit, self.battleState, self.battlePhase)

            self.assertTrue(self.battlePhase.player_attack_hitOnce)
            mock_call.assert_called_with('type_effect_scene')
            mock_print.assert_not_called()

        def test_player_hit_manager_status_condition_effect(self):
            hit = True
            effect = MagicMock()
            effect.class_name = 'Status_condition_effect'
            self.battlePhase.player_last_effect_used = effect

            with unittest.mock.patch('builtins.print') as mock_print, \
                unittest.mock.patch('renpy.call') as mock_call:
                player_hit_manager(hit, self.battleState, self.battlePhase)

            self.assertTrue(self.battlePhase.player_attack_hitOnce)
            mock_call.assert_called_with('status_condition_effect_scene')
            mock_print.assert_not_called()