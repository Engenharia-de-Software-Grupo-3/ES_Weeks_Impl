init python:
    # Import the necessary modules
    import unittest

    # Import the Battle_phase class
    from .class_battle_phase import Battle_phase

    # Define a test class that inherits from unittest.TestCase
    class TestBattlePhase(unittest.TestCase):

        # Define a setUp method that will be called before each test
        def setUp(self):
            # Create a Battle_phase object
            self.battle_phase = Battle_phase()

        # Define a test method for the attack_order function
        def test_attack_order(self):
            # Create player and enemy skills
            class Skill(object):
                def __init__(self, speed):
                    self.speed = speed

            player_skill = Skill(10)
            enemy_skill = Skill(5)

            # Call the attack_order function
            self.battle_phase.attack_order(10, player_skill, 5, enemy_skill)

            # Check that the first attacker is the player
            self.assertEqual(self.battle_phase.fst_attacker, 'player')

        # Define a test method for the check_passive_time function
        def test_check_passive_time(self):
            # Create a passive with activation time "Always"
            class Passive(object):
                def __init__(self, activation_time):
                    self.activation_time = activation_time

            passive = Passive("Always")

            # Call the check_passive_time function
            result = self.battle_phase.check_passive_time(passive)

            # Check that the result is True
            self.assertTrue(result)

        # Define a test method for the is_player_turn function
        def test_is_player_turn(self):
            # Set the first attacker to be the player and the phase to be 1
            self.battle_phase.fst_attacker = 'player'
            self.battle_phase.phase = 1

            # Call the is_player_turn function
            result = self.battle_phase.is_player_turn()

            # Check that the result is True
            self.assertTrue(result)

        # Define a test method for the is_enemy_turn function
        def test_is_enemy_turn(self):
            # Set the first attacker to be the enemy and the phase to be 1
            self.battle_phase.fst_attacker = 'enemy'
            self.battle_phase.phase = 1

            # Call the is_enemy_turn function
            result = self.battle_phase.is_enemy_turn()

            # Check that the result is True
            self.assertTrue(result)