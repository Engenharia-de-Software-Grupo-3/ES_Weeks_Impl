init python:
    # Import the necessary modules
    import unittest

    # Define a test class that inherits from unittest.TestCase
    class TestBattleState(unittest.TestCase):

        # Define a setUp method that will be called before each test
        def setUp(self):
            # Create a player object
            class Player(object):
                def __init__(self, name, type, hp, atk, res, luck, passive, skill_set, sprite_info):
                    self.name = name
                    self.type = type
                    self.hp = hp
                    self.atk = atk
                    self.res = res
                    self.luck = luck
                    self.passive = passive
                    self.skill_set = skill_set
                    self.sprite_info = sprite_info

            player = Player("Player", "Warrior", 100, 10, 5, 5, "None", [], "player.png")

            # Create an enemy team object
            class Enemy(object):
                def __init__(self, name, type, hp, atk, res, luck, passive, skill_set, sprite_info, attack_pattern):
                    self.name = name
                    self.type = type
                    self.hp = hp
                    self.atk = atk
                    self.res = res
                    self.luck = luck
                    self.passive = passive
                    self.skill_set = skill_set
                    self.sprite_info = sprite_info
                    self.attack_pattern = attack_pattern

            enemy1 = Enemy("Enemy1", "Goblin", 50, 5, 2, 2, "None", [], "enemy1.png", [])
            enemy2 = Enemy("Enemy2", "Orc", 75, 8, 3, 3, "None", [], "enemy2.png", [])

            class Enemy_team(object):
                def __init__(self, name, enemy_list, passive):
                    self.name = name
                    self.enemy_list = enemy_list
                    self.passive = passive

            enemy_team = Enemy_team("Enemy Team", [enemy1, enemy2], "None")

            # Create a Battle_state object
            class Battle_state(object):
                def __init__(self, player, enemy_team):
                    self.turn = 0
                    self.current_stage = "Battle_begin"
                    self.original_player = player
                    self.player_name = player.name
                    self.player_type = player.type
                    self.player_hp = player.hp
                    self.player_atk = player.atk
                    self.player_res = player.res
                    self.player_luck = player.luck
                    self.player_passive = player.passive
                    self.player_skill_set = player.skill_set
                    self.player_sprite_info = player.sprite_info
                    self.accurace_boost = 0
                    self.type_boost_dictionare = {}
                    self.player_status_condition_dictionare = {}
                    self.enemy_team_name = enemy_team.name
                    self.enemy_team_current_stats = create_current_stats(enemy_team)
                    self.enemy_team_passive = enemy_team.passive

            self.battle_state = Battle_state(player, enemy_team)

        # Define a test method for the swap_enemy_head function
        def test_swap_enemy_head(self):
            # Swap the head with the second enemy
            self.battle_state.swap_enemy_head(1)

            # Check that the head is now the second enemy
            self.assertEqual(self.battle_state.enemy_team_current_stats[0].enemy_name, "Enemy2")

        # Define a test method for the get_player_typeBoost function
        def test_get_player_typeBoost(self):
            # Add a type boost for the player
            self.battle_state.type_boost_dictionare["Fire"] = 2

            # Check that the type boost for Fire is 2
            self.assertEqual(self.battle_state.get_player_typeBoost("Fire"), 2)

        # Define a test method for the get_enemyHead_typeBoost function
        def test_get_enemyHead_typeBoost(self):
            # Add a type boost for the head enemy
            self.battle_state.enemy_team_current_stats[0].type_boost_dictionare["Fire"] = 2

            # Check that the type boost for Fire is 2
            self.assertEqual(self.battle_state.get_enemyHead_typeBoost("Fire"), 2)

        # Define a test method for the status_condition_downgrade function
        def test_status_condition_downgrade(self):
            # Add a status condition to the player
            class Status_condition(object):
                def __init__(self, name):
                    self.name = name

            venom = Status_condition("Venom")
            self.battle_state.player_status_condition_dictionare[venom] = 3

            # Call the status_condition_downgrade function
            self.battle_state.status_condition_downgrade("Player")

            # Check that the Venom status condition has been removed
            self.assertNotIn(venom, self.battle_state.player_status_condition_dictionare)

        # Define a test method for the check_passive_time function
        def test_check_passive_time(self):
            # Check that a passive with activation time "Always" returns True
            class Passive(object):
                def __init__(self, activation_time):
                    self.activation_time = activation_time

            passive = Passive("Always")
            self.assertTrue(self.battle_state.check_passive_time(passive))

            # Check that a passive with activation time "Before_menu" returns False
            passive = Passive("Before_menu")
            self.assertFalse(self.battle_state.check_passive_time(passive))

        # Define a test method for the getEnemysDefeated function
        def test_getEnemysDefeated(self):
            # Set the HP of the first enemy to 0
            self.battle_state.enemy_team_current_stats[0].enemy_hp = 0

            # Check that the number of defeated enemies is 1
            self.assertEqual(self.battle_state.getEnemysDefeated(), 1)

        # Define a test method for the getTestGrade function
        def test_getTestGrade(self):
            # Set the HP of both enemies to 0
            self.battle_state.enemy_team_current_stats[0].enemy_hp = 0
            self.battle_state.enemy_team_current_stats[1].enemy_hp = 0

            # Check that the test grade is 10
            self.assertEqual(self.battle_state.getTestGrade(), 10)

    # Run the tests
    unittest.main()