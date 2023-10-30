label semana1_dia2:
    scene black
    show text "Dia 2" at truecenter
    # Dia 2
    # Cenário da sala de aula
    scene sala 1 with dissolve
    "Enfim seu verdadeiro primeiro dia naquele lugar"
    "A sala de aula estava agitada e você teria notado isso se não fosse seu primeiro dia"
    "Pessoas comentam sobre você sem nunca se aproximar, mas não há o que fazer sobre o entusiasmo da juventude e você não se incomodava com isso"   
    "O que você sentia era um misto de emoções: animação, curiosidade, insegurança, e por aí vai"
    "Sua primeira aula naquela academia, e isso fazia seu coração se palpitar de emoção, como se sua alma subisse ao céu…"
    # ~Flash e som de trovão~ 
    stop music fadeout 1.0
    play sound "audio/thunder.mp3"
    show ada with blinds
    ada "E seu corpo descesse ao mar"
    "De repente o silêncio"
    ada "Saibam disso: diante de você está Ada Lovelace, a membro mais notável desta infame instalação!"
    $ ada = Character('Ada Lovelace', who_color = '#494848', image = 'ada')
    play music "audio/music (2).mp3"
    "Nas caras dos alunos estava estampado um tédio de que espera na fila do banco."
    "Aparentemente aquilo era só mais uma quarta normal na semana dos que frequentam essa academia"
    ada "Todos vocês se renderam ao acomodo da vida em busca de conforto, não é mesmo?"
    ada "Saibam que o amanhã jamais igualará o ontem; nada, exceto o mutável, pode perdurar!"
    ada "Temos um novo aluno, mas não direi quem é."
    ada "Se quiserem saber se esforcem para perceber como o ontem tornou-se hoje, assim como o amanhã nascerá do ontem"
    show ada at left with move
    "Logo após aquilo, Ada abriu um velho notebook cuja carcaça parecia ser feita a mão, com remendos de outros computadores, e começou a fazer a chamada."
    ada 'Figurante 1'
    show HTML at right
    'Figurante 1' 'Presente'
    hide HTML
    ada "Figurante 2"
    show SQL at right
    'Figurante 2' 'Aqui'
    hide SQL

    ada 'Python'
    #Python - 13
    show pyth 13 at right
    pyt "Presente, professora!"
    hide pyth

    ada "Java"
    # java 6
    show java 6 at right
    $ jav = Character('Java', who_color = '#ff7300', image = "java")
    jav 'Zzzzz…'
    ada 'Como um suco de lágrimas pungidas, está velho, morto e cansado'
    ada '...'
    ada 'Mas pelo menos está de corpo presente. Prosseguindo.' 
    hide java

    ada 'Ruby.'
    # ruby 2
    show ruby 2 at right
    rub 'Presente, professora'
    hide ruby

    ada 'Figurante 3'
    show SQL at right
    'Figurante 2' 'Foi ao banheiro'
    hide SQL
    ada 'Aquela que Ismália deseja!'
    "..." 
    "Silêncio absoluto"

    ada "Lua?"
    # Lua 22
    show lua 22 at right
    lua 'Eu te avisei que não responderia se fizesse essa piada de novo'
    ada 'Ó pesar, vês, eu acabei por ter respeitar, porque sei que nunca me deixará'
    hide lua

    ada 'Dando continuidade: Haskell'
    'Olhando pra trás depois de ouvir um leve barulho de algo batendo na mesa, você vê um olho alado verde.' 
    'Você tem a impressão de que tinha alguém alí, embora não saiba o porquê.'
    ada 'Estou em encantador estado de confusão, mas deixemos isto de lado'
    hide lua

    ada 'Cobol.'
    # cobol 8
    show cobol 8 at right
    cob "Aqui me encontro, senhorita"
    hide cobol

    ada "Swift"
    # swi 18
    show swift 18 at right
    swi "Ai, ai. Todo dia isso." 
    swi "Estou ofendido com seu tratamento seco todo dia comigo"
    ada "3 palavras mais e te ponho novamente num para-raios"
    # swi 22
    show swift 22
    swi 'Tch.'
    hide swift

    ada 'Prolog'
    show pro_owl at right
    'Você vê uma coruja metálica voando com um pirocoptero na cadeira a sua frente'
    'Coruja' "hoo-hoo!"
    hide pro_owl
    ada "Eu já avisei que a coruja não pode marcar presença."

    ada 'Por fim, [player_name].'
    menu:
        "O que fazer?"
        "Se manifestar":
            mc 'Estou aqui'
            ada 'Jamais! Isso não é o bastante'
            ada 'Venha aqui'
            "Ótimo. Parabéns. você podia só ter sutilmente levantado a mão, agora vai ter que fazer sua auto-apresentação de 2 minutos enrolando e falando o mínimo sobre si mesmo"
            "Nada melhor do que esse tipo de ver-… Por que a professora tá pegando uma bola de basquete?"
            play music "audio/battle.mp3"
            show ada ballin at center with move
            ada "Você!" 
            ada 'Você acha que tem o necessário para driblar todos os perigos que a vida acadêmica jogar na sua cara!?'
            mc 'Eu não sei jogar basquete'
            ada 'Oh ho! És destemido o bastante para balbuciar falácias frente a minha face.'
            ada 'Use tal gana para driblar a mim como seu primeiro obstáculo'
            'Ada rapidamente joga a bola para você e se põe numa posição defensiva'
            ada -ballin 'O que está esperando?'
            'A professora falou apontando para um cesto de lixo atrás dela'
            'Agora você sabe porque a sala possui 2 cestos de lixo, um à direita e outro à esquerda do quadro' 
            'Como a maior parte dos alunos parece estar desinteressados nessa cena, provavelmente é algo que acontece com frequência aqui'
            'Você decide entrar na onda. Quanto mais rápido você acabar com isso, mais rápido poderá voltar pro seu-'
            ada 'Muito lento!'
            "A professora avança com uma surpreendente habilidade e rouba a bola de você"
            ada ballin 'Indecisão, esse é seu problema. De fato uma nova vida acadêmica pode ser intimidadora, mas se lembre que estamos aqui pra ajudar você'
            'Jogar basquete no meio da sala não estava ajudando'
            ada 'Mesmo assim, nem sempre estaremos lá pra te defender. Você então vai se virar sozinho. Me mostre que é capaz disso se defendendo do meu ataque!'
            'Ok, agora você está irritado'
            'Um grande circo. Era isso que aquilo parecia. No momento que você teve a bola roubada por alguém num vestido vitoriano aquilo virou pessoal.' 
            'Sim, se aquela senhora queria que você mostrasse sua determinação, é isso que você irá fazer.'
            'Mostre a ela todos os anos em que você jogou com seus amigos durante os 9 anos: Rogério Matos e Ronald Williams'
            'Todo suor derramado na quadra do parquinho perto da sua casa, treinando para jogar com os idosos da geração saúde de seu bairro'
            'Mostre pra todos da turma o seu basquete!'
            'Rogério, essa é pra você!'
            ada 'Isso! Está vivo! Está vivo!'
            ada 'Proteja tal belo lusco-fusco de minha infiltração!'
            show ada ballin at right with move
            'Ada faz seu movimento pela direita com uma arrancada, mas você avança fechando-a e minimizando a distância'
            mc 'Te peguei!'
            ada 'Wrong, my dear!'
            'Ada se prepara para um recuo rápido, mas ao perceber isso, você se antecipa pra frente, assim irá impedir que ela consiga distância'
            ada 'Inocência!'
            show ada ballin at left with move
            'Ada então dá início ao seu avanço numa transição de movimentos anormalmente rápida.'
            show ada ballin at right with move
            'Então você entendeu: era uma armadilha!'
            show ada ballin at left with move
            'O vestido vitoriano da professora demasiadamente grande ocultava seu footwork, assim criando uma finta especial, usável apelas pelas donzelas do século 19.'
            show ada ballin at center with move
            'Ela estava perto demais, vocês vão colidir!'
            'Para evitar isso você tenta recuar, mas seu movimento de avanço preventivo já havia sido feito'
            'Com seu centro de gravidade desalinhado e os rápidos movimentos de ambas as partes, você se desequilibra e cai de bunda no chão'
            'Ada aproveita o momento e acerta a bola no cesto que você tentava defender'
            ada - ballin 'Impressionante. Você é o segundo estudante mais determinado que temos nessa sala.'
            ada 'Não se sinta mal por perder para meu ankle breaker, é uma poderosa técnica que trespassou o tempo, tornando-se letal ainda na modernidade'
            'Ada pega a bola e passa a você'
            ada 'Guarde como recordação desse dia e considere isso como um memento para sempre continuar seguindo em frente'
            ada 'Além disso...'
            "..."
            ada 'Rogério estaria orgulhoso.'
            'Não, Rogério não estaria orgulhoso.'
            'Rogério estaria se contorcendo se soubesse que foi mencionado nessa palhaçada'
            'Você sabe disso, afinal é só o que quer fazer depois que voltou aos seus sensos'
            'Você volta envergonhado pra sua cadeira e se encolhe nela pra tentar esquecer o que aconteceu'
        'Ficar em silêncio':
            'Por quê não responder sua primeira chamada na nova academia? Talvez vergonha?'
            'Uma vontade iminente de tornar-se delinquente? Uma predisposição para o caos?'
            'Sim, seu nome será marcado na história da turma como aquele que ignorou Ada Lovelace no seu primeiro dia!'
            show ada at center with move
            ada 'Ultraje!'
            show ada ballin
            pause 0.7
            show ada
            show bola at truecenter with vpunch:
                zoom 0.75
            pause 0.7
            hide bola
            'Ou como aquele que tomou da mesma uma bolada na cara'
            'A bola de basquete que acertou seu rosto caiu ao lado da sua mesa. Você a apanha confuso'
            mc 'O que foi isso!?'
            ada 'Hão de chorar por ela os cinamomos, mas se os cinamomos não sabem que é ela, por quem chorarão!?' 
            ada 'Uma apresentação é necessária para encravar seu eu na mente daqueles ao redor'
            ada 'Já que você não quis tomar a iniciativa, fiz isso por você'
            ada 'Pode me agradecer depois e ficar com a bola como uma recordação'
    scene sala 1
    #Narrador - (Python 29, Java 11, Ruby 6, Lua 13) 
    show pyth 29 at left
    show java 11 at center
    show ruby 6 at right
    'Realmente aquilo deixou uma recordação na turma, mas você não sabe se vai ser mais uma das coisas que cai na normalidade do seu novo dia a dia acadêmico.'
    #Escurece a tela por alguns segundos para dar a impressão de tempo ter passado
    scene black with dissolve
    play music "audio/music (2).mp3"
    'Depois de uma aula mais competente do que você esperava sobre a história da computação, Ada sai da sala e a turma que estava morta durante boa parte da explicação da professora voltou a vida'
    scene sala 1 with dissolve
    'Você vê pelo canto do olho o rapaz que você viu dormindo ontem na biblioteca se aproximando'
    show java 16 at center with moveinleft
    'Meio acordado, meio intenso. Duas aparencias que não deveriam coexistir, mas de alguma forma ele faz ser possivel'
    'Cabelo bagunçado com uma cor vibrante de laranja, olhos marcados por olheiras e determinação. É, algo estava claro '
    'Ele poderia reinar o mundo inteiro ou cair de cara no chão com a menor das brisas'
    jav 13 'Hey, eu ouvi sobre você.'
    show java 16
    'Ele tenta ser simpático. Não funciona muito, mas o esforço é apreciado'
    mc 'Oi, eu sou [player_name], um estudante novato aqui'
    jav 13 'O atropelado, né? Turing me falou. Sou java, ex-presidente de classe'
    show java 10
    'Ele dá um pequeno sorriso. Sobre você ser atropelado. Ele sorri.'
    jav 13 'Deveria ter sido eu a te acolher ontem, mas tive que mandar Python no meu lugar. Desculpa.'
    show java 16
    menu:
        "Por onde começar..."
        "Ex-presidente de classe?":
            jav 13 'Yeah, trabalho cansativo. Decidi me aposentar esse ano, fui presidente desde o fundamental'
            show java 16
            mc 'Parece ser um trabalho bastante complicado'
            jav 13 'Normalmente não é, mas essa Academia não é a mais normal das instituições'
            jav 'A invasão ninja do ultimo semestre foi um nível completamente diferente do normal'
            mc 'A o quê?'
            show java 16
            'Python se aproxima de vocês dois com um sorriso no rosto'
            show java 16 at left with move
            show pyth at right with moveinright
            pyt 13 'Ei, como vai Senhor Ex-presidente, gostando do estilo de vida aposentado?'
            jav 13 'É bom desacelerar de vez em quando'
            show java 16
        "Você tá bem? Parece cansado.":
            jav 13 'Eu tô bem.'
            show java 16
            'Ele puxa da bolsa a garrafa térmica mais comicamente longa que você já viu em todos os seus anos de vida e dá uma golada'
            show java 14
            'Uma longa golada' 
            '...' 
            'Ainda no processo'
            '...'
            'Qual a chance dele se afogar no processo?'
            '*Gulp*'
            show java 16
            'Enfim acabou'
            jav 13 'Completamente bem'
            'Python se aproxima de vocês dois com um sorriso no rosto'
            show java 16 at left with move
            show pyth at right with moveinright
            pyt 13 'Não se preocupe, é só café. Café o suficiente pra matar um elefante, mas ainda só café.'
        "Você é amigo da Python?":
            jav 13 'É, somos vizinhos desde antes de entrarmos na Academia. Ela me conhece desde a época da Sun Microsystems, na verdade. Datamos de muito tempo atrás'
            show java 16
            mc 'Sério? E como era a pequena Python?'
            jav 13 'Ela ainda é pequena de certa forma. Não mudou muito, a mesma velha e pequena despreocupada, sempre tentando fazer o mundo sorrir'
            'Python se aproxima de vocês dois com um sorriso no rosto'
            show java 16 at left with move
            show pyth at right with moveinright
            pyt 13 'Hey, minhas orelhas tão queimando. O que é que os dois galãs aí estão falando sobre mim'
            jav 13 'Olá senhorita Python. Obrigado pela ajuda com o tour.'
            jav 'Você por acaso não saberia quem desenhou na minha cara com uma caneta permanente ontem, saberia?'
            show java 16
            pyt 'Oh my, Senhor Java. Eu não faço nem ideia. De fato um mistério digno da atenção de Prolog'
            mc 'Eu bem me lembro de ter visto uma jovem loira traquina próxima a você ontem na biblioteca, Java.'
            mc 'Uma jovem loira traquina?'
            mc 'Sim'
            mc 'Se não me engano, ela também tinha enguias no cabelo'
            pyt 'Devemos informar ao director imediatamente, essa é uma séria infração de segurança no terreno acadêmico'
            jav 13 'Chega, vocês dois'
    jav 13 'Ainda tem alguns lugares a serem visitados para completar seu tour. Você está disponível no momento? Eu poderia terminar ele com você'
    'Você de fato está disponível, então decide seguir os dois durante o intervalo'
    # Escurece a tela por alguns segundos para dar a impressão de tempo ter passado e muda o cenário para corredor
    scene black with dissolve
    pause 1.0
    scene corredor with dissolve
    'Mesmo que vocês ainda não possam ser chamados de amigos, tanto Python quanto Java parecem estar dispostos a te receber de forma calorosa' 
    'Talvez isso seja só pra passar uma boa impressão para o cara novo, mas é melhor não tirar conclusões assim tão cedo'
    'De qualquer forma, você mantem um pequeno sorriso enquanto os dois mostram as salas de aula, a lanchonete, te resumem os professores e finalmente...'
    show java 16 at left with moveinleft
    show pyth at right with moveinright
    jav 13 'Ainda temos tempo para ir à loja da Academia. Nós temos acesso a diversos produtos com desconto, além disso...'
    show java 16
    pyt 13 'Não, não. A gente precisa mostrar pra ele a sala de recreação. A gente tem mesas de ping-pong, jogos de tabuleiro, a fonte dos desejos...'
    mc 'Ué, a sala de recreação fica ao ar livre?'
    pyt 'Claro que não, porque você achou isso?'
    mc 'Tem uma fonte dos desejos numa sala fechada?'
    pyt 'Claro que tem uma fonte dos desejos numa sala fechada'
    mc 'E como a água não acaba fazendo uma bagunça lá?'
    pyt 'Essa é a magia dos números pseudo-aleatórios'
    mc '...'
    jav 13 'De qualquer forma, só deve dar tempo de ver um dos locais antes das aulas iniciarem novamente.'
    jav 'E então, o que vai ser: eficiência e comodidades...'
    show java 16
    pyt 'Ou diversões e maravilhas?'
    menu:
        pyt 'Ou diversões e maravilhas?'
        "Ir para a sala de recreação":
            $ sala_recreacao_dia_2 = True
            call .sala_de_recreacao from _call_semana1_dia2_sala_de_recreacao
        "Ir para o mercado":
            $ sala_recreacao_dia_2 = False
            call .mercado from _call_semana1_dia2_mercado
    # Escurece a tela
    scene black with dissolve
    'Você volta para a classe e vê o resto das excêntricas aulas da senhorita Lovelace'
    'Enfim o dia acaba e você vai para casa'
    return
