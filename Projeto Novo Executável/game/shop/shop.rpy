default itens_loja = ["Energético", "Cereal genérico", "Saco de moedas", "Kit de chá",
    "JPEG SSS+", "Calculadora científica", "Picareta", "Óculos escuros", "Garrafa térmica",
    "Camundongo", "Cálice sagrado", "Pedra quente", "Blåhaj", "Power glove", "Feijoada"]
default item_var = -1
default num_itens = -1
default nenhuma_compra = True
default confirma_compra = False

label shop:
    #$ energy -= 1
    scene haskellShop with dissolve
    show haskell at left

    if nenhuma_compra:
        "Haskell" "Saudações! O que deseja?"
    
    else:
        "Haskell" "Mais alguma coisa?"

label shop_1:

    $ num_itens = len(itens_loja)
    $ nenhuma_compra = False

menu shop_choices_1:
    "O que escolher..."
    "[itens_loja[0]]":
        $ item_imagem = 0
        show item at truecenter
        "Haskell" "Aqui está."
        call confirma_loja from _call_confirma_loja
        if confirma_compra:
            if token >= 2:
                $ token -= 2
                $ itens_estado[0] = itens_estado[0] + 1
                "Ótima escolha!"
            else:
                "Haskell" "Você não tem tokens suficientes!"
        hide item
        jump shop

    "[itens_loja[1]]":
        $ item_imagem = 1
        show item at truecenter
        "Haskell" "Aqui está."
        call confirma_loja from _call_confirma_loja_1
        if confirma_compra:
            if token >= 2:
                $ token -= 2
                $ itens_estado[1] = itens_estado[1] + 1
                "Ótima escolha!"
            else:
                "Haskell" "Você não tem tokens suficientes!"
        hide item
        jump shop

    "[itens_loja[2]]" if num_itens > 2:
        $ item_var = itens_lista.index(itens_loja[2])
        $ item_imagem = item_var
        show item at truecenter
        "Haskell" "Aqui está."
        call confirma_loja from _call_confirma_loja_2
        if confirma_compra:
            if token >= 2:
                $ token -= 2
                $ itens_loja.pop(2)
                $ itens_estado[item_var] = True
                "Ótima escolha!"
            else:
                "Haskell" "Você não tem tokens suficientes!"
        hide item
        jump shop
    
    "[itens_loja[3]]" if num_itens > 3:
        $ item_var = itens_lista.index(itens_loja[3])
        $ item_imagem = item_var
        show item at truecenter
        "Haskell" "Aqui está."
        call confirma_loja from _call_confirma_loja_3
        if confirma_compra:
            if token >= 2:
                $ token -= 2
                $ itens_loja.pop(3)
                $ itens_estado[item_var] = True
                "Ótima escolha!"
            else:
                "Haskell" "Você não tem tokens suficientes!"
        hide item
        jump shop
    
    "[itens_loja[4]]" if num_itens > 4:
        $ item_var = itens_lista.index(itens_loja[4])
        $ item_imagem = item_var
        show item at truecenter
        "Haskell" "Aqui está."
        call confirma_loja from _call_confirma_loja_4
        if confirma_compra:
            if token >= 2:
                $ token -= 2
                $ itens_loja.pop(4)
                $ itens_estado[item_var] = True
                "Ótima escolha!"
            else:
                "Haskell" "Você não tem tokens suficientes!"
        hide item
        jump shop
    
    "Próximo" if num_itens > 5:
        jump shop_2
    
    "Sair":
        $ nenhuma_compra = True
        return

label shop_2:
    $ num_itens = len(itens_loja)

