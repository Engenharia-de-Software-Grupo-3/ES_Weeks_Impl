label semana_3:
    call semana3_dia15 from _call_semana3_dia15
    if pythonEventsCounter >= 4:
        call semana3_dia16 from _call_semana3_dia16
    if luaEventsCounter >= 4:
        call semana3_dia17 from _call_semana3_dia17
    if rubyEventsCounter >= 4:
        call semana3_dia18 from _call_semana3_dia18
    if javaEventsCounter >= 4:
        call semana3_dia19 from _call_semana3_dia19
    call semana3_dia20 from _call_semana3_dia20
    return