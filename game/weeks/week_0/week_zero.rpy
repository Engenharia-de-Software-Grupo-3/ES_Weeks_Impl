label semana_0:
    $ renpy.say('', semana)
    call init_python
    return

label init_python:
    init python:
        #Player
        player_name = None
        player_type = None
        #School
        school_name = 'Alura'