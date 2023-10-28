default itens_loja = ["Energético", "Cereal genérico", "Saco de moedas", "Kit de chá",
    "JPEG SSS+", "Calculadora científica", "Picareta", "Óculos escuros", "Garrafa térmica",
    "Camundongo", "Cálice sagrado", "Pedra quente", "Blåhaj", "Power glove", "Feijoada",
    "Sorvete de pistache"]
default item_var = -1
default num_itens = -1
default nenhuma_compra = True

label shop:
    scene black

    show haskell at left

    if nenhuma_compra:
        "Saudações! O que deseja?"   
    else:
        "Mais alguma coisa?"

label shop_1:

    $ num_itens = len(itens_loja)

menu shop_choices_1:

    "[itens_loja[0]]":
        $ itens_estado[0] = itens_estado[0] + 1
        $ nenhuma_compra = False
        "Ótima escolha!"
        jump shop

    "[itens_loja[1]]":
        $ itens_estado[1] = itens_estado[1] + 1
        $ nenhuma_compra = False
        "Ótima escolha!"
        jump shop

    "[itens_loja[2]]" if num_itens > 2:
        $ item_var = itens_lista.index(itens_loja[2])
        $ itens_loja.pop(2)
        $ itens_estado[item_var] = True
        $ nenhuma_compra = False
        "Ótima escolha!"
        jump shop
    
    "[itens_loja[3]]" if num_itens > 3:
        $ item_var = itens_lista.index(itens_loja[3])
        $ itens_loja.pop(3)
        $ itens_estado[item_var] = True
        $ nenhuma_compra = False
        "Ótima escolha!"
        jump shop
    
    "[itens_loja[4]]" if num_itens > 4:
        $ item_var = itens_lista.index(itens_loja[4])
        $ itens_loja.pop(4)
        $ itens_estado[item_var] = True
        $ nenhuma_compra = False
        "Ótima escolha!"
        jump shop
    
    "Próximo" if num_itens > 5:
        jump shop_2
    
    "Retorna":
        $ nenhuma_compra = True
        return

label shop_2:

    $ num_itens = len(itens_loja)

menu shop_choices_2:
    
    "[itens_loja[5]]" if num_itens > 5:
        $ item_var = itens_lista.index(itens_loja[5])
        $ itens_loja.pop(5)
        $ itens_estado[item_var] = True
        $ nenhuma_compra = False
        "Ótima escolha!"
        jump shop

    "[itens_loja[6]]" if num_itens > 6:
        $ item_var = itens_lista.index(itens_loja[6])
        $ itens_loja.pop(6)
        $ itens_estado[item_var] = True
        $ nenhuma_compra = False
        "Ótima escolha!"
        jump shop

    "[itens_loja[7]]" if num_itens > 7:
        $ item_var = itens_lista.index(itens_loja[7])
        $ itens_loja.pop(7)
        $ itens_estado[item_var] = True
        $ nenhuma_compra = False
        "Ótima escolha!"
        jump shop
    
    "[itens_loja[8]]" if num_itens > 8:
        $ item_var = itens_lista.index(itens_loja[8])
        $ itens_loja.pop(8)
        $ itens_estado[item_var] = True
        $ nenhuma_compra = False
        "Ótima escolha!"
        jump shop
    
    "[itens_loja[9]]" if num_itens > 9:
        $ item_var = itens_lista.index(itens_loja[9])
        $ itens_loja.pop(9)
        $ itens_estado[item_var] = True
        $ nenhuma_compra = False
        "Ótima escolha!"
        jump shop
    
    "Próximo" if num_itens > 10:
        jump shop_3
    
    "Anterior":
        jump shop_1

label shop_3:

    $ num_itens = len(itens_loja)

menu shop_choices_3:
    
    "[itens_loja[10]]" if num_itens > 10:
        $ item_var = itens_lista.index(itens_loja[10])
        $ itens_loja.pop(10)
        $ itens_estado[item_var] = True
        $ nenhuma_compra = False
        "Ótima escolha!"
        jump shop
    
    "[itens_loja[11]]" if num_itens > 11:
        $ item_var = itens_lista.index(itens_loja[11])
        $ itens_loja.pop(11)
        $ itens_estado[item_var] = True
        $ nenhuma_compra = False
        "Ótima escolha!"
        jump shop
    
    "[itens_loja[12]]" if num_itens > 12:
        $ item_var = itens_lista.index(itens_loja[12])
        $ itens_loja.pop(12)
        $ itens_estado[item_var] = True
        $ nenhuma_compra = False
        "Ótima escolha!"
        jump shop
    
    "[itens_loja[13]]" if num_itens > 13:
        $ item_var = itens_lista.index(itens_loja[13])
        $ itens_loja.pop(13)
        $ itens_estado[item_var] = True
        $ nenhuma_compra = False
        "Ótima escolha!"
        jump shop
    
    "[itens_loja[14]]" if num_itens > 14:
        $ item_var = itens_lista.index(itens_loja[14])
        $ itens_loja.pop(14)
        $ itens_estado[item_var] = True
        $ nenhuma_compra = False
        "Ótima escolha!"
        jump shop
    
    "[itens_loja[15]]" if num_itens > 15:
        $ item_var = itens_lista.index(itens_loja[15])
        $ itens_loja.pop(15)
        $ itens_estado[item_var] = True
        $ nenhuma_compra = False
        "Ótima escolha!"
        jump shop
    
    "Anterior":
        jump shop_2