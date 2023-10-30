# JAVA INTERAÇÃO 1
label javaEvent0:
    scene escola with dissolve
    show java with moveinright
    jav 'Oh, olá, [player_name]. Você está gostando daqui?'
    show java 2
    menu:
        "O que dizer..."
        "Eu estou gostando bastante!":
            jav -2 'Fico feliz de ouvir isso. Eu não sou mais o presidente de classe, mas não
hesite em me procurar caso você precise de alguma coisa.'
        "Ah, tem seus altos e baixos.":
            jav -2 'Fico feliz de ouvir isso. Eu não sou mais o presidente de classe, mas não
hesite em me procurar caso você precise de alguma coisa.'
        "Eu não sei se “gostando” é a palavra certa…":
            jav -2 'Eu imagino que deve ser bem intimidador nas primeiras semanas, mas prometo que você irá se acostumar.'
    show java 2
    mc 'Foi assim para você? Quero dizer, quando você começou.'
    jav -2 'Para mim? Não, na verdade, não. Mas eu vim para cá há bastante tempo. Eu
estudei aqui praticamente a vida inteira.'
    show java 2
    "Seus olhos vagaram preguiçosamente, meio por causa da nostalgia, e meio por causa da
severa privação de sono."
    jav 7 'O segredo é dar um passo de cada vez.'
    show java 2
    mc 'Um passo?'
    jav -2 'Você começa se acostumando com as pequenas coisas, e então pega o fluxo
das maiores. Primeiro, pense em um objeto.'
    show java 12
    mc 'Um objeto?'
    jav -2 'Qualquer objeto com o qual você não seja familiar, de um jeito abstrato.' 
    jav 'Pode ser um professor que você acha peculiar, um lugar que você acha estranho.' 
    jav 'O que importa é que você pense em um único objeto, e que se oriente a partir dele.'
    show java 2
    mc 'E quando eu me familiarizar com este objeto, eu escolho outros objetos.'
    jav 8 'Exato! Eu chamo isso de ser orientado a objetos. Você separa seus dias em
pequenos fragmentos, pequenos objetos, e passa por eles de um em um.'
    jav 7 'Eu, por exemplo, sempre começo o dia com uma boa xícara de café.'
    jav -7 'Então, tomo meu café da manhã, escovo meus dentes, checo meus e-mails e, de objeto em
objeto, minha rotina matinal se completa.'
    show java 2
    mc 'Entendi! Neste caso, acho que eu já tenho um pequeno ponto de partida.'
    jav -2 'O que você quer dizer?'
    show java 2
    mc 'Bem, acho que você é o “objeto” com o qual eu estou me familiarizando.'
    show java 10
    'Um pequeno sorriso surge no canto dos lábios dele.'
    jav 8 'Pois bem, acho que você está certo.'
    'Você sente que compreende Java um pouco mais.' 
    'Seu laço com ele aumenta.'
    $ javaEventsCounter = 1
    return

# Java 2º Interação:
label javaEvent1:
    scene escola with fade
    show java i with moveinright
    jav 19 'Oh, [player_name], que bom ver você. Você está fazendo alguma coisa agora?'
    show java i
    mc 'Para falar a verdade, não. Por quê?'
    jav 19 'Eu estava planejando me inscrever em algumas atividades de clube.' 
    jav 'Nunca tive muito tempo para elas quando era presidente de classe.'
    jav 'Agora que estou livre, talvez você possa me ajudar a escolher uma ou duas para completar meu horário.'
    show java i
    mc 'Eu não sabia que tínhamos atividades de clube. Quais são as opções?'
    jav 19 'São várias. Não quero me gabar, mas melhorar as atividades de clube foi uma
das minhas prioridades no meu tempo como presidente.' 
    jav 20 'Desde que assumi, nós tivemos
mais do que o dobro de opções para os estudantes. Aqui, veja a lista.'
    show java i
    mcN 'Realmente há bastante coisa. Xadrez, Teatro, Matemática
Competitiva, Ginástica, Esgrima, Skateboarding, Apreciação de Música, Supernatural
(Oculto), Supernatural (Série de TV),' 
    mcN 'Equitação, Banda, Cozinha, Caça ao Yeti,
