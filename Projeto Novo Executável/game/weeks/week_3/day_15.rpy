label semana3_dia15:
    scene black with dissolve
    "Deitado na cama, você acorda de madrugada ouvindo os sons da cidade pela janela. Sua mente é inundada com pensamentos do que está por vir."
    mc 'Vai ter mais uma prova no final dessa semana....'
    mc 'Oh, e eu também preciso começar a estudar os assuntos do capítulo 3 de Ada, porque deus sabe que eu não vou entender o assunto durante a aula, e...'
    mc 'Tenho que voltar para consultar o médico e conferir se o atropelamento teve sequelas, preciso ir ao lago vender mais alguns peixes, tenho que preparar o almoço para a semana...'
    mc '...'
    mc 'Por que eu estou fazendo isso?'
    'Você se levanta, andando em passos lentos até a janela mais próxima. O vento frio acerta sua cara, irritando os olhos. Sua visão se perde no céu aberto, nas estrelas distantes, e sua imaginação se perde no espaço infinito.'
    mc 'Eu entrei na Academia porque pensei que iria facilitar minha vida. Porque iria me dar um senso de... um senso de destino. De finalidade.' 
    mc 'Mas até agora, não sinto que nada mudou. Todas as preocupações que eu tinha antes permanecem as mesma, só que agora eu tenho ainda mais. Eu não sei nem se eu gosto de estudar essa área.'
    mc 'Ainda é cedo.'
    mc 'Eu ainda posso mudar.'
    mc 'Mas será que eu vou? E se for só isso? E se eu terminar toda essa história no mesmo lugar que eu comecei?'
    mc '...'
    mc 'Tá cedo demais.'
    mc 'Eu deveria voltar a dormir.'
    'Você volta para a cama e fecha os olhos, mas sua mente permanece a mesma....'
    'E talvez, sempre permanecerá.'
    scene black
    pause 1
    scene escola
    play music "audio/music (2).mp3"
    'A caminho da Academia.'
    mc 'Eu dormi feito lixo....'
    mc 'Culpa minha, quem mandou ficar até tarde assistindo House M. D.?'
    mc 'Culpa de House, quem mandou ficar fazendo negligência médica parecer tão interessante?'
    mc 'Bem, não importa agora. Nova semana, novo eu. Só tenho que sobreviver a nova semana agora...'
    mc 'A eleição do novo presidente estudantil é essa semana, né? Eles devem cancelar a aula no dia de campanha, para que os candidatos possam fazer seus discursos. Isso vai ser um bom momento para parar e respirar.'
    mc 'Bem, não importa agora.'
    mc 'Você diz para si mesmo, mas sua cabeça sonha com o breve intervalo de calma e tranquilidade no turbilhão que foram suas últimas semanas.'
    
    if pythonEventsCounter == 4:
        call semana3_dia15_python from _call_semana3_dia15_python
    
    scene sala 1 with dissolve
    "A aula passa normalmente, mas suas preocupações não lhe deixam prestar atenção." 
    "Quando a noção finalmente bate na sua testa como um bumerangue metafórico, aquela aula já havia acabado."
    "Você decide sair um pouco pra tomar um ar e ver se isso melhora o estado em que se encontra"
    
    if rubyEventsCounter == 4:
        call semana3_dia15_ruby from _call_semana3_dia15_ruby

    scene corredor with dissolve
    "Agora já é o almoço e você tenta relaxar."
    mc 'Tacos!'
    mc 'Ninguém pode ficar nervoso na Segunda dos Tacos!'
    mc 'É literalmente impossível.'
    mc 'Você não tem como pensar que os tacos são uma metáfora!'
    mc 'E que eles, na verdade, representam o seu futuro!'
    mc 'Engessados em uma casca frágil, recheados com incerteza, levemente danosos para o seu fígado!'
    mc 'Fracos, incertos, perigosos, assustadores, sem seguridade, com um mercado de trabalho instável,' 
    mc 'sem seguro de saúde a partir dos 21 anos de idade, inflacionados, mercado imobiliária em ascensão, vivendo sozinho pelo resto da sua vida sem saber o que é amor verdadeiro....'
    mc '....'
    mc 'Tacos!'

    if  luaEventsCounter == 4:
        call semana3_dia15_lua from _call_semana3_dia15_lua 

    scene escola with dissolve
    'Depois disso, o dia passa como rapidamente, como um pinguim esquiando montanha abaixo.'
    'Mais um dia, mais tarefas, mais da mesma rotina que lhe enche de incertezas.'

    if javaEventsCounter == 4:
        call semana3_dia15_java from _call_semana3_dia15_java
    'Não há mais nada a se fazer na academia, então você volta para casa'
    stop music
