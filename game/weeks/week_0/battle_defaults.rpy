# Types
default normal = Type("Neutral")
default analy = Type("Analytical")
default theo = Type("Theoretical")
default math = Type("Mathematic")

# Status_conditions

default calculating = Status_condition('Calculating', 'Battle_End', poison_effect, 4)
default shocked = Status_condition('Shock', 'Turn_start', paralys_effect, 4)
default confused = Status_condition('Confusion', 'Turn_start', confusion_effect, 4)

# Create Effects
default dmg100 = Status_effect(1, 'hp', '-', 100, 100)
default dmg50 = Status_effect(1, 'hp', '-', 50, 100)
default dmg30 = Status_effect(1, 'hp', '-', 30, 100)
default dmg30P90 = Status_effect(1, 'hp', '-', 30, 90)
default hitkill = Status_effect(1, 'hp', '*', 0, 20)
default dmg50P = Status_effect(1, 'hp', '*', 0.50, 100)

default selfDmg50 = Status_effect(0, 'hp', '-', 50, 100)
default selfdmg25 = Status_effect(0, 'hp', '-', 25, 100)

default heal50 = Status_effect(0, 'hp', '+', 50, 100)
default heal50P = Status_effect(0, 'hp', '*', 2, 100)

default luckPlus = Status_effect(0, 'luck', '*', 1.25, 100)
default luckMinus = Status_effect(1, 'luck', '*', 0.75, 100)
default luckMinusSelf = Status_effect(0, 'luck', '*', 0.75, 100)
default atkPlus = Status_effect(0, 'atk', '*', 1.25, 100)
default atkMinus = Status_effect(1, 'atk', '*', 0.75, 100)
default resPlus = Status_effect(0, 'res', '*', 1.25, 100)
default resMinus = Status_effect(1, 'res', '*', 0.75, 100)

default analy_boost = Type_effect(0, analy, '+', 100)
default theo_boost = Type_effect(0, theo, '+', 100)
default math_boost = Type_effect(0, math, '+', 100)

default calculatingPlus = Status_condition_effect(1, '+', calculating, 75)
default shockedPlus = Status_condition_effect(1, '+', shocked, 75)
default confusedPlus = Status_condition_effect(1, '+', confused, 75)
default calculatingMinus = Status_condition_effect(0, '-', calculating, 100)
default shockedMinus = Status_condition_effect(0, '-', shocked, 100)
default confusedMinus = Status_condition_effect(0, '-', confused, 100)

# Skills
        # Characters 
default pythonCureS = Skill("Print('Cure')", "Sequential", normal, [heal50P, luckMinusSelf])
default pythonHitS = Skill("Snakes, Go!", 'SEQUENTIAL', normal, [dmg50, calculatingPlus])

default javaHitS = Skill('Throw Objects;', 'Sequential', math, [dmg30, dmg50])
default javaDefUpS = Skill('Resistance++;', "Sequential", normal, [resPlus])

default rubyHitS = Skill("3.Hit", "Sequential", theo, [dmg30, dmg30, dmg30], 1)
default rubyLuckUpS = Skill("On Rails", "SEQUENTIAL", normal, [luckPlus])

default luaHitS = Skill("Index 0", 'SEQUENTIAL', analy, [dmg30, confusedPlus], 1)
default luaAtkPlusS = Skill("Mod Strength", 'SEQUENTIAL', analy, [atkPlus])

        # Battle intro
default genericMathS = Skill("Math Atk", 'SEQUENTIAL', math, [dmg50])
default genericAnalyS = Skill("Analytic Atk", 'SEQUENTIAL', analy, [dmg50])
default genericTheoS = Skill("Theoretic Atk", 'SEQUENTIAL', theo, [dmg50])

        # Battle 1
default b1ConfusionS = Skill("Derive IQ", 'SEQUENTIAL', math, [dmg50, confusedPlus])
default b1MultHitS = Skill("Integrate Pain", 'SEQUENTIAL', theo, [dmg30, dmg30])

        # Battle 2
default b2MultHitS = Skill("Linked Hit", 'SEQUENTIAL', theo, [dmg30P90, dmg30P90, dmg50])
default b2LifeStealS = Skill("pop(HP)", 'SEQUENTIAL', normal, [dmg50, heal50], -1)
default b2ParalysS = Skill("Binary Search", "Sequential", analy, [confusedPlus, shockedPlus])

        # Library
