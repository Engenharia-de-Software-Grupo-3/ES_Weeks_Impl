init python:

    import unittest
    from unittest.mock import MagicMock

    from .menu_battle import battle_menu, battle_skill_menu, start_battle_phase, battle_change_menu

    class TestBattle(unittest.TestCase):

        def setUp(self):
            self.battleState = MagicMock()
            self.battleState.player_skill_set = [MagicMock(), MagicMock(), MagicMock(), MagicMock()]
            self.battleState.enemy_team_current_stats = [MagicMock(), MagicMock(), MagicMock(), MagicMock(), MagicMock(), MagicMock()]
            self.battlePhase = MagicMock()
            self.battlePhase.fst_attacker = 'PLAYER'
            self.battlePhase.current_stage = 'Turn_start'
            self.battlePhase.phase = 1
            self.battlePhase.enemy_skill = MagicMock()
            self.battlePhase.enemy_skill.name = 'Test Skill'
            self.battlePhase.enemy_attack_blocked = False
            self.battlePhase.enemy_attack_blockedMsg = None
            self.battlePhase.enemy_attack_hit = False
            self.battlePhase.enemy_attack_hitOnce = False
            self.skill_i = 0
            self.i = 0

        def test_battle_menu_fight(self):
            self.battle_choice = 'Fight'
            with unittest.mock.patch('renpy.call') as mock_call:
                with unittest.mock.patch('renpy.hide') as mock_hide:
                    with unittest.mock.patch('renpy.show') as mock_show:
                        with unittest.mock.patch('renpy.narrator') as mock_narrator:
                            with unittest.mock.patch('renpy.return_') as mock_return:
                                with unittest.mock.patch('renpy.call') as mock_call2:
                                    battle_menu(self.battleState, self.battlePhase)

            mock_call.assert_called_with('battle_skill_menu')
            mock_hide.assert_called_with('battle_menu_box')
            mock_show.assert_called_with('battle_menu_box')
            mock_narrator.assert_not_called()
            mock_return.assert_not_called()
            mock_call2.assert_not_called()

        def test_battle_menu_item(self):
            self.battle_choice = 'Item'
            with unittest.mock.patch('renpy.call') as mock_call:
                with unittest.mock.patch('renpy.hide') as mock_hide:
                    with unittest.mock.patch('renpy.show') as mock_show:
                        with unittest.mock.patch('renpy.narrator') as mock_narrator:
                            with unittest.mock.patch('renpy.return_') as mock_return:
                                with unittest.mock.patch('renpy.call') as mock_call2:
                                    battle_menu(self.battleState, self.battlePhase)

            mock_call.assert_not_called()
            mock_hide.assert_called_with('battle_menu_box')
            mock_show.assert_called_with('battle_menu_box')
            mock_narrator.assert_called_with('You dont have any items.')
            mock_return.assert_not_called()
            mock_call2.assert_not_called()

        def test_battle_menu_enemies(self):
            self.battle_choice = 'Enemies'
            with unittest.mock.patch('renpy.call') as mock_call:
                with unittest.mock.patch('renpy.hide') as mock_hide:
                    with unittest.mock.patch('renpy.show') as mock_show:
                        with unittest.mock.patch('renpy.narrator') as mock_narrator:
                            with unittest.mock.patch('renpy.return_') as mock_return:
                                with unittest.mock.patch('renpy.call') as mock_call2:
                                    battle_menu(self.battleState, self.battlePhase)

            mock_call.assert_called_with('battle_change_menu')
            mock_hide.assert_called_with('battle_menu_box')
            mock_show.assert_called_with('battle_menu_box')
            mock_narrator.assert_not_called()
            mock_return.assert_not_called()
            mock_call2.assert_not_called()

        def test_battle_menu_other(self):
            self.battle_choice = 'Other'
            with unittest.mock.patch('renpy.call') as mock_call:
                with unittest.mock.patch('renpy.hide') as mock_hide:
                    with unittest.mock.patch('renpy.show') as mock_show:
                        with unittest.mock.patch('renpy.narrator') as mock_narrator:
                            with unittest.mock.patch('renpy.return_') as mock_return:
                                with unittest.mock.patch('renpy.call') as mock_call2:
                                    battle_menu(self.battleState, self.battlePhase)

            mock_call.assert_not_called()
            mock_hide.assert_called_with('battle_menu_box')
            mock_show.assert_called_with('battle_menu_box')
            mock_narrator.assert_called_with("No! There's no running from a battle!")
            mock_return.assert_not_called()
            mock_call2.assert_not_called()

        def test_battle_skill_menu(self):
            with unittest.mock.patch('renpy.show') as mock_show:
                with unittest.mock.patch('renpy.call') as mock_call:
                    with unittest.mock.patch('renpy.hide') as mock_hide:
                        with unittest.mock.patch('renpy.return_') as mock_return:
                            battle_skill_menu(self.battleState, self.battlePhase)

            mock_show.assert_called_with('battle_menu_box')
            mock_call.assert_called_with('screen', 'battle_skill_menu')
            mock_hide.assert_called_with('battle_menu_box')
            mock_return.assert_not_called()

        def test_start_battle_phase_player_turn(self):
            self.battlePhase.fst_attacker = 'PLAYER'
            with unittest.mock.patch('renpy.call') as mock_call:
                with unittest.mock.patch('renpy.return_') as mock_return:
                    with unittest.mock.patch('renpy.narrator') as mock_narrator:
                        start_battle_phase(self.battleState, self.battlePhase)

            mock_call.assert_called_with('bp_player_turn')
            mock_return.assert_not_called()
            mock_narrator.assert_not_called()

        def test_start_battle_phase_enemy_turn(self):
            self.battlePhase.fst_attacker = 'ENEMY'
            with unittest.mock.patch('renpy.call') as mock_call:
                with unittest.mock.patch('renpy.return_') as mock_return:
                    with unittest.mock.patch('renpy.narrator') as mock_narrator:
                        start_battle_phase(self.battleState, self.battlePhase)

            mock_call.assert_called_with('bp_enemy_turn')
            mock_return.assert_not_called()
            mock_narrator.assert_not_called()

        def test_battle_change_menu(self):
            with unittest.mock.patch('renpy.show') as mock_show:
                with unittest.mock.patch('renpy.call') as mock_call:
                    with unittest.mock.patch('renpy.hide') as mock_hide:
                        with unittest.mock.patch('renpy.return_') as mock_return:
                            battle_change_menu(self.battleState, self.battlePhase)

            mock_show.assert_called_with('battle_menu_box')
            mock_call.assert_called_with('screen', 'battle_enemy_menu')
            mock_hide.assert_called_with('battle_menu_box')
            mock_return.assert_not_called()