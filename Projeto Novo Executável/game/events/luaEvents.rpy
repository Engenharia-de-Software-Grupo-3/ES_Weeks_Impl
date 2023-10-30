# Lua First Interaction
label luaEvent0:
    scene sala_recreacao with fade
    show lua 2 with fade
    lua 3 'Yo, P-kun, qual o seu tipo de jogo favorito?'
    show lua 2
    mc 'Hum?'
    menu:
        "RPG’s or FPS’s":
            lua 3 'Oh, esses são ótimos! Eu já te contei que eu fazia stream nesse gênero?'
            show lua 2
            mc 'Você era uma streamer?'
            lua 3 'É, eu tentei alguns anos atrás. Não deu muito certo....'
            lua 'Mas foi muito divertido! Nossa, eu queria fazer de novo....'
            show lua 2
            mc 'Por que você parou? Não fez o sucesso que você queria?'
            lua 3 'Quê? Não, eu era bem popular. Acho que eu tinha em média, tipo, 10k viewers.'
            show lua 2
            mc '10 MIL?'
            lua 5 'É, por aí. Eu só parei porque a Receita Federal achou meu canal e começou e rastrear meu vídeos. Bando de filhos da....'
            lua 3 'Oh, acho que me exaltei um pouco.'
            mc 'Não, não, tudo bem.'
        "Tabuleiro":
            lua '…'
            lua 3 'Não era esse tipo de jogo que eu estava falando...'
            show lua 2
            mc 'Oh, videojogos. Gosto do Colheita Feliz'
        "Gacha’s":
            lua 3 'Oh…'
            lua 'Então você é um desses...'
            show lua 2
            mc 'U-um desses?'
            lua 3 'Não é nada demais, alguns dos meu melhores amigos são jogadores de Gacha!'
            lua 5 ' Eu só nunca consegui entrar muito no gênero, sabe?'
            show lua 2
            mc 'Não, não, tudo bem.'
        "Fighting games or MOBA’s":
            lua 8 'OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOH!'
            lua 'ESSES TAMBÉM SÃO MEU FAVORITOS!'
            'Lua lhe agarra pelos ombros, seus olhos estrelados encarando o fundo da sua alma, suas mãos lhe chacoalhando como um bartender em uma centrífuga.'
            lua 7 'Eu já te contei sobre como em New Super Street Kombat Bros 2 - Ultra Instinct - Neo Challengers Anniversary Edition HD Remix 64… & Knuckles, se você derrotar todos os bosses no modo arcade 
            no ordem certa até você soletrar o código Konami, você consegue desbloquear…'
            'Ela continuou dando detalhes específicos para uma série de ações das quais, para ser bem sincero, você não fazia a mínima ideia o que significavam.'
            lua 3 'Oh, acho que me exaltei um pouco.'
            show lua 2
            mc 'Não, não, tudo bem.'
    lua 3 'Sério? Há, então já sei!'
    lua 7 'Na próxima vez que a gente se encontrar, eu levo o meu portátil para a gente jogar.'
    lua 8 'Até!'
    hide lua with moveoutright
    'Lua some sem dar muitas explicações, mas você sente que os dois entendem-se um pouco melhor agora.'
    $ luaEventsCounter = 1
    return

label luaEvent1:
    scene sala_recreacao with fade
    show lua 2 with fade
    lua 3 'Yo, [player_name]! Aqui, como eu disse.'
    'Lua segura uma TV, uma sacola cheia de cabos e uma grande caixa de papelão, equilibrando tudo com duas mãos e uma cabeça.'
    show lua 2
    mc 'Você não disse que ia trazer um portátil?'
    lua 2 '?'
    lua 3 'Esse é o meu setup portátil. Você devia ver o outro….'
    lua 5 'Enfim, me dá alguns minutinhos, eu não monto isso faz um tempo.'
    show lua 2
    mc 'Deixa eu ajudar.'
    show lua 2
    lua 3 'Sério? Valeu aí.'
    'Vocês demoram mais de “alguns minutinhos” organizando uma série de fios e componentes eletrônicos e resolvem conversar no meio tempo.'
    lua 24 'Hum… então… tipo… qual o seu pastel favorito?'
    show lua 23
    mc 'Meu… pastel favorito?'
    lua 24 'É… eu não sou muito bom de conversar, sabe?'
    lua 'Normalmente eu só falo de coisas relacionadas a jogos.'
    show lua 23
    mc 'Você gosta tanto assim?'
    lua 24 'Eu gosto, mas tipo… é também o motivo pelo qual eu sou conhecida, sabe?'
    lua 'Depois de um tempo, era tudo o que as pessoas esperavam que eu falasse. E como era tudo que as pessoas esperavam que eu falasse….'
    show lua 23
    mc 'Então se tornou tudo sobre o que você fala.'
    lua 23 '...'
    lua 26 'Por aí…'
    show lua 23
    mc 'Olha, eu não te conheço a muito tempo….'
    mc 'Mas isso também significa que eu não sei muito o que esperar de você falar, não é mesmo?'
    lua '!'
    lua 24 'Eu acho que sim.'
    lua 'Então eu posso falar de qualquer coisa.'
    show lua 2
    mc 'Do que você quiser.'
    lua 28 'Eu estou completamente livre!'
    lua 29 'Mwahahahahaha!'
    'Nesse momento, o sinal de próxima aula toca'
    lua 3 'F*#. Bem, não completamente livre. E agora que terminamos de montar o console…. A gente joga na próxima, okay? E eu vou falar um monte de coisas na próxima vez, você nem imagina!'
    show lua 2
    mc 'Estarei esperando.'
    'E com isso, Lua sai correndo em direção a próxima aula, e você não pode evitar de pensar que agora você e Lua cresceram mais próximos.'
    $ luaEventsCounter = 2
    return

