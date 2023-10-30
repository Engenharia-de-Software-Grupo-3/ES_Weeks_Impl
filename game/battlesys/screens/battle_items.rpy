screen battle_item_menu:
    vbox:
        spacing 1
        xalign 0.7
        yalign 0.875
        xmaximum 400
        style_prefix 'battle'
        if bItem[0]:
            textbutton "- POTION" action [SetVariable('item_i', 0), Return()]
        if bItem[1]:
            textbutton "- SUGAR CANDY" action [SetVariable('item_i', 1), Return()]
        if bItem[2]:
            textbutton "- TRANQUILIZER" action [SetVariable('item_i', 2), Return()]
        if bItem[3]:
            textbutton "- MIND GEM" action [SetVariable('item_i', 3), Return()]
    vbox:
        xalign 0.95
        yalign 0.95
        xmaximum 400
        style_prefix 'battle'
        textbutton '{size=*1.5}⏎{/size}' action Return() 