label .sala_de_recreacao:
    pyt 'Yes! Garanto que não vai se arrepender'
    jav 13 'Parece que foi derrotado nos votos. Vão vocês dois, eu tenho que passar na loja pra comprar mais pó de café'
    jav 'Vejo vocês na classe.'
    show java 16
    pyt 'Até!'
    hide java
    show pyth 13 at center with move
    pyt 'Então, acho que somos só nós 2 de novo, né?'
    mc 'Java é sempre assim?'
    pyt 'Assim como?'
    menu:
        pyt 'Assim como?'
        'Tão formal':
            pass
        'Tão cansado':
            pass
    pyt 12 'Sim, um pouco.'
    pyt 13 'Ele tem as melhores notas da turma em todos os assuntos, faz diversas atividades extracurriculares'
    pyt 'E apenas agora largou a presidência. Você não tava aqui para ver o incidente de debandada de ouriços.'
    pyt 'Meu amigo, aquilo foi uma bagunça!'
    mc 'De novo: a o quê?'
    pyt 'Ele sempre tá se cobrando demais. Estudando, planejando, e, além disso...'
    pyt 12 'Toma. Tanto. Café.'
    pyt 13 'Duvido que tenha mais de 5 horas de sono durante a noite.'
    pyt 'Mas não deixe aquela cara séria te enganar: ele tem um senso de humor bizarro!'
    mc 'O que você quer dizer?'
    pyt 'Eventualmente você vai perceber '
    pyt 15 'Apenas seja grato por não estar aqui durante sua era de Imperador do Pinguim Imperador'
    pyt 13 'Chegamos!'

    scene sala_recreacao with dissolve
    show pyth 13 at center
    play music "audio/music (2).mp3"
    pyt 'Essa é a sala de recreação, e essa é a fonte mágica. Toma, faz um pedido'
    'VOCÊ RECEBEU 1 TOKEN!'
    hide pyth
    'Você se aproxima o bastante para jogar o TOKEN na fonte'
    'Ela jorra majestosamente, o ar se torna uma brisa de verão e uma rápida esfera d’agua acerta seu rosto, te deixando ensopado'
    'Algo cai em suas mãos'
    'VOCÊ RECEBEU 1 ITEM GENÉRICO DEMASIADAMENTE BRILHANTE!!!!!!!!!!!!!!!!!'
    show pyth 13 at center with moveinright
    pyt 'Hey, esse é um item bem raro! A sorte tá do seu lado, hein?'
    mc 'Eh, acho que sim'
    'Pra ser sincero, você não acha que vai usar essa coisa de novo. O prêmio não vale a chance de gripar no dia seguinte'
    pyt 15 'E é isso, com exceção da loja acadêmica, você visitou todos os lugares.'
    pyt 13 'Foi legal te mostrar as coisas, mas agora você tá por conta própria. Se abaixa aqui por favor, eu quero te dar algo'
    show pyth
    'Você se agacha, ficando olho-à-olho com Python, a qual te encara com um sorriso'
    'A temperatura do seu rosto aumenta, e você reza que não o bastante pra te fazer corar a medida que Python se aproxima cada vez mais...'
    show pyth ii 53 at truecenter:
        zoom 3.0
    'Para que as duas cobras dela te beijem nas bochechas'
    show pyth 13:
        zoom 1.0
    pyt 'Te vejo depois'
    hide pyth
    'Ela vai embora com um sorriso bobo no rosto'
    'E você é deixado lá plantado, meio envergonhado, meio feliz, demasiadamente estupefato para mover-se.'
    'E é nesse estado que você começa a ouvir um estranho barulho vindo da janela. '
    'Um tintilar metálico, seguido por um vupt-vupt-vupt e então...'
    mc 'Aquilo é um grappling hook?'
    'Você escuta uma respiração ofegante à medida que um garoto ruivo se esgueira através da janela e cai no carpete.'
    'Enquanto você, de forma sensata e razoável, se esconde atrás do sofá'
    show ruby 4
    rub 'Ótimo, não tem ninguém aqui'
    'Ah se ele soubesse'
    'Ele tira do bolso uma moeda de prata – não, um TOKEN – e joga na fonte'
    'Ela jorra majestosamente, o ar se torna uma brisa de verão e uma rápida esfera d’agua acerta o rosto do garoto'
    'Você dá um suspiro de alívio ao perceber que não há perigo ali, apena um garoto pateta e seu vício em gacha'
    'Ele se mantem de pé lá, soltando um suspiro como o seu, mas de decepção enquanto segura um sorvete de pistache...'
    'Antes de tirar mais 100 TOKENS e jogá-los na fonte'
    'Dela sai uma mensagem'
    'VOCÊ RECEBEU 99 ITENS COMUNS E UM ITEM SUPER RARO...'
    'O corpo dele estremece de ânimo, você consegue sentir a esperança emanando nele'
    rub 9 'REPETIDO!'
    'Ele joga o item para longe e cai de joelhos ao chão, socando o mesmo'
    'E claro, o item jogado acaba voando pela sala'
    'Acertando sua cabeça atrás do sofá' with vpunch
    mc 'Ouch!'
    rub 6 'Quem está aí!?'
    show ruby 7
    'É, agora que você foi descoberto seria melhor se apresentar ao rapaz logo'
    mc 'Olá'
    rub 6 'Ahhh!'
    rub 'Você… você não viu nada, viu…?'
    show ruby 7
    mc '…'
    rub 8 '…'
    rub 13 'Minha vida está arruinada'
    mc 'Por causa do gacha?'
    rub 9 'Meu segredo foi descoberto e pelo quê? Um SSR repetido vindo no hard pity'
    rub 'Talvez se eu trocar alguns dólares ou reais por TOKENS num banco, eu tenha mais sorte da próxima. '
    rub 'Afinal, TOKENS são a 3° moeda do país, então eu só estaria mudando a forma que guardo dinheiro'
    rub 10 'Não, não. Controle-se, Ruby, você precisa resistir à tentação de pôr dinheiro no gacha'
    mc 'Você pode se acalmar e explicar as coisas direito?'
    show ruby
    rub '...'
    rub 2 'Desculpa, perdi a compostura por um momento.'
    show ruby
    'Você acha que o rapaz se acalmou um pouco, mas então ele vê o item que você ganhou da fonte e entra em estado de choque'
    rub 26 'I-isso é um JPEG Super Raro SSS+ edição limitada de banner?'
    mc 'Isso? Eu não sei, como disse, simplesmente consegui na fonte'
    rub 31 'Você simplesmente conseguiu?!'
    show ruby 28
    mc 'Yeah. Python tava me ensinando a usar a fonte. Na minha opinião, a bola d’agua acertar sua cara é bastante desnecessá-'
    rub 31 'VOCÊ CONSEGUIU NA PRIMEIRA TENTATIVA?!'
    rub 36 'Eu tava tentando a pelo menos 3 meses...'
    mc 'Oh... Você pode ficar com ele se quiser'
    show ruby 37
    'Ele olha pra você com olhos de cachorrinho, brilhando com lágrimas de emoção'
    rub 'Você faria isso?'
    mc 'Claro que sim. Parece ser bem importante para você, e eu nem mesmo sei o que fazer com isso pra ser sincero'
    show ruby 36
    'E agora ele está à beira de desabar em lágrimas'
    'Um sentimento parental de proteger essa criança te enche por dentro'
    mc 'Tá tudo bem. Agora, porque você entrou pela janela?'
    rub 24 'Oh. Yeah. Isso. '
    rub 2 'Acho que deve ter parecido bem estranho para você, não é?'
    mc 'É, um pouco'
    rub 3 'A verdade é que eu meio que faço meus desejos para a fonte em segredo. Ninguém sabe sobre.'
    rub 'Eu normalmente checo o ponto de bater cartões pra saber se ainda tem alguém na sala antes de entrar, e Python já tinha saído'
    rub 'Como é que você entrou aqui sem deixar um registro? Você também veio pela janela?'
    rub 'Porque se for esse o caso, eu gostaria de alguns conselhos. Eu toda vez machuco meus pulsos na subida e...'
    show ruby
    mc 'Ah, não. Eu sou novo aqui, então nem sequer tenho um cartão ainda. Entrei com Python, mas ela teve que ir embora'
    rub 3 'Oh, você é o cara novo!'
    rub 'Eu ouvi que você saiu atropelando todo o processo seletivo'
    mc 'Eu acho que é uma forma de se ver'
    rub 4 'Meu nome é Ruby, entrei aqui ano passado'
    rub 3 'Eu ainda sou meio que novo aqui, então eu tento esconder meu hobby em gachas.'
    rub 'Não quero algumas pessoas fazendo ainda mais piadas sobre mim, então eu apreciaria se você mantivesse isso só entre nós '
    rub 'Aqui! Vou até te dar um sorvete de pistache'
    mc "..."
    mc 'Obrigado'
    rub 'Eu que lhe agradeço'
    rub 'Agora, se me der licença'
    'Ruby amarra todos os itens num saco de pano e põe sobre o ombro como um cowboy que acaba de roubar um trem'
    hide ruby
    'Enquanto ele desce pelo seu grappling hook, você reza pra que ele não seja confundido com um assaltante e levado sob custódia pela polícia.'
    mc 'Oh, droga! Vou me atrasar para a aula!'
    return