label luaEvent2:
    scene sala_recreacao with fade
    "Como eu queria aquele Blåhaj..."
    "Oh, [player_name]!"
    show lua
    lua 17 'Ei, quer finalmente jogar com uma pro-player como eu mesma?'
    show lua 16
    mc 'Bora.'
    lua 7 'Aqui, vamos jogar esse jogo.'
    show lua 6
    mc 'Virtual Fighter?'
    lua 7 'É! É um jogo de luta em que você joga como V-Tubers ou Vocaloids! É muito bom!'
    show lua 6
    mc 'Então eu vou com… essa de cabelo azul longo.'
    lua 8 'Primeira partida e já está indo de META, né? Tá bom, deixa eu te mostrar como se faz….'
    show black with fade
    'Lua limpa o chão com você em exatamente 23 segundos'
    hide black with fade
    show lua 6
    mc 'Nossa.'
    mc 'Tipo…'
    mc 'Nossa.'
    lua 15 'Eu disse que era boa.' 
    lua 17 'Aí aí…. aqui, deixa eu jogar com meus pés, talvez você tenha uma chance.'
    show black with fade
    'Vocês jogam mais uma partida, ela usando os pés e você controlando normal' 
    'E mesmo que esteja mais acirrada, você não pode deixar de se sentir um pouco humilhado…' 
    'Especialmente quando você perde...'
    hide black with fade
    show lua 8
    mc 'COMO?'
    lua 'Mwahahahahaha!'
    lua 'EU. SOU. MUITO. BOA!'
    lua 7 'Ai ai…. Ei, por que você escolheu essa personagem?'
    show lua 6
    mc 'Huh? Eu achei ela meio bonitinha.'
    lua 15 'Meio bonitinha?'
    show lua 14
    mc 'Tá bom, bem bonitinha.'
    lua 17 'É… eu também gosto muito dela. Na verdade, eu estava pensando….'
    lua 13 'Nah, deixa prá lá.'
    show lua 23
    mc 'Fala.'
    lua 24 'Não agora… eu ainda não tenho certeza.'
    lua 'Mas, se eu for falar para alguém….'
    lua 29 'Esse alguém sem dúvida vai ser você. Até!'
    'Mesmo com a curiosidade lhe comendo vivo, você ainda sente que se aproximou mais de Lua hoje.'
    $ luaEventsCounter = 3
    return

label luaEvent3:
    scene sala_recreacao with fade
    show lua 23 with moveinright
    lua 24 'Então, [player_name]!'
    lua 'Eu decidi que vou fazer Cosplay!'
    show lua 23
    mc 'Cosplay?'
    lua 24'Cosplay!'
    show lua 23
    mc 'Aquela coisa de fantasia?'
    lua 15 'Nah, cosplay é bem mais do que só uma coisa de fantasia! É você encarnar a personagem!'
    lua 13 'Lembra da personagem que você usou quando jogamos? A bonitinha de cabelo azul?'
    show lua 23
    mc 'Sim.'
    lua 24 'Eu vou ser ela! Eu sempre quis fazer o Cosplay de algum personagem, e ela vai ser minha primeira.'
    show lua 23
    mc 'Mas ela parece bem complicada, não acha?'
    lua 26 'E por que eu iria começar com alguém simples? Qual a graça disso?'
    lua 24 'Sem falar quê….'
    show lua
    'Ela fala algo inteligível, um murmuro em que você só entende as palavras “você” e “bonitinha”?'
    show lua 2
    mc 'O que foi isso!'
    lua 3 'Nada!'
    lua 5 'Nada! Eu disse nada, ignora essa última parte.'
    lua 3 'Enfim, eu só queria lhe agradecer.'
    show lua 2
    mc 'Pelo quê? Eu não fiz nada.'
    lua 3 'Por me deixar conversar com você, né? Sem isso, eu não acho que teria decidido fazer Cosplay.'
    lua 'Enfim, eu te aviso quando eu for usar.'
    lua 7 'E então você vem correndo para me admirar, entendeu?'
    show lua 6
    mc 'Você que manda!'
    lua 8 'É assim que eu gosto.'
    'Você sente que se aproximou mais de Lua.'
    if itens_estado[12] == True:
        mc "Lua..." 
        lua 2 "?"
        mc "eu tenho um presente para você."
        lua 3 "Isso é..."
        lua 8 "UM BLAHAJ?"
        lua "Eu queria muito um desse! Como você sabia?"
        lua 7 "Muito obrigada!"
        "A felicidade está no ar... Em cada sorriso. Em cada olhar!"
        $ itens_estado[12] = False
        $ luaLoveCounter += 3
    $ luaLoveCounter += 3
    $ luaEventsCounter = 4
    return