return

label semana3_dia15_python: 
    scene corredor
    "Equanto caminha para sala, você escuta alguém lhe chamando"
    pyt 'Psiu. Psiu! [player_name]!'
    mc  'Python?'
    'Você não esperava encontrar Python se esgueirando em uma sala vazia, se escondendo com a porta entreaberta e lhe chamando com urgência.'
    pyt 'Entra aqui!'
    scene black
    'Você entra na sala deserta, com as cortinas fechadas e luz apagada. A única luz que você encontra são os raios fracos que escapam das persianas e a aura clara de Python.'
    mc 'O que você está fazendo? Por que está se escondendo aqui?'
    show pyth 7 
    pyt 'Fala baixo. Ninguém mais pode saber que estamos aqui.'
    mc 'Por quê?!'
    show pyth 6
    pyt '[player_name].... Eles estão vindo atrás de mim.'
    mc 'Q-quê?!'
    show pyth 5
    pyt 'Eles vão chegar a qualquer momento.... E eu não tenho nada para entregar para eles....'
    mc 'Quem são eles? Entregar o quê?'
    show pyth 6
    pyt 'Talvez eu possa fugir do país. Só por um tempinho, até as coisas se acalmarem. Oh! Eu poderia também entrar em um coma temporário! Assim ninguém poderia me culpar quando-'
    mc 'Fugir do país? Coma? Python, você emprestou dinheiro para algum chefe de máfia?'
    pyt 'Quem me dera! É muito pior que isso?'
    mc 'Meu deus, você se prometeu se casar com o filho do chefe de máfia, porém agora percebeu que você não o ama de verdade e precisa cancelar o casamento. Mas o filho do chefe de máfia precisa do seu casamento para consolidar o poder, então-'
    show pyth 5
    pyt 'Não! É pior que isso! É pior que qualquer coisa envolvida com a máfia.'
    pyt 'Eu...'
    pyt 'Eu....'
    show pyth 6
    pyt 'Eu esqueci de planejar a festa de acolhimento!'
    pyt '....'
    mc '....'
    pyt '....'
    mc '....'
    '....'
    mc 'Só isso?'
    show pyth 4
    pyt 'COMO ASSIM SÓ ISSO? VOCÊ PERCEBE QUE A FESTA DE ACOLHIMENTO É UMA TRADIÇÃO DA ACADEMIA DESTE O SEU NASCIMENTO E SER ESCOLHIDOCOMOORGANIZADORÉUMAGRANDEHONRAEEUNÃO-'
    mc 'Okay, okay. Calma. Eu sou um novato aqui, ainda não entendo bem as tradições.'
    show pyth 6
    pyt 'Oh. É verdade. Desculpa.'
    pyt 'Todo ano, no primeiro mês de aulas, a Academia realiza a cerimônia de acolhimento. É basicamente uma grande festa, como todos os alunos e corpo docente. E, período passado, eu fui escolhida para organizar a deste ano.'
    pyt 'Mas, com tudo que aconteceu, eu acabei esquecendo! Agora só me restam alguns dias para eu poder organizar tudo. Eu era para ter feito isso nas férias....'
    mc 'Como você esqueceu?'
    show pyth 5
    pyt 'Oh, eu fiquei assistindo House M. D..'
    mc 'Oh, eu também.'
    show pyth 28
    pyt 'Sério?'
    mc 'Sim, é muito bom. A quarta temporada é a melhor.'
    show pyth 14
    pyt 'Eu sei! Todo o elenco é tão bom, e a season-finale é simplesmente- '
    show pyth 3
    pyt 'Não, pera, foco!'
    mc 'Oh, sim. E o que você vai fazer agora?'
    show pyth 6
    pyt 'Eu não sei!'
    show pyth 2
    pyt 'Bem, seu sei um pouco.'
    pyt 'Eu já tinha feito a parte do planejamento da festa. Então eu já sei o que precisa ser feito, e como fazer.'
    show pyth 5
    pyt 'Mas eu não tenho como fazer tudo ao mesmo tempo! Por isso eu preciso de ajuda.'
    mc 'Oh. Isso não parece ser tão difícil então. Você quer minha ajuda? Eu já tinha dito que iria ajudar a organizar a sua outra ideia de festa, então talvez eu deva começar a pegar prática, né?'
    show pyth 8
    pyt 'Sim! Era justamente nisso que eu estava pensando.'
    mc 'Devemos chamar mais alguém pra ajudar? Um professor ou um veterano. Aposto que Java até deve ter um plano de contingência para isso ou-'
    show pyth 18
    pyt 'Não! Não pode ser nenhum dos professores, eles não podem saber que eu esqueci. E os alunos estavam contanto comigo! Não posso mostrar que eu os decepcionei. '
    show pyth 2
    pyt 'Além disso, eu confio em você. Não que eu não confie nos outros, eu confio em Java, Lua, Ruby, todos os meus amigos. Mas eles têm suas próprias coisas e já tem uma imagem minha formada. '
    show pyth 6
    pyt 'Então....?'
    'Ela segura sua mão, o rosto dela apenas alguns centímetros do seu nariz, os olhos delas no seu....'
    mc 'O-ok, então vai ser só nós mesmo.'
    show pyth 23
    pyt 'Muito obrigada! Eu nunca vou esquecer isso.'
    show pyth
    pyt 'Eu te mando a lista de tarefas por e-mail mais tarde. Agora deveríamos ir, as aulas já vão começar.'
    'Você nem tem tempo para processar o que você aceitou quando acontece.'
    'Mwah!'
    hide pyth
    'Um beijo. Na sua bochecha. Tão rápido que você demora um tempo para perceber e, quando percebe, Python já está correndo para a aula. '
    'Você deveria fazer o mesmo, mas algo lhe prende. Você fica parado na sala, mão no rosto, esperando seu rosto voltar ao normal. Apenas então você vai para a aula.'
