image inventoryScene = "images/Fotos/chestInventory.jpg"

default token = 0

default itens_lista = [
    "Energético", "Cereal genérico", "Saco de moedas", "Kit de chá", "JPEG SSS+", 
    "Calculadora científica", "Picareta", "Óculos escuros", "Garrafa térmica", "Camundongo", 
    "Cálice sagrado", "Pedra quente", "Blåhaj", "Power glove", "Feijoada"]
default itens_estado = [0, 0, False, False, False, False, False, False, False, False,
    False, False, False, False, False]
default items = ""
default item_imagem = 0

label inventory:
    scene inventoryScene with dissolve
    "Levantamento de Recursos"

    if token == 0:
        $ renpy.say("{color=#000}Carteira:{/color}", "Em termos de dinheiro")
        "Carteira:" "Nós não temos dinheiro."
    else:
        $ strToken = str(token)
        "Carteira" "[strToken] token."
    
    if itens_estado[0] > 0:
        $ items = items + "Energético x" + str(itens_estado[0]) + ", "
    
    if itens_estado[1] > 0:
        $ items = items + "Cereal Genérico x" + str(itens_estado[1]) + ", "
    
    if itens_estado[2]:
        $ items = items + "Saco de moedas, "

    if itens_estado[3]:
        $ items = items + "Kit de chá, "
    
    if itens_estado[4]:
        $ items = items + "JPEG SSS+, "
    
    if itens_estado[5]:
        $ items = items + "Calculadora científica, "
    
    if itens_estado[6]:
        $ items = items + "Picareta, "
    
    if itens_estado[7]:
        $ items = items + "Óculos escuros, "
    
    if itens_estado[8]:
        $ items = items + "Garrafa térmica, "
    
    if itens_estado[9]:
        $ items = items + "Camundongo, "
    
    if itens_estado[10]:
        $ items = items + "Cálice sagrado, "
    
    if itens_estado[11]:
        $ items = items + "Pedra quente, "
    
    if itens_estado[12]:
        $ items = items + "Blåhaj, "
    
    if itens_estado[13]:
        $ items = items + "Power glove, "
    
    if itens_estado[14]:
        $ items = items + "Feijoada, "

    $ items = items[:-2]

    if len(items) > 0:
        "Inventário:" "[items]"
    else:
        "Inventário:" "Nenhum item no inventário."
    $ items = ""

    return