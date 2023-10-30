init python:

    class Battle_phase(object):
        def __init__(self) :
            #Inicias
            self.fst_attacker = None
            self.snd_attacker = None

            self.player_skill = None
            self.enemy_skill = None

            #Field
                # Battle_Start | Turn_start | Effect_calculate | Effect_hit | Battle_end
            self.current_stage = "Battle_start"
                # 0 | 1 | 2
            self.phase = 0

            #Abilities_info
            self.player_attack_hit = False
            self.player_attack_hitOnce = False
            self.player_attack_blocked = False
            self.player_attack_blockedMsg = ""
            
            self.enemy_attack_hit = False
            self.enemy_attack_hitOnce = False
            self.enemy_attack_blocked = False
            self.enemy_attack_blockedMsg = ""

            #Battle_info
            self.player_last_effect_used = None

            self.enemy_last_effect_used = None


        def attack_order(self, p_speed, player_skill, e_speed, enemy_skill):
            self.player_skill = player_skill
            self.enemy_skill = enemy_skill

            if player_skill.speed != enemy_skill.speed:
                if player_skill.speed > enemy_skill.speed:
                    self.attack_order_aux('player', 'enemy')
                else:
                    self.attack_order_aux('enemy', 'player')
            else:
                if p_speed >= e_speed:
                    self.attack_order_aux('player', 'enemy')
                else:
                    self.attack_order_aux('enemy', 'player')

        def attack_order_aux(self, fst_attacker, snd_attacker):
            self.fst_attacker = fst_attacker
            self.snd_attacker = snd_attacker

        def check_passive_time(self, passive):
            return (passive.activation_time.upper() == 'ALWAYS' 
                    or passive.activation_time.upper() == self.current_stage.upper())

        def check_statusCondition_time(self, status_condition_dictionare):
            status_list = status_condition_dictionare.keys()
            saida = []
            for s in status_list:
                if (s.activation_time.upper() == 'ALWAYS' 
                    or s.activation_time.upper() == self.current_stage.upper()):
                    saida.append(s)
            return saida

        def is_player_turn(self):
            return ((self.fst_attacker is not None and self.fst_attacker == 'player' and self.phase == 1)
                    or (self.snd_attacker is not None and self.snd_attacker == 'player' and self.phase == 2))

        def is_enemy_turn(self):
            return ((self.fst_attacker is not None and self.fst_attacker == 'enemy' and self.phase == 1)
                    or (self.snd_attacker is not None and self.snd_attacker == 'enemy' and self.phase == 2))
                