return 

label semana3_dia15_ruby:
    'Contudo, antes que você possa sair, alguém surge na sua mesa.'
    show ruby 10
    rub  '[player_name]?'
    'Ruby aparece na sua frente, tremendo como uma máquina de lavar roupas cheia de Coca-Cola e Mentos.'
    mc  'Ruby, aconteceu alguma coisa?'
    show ruby 11
    rub  'É... um...tipo....'
    rub  'Você está ocupado essa semana?'
    mc  'Essa semana? Bem, eu-'
    show ruby
    rub  'Você poderia ser meu consultor?'
    mc  '....'
    mc  'Consultor?'
    show ruby 16
    rub  'Eu vou me candidatar para Presidente de Classe! Bem, eu me candidatei para Presidente, mas ainda não tenho um consultor para a campanha. '
    mc  'E você quer que eu seja o consultor?'
    show ruby 27
    rub  'Sim! Por favor, eu preciso da sua ajuda.'
    mc  'Você não acha que deveria chamar outra pessoa? Eu ainda sou um novato, não conheço muita gente aqui, e nunca fui muito bom com política.'
    show ruby 12
    rub  'Eu não vou mentir, eu pensei nisso. Python é popular, sim, mas ela não é boa confrontando pessoas. Lua é boa confrontando pessoas, mas ela não é responsável para isso. E Java... eu não posso chamar Java. '
    show ruby 16
    rub  'Sem falar que Swift é o meu maior adversário! Você é a única pessoa que confrontou Swift tão diretamente!'
    mc  'Ainda assim....'
    show ruby 29
    rub  'Por favor! Não é muito trabalho. Você só precisa me ajudar com a campanha, fazer um discurso, impedir que Swift fique roubando meu almoço e me empurrando no armário quando eu não estou prestando atenção e-'
    mc  'Isso me parece muita coisa.'
    show ruby 11
    rub  'Eu sempre quis ser Presidente de Classe. Se eu fosse, as pessoas finalmente iam me ver como alguém maduro e responsável. '
    rub 'Eu ia poder fazer uma diferença real dentro da academia, onde pessoas como Swift e COBOL não tivessem tanto espaço livre para fazerem o que quiser.' 
    show ruby 20
    rub 'Eu poderia criar um ambiente onde ninguém vai ter seu almoço roubado e ser jogado no armário quando não estão prestando atenção! Pense nisso! Um mundo onde todos podem sair do armário!'
    mc  'Bem, isso sem dúvida iria ajudar você e Swift....'
    show ruby 4
    rub  'Exato! E eu quero fazer isso se tornar a nova realidade. A Academia não aceita muitos alunos, e, dos novatos que ela aceita, muitos acabam saindo porque não conseguem lidar com a pressão.' 
    show ruby 17
    rub 'Mas eu sei que essa é uma ótima instituição! Aqueles que conseguem sair formados vão para mudar o mundo afora. Por isso eu quero fazer com que todos que entrem aqui se sintam aceitos.'
    'Ruby falava com paixão e precisão. Era como se todo o nervosismo que normalmente o acompanhava tivesse desaparecido. E o que ele falava era atrativo....'
    show ruby 11
    rub  'Agora, você é um dos novatos, e eu sei que não é fácil. Por isso eu quero que você seja meu consultor. Você vai entender os problemas melhor do que qualquer outro.'
    show ruby 30
    rub  'Por favor, [player_name]....'
    'Você o encara, meio-incrédulo. O Ruby que você conhece ainda está lá, com os olhos segurando lágrimas.' 
    'Mas você nota uma outra versão escondida nele. Um Ruby determinado, faminto pela mudança. Alguém que lutaria com garras e unhas para alcançar a mudança com que ele tanto sonhou. Alguém apaixonado pela própria visão...'
    'Alguém que você não consegue dizer não para.'
    mc  'Se for assim, Ruby, seria uma honra ser seu Consultor. '
    show ruby 37
    rub  'Você... você aceita a posição?'
    mc  'Eu aceito. E juntos, iremos mudar a Academia.'
    show ruby 27
    'Mesmo com a mesa entre vocês, ele se joga em um abraço surpresa. Os braços de macarrão dele lhe puxam para perto e o queixo dele descansa no seu ombro. Você tenta se concentrar em outros detalhes para não parecer tão surpreso quanto você realmente está.'
    show ruby 25
    rub  'Muito obrigado. Eu não vou esquecer isso. Mais tarde eu te mando os detalhes da estratégia de campanha! '
    hide ruby 25
    'E, quando ele finalmente sai, você não para de lembrar os pequenos detalhes do que acabou de acontecer, como os cabelos ruivos com cheiro de cereja, a franqueza e esperança na voz dele, ou o sorriso estampado em seu rosto....'
    'E então, momentos depois, você enfim deixa a sala'
