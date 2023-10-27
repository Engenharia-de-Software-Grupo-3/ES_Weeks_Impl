label semana1_dia1:
    scene black
    show text "Dia 1" at truecenter
    # Chegada
    play music "audio/music (2).mp3" volume 0.5
    scene escola with dissolve
    mc "Rapaz, eu estou nervoso." 
    mc "Vamos, você ensaiou isso dezenas de vezes com a sua mãe…"
    mc "“Olá, meu nome é...”"
    $ player_name = renpy.input("Olá, meu nome é...", length=32)
    $ mc = Character("[player_name]", who_color = "#0004ff")
    $ mcN = Character("[player_name]", who_color = "#0004ff", what_color = "#6d6d6d", what_prefix = "(", what_suffix = ")")
    mc "“Eu sou uma linguagem de programação…”"
    menu:
        mc "“Eu sou uma linguagem de programação…”"
        "Procedural":
            $ player_type = "Procedural"
        "Orientada a Objetos":
            $ player_type = "Orientada a Objetos"
        "Funcional":
            $ player_type = "Funcional"
        "Lógica":
            $ player_type = "Lógica"
    mc "“E espero que tenhamos um bom semestre juntos…”"
    mc "..." 
    mc "Eu soo como um idiota"
    "Smack!" with vpunch 
    "Você dá um tapa em si mesmo"
    mc "Se componha! Você foi selecionado assim como qualquer outro estudante aqui!" 
    mc "Eu ainda me lembro como se fosse ontem…"
    # Flashback
    call dia1_flashback from _call_dia1_flashback
    # Python Intro
    mc "Ok, talvez isso não me encha de confiança como achei que faria"
    mc "Não importa! Respire, relaxe, não tem do quê tem medo"
    pyt "Olá?"
    mc "AHHH!"
    "Você dá um pulo para traz quando uma garota com um brilho nos olhos cutuca seu ombro"
    show pyth i with moveinleft
    pyt "Você é o estudante novo?"
    "Rápido, você tem que se apresentar." 
    "Não há mais tempo para pensar, diz a primeira coisa que vier à sua mente."
    menu:
        "Não há mais tempo para pensar, diz a primeira coisa que vier à sua mente."
        "Introdução descolada":
            mc "Y-yo-yo! Se liga, mano-bro, aqui é P-kun na área!"
            pyt 34 "..."
            mc "..."
            mcN "Eu devo ter algum problema"
            pyt -34 "Yo-yo!"
            mc "!"
            pyt "Aqui é DJ Python falando, trazendo para o baile o mais venenoso grave!"
            mcN "Ela devolveu!" 
        "Introdução comum":
            mc "Olá, meu nome é [player_name]"
            pyt "Muito prazer, [player_name]. Eu me chamo Python e vim aqui pra te receber na academia."
            mc '...'
        "Introdução em Haiku":
            mc "Aluno novo" 
            mc "cujo nome restrito" 
            mc "depois te digo."
            pyt 34 "..."
            mc "..."
            mcN "Eu devo ter algum problema"
            pyt -34 "Seja bem-vindo NameError Exception nessa Academia. Me chamo Python"
            mcN "Ela devolveu!"
    $ pyt = Character('Python', who_color = '#fffb00', image = "pyth")
    show pyth i 32
    "Ela manteve a pose por alguns segundos, antes de rir de forma animada"
    show pyth i
    pyt "Não precisa ficar nervoso, eu sou uma de suas colegas de classe."
    mc "Obrigado."
    mc "E desculpa, eu nunca achei que iria ter um tour nessa academia, quem dirá estudar nela."
    pyt "Relaxa, eu soube que você foi escolhido a dedo pelo diretor. Ele pode ser meio esquisito, mas ele normalmente acerta em cheio nesse tipo de coisa."
    mc "Se você diz."
    pyt "O semester começa amanhã, então a gente vai ter que acelerar as coisas e te dar um intensivão sobre como a Academia funciona."
    hide pyth i
    "Vocês começam a andar enquanto Python lhe apresenta as instalações do local"
    #Biblioteca
    scene biblioteca with dissolve
    show pyth i
    pyt "Aqui é a biblioteca."
    hide pyth i
    jav "Zzzzz..."
    show java 9
    mc "E quem é aquele ali?"
    jav "Zzzzz..."
    hide java
    show pyth 14 with moveinleft
    pyt "Ignore o dorminhoco, ele vai acordar antes do natal."
    pyt "Na biblioteca, você pode estudar com um parceiro!"
    pyt "Estudar em conjunto é uma ótima forma de ficar mais próximo a um colega, além de te preparar para provas adquirindo estratégias."
    pyt "Durante as batalhas de término da semana, você e um parceiro podem usar suas estratégias para enfrentar questões."
    menu:
        pyt "Durante as batalhas de término da semana, você e um parceiro podem usar suas estratégias para enfrentar questões."
        "Batalhas?":
            pyt 12 "Soa estranho não é. Não sei como começou, mas o pessoal por aqui chama as provas de 'batalha'."
            pyt 14 "Nas batalhas, Existem 3 tipos de questões, assim como tipos de estratégias: teórica, algébrica e analítica"
            pyt "Você pode levar para a batalha até 4 estratégias."        
            pyt "Ao ter sucesso num teste, você fica mais proximo de seu parceiro escolhido. Mas tenha cuidado, porque falhar nele pode distanciar vocês."
        "Entendo...":
            pass
    show pyth i
    pyt "Que tal praticar comigo? Eu sou bem esperta, sabia?"
    menu:
        pyt "Que tal praticar comigo? Eu sou bem esperta, sabia?"
        "Participar da batalha":
            pyt 32 "Fight on!"
            call prepare_tutorial_battle from _call_prepare_tutorial_battle
            scene biblioteca with dissolve
            play music "audio/music (2).mp3"
            show pyth i
            pyt "Isso ai! Terminamos."
            pyt "Como derrotamos [teste0_Acertos] questões, conseguimos nota [teste0_Nota] nesse teste."
            pyt 32 "Boa luta. Se quiser estudar comigo novamente, pode me chamar."
        "Recusar a proposta":
            pyt i 35 "É uma pena. Se quiser estudar comigo em algum outro momento, pode me chamar."
    show pyth i
    pyt "Acho que chega de biblioteca."
    pyt "Vamos, ainda tenho muito pra te mostrar!"
    hide pyth
    # Encerrar
    scene corredor with dissolve
    "Assim, vocês continuam o passeio pela Academia" 
    "O qual não pôde durar muito tempo, já que vocês foram interrompidos por um aviso que vinha dos alto-falantes no corredor"
    alan "Python, perdão interromper o seu serviço, mas vocês vão ter que sair."
    alan "Já bateu a hora da escola fechar os portões e não posso perder a audiência de custódia da Computação."
    show pyth 28 with moveinleft
    pyt "Awww, parece que vamos ter que deixar as coisas pra depois"
    show pyth i
    pyt "Então te vejo amanhã, [player_name]. Espero que possamos ser amigos"
    hide pyth
    scene black with dissolve
    "E assim terminou seu primeiro dia na Academia antes do seu primeiro dia na Academia" 
    "Você estava imaginando que as coisas seriam bem mais caóticas do que de fato foram, e, sinceramente, aquilo te dá um certo alívio" 
    "A maior parte do seu nervosismo sumiu por causa da recepção recebida. Agora você mal pode esperar para seu segundo dia"
    return

