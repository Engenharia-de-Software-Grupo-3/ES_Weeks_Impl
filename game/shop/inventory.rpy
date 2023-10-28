image inventoryScene = "images/Fotos/chestInventory.jpg"

default itens_lista = ["Energético", "Cereal genérico", "Saco de moedas", "Kit de chá",
    "JPEG SSS+", "Calculadora científica", "Picareta", "Óculos escuros", "Garrafa térmica",
    "Camundongo", "Cálice sagrado", "Pedra quente", "Blåhaj", "Power glove", "Feijoada",
    "Sorvete de pistache"]
default itens_estado = [1, 0, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False]

label inventory:
    scene inventoryScene with dissolve
    $ items = ""
    
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
    
    if itens_estado[15]:
        $ items = items + "Sorvete de pistache, "

    $ items = items[:-2]

    if len(items) > 0:
        "Estes são seus itens:"
        "{color=#000000}Inventário:" "[items]" 
    else:
        "Nenhum item no inventário!"

    return