return 

label semana3_dia15_lua:
    show lua 18
    lua "Yo! [player_name]!"
    "Lua se aproxima animadamente, segurando um prato cheio de tacos em uma mão e um engradado de Beast Energy Drink na outra."
    show lua 16
    lua "Eu estava de procurando!"
    show lua 9
    lua "Eu tenho uma oferta completamente, indiscutivelmente imperdível para você!"
    show lua 10
    lua "É melhor que a promoção de inverno da Steam, e no mínimo 3 vezes mais economicamente vantajoso do que um PS2 após a revisão de preço!"
    lua "Mas é uma oferta limitada, então você tem que aceitar!"
    lua "Tipo."
    show lua 22
    lua "Aceitar agora-agora."
    show lua 23
    "Ver Lua tão animada assim lhe alegra um pouco, de uma forma contagiante. Ela deve estar falando de algum jogo multiplayer novo, ou talvez um novo console estranho e obscuro. Você só espera que não seja um esquema de pirâmide...."
    mc "Okay, okay. Você praticamente já me convenceu. Qual é a oferta?"
    show lua 24
    lua "Você quer dormir comigo essa semana?"
    mc "Se eu quero o quê?"
    "Antes que o seu cérebro entre em curto-circuito, ela lhe entrega um panfleto escrito com canetas coloridas e glitter à gosto."
    mc "Você quer fazer uma.... testa do pigama?"
    show lua 13
    lua "Uma festa do pijama!"
    mc "Oh... OH! Então eu iria dormir na sua casa?"
    show lua 3
    lua "Dã. O que você achou que eu queria dizer com dormir comigo?"
    show lua
    lua "Fala sério, você é meio lentinho né?"
    "[player_name] pensando"  "Acho melhor não falar o que eu pensei que seria...."
    show lua 13
    lua "Enfim, eu vou fazer uma festa do pijama! Vai ter um campeonato de New Super Street Kombat Bros 2 – Ultra Instinct – Neo Challengers Anniversary Edition HD Remix 64.... & Knuckles!"
    mc "E isso é….?"
    show lua 20
    lua "Um jogo de luta, obviamente."
    show lua 14
    lua "E eu preciso de um parceiro para treinar." 
    show lua 17
    lua "Eu vou ficar em cima de você a noite toda, até você não aguentar mais!"
    "[player_name] pensando"  "Ela tem que estar falando assim de propósito, não pode ser."
    show lua 3
    lua "E então? Você aceita?"
    mc "Eu não sei. Nunca fui muito bom com jogos de luta."
    show lua 11
    lua "Não importa, aceita vai."
    mc "E treinar para um campeonato? Eu praticamente vou servir de ajuda nenhuma!"
    show lua 9 
    lua "Não importa, aceita!"
    mc "E você não conhece Python e Ruby a mais tempo? Eles não seriam-"
    show lua 19
    lua "Aceeeeeeeeeeeeeita! Aceita, aceita, aceita, aceita-"
    mc "Espera, Lua, pense bem sobre isso! Eu não quero te atrapalhar e-"
    "Lua de repente lhe agarra o rosto, colocando sua resta na dela e lhe apertando como um peixinho."
    show lua 20
    lua "Aceitaaceitaceitaceitaaceita-"
    mc "Tá bom! Tá bom, eu aceito!"
    show lua 8
    lua "Excelente!"
    show lua
    lua "Mas você está certo, eu também deveria chamar Python."
    show lua 11
    lua "Eu até chamaria Ruby, mas ele provavelmente tá ocupado com a eleição e eu odiaria atrapalhar ele."
    "Lua se vira para sair, antes mesmo de terminar os tacos, mas uma questão não consegue sair da sua mente...."
    mc "Espera!"
    show lua 3
    lua "O quê?"
    mc  "Por que você quer tanto que eu vá? Eu não vou ter como te ajudar?"
    show lua 2
    lua "?"
    show lua 13
    lua "Eu não preciso de ajuda. Eu sou ótima no jogo. Eu quero que você vá pela mesma razão pelo qual eu quero competir, ou pelo qual eu estou na Academia." 
    lua "Francamente, eu diria que eu quero que você vá pela mesma razão pelo qual eu faço qualquer coisa."
    mc  "Você ainda não falou a razão."
    show lua 16
    lua "É porque eu acho que você é legal, dã!"
    lua "Você é mesmo meio lento. Mas tudo bem, vai ser ainda mais fácil amassar a sua cara no jogo. Te mando os detalhes de noite!"
    hide lua 16
    "E ela se vira em busca de Python, sem sequer olhar para trás, lhe deixando apenas com uma cabeça confusa, um sorriso bobo involuntário no rosto e um prato cheio de tacos."