Desenvolvimento de Jogos, Como Defender um Assassino (Série de TV), Como
Defender um Assassino (não a série de TV) ... não acaba nunca.' 
    jav 19 'Então? Tem algo que você acha que combine comigo?'
    show java i
    menu:
        jav 'Então? Tem algo que você acha que combine comigo?'
        "Xadrez": # Escolha
            jav 19 'O Clube de Xadrez? De fato, eu sou conhecido por brincar um pouco no jogo,
mas não acho que os membros ficariam felizes de me receber.'
            show java i
            mc 'Por quê? Eles não gostam de você?'
            jav 19 'Você pode dizer que sim. Mais ou menos dois verões atrás, o clube de xadrez
organizou uma partida de apresentação bem realista.'
            show java i
            mc 'Oh, com um tabuleiro gigante e as pessoas jogando como se fossem as peças?'
            jav 19 'Sim, algo assim. Naquele dia, eu tive que encerrar todo o evento quando eles
esqueceram de alimentar os cavalos.'
            show java i
            mc 'Oh, enten- pera aí, cavalos de verdade?'
            jav 19 'Eles sentiram o cheiro da barraca das maçãs-do-amor e enlouqueceram. E
depois de todo o trabalho que eles tiveram para ser ordenados bispos pela igreja...'
        'Matemática Competitiva': # Escolha
            jav 20 'Seria uma boa aplicação dos meus talentos…'
            show java i
            mc 'Você parece alguém que gostaria das competições.'
            jav 19 'Oh, eu gosto, na verdade. Eu participei todos os anos, até mesmo quando era
presidente, apenas não tinha tempo para entrar no clube.'
            jav 'Eles até tinham um apelido
para mim.'
            jav 20 'O Ninja Matemático.'
            show java i
            mc 'Isso é porque você termina as provas muito rápido?'
            mc 'Ou talvez porque você
sempre compete, mas não participa das atividades do clube?'
            jav 19 'Oh, sim, isso faria sentido. Mas, não. É por causa das tentativas de
assassinato.'
            show java i
            mc 'Das o quê?'
            jav 19 'Todo ano, para me impedir de competir, a Academia Rival envia alguns dos
seus capangas para tentar me parar.' 
            jav 20 'Ano passado eles foram longe demais. Eu quase
perdi as botas.'
            show java i
            mc 'O que eles fizeram?'
            jav 19 'Me sequestraram e me mandaram em um avião para o Uruguai.' 
            jav 20 'Eu quase não
cheguei a tempo de derrotá-los.'
        "Esgrima": # Escolha
            jav 19 'Oh, esgrima! Essa é uma ótima ideia.'
            show java i
            mc 'Sério? Eu não esperava que você gostasse tanto.'
            jav 19 'Pelo contrário. Embora você só esteja sabendo agora, eu sou bastante ágil com
uma espada.' 
            jav 'Durante a Primeira Revolução dos Bugs, eu e Python seguramos as forças
inimigas com apenas uma espada, um canhão de água e uma moldura de porta bem
colocada.'
            show java i
            mc 'A Primeira Revolução dos Bugs?'
            jav 19 'É, houve três delas. Mas a primeira foi a mais feroz, na minha opinião.'
    show java i 22 
    mc 'Você parece ter vivido muitas histórias interessantes no seu tempo como
presidente.'
    jav 19 'É mesmo? Eu nunca pensei muito sobre isso, agora que você mencionou.'
    jav 'Naquela época, tudo parecia bastante cotidiano. Mas eu suponho que há alguns contos
curiosos de tempos em tempos.'
    jav 'Quando nos encontrarmos novamente, eu tentarei trazer
alguns para você.'
    $ javaEventsCounter = 2
    return

# Java 3º Interação
label javaEvent2:
    scene escola with fade
    jav "Estou precisando de uma garrafa térmica..."
    "Oh, [player_name]!"
    show java 10 with moveinleft
    jav 8 'Ótimo momento. Eu estava pensando sobre o que você falou na nossa
última conversa...' 
    jav 'E acabei lembrando de algumas histórias interessantes de quando eu
era presidente.'
    show java 10
    mc 'Oh, é mesmo?'
    jav 8 'Sim! Mas prepare-se, eu não sou de me gabar, mas acho que escolhi alguns contos bem
picantes.'
    show java 10
    "Picantes? Você não esperava isso de Java. Talvez ele seja um pouco mais como os
