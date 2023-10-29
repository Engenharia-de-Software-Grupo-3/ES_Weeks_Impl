init python:

    import unittest
    from unittest.mock import MagicMock

    from .effect_scenes import damage_scene, hp_effect_scene, atk_effect_scene, res_effect_scene

    class TestEffectScenes(unittest.TestCase):

        def setUp(self):
            self.battleState = MagicMock()
            self.battleState.player_hp = 100
            self.battleState.original_player = MagicMock()
            self.battleState.original_player.hp = 100
            self.battleState.enemy_team_current_stats = [{}, {}, {}]
            self.battleState.enemy_team_current_stats[0].enemy_hp = 100
            self.battleState.enemy_team_current_stats[0].original_enemy = MagicMock()
            self.battleState.enemy_team_current_stats[0].original_enemy.hp = 100

        def test_damage_scene_player(self):
            effect = MagicMock()
            effect.target = 'player'
            effect.value = 10
            crit = False
            superEffective = 1

            with unittest.mock.patch('builtins.print') as mock_print:
                damage_scene(effect, crit, superEffective, self.battleState)

            self.assertEqual(self.battleState.player_hp, 90)
            mock_print.assert_called_with("[player_name] took 10 damage.")

        def test_damage_scene_enemy(self):
            effect = MagicMock()
            effect.target = 'enemy'
            effect.value = 10
            crit = False
            superEffective = 1

            with unittest.mock.patch('builtins.print') as mock_print:
                damage_scene(effect, crit, superEffective, self.battleState)

            self.assertEqual(self.battleState.enemy_team_current_stats[0].enemy_hp, 90)
            mock_print.assert_called_with("[enemy_name] took 10 damage.")

        def test_damage_scene_player_crit(self):
            effect = MagicMock()
            effect.target = 'player'
            effect.value = 10
            crit = True
            superEffective = 1

            with unittest.mock.patch('builtins.print') as mock_print:
                damage_scene(effect, crit, superEffective, self.battleState)

            self.assertEqual(self.battleState.player_hp, 90)
            mock_print.assert_called_with("[player_name] took 10 damage. A critical hit!")

        def test_damage_scene_enemy_super_effective(self):
            effect = MagicMock()
            effect.target = 'enemy'
            effect.value = 10
            crit = False
            superEffective = 2

            with unittest.mock.patch('builtins.print') as mock_print:
                damage_scene(effect, crit, superEffective, self.battleState)

            self.assertEqual(self.battleState.enemy_team_current_stats[0].enemy_hp, 80)
            mock_print.assert_called_with("[enemy_name] took 10 damage. It's super effective!")

        def test_hp_effect_scene_player_add(self):
            effect = MagicMock()
            effect.target = 'player'
            effect.operator = '+'
            effect.value = 10

            with unittest.mock.patch('builtins.print') as mock_print:
                hp_effect_scene(effect, self.battleState)

            self.assertEqual(self.battleState.player_hp, 100)
            mock_print.assert_called_with("[player_name]'s HP was restored.")

        def test_hp_effect_scene_player_subtract(self):
            effect = MagicMock()
            effect.target = 'player'
            effect.operator = '-'
            effect.value = 10

            with unittest.mock.patch('builtins.print') as mock_print:
                hp_effect_scene(effect, self.battleState)

            self.assertEqual(self.battleState.player_hp, 90)
            mock_print.assert_called_with("[player_name]'s is damaged by recoil.")

        def test_hp_effect_scene_player_multiply(self):
            effect = MagicMock()
            effect.target = 'player'
            effect.operator = '*'
            effect.value = 2

            with unittest.mock.patch('builtins.print') as mock_print:
                hp_effect_scene(effect, self.battleState)

            self.assertEqual(self.battleState.player_hp, 100)
            mock_print.assert_called_with("[player_name]'s HP rose!")

        def test_atk_effect_scene_enemy_add(self):
            effect = MagicMock()
            effect.target = 'enemy'
            effect.operator = '+'
            effect.value = 10

            with unittest.mock.patch('builtins.print') as mock_print:
                atk_effect_scene(effect, self.battleState)

            self.assertEqual(self.battleState.enemy_team_current_stats[0].enemy_atk, 10)
            mock_print.assert_called_with("[enemy_name]'s Attack rose!")

        def test_atk_effect_scene_enemy_subtract(self):
            effect = MagicMock()
            effect.target = 'enemy'
            effect.operator = '-'
            effect.value = 10

            with unittest.mock.patch('builtins.print') as mock_print:
                atk_effect_scene(effect, self.battleState)

            self.assertEqual(self.battleState.enemy_team_current_stats[0].enemy_atk, 1)
            mock_print.assert_called_with("[enemy_name]'s Attack fell!")

        def test_atk_effect_scene_enemy_multiply(self):
            effect = MagicMock()
            effect.target = 'enemy'
            effect.operator = '*'
            effect.value = 2

            with unittest.mock.patch('builtins.print') as mock_print:
                atk_effect_scene(effect, self.battleState)

            self.assertEqual(self.battleState.enemy_team_current_stats[0].enemy_atk, 20)
            mock_print.assert_called_with("[enemy_name]'s Attack rose!")

        def test_res_effect_scene_player_add(self):
            effect = MagicMock()
            effect.target = 'player'
            effect.operator = '+'
            effect.value = 10

            with unittest.mock.patch('builtins.print') as mock_print:
                res_effect_scene(effect, self.battleState)

            self.assertEqual(self.battleState.player_res, 10)
            mock_print.assert_called_with("[player_name]'s Defense rose!")

        def test_res_effect_scene_player_subtract(self):
            effect = MagicMock()
            effect.target = 'player'
            effect.operator = '-'
            effect.value = 10

            with unittest.mock.patch('builtins.print') as mock_print:
                res_effect_scene(effect, self.battleState)

            self.assertEqual(self.battleState.player_res, 1)
            mock_print.assert_called_with("[player_name]'s Defense fell!")

        def test_res_effect_scene_player_multiply(self):
            effect = MagicMock()
            effect.target = 'player'
            effect.operator = '*'
            effect.value = 2

            with unittest.mock.patch('builtins.print') as mock_print:
                res_effect_scene(effect, self.battleState)

            self.assertEqual(self.battleState.player_res, 20)
            mock_print.assert_called_with("[player_name]'s Defense rose!")