label dia1_flashback:
    play sound "audio/FlashbackSoundEffect.mp3" fadein 1.0
    pause 1.0
    scene rua with dissolve
    "Dia de ontem..."
    mc "R$93,75 da conta d’água…" 
    mc "R$50,00 vai ter que ir para a troca do botijão de gás…"
    mc "Pelo que parece a cesta básica tá variando de preço bastante de mercado pra mercado, dependendo do canto acaba até melhor comprar as coisas separado…" 
    mc "Se é assim, por que diabos fazer a cesta básica?"
    mcN "Eu folheava os papéis que estavam em minhas mãos enquanto andava pela calçada."
    mcN "Contas, panfletos de mercado, o cartão de visitas do “Motoboy gás”, número da lotérica, etc." 
    mcN "Nem sempre foi assim, porém, devido a circunstâncias que não valem a pena serem relembradas, a coisa chegou onde chegou."
    mc "Isso é mal, eu vou precisar arrumar pelo menos um emprego de meio período." 
    mc "Talvez o ‘Metrô’ contrate alguém sem experiência, não deve ser muito complicado montar um sanduíche."
    mc "Também pode ser que eu consiga algo como ‘desempacotador’ se ir de porta em porta nos mercados da região." 
    mc "No pior dos casos, posso tentar o jogo do bicho."
    mcN "Eu analisei minhas opções enquanto checava as contas que tinha pra pagar daqui à uma semana."
    mcN "Existem diversas formas de conseguir dinheiro, mas nenhuma parecia a resposta correta para minha situação"
    mc "A conta de luz deu R$114,55? Como? Eu tomei um cuidado especial pra economizar energia esse mês. O que pode ter acontec-" 
    mc "TAXA DE USO COMUNITÁRIO DE R$89,99!?" with vpunch
    mcN "Jogo do bicho era a resposta correta para minha situação."
    mc "A coisa realmente descarrilou…"
    mcN "As contas iam ser atrasadas e isso ia virar uma bola de neve. Água e luz são cortados com 3 meses de atraso e eu já tava no segundo." 
    mcN "Mesmo que arrumasse um emprego, não seria a tempo de pagar as contas. Ainda por cima eu teria que pagar a taxa de religação de água e luz após pôr as contas em dia." 
    mcN "Já consigo me ver entrando no jogo do bicho: dinheiro fácil no início, depois vem o endividamento, agiotas batendo em minha porta e por fim eu aparecendo no jornal local." 
    mcN "Um certo padre uma vez disse que se o ser humano soubesse de sua inevitável danação, viveria mais feliz após aceitar ela."
    mcN "Talvez fosse verdade, porque ao chegar na esquina, senti meu corpo mais leve." 
    mcN "Parecia uma força externa tirando meus pés do chão e jogando meu corpo pro ar."
    mcN "Tudo estava as mil maravilhas, até que uma dor que se espalhou por todo o lado direito do meu corpo me fez perceber algo: não parecia, de fato era o que estava acontecendo"
    mcN "Tudo ficou mais claro quando virei minha cabeça para a direita e vi qual o objeto cor de vinho que havia me acertado." 
    play sound "audio/CarCrashSound.mp3"
    pause 3.0
    show text "" with vpunch
    show text "" with vpunch
    pause 0.5
    mcN "Meu corpo foi jogado pra cima do capô escaldante digno de um dia ensolarado de 40°C enquanto o carro freou bruscamente." 
    mcN "Fiquei deitado esparramado lá. Não estava com disposição para levantar. Seria esse o meu fim? Frito como uma coxinha na air frier após ser amassado como uma batata que vai virar purê?"
    alan "Está tudo bem, o carro não estava rápido o bastante para terminar sua existência"
    mcN "Eu me recuso a acreditar que a pessoa que me atropelou disse que tá tudo bem em me atropelar"
    show alan with zoomin
    alan "As máquinas me surpreendem muito frequentemente. Quem diria que meu carro poderia ir de 80 para 0 tão rápido durante uma curva fechada." 
    alan "Enfim, deixa eu te ajudar"
    mcN "O homem me tirou de cima do capô e me pôs deitado na calçada enquanto calmamente ligava para uma ambulância"
    alan "Qual é mesmo seu nome?"
    menu:
        alan "Qual é mesmo seu nome?"
        "Dizer seu nome":
            alan "Então é você?..."
            mcN "Ele parecia um pouco reflexivo depois de ouvir meu nome."
            alan "Muito bem, sua colaboração se faz necessária para o que vem a seguir."
        "Gemer de dor":
            alan "Vamos, você não está tão ruim assim. Só estou ligando para a ambulância para ter certeza disso…"
            alan "E para não ser processado por não dar assistência ao atropelado."
            mcN "O homem viu as contas que eu levava e parecia confuso por um momento"
            alan "Então é você?..." 
    mcN "Ele começou a recolher os pápeis que eu segurava já que eles se espalharam após eu ser acertado."
    mcN  "Deu para ver um sorriso suspeito em seu rosto, o que me deu um péssimo pressentimento."
    alan "Nós só podemos ver um pouco do futuro, não é mesmo?"
    alan "Se eu não estiver enganado, você parece estar numa situação preocupante."
    menu:
        alan "Se eu não estiver enganado, você parece estar numa situação preocupante."
        "Estou. Acabo de ser atropelado":
            alan "Você é do tipo que guarda mágoas, ao que parece."
            alan "Águas passadas não movem moinhos, assim como um rio nunca é o mesmo."
            mcN "..."
        "Não é da sua conta":
            alan "Realmente, essas contas são suas."
            mcN "..."
        "Não se preocupe com isso":
            alan "Me preocupo. Como eu poderia não me preocupar com uma oportunidade como essa."
            mc "?"
    alan "Algo que você deveria saber sobre mim:"
    alan "Eu acredito que às vezes são as pessoas de quem ninguém espera nada que fazem as coisas que ninguém consegue imaginar."
    mcN "E o que isso deveria significar?"
    alan "Meu nome é Alan Turing. Eu sou diretor de uma certa Academia Prestigiada: a Academia [school_name]."
    $ alan = Character('Alan Turing', who_color = '#494848')
    alan "E eu gostaria de lhe convidar à vir participar dela."
    mcN "Do que diabos ele está falando?"
    alan "Você deve estar se perguntando o motivo de eu estar lhe convidando assim de repente"
    alan "Um estranho lhe convida para integrar uma das instituições mais renomadas do país, claro que você acharia que é um novo tipo de golpe"
    alan "Mas não se pergunte porque te ofereço essa vaga, pois não adianta esclarecer esse ponto agora. Se pergunte porque você deveria aceitar"
    alan "Nós iremos pagar as despesas básicas que você tiver, assim como pagar as devidas contas para que comece do zero. Muito tentador não acha?"
    mcN "Eu pude ouvir já perto o som da sirene da ambulância se aproximando"
    alan "Parece que estamos sem tempo. De qualquer forma, também estou com pressa"
    mcN "O homem tirou da sua roupa uma carta e a pôs em minhas mãos, indo em seguida na direção da ambulância"
    alan "Se você decidir aceitar a proposta da carta, apenas apareça na academia. Deixarei os preparativos prontos para recebê-lo"
    alan "Se não aparecer, saberei que me enganei sobre você e será melhor que ambos esqueçamos o que aconteceu aqui"
    alan "Desejo a você sucesso em sua futura empreitada."
    hide alan with fade
    mcN "Fui posto dentro da ambulância e levado para o hospital, e durante o tempo todo eu só conseguia pensar: “o que acabou de acontecer?”"
    play sound "audio/FlashbackSoundEffect.mp3" fadein 1.0
    pause 0.4
    scene escola with dissolve
    "Dia de hoje..." 
    return