menu shop_choices_2:
    "O que escolher..."
    "[itens_loja[5]]" if num_itens > 5:
        $ item_var = itens_lista.index(itens_loja[5])
        $ item_imagem = item_var
        show item at truecenter
        "Haskell" "Aqui está."
        call confirma_loja from _call_confirma_loja_5
        if confirma_compra:
            if token >= 2:
                $ token -= 2
                $ itens_loja.pop(5)
                $ itens_estado[item_var] = True
                "Ótima escolha!"
            else:
                "Haskell" "Você não tem tokens suficientes!"
        hide item
        jump shop

    "[itens_loja[6]]" if num_itens > 6:
        $ item_var = itens_lista.index(itens_loja[6])
        $ item_imagem = item_var
        show item at truecenter
        "Haskell" "Aqui está."
        call confirma_loja from _call_confirma_loja_6
        if confirma_compra:
            if token >= 2:
                $ token -= 2
                $ itens_loja.pop(6)
                $ itens_estado[item_var] = True
                "Ótima escolha!"
            else:
                "Haskell" "Você não tem tokens suficientes!"
        hide item
        jump shop

    "[itens_loja[7]]" if num_itens > 7:
        $ item_var = itens_lista.index(itens_loja[7])
        $ item_imagem = item_var
        show item at truecenter
        "Haskell" "Aqui está."
        call confirma_loja from _call_confirma_loja_7
        if confirma_compra:
            if token >= 2:
                $ token -= 2
                $ itens_loja.pop(7)
                $ itens_estado[item_var] = True
                "Ótima escolha!"
            else:
                "Haskell" "Você não tem tokens suficientes!"
        hide item
        jump shop
    
    "[itens_loja[8]]" if num_itens > 8:
        $ item_var = itens_lista.index(itens_loja[8])
        $ item_imagem = item_var
        show item at truecenter
        "Haskell" "Aqui está."
        call confirma_loja from _call_confirma_loja_8
        if confirma_compra:
            if token >= 2:
                $ token -= 2
                $ itens_loja.pop(8)
                $ itens_estado[item_var] = True
                "Ótima escolha!"
            else:
                "Haskell" "Você não tem tokens suficientes!"
        hide item
        jump shop
    
    "[itens_loja[9]]" if num_itens > 9:
        $ item_var = itens_lista.index(itens_loja[9])
        $ item_imagem = item_var
        show item at truecenter
        "Haskell" "Aqui está."
        call confirma_loja from _call_confirma_loja_9
        if confirma_compra:
            if token >= 2:
                $ token -= 2
                $ itens_loja.pop(9)
                $ itens_estado[item_var] = True
                "Ótima escolha!"
            else:
                "Haskell" "Você não tem tokens suficientes!"
        hide item
        jump shop
    
    "Próximo" if num_itens > 10:
        jump shop_3
    
    "Anterior":
        jump shop_1

label shop_3:

    $ num_itens = len(itens_loja)

menu shop_choices_3:
    "O que escolher..."
    "[itens_loja[10]]" if num_itens > 10:
        $ item_var = itens_lista.index(itens_loja[10])
        $ item_imagem = item_var
        show item at truecenter
        "Haskell" "Aqui está."
        call confirma_loja from _call_confirma_loja_10
        if confirma_compra:
            if token >= 2:
                $ token -= 2
                $ itens_loja.pop(10)
                $ itens_estado[item_var] = True
                "Ótima escolha!"
            else:
                "Haskell" "Você não tem tokens suficientes!"
        hide item
        jump shop
    
    "[itens_loja[11]]" if num_itens > 11:
        $ item_var = itens_lista.index(itens_loja[11])
        $ item_imagem = item_var
        show item at truecenter
        "Haskell" "Aqui está."
        call confirma_loja from _call_confirma_loja_11
        if confirma_compra:
            if token >= 2:
                $ token -= 2
                $ itens_loja.pop(11)
                $ itens_estado[item_var] = True
                "Ótima escolha!"
            else:
                "Haskell" "Você não tem tokens suficientes!"
        hide item
        jump shop
    
    "[itens_loja[12]]" if num_itens > 12:
        $ item_var = itens_lista.index(itens_loja[12])
        $ item_imagem = item_var
        show item at truecenter
        "Haskell" "Aqui está."
        call confirma_loja from _call_confirma_loja_12
        if confirma_compra:
            if token >= 2:
                $ token -= 2
                $ itens_loja.pop(12)
                $ itens_estado[item_var] = True
                "Ótima escolha!"
            else:
                "Haskell" "Você não tem tokens suficientes!"
        hide item
        jump shop
    
    "[itens_loja[13]]" if num_itens > 13:
        $ item_var = itens_lista.index(itens_loja[13])
        $ item_imagem = item_var
        show item at truecenter
        "Haskell" "Aqui está."
        call confirma_loja from _call_confirma_loja_13
        if confirma_compra:
            if token >= 2:
                $ token -= 2
                $ itens_loja.pop(13)
                $ itens_estado[item_var] = True
                "Ótima escolha!"
            else:
                "Haskell" "Você não tem tokens suficientes!"
        hide item
        jump shop
    
    "[itens_loja[14]]" if num_itens > 14:
        $ item_var = itens_lista.index(itens_loja[14])
        $ item_imagem = item_var
        show item at truecenter
        "Haskell" "Aqui está."
        call confirma_loja from _call_confirma_loja_14
        if confirma_compra:
            if token >= 2:
                $ token -= 2
                $ itens_loja.pop(14)
                $ itens_estado[item_var] = True
                "Ótima escolha!"
            else:
                "Haskell" "Você não tem tokens suficientes!"
        hide item
        jump shop
    
    "Anterior":
        jump shop_2

menu confirma_loja:

    "Haskell" "É esse o item que deseja?"

    "Sim":
        $ confirma_compra = True
        return
    "Não":
        $ confirma_compra = False
        return