default analyBoostS_ = Skill("Data Analysis", 'SEQUENTIAL', normal, [analy_boost])
default theoBoostS_ = Skill("Machine Learning", 'SEQUENTIAL', normal, [theo_boost])
default mathBoostS_ = Skill("Scientific Computing", 'SEQUENTIAL', normal, [math_boost])
default confusedPlusS_ = Skill("Ambiguous Answer", 'Inverted', normal, [confusedPlus, selfdmg25])
default luckKick = Skill("Feeling luck?", 'Inverted', normal, [hitkill, selfDmg50], -1)

# Passives
default identationP = Passive("IdentationError", "Turn_start", pythonPassiveF_)
default compileP = Passive("Coffe Compiler", "Battle_end", javaPassiveF_)
default cuteFaceP = Passive("Cute Face", "Turn_start", rubyPassiveF_)
default tableP = Passive("Annoying Tutorial", "Battle_begin", luaPassiveF_)

default introP = Passive("IdentationError", "Show_fighters", tcPassiveF_)
default noCalculatorP = Passive("Without Calculator", "Before_menu", calculusPassiveF_)
default sortP = Passive("Sort Algorithm", "Always", edaPassiveF_)

# Sprite Infos
default pytSI = Sprite_info("pyth battle", 0.5, 1.0, "pyth battle atk", "pyth battle dmg")
default javSI = Sprite_info("java battle", 0.5, 1.0, "java battle atk", "java battle dmg")
default rubSI = Sprite_info("ruby battle", 0.5, 1.0, "ruby battle atk", "ruby battle dmg")
default luaSI= Sprite_info("lua battle", 0.5, 1.0, "lua battle atk", "lua battle dmg")

default mathSI = Sprite_info("mathEnemy", 0.64, 0.7, "mathEnemy atk", "mathEnemy dmg")
default theoSI = Sprite_info("teoricoEnemy", 0.61, 0.68, "teoricoEnemy atk", "teoricoEnemy dmg")
default analySI = Sprite_info("analyticEnemy", 0.632, 0.63, "analyticEnemy atk", "analyticEnemy dmg")     

# Player
default pythonTutorialPC = Pc("Python", normal, 300, 50, 50, 50, identationP, pytSI, [genericMathS, genericTheoS, genericAnalyS, pythonCureS])
default pythonPC = Pc("Python", normal, 300, 50, 50, 50, identationP, pytSI, [pythonHitS, pythonCureS, None, None])
default javaPC = Pc("Java", math, 350, 55, 50, 40, compileP, javSI, [javaHitS, javaDefUpS, None, None])
default rubyPC = Pc("Ruby", theo, 280, 60, 50, 60, cuteFaceP, rubSI, [rubyHitS, rubyLuckUpS, None, None])
default luaPC = Pc("Lua", analy, 301, 51, 51, 51, tableP, luaSI, [luaHitS, luaAtkPlusS, None, None])

# Enemys
        # Introduction
default icMathE_ = Enemy('∑liminate', math, 70, 40, 50, 50, [genericMathS], mathSI, attackPattern)
default icTheoE_ = Enemy('ENIAC', theo, 70, 40, 50, 50, [genericTheoS], theoSI, attackPattern)
default icAnalyE_ = Enemy('ASC FF', analy, 70, 40, 50, 50, [genericTheoS], analySI, attackPattern)
        # Calculus II
default limitE_ = Enemy('limF(ear)', math, 70, 50, 50, 50, [genericMathS], mathSI, attackPattern)
default derivE_ = Enemy('d/dFeat', math, 75, 50, 50, 50, [genericMathS, b1ConfusionS], mathSI, attackPattern2)
default integE_ = Enemy('∫Trage dY', analy, 80, 50, 50, 50, [genericTheoS, b1MultHitS], analySI, attackPattern2)
        # EDA
default stackE_ = Enemy('StackPanic', theo, 80, 60, 50, 50, [genericTheoS, b2LifeStealS], theoSI, attackPattern2)
default listE_ = Enemy('NaughtyList', theo, 85, 60, 50, 50, [genericTheoS, b2MultHitS], theoSI, attackPattern2)
default treeE_ = Enemy('WhompingTree', analy, 90, 60, 50, 50, [genericTheoS, b2ParalysS], analySI, attackPattern2)

# Enemy_teams
default icEnemyTeam = Enemy_team("Introduction to Computing", introP, [icMathE_, icTheoE_, icAnalyE_, None, None, None], None)
default calculusEnemyTeam = Enemy_team("Calculus II", noCalculatorP, [limitE_, derivE_, integE_, None, None, None], None)
default edaEnemyTeam = Enemy_team("Data Structure", sortP, [stackE_, listE_, treeE_, None, None, None], None)

# Battle_state
default battleState = None
default battlePhase = None

