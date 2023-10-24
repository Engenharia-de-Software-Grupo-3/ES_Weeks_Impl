# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# define e = Character("Eileen")


# The game starts here.

label start:

    $ w = 0
    while True:
        if w == 4: 
            return
        $ semana = 'semana_' + str(w)
        call expression semana from _call_expression
        $ w = w + 1

    # This ends the game.


return