outros adolescentes do que você imaginava."
    jav 8 'Por exemplo, eu cheguei a mencionar da trapaça escandalosa que tivemos em
Abril do ano passado?'
    show java 10
    mc 'Vocês tiveram esse tipo de escândalo?!'
    'Talvez seja por isso que há tanta hostilidade entre javy e Swift! Eles tinham um
romance malicioso no passado!'
    'Ou será que foi um romance ardente entre Alan Turing
e Arnold Murray?'
    jav 8 'Exato! Foi durante a prova final da Srta. Lovelace.' 
    jav -8 'Tivemos um semestre particularmente difícil, então muitas pessoas precisavam de boas notas para passar.'
    show java 10
    'Oh, então é uma trapaça acadêmica.' 
    jav 8 'Ainda assim, é um escândalo considerável, trapacear em uma instituição tão prestigiosa.'
    jav -8 'Talvez eles tenham usado um mecanismo secreto para esconder as respostas, ou inventaram um código à base de luz para brilhar
regularmente pela janela...'
    jav 8 'Então, no meio da prova, um celular tocou! Qualquer um podia ouvir!' 
    jav 'Você
tem que desligar seus eletrônicos durante a aplicação, todo mundo sabe disso, então
imagine a surpresa!' 
    jav 'Tivemos que interromper tudo, e eu, sendo o presidente de classe,
estava encarregado de apreender o celular em questão.'
    show java 10
    'Isso é… significantemente mais entediante do que eu esperava.'
    jav 8 'No fim, era o celular da própria Srta. Lovelace! Rá! Aposto que você não
antecipou esta revelação.'
    jav 'Mas é verdade! Oh, aqueles selvagens dias de juventude... Eu
nunca vou esquecer.'
    show java 10
    mc 'Essa certamente é… uma história interessante.'
    jav 8 'Sim, tem toda razão. E pensar que, se o FBI não estivesse investigando o
colégio naquela semana, o telefone dela ainda estaria no silencioso.'
    show java 10
    mc 'O-o FBI?'
    jav 8 'Oh, sim, você não ouviu falar sobre a investigação do FBI ainda. Contudo, já
tivemos muita emoção para um dia. Vou contar sobre isso em outra ocasião.'
    $ javaEventsCounter = 3
    return

#Java 4º Interação:
label javaEvent3:
    scene escola with fade
    show java i with moveinleft
    jav 19 'Olá, [player_name]. Você gostaria de almoçar comigo?'
    show java i
    mc 'Claro, vamos lá.'
    scene black with fade
    'Vocês dois seguem para a cafeteria, jogando conversa fora pelo caminho'
    scene cafeteria with dissolve
    show java i with fade
    jav 19 'Sabe, eu falei bastante sobre mim mesmo nos últimos tempos, mas ainda sei
muito pouco sobre você.'
    show java i
    mc 'Acho que eu apenas não tenho muitas histórias interessantes para contar.'
    jav 19 'Bem, antes de conhecer você, eu pensava assim sobre mim mesmo. Mas você
pareceu gostar das minhas histórias.'
    show java i
    mc 'Tem razão. Deixe-me ver…'
    menu:
        mc "Oh, já sei..."
        'Eu trabalhei brevemente como advogado de defesa, uma vez': # Escolha
            jav 19 'Sério? Como isso aconteceu?'
            show java i
            mc 'Foi no ano passado, na verdade. Eu estava ajudando minha vizinha, Inca.' 
            mc 'A irmã dela era uma grande advogada, então um cara de uma corporação malvada sequestrou e
incriminou a Inca.'
            jav 19 'Fascinante. Acho que eu li algo sobre isso nos jornais. Por acaso era o Sr.
Violet, o sequestrador, da Purplecorp?'
            show java i
            mc 'Sim, exatamente. Ele era tão influente naquela época que nenhum advogado
queria contrariá-lo.' 
            mc 'Para a sorte de Inca, eu havia encontrado um distintivo de advogado
numa casa de poker aleatória na semana anterior, então eu resolvi ajudar.'
            mc 'Mas minha mente estava tão perdida ali... Se Inca não tivesse sido capaz de
telepaticamente contatar sua irmã, acho que eu não teria conseguido.' 
            mc 'O fato do Sr.Violeta ser maluco também ajudou.'
        "Eu conheci um panda robô maligno, uma vez.": # Escolha
            jav 19 'Sério? Como isso aconteceu?'
            show java i
            mc 'Foi quando eu ainda estava no Ensino Médio. Havia essas duas gêmeas estranhas
