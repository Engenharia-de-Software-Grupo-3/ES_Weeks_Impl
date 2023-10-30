image pyth perguntando = "images/Sprites Python/python 7.png"

image pyth escutando = "images/Sprites Python/python 8.png"

image pyth alegre1 = "images/Sprites Python/python 11.png"

image pyth alegre2 = "images/Sprites Python/python 13.png"

image pyth impressionada =  "images/Sprites Python/python 23.png"

image pyth pesames1 =  "images/Sprites Python/python 36.png"

image pyth pesames2 =  "images/Sprites Python/python 37.png"

image pyth confusa = "images/Sprites Python/python 34.png"

image pyth semhumor =  "images/Sprites Python/python 35.png"

label pythonEvent2:

    play music "audio/music.mp3" volume 0.5

    scene sala 1 with fade

    pyt "Um Cálice Sagrado ficaria tão legal no meu quarto..."

    pyt "Oh, [player_name]!"

    show pyth perguntando

    pyt "Você tem algo que goste de fazer no seu tempo livre?"

    show pyth escutando

    mc "Acho que nada muito específico."

    mc "Faço o que as pessoas geralmente fazem, como assistir filmes na TV, ver vídeos na internet, etc."

    mc "Mas não me importo muito com isso pra ser sincero."

    show pyth perguntando

    pyt "Hum, então você não tem um interesse especial por nenhuma atividade?"

    show pyth alegre1

    pyt "Não precisa ser coisas que dependam só de você."

    show pyth alegre2

    pyt "Eu por exemplo gosto de ir em festas e organizar elas, além de gostar de passar o tempo com meus amigos."

    show pyth escutando

    mc "Não mais. Agora que você falou, nos últimos anos eu não tenho feito muita coisa."

    show pyth alegre1

    pyt "Se 'não mais', quer dizer que você tinha algo antes, né? O que era?"

    mc "Eu praticava esportes."

    show pyth impressionada

    pyt "Ohhhhhh, um esportista nato."

    show pyth alegre1

    mc "Eu não diria isso. Pra ser sincero eu só gostava de jogar com meus amigos, mas aos poucos a gente foi parando de se falar, então também fui parando de jogar aos poucos."

    show pyth pesames1

    pyt "Nossa, isso é muito triste. Vocês brigaram?"

    show pyth pesames2

    mc "Na verdade não, eu acho que apenas estávamos envergonhados demais pra olhar na cara um do outro."

    show pyth pesames1

    pyt "Por que? O que aconteceu?"

    show pyth pesames2

    mc "Não foi nada demais, é só uma história tediosa mesmo."

    show pyth alegre2

    pyt "Mas eu adoraria saber! Vamos lá, o que vocês jogavam?"

    menu:

        "Basquete":

            mc "Basquete."

            mc "Era eu e mais 4 amigos que jogávamos de forma casual, até que um dia decidimos nos inscrever num torneio e lá encontramos eles na final."

            show pyth perguntando

            pyt "Eles quem?"

            show pyth escutando

            mc "Os Taiko Sentai."

            mc "Eram chamados assim por se vestirem cada um com uma cor e o pessoal que ficava no banco ficava tocando tambores a partida inteira para motivar o time."

            mc "Tinhamos o Taiko Vermelho que era o líder do time e Mãe Diná, o Taiko Verde que era um ex-atirador do exército, o Taiko Amarelo que jogava carregando uma impressora nas costas, ..."

            mc "... o Taiko Roxo que era um especialista em interpretar montanhas em peças escolares e o Taiko Azul que dançava hip-hop."

            mc "Acontece que eles eram muito bons e estamos sendo destruídos."

            show pyth pesames1

            pyt "Quer dizer que o peso de uma grande derrota afastou você de seus amigos?"

            show pyth pesames2

            mc "Foi o peso de uma dívida bancária na verdade."

            show pyth confusa

            pyt "?"

            mc "Acontece que a Taiko Sentai tinha um 6 membro que não havíamos visto que entrou no meio da partida."

            mc "Ele era um ex-espião do governo que tinha uma capa de invisibilidade, o problema é que por causa disso eu não vi ele e um passe com toda a minha força acabou acertando o espião e mandando o magrelo voando, o qual acertou os tambores, quebrando eles."
            
            mc "Ao terem seus tambores quebrados, a Taiko entrou em estado de choque e os jogadores tiveram que ser levados de ambulância para o hospital."

            mc "Ganhamos o torneio e uma multa por danos materiais e imateriais vinda dos gerentes do time, então o dinheiro coletivo de todos foi para a vala."


        "Futebol":

            mc "Futebol"

            mc "Era eu e um time de amigos que jogávamos de forma casual."

            mc "Era divertido até que decidimos entrar num torneio oficial."

            mc "Tava tudo bem até que encontramos eles na final."

            show pyth perguntando

            pyt "Eles quem?"

            show pyth escutando

            mc "O time do Ramon, um grupo de estudantes que utilizava poderes chamãs durante o jogo, invocando fantasmas e criaturas mitológicas pra ajudar eles."

            mc "Por isso eram imbatíveis."

            show pyth pesames1

            pyt "Quer dizer que o peso de uma grande derrota afastou você de seus amigos?"

            show pyth pesames2

            mc "Foi o peso de uma dívida bancária na verdade."

            show pyth confusa

            pyt "?"

            mc "Acontece que eu achei aquilo estranho, porque o regulamento do torneio deixava explícito que não poderia haver o uso de espíritos para auxiliar no jogo, mas ninguém se lembrava disso, porque foi uma regra feita como piada."

            mc "Apenas as pessoas do meu time lembravam, mas queríamos jogar contra eles e se as coisas continuassem, eles provavelmente seriam desclassificados."

            mc "Por sorte, eu havia trazido na bolsa uma edição de 'Exorcismo para leigos', então os exorcizamos para eles não serem desclassificados. O problema é que..."

            mc "... aparentemente, aqueles espíritos e seres lendários eram regulamentados pelo Ibama e fomos multados por maus tratos contra animais silvestres. Vencemos o jogo, mas todo o dinheiro do prêmio e parte de fora do prêmio foi usada pra impedir que meu time fosse pra cadeia."

    show pyth semhumor

    pyt "E você ainda disse que não fez nada nos últimos anos."

    show pyth pesames2

    mc "Isso não foi grande coisa, só algo que todo mundo faz se dedicar um pouco de tempo."

    mc "Toda semana acontecia coisa do tipo e minhas dívidas só iam crescendo."

    mc "... – Python estava perplexa"

    show pyth semhumor

    pyt "[player_name], eu acho que começo a entender como você saiu ileso de um atropelamento."

    hide pyth with moveoutright

    mc "Python disse antes de se virar e ir para a sala de aula."

    mc "O que será que ela quis dizer com isso?"

    $ pythonEventsCounter = 3
    return