label .mercado:
    jav 13 'Ótimo. Eu preciso ir lá comprar algumas coisas, então posso te acompanhar.'
    show java 16
    pyt 'Bem, se divirtam com isso. Eu preciso ir pra sala de recreação pra jogar ping-pong com Phy e Thon'
    scene black with dissolve
    'Python vai embora e você começa à andar com Java até pararem na frente de uma porta automática de vidro'
    jav 'Chegamos'
    scene mercado with dissolve
    'Um super mercado. Claro que seria um supermercado'
    show java
    jav 'Vim comprar um novo carregador pra JVM. Você pode dar uma olhada por aqui, só cuidado pra não se perder'
    hide java with moveoutright
    'Você e Java partem caminhos. A quantidade de coisas à venda pelos corredores é impressionante'
    'Comida de cachorro, pneus de carro e moto, varas de pesca, churrasqueira elétrica e por aí vai'
    'Enquanto você perambulava por ali, acabou chegando numa seção isolada com móveis à disposição.'
    'Em um dos sofás estava deitada uma garota segurando algo que parecia ser um videogame portátil. Ela falava em voz em voz alta o que estava digitando no console'
    show lua 19
    lua 'If you keep *** on your **** lane while those ********** keep farming my **********************lane, I’m gonna burn your house to the ground you little piece of *********'
    lua 13 'Oh, olá'
    'Ela te cumprimenta ao notar sua presença'
    show lua 2
    mc 'Olá, meu nome é...'
    lua 3 '[player_name]. Eu lembro de você da chamada'
    mc 'Ah, é verdade, você está na minha classe. Lua, não é?'
    lua 7 'Bingo'
    show lua 2
    'Lua levanta para sentar-se no sofá'
    mc 'Desculpa te atrapalhar'
    lua 3 'Nah, sem problemas. Se eu continuasse jogando Terracraf naquele servidor eu provavelmente esganaria alguém.'
    lua 5 'Sério, esse tipo de gente faz eu quase me arrepender de ter dado um calote no banco pra comprar essa nova versão do DXphere'
    show lua 2
    mc 'Você o que?'
    lua 3 'Mais importante, o que você veio fazer aqui?'
    show lua 2
    'Com a impressão de que a garota está desviando de um assunto importante, você decide seguir o fluxo'
    mc 'Só dando uma olhada'
    lua 3'Sem um guia?'
    show lua 2
    mc 'Porque eu precisaria de um no mercado?'
    lua 3 'Você realmente não sabe do que tá falando, né?'
    lua 'Como chegou até essa seção da loja?'
    show lua 2
    mc'Passei pela seção de animais, automobilística, itens de pesca e por último a de itens para churrasco'
    lua 3 'Cadê a seção de churrasco?'
    show lua 2
    mc 'Tá ali...'
    mc '... '
    mc 'Cadê a seção de churrasco?'
    lua 3 'Tá à 3 seções de distancia daqui'
    show lua 2
    mc 'Mas eu cheguei aqui depois de passar por ela!'
    lua 3 'Geração procedural'
    show lua 2
    mc 'Geração procedural?'
    lua 3 'Tipo roguelike'
    show lua 2
    mc 'Isso não faz o menor sentido'
    lua 15 'Não reclame comigo. É a magia dos números pseudo aleatórios'
    show lua 14
    'Você começa a perceber que as coisas aqui no terreno da academia não obedecem ao senso comum}'
    'Então é melhor deixa de lado o “como é possível” e começar a perguntar “como resolver o problema”'
    mc 'Certo, como é que eu saio daqui?'
    lua 13 'Mesmo o layout sendo randômico, algumas regras são sempre fixas'
    lua 'A mais simples é em relação à loja de Haskell que tem aqui dentro'
    show lua 2
    mc 'Tem uma loja dentro da loja?'
    lua 3 'É claro que tem uma loja dentro da loja'
    show lua 2
    mc '...'
    mc 'Ok, e qual é a regra?'
    lua 3 'A loja dele sempre tá à 2 seções da saída, por isso ele sempre sabe como ir embora da loja da escola '
    lua 'Se quiser eu posso te levar até ela'
    show lua 2
    mc 'Adoraria'
    lua 7 'Beleza, vem comigo'
    show black with dissolve
    'após algo em torno de 15 minutos andando, três baús e um miniboss, vocês chegam à dita loja que mais parecia uma pequena banca de jornais'
    hide black with dissolve
    show lua 3
    lua 'Ok, daqui você se vira. Vou voltar pro meu sofá'
    'Obrigado pela ajuda'
    lua 7 'Não tem de quê'
    hide lua with moveoutleft
    'Lua vai embora e você é deixado lá em frente à loja de Haskell'
    scene haskellShop with dissolve
    mc 'Olá? Tem alguém aí?'
    'Nada...'
    'Você começa a se perguntar se você foi largado ali sem ninguém pra ajudar'
    'Na pior das hipóteses você vai se perder de novo e não vai encontrar ninguém no caminho'
    has 'Ei...'
    mc 'Se eu desaparecer por muito tempo, provavelmente vão enviar uma equipe de busca, então tá tudo bem.'
    has 'Eeeeeeeeei...'
    mc 'Mesmo que eles demorem pra me encontrar, eu posso me manter de forma confortável aqui no mercado'
    mc 'Olha só, tem até uma feijoada aqui se eu ficar com fome'
    has 'Se afasta da feijoada!' with vpunch
    mc 'AHHHHH!'
    show haskell with zoomin
    'Um rapaz aparece de repente muito próximo ao seu rosto'
    'Na verdade, aquilo é uma pessoa? Ele parece mais uma estátua'
    has neutral 2 'Oh, você tá na minha turma.'
    has 'Não ache que eu vou deixar você pegar as coisas da loja de graça'
    'O rapaz vira de costas para arrumar as coisas na loja'
    mc 'Ei, como é que eu sai-'
    hide haskell with dissolve
    'E de repente, o rapaz some novamente'
    mc 'Eeeeei, pra onde você foi?'
    mc 'Aparece'
    show haskell neutral 2
    has 'Para de gritar, eu nem saí daqui'
    mc 'E como você fica sumindo assim?'
    has neutral 'Não por vontade própria. Tratamento de impureza em interações IO é difícil de fazer'
    mc 'O que diabos é isso?'
    has neutral 2 'Vai querer comprar algo ou não? Mercadoria exclusiva aqui na minha loja e aceitamos TOKENS'
    mc 'Que tipo de TOKENS?'
    has 'TOKEN, a 3° moeda oficial do país'
    has 'Você pode comprar itens na minha loja para dar à outras pessoas ou usar em provas, '
    has neutral 'E se você tiver um bom desempenho acadêmico, sou legalmente permitido a lhe vender item especial.'
    mc 'Certo, isso é legal, mas por favor me ajuda a sair daqui'
    has neutral 2 'Vire para esquerda e comece a andar de costas durante a próxima seção inteira. Pule e gire 180 graus e você verá a saída'
    mc 'Obrigado amigo, você é um amigo'
    has 'Adeus'
    hide haskell with dissolve
    show black with dissolve
    'Seguindo as instruções do rapaz, você consegue sair da loja e se encontra com Java na frente dela'
    scene corredor with dissolve
    show java
    jav 'Como foi sua primeira experiência com a loja da academia?'
    show java 2
    mc 'Não quero falar sobre isso'
    jav -2 'Deixando isso de lado, temos que nos apressar para chegar à tempo para as aulas restantes'
    mc 'Ah, é verdade! Esqueci completamente disso'
    return