que estudavam comigo.' 
            mc 'Uma era uma fashionista famosa, top-model de verdade e essas
coisas, e a outra era super atlética, quase como um soldado.' 
            mc 'A feshionista era bem popular, mas ela vivia falando sobre desespero e esperança, e sendo esquisita desse
jeito, enquanto a irmã dela tinha esse crush massivo em um garoto.'
            mc 'Então, um dia, elas criaram esse panda robô para testar a esperança e o desespero
da nossa turma.'
            mc 'Elas trancaram 16 estudantes no campus até que nós vencêssemos seu
desafio ou algo assim, usando a irmã soldado para nos impedir de escapar.' 
            mc 'Mas então o
crush dela perguntou se ela pararia com tudo aquilo caso ele a chamasse para sair.'
            mc 'A soldado então chutou a bunda da irmã e tirou todo mundo de lá, mas elas ainda
usam o robô para festas e essas coisas.'
            jav '…'
            jav 19 'Isso não era o que eu estava esperando.'
            show java i
        "Eu fiz parte de um Clube de Literatura assombrado, uma vez": # ESCOLHA
            jav 19 'Sério? Como isso aconteceu?'
            show java i
            mc 'Eu tinha essa amiga que precisava de um membro para o clube dela, para que a
escola não o fechasse.'
            mc 'Então eu entrei. Havia uma garota tímida, uma que gostava de
mangá, a presidente do clube, minha amiga e eu.'
            mc 'Nós nos encontrávamos a cada dois
dias para escrever poemas e discutir livros.'
            jav 19 'E como era assombrado?'
            show java i
            mc 'Depois de algumas semanas, os membros começaram a desaparecer!'
            mc 'Primeiro a
minha amiga, depois a garota tímida, a que gostava de mangá e, finalmente, havia
apenas eu e a presidente restando.' 
            mc 'Era super bizarro, mas ela parecia estar de boa com
tudo que estava acontecendo.'
            jav 19 'Elas desapareceram? Como?'
            show java i
            mc 'Eu não sei! Eu fui visitor minha amiga um dia, e... quando eu lentamente abri a
porta, tudo que eu vi foi uma corda.'
            jav 19 'Uma corda?'
            show java i
            mc 'Sim! Ela estava pulando corda. Ela pulava tão rápido que, quando eu piscava
meus olhos, ela desaparecia.'
            jav 19 'De fato, parece estranho. Era um fantasma?'
            show java i
            mc 'Não. No fim das contas, nós percebemos o que estava acontecendo. A presidente
estava acidentalmente as enviando para uma dimensão de bolso.'
            jav 19 'Oh, é claro! Isso faz todo o sentido!'
    jav 19 'E você disse que não tinha histórias interessantes. Eu sinto que conheço você
um pouco melhor agora, [player_name].' 
    jav 'Desculpa se isso parecer muito repentino, mas você
aceitaria ser meu guarda-costas na Olimpíada de Matemática Competitiva?'
    show java i
    mc 'Guarda-costas? Por quê?'
    jav 19 'Você sabe, em caso de tentativa de assassinato. Eu sei que a escola rival está
planejando algo grande este ano. Eles sempre estão.'
    show java i
    mc 'Eu não sei, não tenho certeza se estou à altura do desafio.'
    mc 'Mas por que eu? Eu não sou exatamente o tipo “guarda-costas”.'
    mc 'Claro, eu estarei lá para o que você precisar.'
    jav 19 'Muito obrigado. Eu prometo que não vai ser nada perigoso.' 
    jav 'Eu tenho bastante
experiência em lidar com as tolices deles agora, então tudo o que eu preciso é de outro
par de olhos para me manter atualizado.'
    if itens_estado[8] == True:
        mc "Java..." 
        show java i
        jav "?"
        mc "eu tenho um presente para você."
        jav 19 "Isso é..."
        jav "Uma garrafa térmica?"
        jav 20 "Estava precisando de uma. Obrigado."
        show java i 23
        "A felicidade está no ar... Em cada sorriso. Em cada olhar!"
        $ itens_estado[8] = False
        $ javaLoveCounter += 3
    $ javaLoveCounter += 3
    $ javaEventsCounter = 4
    return