return

label semana3_dia15_java:
    'Já na porta da Academia, com a mente distante, você escuta alguém chamando seu nome.'
    show java
    jav '[player_name], ainda bem que te encontrei!'
    mc 'Oh, Java! Você estava me procurando?'
    show java 7
    jav 'Oh, sim. Queria discutir alguns assuntos com você. Teria um momento?'
    mc 'Eu acho que sim.'
    jav 'Excelente. Por favor, me siga. Tem uma pracinha não muito longe daqui.'
    'Java lhe leva até uma praça da Academia, recheada de jovens discutindo de forma descontraída, cheirando as belas flores coloridas e jogando pedrinhas no lago cristalino.' 
    'Ele encontra uma mesa limpa e vazia, onde ele prepara a cafeteira JVM e prepara duas xícaras de café. '
    show java 
    jav 'Gostaria de açúcar? Leite? Adoçante?'
    mc 'Um pouco de leite seria bom, obrigado.'
    show java 8
    jav 'Aqui, deixe-me fazer essa cortesia.'
    'Ele prepara a sua xícara e lhe serve enquanto ainda quente. O primeiro gole já lhe enche de energia. Você nunca tomou um café como esse. Depois de algum tempo, ambos apreciando a bebida e conversando levianamente, Java adota uma postura séria.'
    show java 2
    jav 'Bem, embora eu aprecie tomar esse café com você, eu vim aqui falar de negócios.'
    show java
    jav 'A competição está se aproximando e eu acho que a escola Rivel está planejando algo especial desta vez. '
    mc 'O que lhe faz pensar isso?'
    show java 16
    jav 'Eu tenho alguns informantes. Contudo, a escola Rivel está se atentando mais aos meus métodos. Eles devem ter percebido que eu tinha alguém escondido entre eles e começaram a liberar rumores falsos para me distrair.'
    jav 'Estão falando de tudo, desde trancar minha porta pelo lado de fora até soltar os animais do zoológico para me impedir de chegar no lugar.'
    show java 17
    jav 'Com tantos rumores, não tem como eu saber qual é o verdadeiro plano deles.'
    mc 'Hum.... Isso parece preocupante.'
    show java
    jav 'De fato. É por isso que eu preciso conversar com você.'
    mc 'Você está se referindo a minha função como guarda-costas?'
    show java 7
    jav 'Precisamente. Antes, quando eu poderia prever facilmente as atividades de Rivel, um guarda-costas era apenas uma camada de segurança extra. Apesar de eu ter confiança em você na função, os riscos ainda seriam mínimos...'
    show java 4
    jav 'Mas agora....'
    show java 7
    jav 'Eu não sei mais se posso garantir sua segurança. Por isso, estou pensando em te livrar das obrigações como guarda-costas.'
    mc 'Ãh? Me livrar de minhas obrigações.'
    show java 4
    jav 'Não tenho intenção alguma de lhe ofender, quero deixar bem claro. Pelo contrário. Estaria fazendo isso pelo seu bem.'
    mc 'Deixa eu ver se eu entendi direito.'
    mc 'Você constatou, com base em espiões que você aparentemente tem na escola Rivel-'
    show java 5
    jav 'Resquícios da minha época como Presidente.'
    mc '...'
    mc  'Sim, claro. A partir dos espiões que você mantem pela sua época como Presidente, você constatou que a escola Rivel está escalando seus planos e mexendo para uma estratégia mais perigosa, que você não tem como prever.'
    mc 'E o seu plano para lidar com isso é eliminar ainda mais medidas de segurança?'
    show java
    jav 'Você está me entendendo mal. Sim, seria um risco maior para mim, mas ainda um risco pequeno. Você é um aluno novato aqui, e ainda resta em minhas responsabilidades, como Ex-Presidente, garantir que nenhum mal lhe ocorra.'
    mc 'E você tem muitas responsabilidades como Ex-Presidente?'
    show java 13
    jav 'Bem, nenhuma formal, mas eu me auto encargo de algumas e-'
    mc 'E você as leva à sério? Elas ajudam na Academia?'
    show java 16
    jav 'É claro. Eu me esforço ao máximo para melhorar o nome e status da academia, assim como acomodar os alunos que temos. Eu ainda carrego, em minhas costas, o peso de ser um dos representantes da Academia. '
    jav 'Seja em competições, atividades extracurriculares, trabalhos voluntários, desempenho acadêmico, não importa. Eu devo me manter de queixo erguido e fazer meu melhor para manter o prestígio que meu nome incube.'
    mc 'Hum... entendo....'
    mc 'E por isso mesmo eu irei continuar como seu guarda-costas.'
    show java 11
    jav '?!'
    mc 'Eu não poderia deixar nada de mal acontecer com alguém com tantas conquistas e responsabilidades, não é mesmo? Se você é tão importante para a Academia, e eu estudo na Academia, então vale notar que te proteger é uma forma de me proteger também.'
    mc 'E, além disso, possivelmente mais importante, você é meu amigo, que fez um esforço especial para me acolher quando eu conhecia quase ninguém.'
    show java 14
    jav '[player_name], você tem certeza disso? Essa responsabilidade é minha você não precisa-'
    mc 'Essa responsabilidade agora é nossa. Deixe-me lhe ajudar.'
    jav '....'
    show java 2
    jav 'Está bem, e....'
    show java 10
    jav 'Obrigado. Eu não irei esquecer sua ajuda.'
    mc 'É para isso que amigos servem.'
    hide java 10
    'Java se levanta, resoluto. Você não o conhece a muito tempo, mas sente que uma conexão foi formada entre os dois. Apenar do breve tempo, você consegue perceber que ele agora se move como se parte de um peso tivesse sido tirado de seus ombros.'
    'Não tudo, mas uma parte, e você se sente feliz em saber que ajudou.'

return 