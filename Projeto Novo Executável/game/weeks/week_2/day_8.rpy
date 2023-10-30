image lua_parca = "images/Sprites Lua/lua 1.png"
image java_parca = "images/Sprites Java/java 1.png"
image python_parca = "images/Sprites Python/python 1.png"
image ruby_parca = "images/Sprites Ruby/ruby 1.png"

default falas_java = [jav, "Seria um prazer.", "Uma aspirante a detetive que resolveu inúmeros casos, contribuindo para a melhora da sociedade...", 'E então, vamos começar?', 'Seria uma boa ideia eu procurar informações do funcionamento intrínseco de tecnologias da área de computação, não apenas de computadores propriamente ditos.','Posso fazer isso com o próprio material existente aqui na biblioteca.', 'Acredito que você consegue concluir essa árdua tarefa?', ' Se você não sabia sobre, é melhor correr pra recuperar o tempo perdido. Posso ajudar se quiser.', 'Me dê 2 dias e garanto que tudo estará completo.', 'Aproveitando a deixa, vou pra biblioteca começar minha parte no trabalho. Até amanhã.']
default falas_python = [pyt, "Claro que sim!", 'Uma garota maravilhosa que está sempre ajudando os outros... ', 'Olha eles aí', 'Eu posso entrevistar os professores da academia.', 'A maior parte deles teve muita importância sobre como a história dessa área progrediu.', 'Você vai ficar bem?', 'Ué, eu te falei sobre no primeiro dia sobre isso', 'Vou fazer as entrevistas ainda hoje, e amanhã vocês podem ir a sala de recreação pegar', 'Eu também vou indo, preciso preparar algumas coisas para amanhã. Tchau, pessoal!']
default falas_lua = [lua, "Olha só, não é uma má ideia.", 'Uma garota cujo Deus errou na hora de fazer a ficha de personagem e de alguma forma nasceu com parafusos a mais e a menos...', 'Já era hora de aparecerem', 'Você não deve subestimar fóruns onlines alternativos. Se você for alguém habilidosa como eu e conseguir filtrar o que é útil, o que é inútil...', 'e o que é propaganda com vírus sobre mães solteiras na sua cidade, dá pra achar coisas muito impressionantes no meio desse garimpo. Vou procurar informações por ali.', 'Que deus te tenha', 'Não se preocupa, eu também ainda não comecei a estudar porque ainda falta tempo.', 'Não deve ser difícil pegar as coisas da net, então vai ser rápido.', 'Essa garota nunca para de surpreender. Bem não é da minha conta, tenho que ir pra casa começar o novo evento do Destination 2.']
default falas_ruby = [rub, "Sim, pode contar comigo!", 'Uma mulher determinada que vai até o fim quando decide fazer algo...', 'O que você queria discutir?', 'A professora também mencionou sobre a etapa de avaliação de custos para a criação de tecnologias.', 'A parte de planilhas, planejamento e coleta de valores podem confiar em mim para fazer. Garanto que não vão se arrepender.', 'Você não pode se sobrecarregar com tantas atividades assim', 'Eu espero que eu seja capaz de acertar tudo. Sempre fico nervoso antes desse tipo de coisa.', 'Tenho que fazer algumas coisas amanhã, mas até lá termino as planilhas e podem ir pegar comigo na sala de recreação.', '- Muito obrigado pela chance de trabalhar com você! Vou para casa começar a análise de custos, então até mais.']
default parceiro1 = []
default parceiro2 = []
default imagem_parceiro1 = "images/prolog  bird.png"
default imagem_parceiro2 = "images/prolog  bird.png"

label semana2_dia8:
    scene black
    show text "Dia 8" at truecenter
    pause 2
    scene sala 1 with dissolve
    play music "audio/music (2).mp3" volume 0.5
    "A trancos e barrancos, você sobreviveu à sua primeira semana na Academia. Tudo nela é tão diferente e absurdo que causa uma grande estranheza, mas, no fim de tudo, não é um lugar ruim."
    "Você estava na sala e ela se encontrava naquele estado de bagunça antes da entrada de autoridades que pudessem acalmá-la, coisa essa que acontece meros segundos após sua observação, com a ada abrindo a porta em um estourou."
    show ada at center
    ada "Aos jovens declaro minha presença, e trago comigo um buquê de crisântemos para não dizer que não falei dos mesmos!"
    "Ada passa pela sala distribuindo as flores, uma para cada estudante, prosseguindo com uma escrita errática no quadro."
    show ada at left with move
    ada "Crisântemos, flor da vida, mas também da morte." 
    show ada at center with move
    ada 'Morte, a chegada da paz eterna.'
    show ada at right with move
    ada 'Paz, a antítese da guerra.'
    show ada at center with move 
    ada 'Guerra, aquilo que move a engenhosidade humana.'
    ada "Agora, me digam, alunos: o que é criado a partir de tal engenhosidade?!"
    hide ada
    show pyth 14 at center
    pyt "Cinema inglês!"
    hide pyth 14
    show java at center
    jav "Cafeteiras portáteis."
    hide java
    show lua 6
    lua "Vídeo games."
    hide lua 6
    show ruby 16 at center
    rub "Boy bands?"
    hide ruby 16
    show swift 13 at center
    swi "Frutas de luxo, é claro."
    hide swift 13
    show cobol 5 at center
    cob "Tabelas ACID."
    hide cobol 5
    show haskell neutral 2 at center 
    has "M̸̟͇͗̉͝ā̸̫̥q̶̮̃̌̅ų̷̙̦͊i̴̯̕ǹ̷̮̌̈́e̵͚̔̍ẗ̵̩̮́̕ȧ̸̘̟ ̴̤̈́b̶̦͍͗͘͢l̶̙̍̕͝u̵͍̹̮͗͘e̶̦͓̽͜͠ẗ̵̘́͐ō̵̭̅ö̷̩̥́̊t̸͖͓͊͜ḩ̶͔́̚ͅ."
    hide haskell neutral 2
    show ada at center
    ada "Claro, mas é claro! Todos estão certos, mas não pelo motivo imaginado." 
    ada "Tudo isso só pode ser feito por causa da evolução da tecnologia, e com a mesma, a Computação." 
    ada "É importante saber nossas raízes e toda a trajetória até o atual ponto, por isso vocês vão fazer um trabalho em grupo sobre a história da computação!"
    "A turma deu um suspiro coletivo de desânimo."
    ada "Oh, a doce tolice! Dádiva da juventude! Agora para as instruções: um documento estruturado em menos de 60 páginas seguindo as normas da ABNT com margem de..."
    scene black with dissolve
    "O tempo passa..."
    scene sala 1 with dissolve
    show ada at center
    ada "...capa essa que precisa possuir uma Máquina Turing Reconhecível que divide a palavra em 3 partições de mesmo tamanho, tendo o início de toda nova partição marcada por..."
    scene black with dissolve
    "Mais meia hora passa."
    scene sala 1 with dissolve
    show ada at center
    ada "Com parte da seção da análise de custos sobre a criação de processadores feita com a fonte Comic Sans de tamanho 12, fundo roxo e cor dourada para demonstrar a nobreza de um registrador, formado por..."
    "Meu deus"
    scene black with fade
    pause 1.2
    scene sala 1 with dissolve
    show ada at center
    ada "E isso é tudo!"
    "O horror no rosto dos estudantes era palpável. O trabalho em si não era difícil, mas o processo de criação do documento parecia algo mais doloroso do que produzir um sitcom de exibição diária durante seis meses." 
    "Estavam aliviados e à beira de um colapso após ouvir unicamente instruções de como fazer o projeto durante mais da metade da aula."
    ada "Devem enviar os trabalhos pra mim até sábado às 23:59h. Não é um trabalho complicado, então espero qu- Ah, é verdade! Tem mais um problema!"
    "O desespero coletivo tomou conta da turma pela simples ideia de que o resto da aula também seria para explicar a formatação maluca do documento de entrega."
    hide ada
    "Figurante 1" "EU NÃO AGUENTO MAIS!"
    "Figurante 1 vai em direção à janela prestes a abri-la e se defenestrar, mas é parado por Figurante 3"
    "Figurante 3" "Eieieieieieieieieiei, se acalma, se acalma cara!"
    "Figurante 1" "CALMA NADA! A PESSOA DO NOSSO GRUPO RESPONSÁVEL PELA DOCUMENTAÇÃO DA ÚLTIMA VEZ FOI O 2 E O TEPT ADQUIRIDO FOI TÃO GRANDE QUE OLHA A REAÇÃO DELE AGORA QUE A PROFESSORA ADA FALA DE PROJETO!"
    "Figurante 2" "Os esqueletos estão vindo... Eu não tenho determinação, eu não tenho determinação!"
    show ada at center
    ada "Isso mesmo, não jogue sua vida fora! Mesmo que isso fosse resolver o problema que eu iria apresentar."
    "Você fica confuso e preocupado com tal declaração, por isso decide perguntar:"
    mc "Com licença, mas o que é o problema que a senhora estava dizendo?"
    ada "Proatividade louvável, logo, irei respondê-lo. O trabalho é feito em trios, mas com sua adição, o número de alunos não é mais múltiplo de 3, mas bem..."
    "Ada passeia os olhos pela sala antes de continuar"
    ada "Uma das estudantes está faltando, e dessa vez nem sequer teve o esforço de deixar sua coruja aqui. Ultrajante!" 
    "Pois ela que se vire pra arrumar grupo depois. Agora, vamos lá alunos: escolham seus trios nesse momento."
    hide ada
    "Um trio, não é? Alguns nomes vêm à sua mente: Java, Lua, Ruby e Python."
    "Nenhum deles provavelmente se incomodaria de formar um grupo com você."
    call escolhendo_grupo from _call_escolhendo_grupo
    
    #Definição dos sprites dos parceiros
    if parceiro1[0].name == "Python":
        $ imagem_parceiro1 = "python_parca"
        $ grupoPythonRuby = True
    elif parceiro1[0].name == "Java":
        $ imagem_parceiro1 = "java_parca"
        $ grupoJavaLua = True
    elif parceiro1[0].name == "Ruby":
        $ imagem_parceiro1 = "ruby_parca"
        $ grupoPythonRuby = True
    else:
        $ imagem_parceiro1 = "lua_parca"
        $ grupoJavaLua = True
    
    if parceiro2[0].name == "Python":
        $ imagem_parceiro2 = "python_parca"
        $ grupoPythonRuby = True
    elif parceiro2[0].name == "Java":
        $ imagem_parceiro2 = "java_parca"
        $ grupoJavaLua = True
    elif parceiro2[0].name == "Ruby":
        $ imagem_parceiro2 = "ruby_parca"
        $ grupoPythonRuby = True
    else:
        $ imagem_parceiro2 = "lua_parca"
        $ grupoJavaLua = True
    
    $ nome_parceiro1 = parceiro1[0]
    $ nome_parceiro2 = parceiro2[0]
    #Fim do setup dos parceiros

    mc "Ei, pessoal, querem formar um grupo comigo?"
    python:
        renpy.show(imagem_parceiro1, at_list = [Position(xpos = 400, ypos = 1100)])
    nome_parceiro1 "[parceiro1[1]]"
    python:
        renpy.show(imagem_parceiro2, at_list = [Position(xpos = 1600, ypos = 1100)])
    nome_parceiro2 "[parceiro2[1]]"
    mc "Obrigado por aceitarem!"
    python:
        renpy.hide(imagem_parceiro1)
        renpy.hide(imagem_parceiro2)
    "Algum tempo passa e então a professora volta a falar"
    show ada at center 
    ada "Muito bem, alunos, venham aqui e escrevam no quadro os integrantes de seu trio."
    hide ada
    "Você decide ir lá e fazer essa tarefa. Não demora muito tempo, e então, o quadro está cheio de nomes e todos os estudantes voltam a se sentar."
    show ada at center
    ada "Esplendido, agora que tudo foi acertado, voltemos à aula de hoje. Aqui podemos ver que..."
    hide ada
    stop music
    "Ada vai prosseguindo por mais ou menos 10 minutos até que você começa a escutar algo, vindo do lado de fora da janela"
    pro "... janela!"
    "Você começa a escutar um barulho estranho. Como se fosse um helicóptero em miniatura."
    pro "Abre a janela!"
    scene prolog_entra with dissolve
    pro "E aí, como estão pessoal?"
    "Era uma garota pendurada de cabeça pra baixo num trapézio sustentado por sabe-se lá o que."
    ada "Prolog, você podia entrar pela porta da sala da próxima vez que faltar durante uma semana seguida tendo a presença da sua coruja na sala como único sinal de vida?"
    $ pro.name = "Prolog"
    pro "E qual seria o charme disso? Além do mais, a janela era a entrada mais rápida já que eu tava no terraço do prédio ao lado. Você sabia que a “queda” é o meio de transporte mais eficiente já inventado pelo ser humano?"
    ada "Admiro seu espírito, mas não muda o fato de você estar atrapalhando a aula."
    pro "Não seja por isso."
    scene sala 1 with dissolve
    show prolog 5 at center
    'A garota entra na sala pela janela após Ada abri-la e fica ali parada de pé. Ela olha pro quadro e ri ao ver os nomes nele.'
    show prolog at center
    pro 'Mais um trabalho em grupo? Legal! E aí, quem é que está no meu?'
    show prolog at left with move
    show ada at right
    ada 'Você perdeu a etapa de formação de grupos.'
    show prolog 4 at left 
    pro 'Ufufufu... Você me subestima. Mesmo que eu tenha faltado, o número de estudantes dessa sala é múltiplo de 3,'
    show prolog 17 at left
    pro 'então sempre haverá um grupo com uma vaga sobrando no qual serei automaticamente encaixada!'
    show prolog 19 at left
    pro 'Vamos lá, me diga: em que grupo estou? Sei que não estava aqui, mas deveriam ao menos ter posto meu nome no quadro logo pra eu saber. Deixa eu ver, cadê o grupo incompleto...'
    'Ela foi pra frente da sala analisar o quadro, até que caiu a ficha e ela perguntou preocupada:'
    show prolog 21 at left
    pro 'Cadê o grupo incompleto?'
    show ada at right
    ada 'Não tem grupo incompleto.'
    pro 'Pardon?'
    'Ada então aponta pra você mais uma vez e Prolog lhe encara.'
    hide ada
    show prolog 3 at center with move
    pro 'Ohhhhhhhhhhhhhhhhh!'
    'Ela lhe contempla como quem acaba de fazer uma descoberta'
    show prolog 25 at center
    'Seus olhos voltam para o quadro, mas dessa vez seu dedo indicador também o percorre com velocidade, como um cão farejador numa revista da polícia.'
    pro 'Achei! E como resto do trio temos [parceiro1[0].name] e [parceiro2[0].name], uma ótima escolha, devo pontuar.'
    'A garota pega o lápis de quadro e rapidamente escreve o nome dela abaixo do seu na divisão de grupos. Após isso ela caminha até você e lhe estende a mão.'
    show prolog 2 at center
    pro 'Muito prazer, Prolog. [player_name], presumo eu. Espero que possamos nos dar bem como companheiros de grupo.'
    mc "..."
    mc 'Eh?'
    show prolog 6
    pro '[player_name] se encontra em estado atônito, Gepeto.'
    'A garota falava com sua coruja'
    pro 'Pressuponho que o motivo seja minha presença e minhas ações nos últimos minutos, no entanto, uma maior  coleta de dados precisa ser feita com o objetivo de delimitar o escopo de possibilidades para o motivo especifico da surpresa do novo estudante.' 
    pro 'Foi minha entrada pela janela? A exaustiva apresentação do trabalho da senhorita Ada? Talvez minha integração repentina em seu grupo. De fato um mistério à ser elucidado.'
    mc 'Quem diabos é você pra começo de conversa?'
    show prolog 3
    pro 'Oya? Gepeto, aparentemente [player_name] não é o tipo de pessoa “easy come, easy go”, tal fato deve ser lembrado para futuras interações.'
    show prolog 4
    pro 'Seja como for, vinda de mim a informação pode perder credibilidade se você possui tal estranheza sob minha pessoa, então deixe que seus amigos falem! Digam a ele, quem eu sou?'
    'A garota então apontou seu para seus companheiros de equipe.'
    python:
        renpy.show(imagem_parceiro1, at_list = [Position(xpos = 400, ypos = 1100)])
    nome_parceiro1 "[parceiro1[2]]"
    python:
        renpy.show(imagem_parceiro2, at_list = [Position(xpos = 1600, ypos = 1100)])
    nome_parceiro2 "[parceiro2[2]]"
    python:
        renpy.hide(imagem_parceiro1)
        renpy.hide(imagem_parceiro2)
    show prolog 17
    pro "Non! Sou apenas Prolog, uma estudante da [school_name]!"
    "Exclamou a garota enquanto posava como uma garota magica dos anos 90." 
    'Quanto mais se reza, mais assombração aparece. Uma aparente estudante detetive invade a sala pela janela e agora ela está no seu grupo para o trabalho... Ela tá no seu grupo?'
    mc 'Porque você emburacou no grupo sem mais nem menos sendo que ele tá completo?'
    show prolog
    pro 'E em que outro grupo eu iria?' 
    show prolog 12
    pro 'Porque você entrou na turma, meu plano original foi pras cucuias, então eu seria posta em qualquer grupo já completo de qualquer forma. Mas a senhorita Ada realmente valoriza um aumento nas experiências interpessoais de seus estudantes,' 
    show prolog 2
    pro 'e como eu passei a semana passada toda procurando a senha para o cofre com mecanismo de autodestruição da minha tia, nem sequer troquei uma palavra com você ainda, [player_name]. Diante disso, não tem problema eu ficar nesse grupo, não é, senhorita Ada?'
    show prolog 2 at left with move
    show ada at right
    ada 'Claro que não tem. Considero a opção de resultado mais intrigante sendo sincera. Muito bem! Prolog será a quarta integrante de seu grupo, [player_name].'
    show prolog 1
    pro 'Como eu disse antes, espero que possamos nos dar bem como companheiros de grupo.'
    scene black with dissolve
    'Após dizer isso, Prolog se dirigiu à sua cadeira e lá sentou. Você fica impressionado em como a aula prosseguiu como de costume sem que mais ninguém além de você estivesse extremamente conflitado sobre a sequencia de eventos dos últimos 10 minutos.'
    scene sala 1 with dissolve
    show ada at center
    ada 'E isso é tudo por hoje turma, espero que estejam preparados para os eventos desse fim de semana.'
    hide ada
    'Ada então deixa a sala. Você está arrumando suas coisas pra ir embora quando uma figura de cabelo roxo aparece em sua frente.'
    show prolog
    pro '[player_name], reunião sobre o projeto.'
    mc 'Claro, quando vai ser?'
    show prolog 3
    pro 'Mas é claro que agora.'
    mc 'Eh, sério?'
    show prolog 7
    pro 'Está ocupado?'
    mc 'Na... na verdade não.'
    show prolog 2
    pro 'Então vamos lá.'
    'Você suspira'
    mc 'Claro, claro. Vamos lá.'
    scene corredor with dissolve
    show prolog 5
    'Prolog vai guiando o caminho e lhe levando para o lugar da reunião. A verdade é que você ainda está um pouco atordoado por causa de como as coisas se sucederam. '
    'Prolog não parece ser uma pessoa ruim, muito pelo contrário; segundo seus colegas de grupo, aquela garota é alguém extremamente confiável.'
    'É só que ela também é um pouco intensa e difícil de ser acompanhada, o que te deixa com um pé atrás em relação a ela.'
    show prolog 7
    pro 'Eu não sou tudo isso que você pensa.'
    mc "?"
    show prolog 6
    pro 'Você tá extremamente quieto desde que nos conhecemos, mas não parece ser o tipo de pessoa tímida. Eu sou tão intimidadora assim?'
    mc 'Você deixou uma grande primeira impressão.'
    show prolog 7
    pro 'Então provavelmente foi uma primeira impressão equivocada. Eu sou só uma garota que gosta de livros de mistério, maquinas, matemática e bonsai.'
    mc 'Bonsai?'
    show prolog 29
    pro 'Não parece?'
    mc 'Sem ofensa, não muito.'
    show prolog
    pro 'Pois é. Provavelmente um dos meus hobbies favoritos. A ideia de um mimetismo em miniatura, o processo cuidadoso de seleção da espécie certa pra cada ocasião, o processo meticuloso para prover os devidos cuidados e o empenho para manter a árvore sempre saudável. Gosto muito de tudo isso.'
    mc 'Eu não entendo muito sobre o assunto, então sinceramente não seu o que comentar sobre.'
    show prolog 8
    pro 'você não precisa comentar nada. Eu sabia que tinha algo sobre sua atitude que tava me incomodando, como se algo estivesse faltando e acho que descobri o que é.'
    mc 'É mesmo? E o que seria essa tal coisa que tava faltando?'
    show prolog 6
    pro 'O esforço que você faz pra se manter como interlocutor. O uso excessivo de recursos fáticos para impedir a morte do canal de comunicação, o que faz com que o outro lado sinta que de fato você se interessa pelo que ele diz. Você já havia percebido isso?'
    mc 'Na verdade não.'
    show prolog 18
    pro 'Gepeto, [player_name] mantém a comunicação de forma natural sem perceber tal habito. De qualquer forma, você fazer isso sem perceber é apenas atestado da sua gentileza.'
    'Um esforço pra manter a conversa? Você nunca percebeu tal costume, mas agora que foi pontuado, a garota provavelmente tinha razão. Parece que de fato ela é tu-'
    show prolog 29
    pro 'Não, já disse que não sou tudo que dizem. Era nisso que estava pensando e agora pensa ainda mais por eu parecer algum tipo de telepata.'
    pro 'Não importa se pensa isso de alguém, não pense isso de alguém! Assim que você bota alguém no pedestal se torna muito mais difícil se aproximar da pessoa, e não gostaria que essa fosse a situação entre nós dois. Entendido?'
    mc '...'
    mc 'Certo'
    'Talvez Prolog tenha razão e você tenha passado muito tempo colocando todos num pedestal. Isso pode realmente dificultar se aproximar de alguém que você considere melhor que você, então talvez seja melhor seguir o conselho da garota e pensar nas coisas de uma forma diferente.'
    'Enquanto você está perdido em pensamentos, um grupo de estudantes, passa por vocês e os cumprimenta.'
    "Figurante 4" 'Prolog! Muito obrigado por semana desmascarar o meu namorado que queria roubar sua tia, dei um pé na bunda do infeliz assim que soube do seu escândalo com lavagem de dinheiro.'
    show prolog 6
    pro 'A-ah, é claro, pode sempre chamar quando precisar.'
    "Figurante 8" 'Deixa de modéstia. Você resolve até problemas que nem sabíamos que existiam. Como descobriu que o corte de salario do meu pai foi devido ao desfalque que o namorado da estudante A causou com o desvio de dinheiro da empresa?'
    show prolog 13
    pro 'B-bem, uma c-coisa levou a outra e as peças que já existiam simplesmente caíram no lugar.'
    "Figurante 16" "Isso é pouco! Você resolveu quebra-cabeças que nunca sequer haviam sido fabricados ainda. Por sua causa, a empresa de cofres do meu irmão escapou de um grande processo que poderia ocorrer no futuro já que devido a forma como o cofre de autodestruição era estruturado, "
    "Figurante 16" "ele poderia levar o infrator a óbito, fazendo com que parte da responsabilidade da morte recaísse sobre meu irmão, o projetista do mecanismo de segurança."
    show prolog 15
    pro 'I-i-isso n-não f-f-f-foi nada demais! Sério!'
    "Figurante 4" 'Realmente a mestre detetive é um poço de simpatia sem fundo vamos parar de te incomodar com isso, só queríamos agradecer. Tchau, Prolog.'
    show prolog 10
    pro '...Tchau'
    "Os estudantes foram embora" 
    "Ficaram apenas você e ela no corredor. Você e a mestre detetive."
    mc '...'
    show prolog 11
    pro '...'
    mc 'O pedestal tá cada vez mais alto.'
    show prolog 15
    pro 'Eu juro que não sou tudo que dizem!'
    scene black with fade
    pause 1.5
    scene biblioteca with dissolve
    play music "audio/Righteous.mp3" volume 0.5
    python:
        renpy.show(imagem_parceiro1, at_list = [Position(xpos = 400, ypos = 1100)])
        renpy.show(imagem_parceiro2, at_list = [Position(xpos = 1600, ypos = 1100)])
    'Finalmente você e Prolog chegam à biblioteca. Lá esperando já estavam [parceiro1[0].name] e [parceiro2[0].name]'
    nome_parceiro1 "[parceiro1[3]]"
    nome_parceiro2 "[parceiro2[3]]"
    show prolog 6
    pro 'Certo, deveríamos separar antes de tudo os papeis de cada um na produção. Algum de vocês já sabe o que gostariam de fazer?'
    nome_parceiro1 "[parceiro1[4]]"
    nome_parceiro1 "[parceiro1[5]]"
    nome_parceiro2 "[parceiro2[4]]"
    nome_parceiro2 "[parceiro2[5]]"
    python:
        renpy.hide(imagem_parceiro1)
        renpy.hide(imagem_parceiro2)
    show prolog 3
    pro 'Muito bem. Dessa forma já cobrimos boa parte daquilo que foi requisitado pela professora Ada. '
    pro 'O que não for coberto pelas atividades de vocês eu poderei fazer e preencher os buracos, dessa forma teremos todo o conteúdo necessário para a entrega do documento. '
    show prolog 6
    pro 'Só resta agora o elefante na sala: o documento de entrega.'
    'Os 4 se entreolharam naquele estante. Era nítido que nenhum de nós desejava aquilo, mas  algo que tinha que ser feito. Então, Prolog deu um passo a frente.'
    show prolog 7
    pro 'Tá legal. Eu faço isso.'
    python:
        renpy.show(imagem_parceiro1, at_list = [Position(xpos = 400, ypos = 1100)])
        renpy.show(imagem_parceiro2, at_list = [Position(xpos = 1600, ypos = 1100)])
    nome_parceiro1 "[parceiro1[6]]"
    nome_parceiro2 "[parceiro2[6]]"
    python:
        renpy.hide(imagem_parceiro1)
        renpy.hide(imagem_parceiro2)
    show prolog 25
    pro 'Não se preocupem! Afinal, eu terei ajuda.'
    'A detetive então aponta para você'
    mc 'Sabia que ia sobrar pra mim...'
    show prolog 26
    pro 'Veja pelo lado bom, compartilhar da documentação comigo será sua única responsabilidade. Não quer dizer que isso vai ser fácil, mas pelo menos terá só uma coisa pra se preocupar além do outro problema esse fim de semana.'
    mc 'Outro problema?'
    python:
        renpy.show(imagem_parceiro1, at_list = [Position(xpos = 400, ypos = 1100)])
    nome_parceiro1 "[parceiro1[7]]"
    python:
        renpy.show(imagem_parceiro2, at_list = [Position(xpos = 1600, ypos = 1100)])
    nome_parceiro2 "[parceiro2[7]]"
    show prolog 6
    pro 'Estamos falando dos testes semanais da Academia. E garanto que se não se preparar para eles vai se arrepender.'
    show prolog 7
    mc 'Então temos esse teste e o trabalho para o mesmo dia? Ótimo.'
    show prolog 6
    pro 'Devemos tentar agilizar as coisas pra terminarmos antes do ultimo dia, mas na pior das hipóteses a documentação ainda poderá ser terminada após fazermos a prova, [player_name].'
    nome_parceiro1 "[parceiro1[8]]"
    nome_parceiro2 "[parceiro2[8]]"
    show prolog
    pro 'Então estamos de acordo! Acho que isso é tudo que eu tinha para dizer, então estamos todos dispensados. Agora se me dão licença, preciso ir resolver algumas coisas.'
    'E logo após dizer isso, Prolog abre a janela. Da sua coruja sai uma barra, na qual ela segura logo antes de pular pra fora e ser sustentada por Gepeto, assim indo embora.'
    hide prolog
    nome_parceiro1 "[parceiro1[9]]"
    python:
        renpy.hide(imagem_parceiro1)
    nome_parceiro2 "[parceiro2[9]]"
    python:
        renpy.hide(imagem_parceiro2)
    'E assim, todos deixam a sala, sendo você a ultima pessoa a estar nela. Não parece que vai haver problemas com esse trabalho, mas alguma coisa lhe grita que não vai ser tão fácil quanto parece.'
    stop music
return

    
label escolhendo_grupo:
    menu:
        "E então, quem será a primeira pessoa que estará ao seu lado através da dor e sofrimento que será a produção desse trabalho?"
        "Python":
            $ falas_python[0] = pyt
            $ parceiro1 = falas_python
        "Lua":
            $ parceiro1 = falas_lua
        "Java":
            $ falas_java[0] = jav
            $ parceiro1 = falas_java
        "Ruby":
            $ parceiro1 = falas_ruby
    menu:
        "E quem será a segunda?"
        "Python":
            $ falas_python[0] = pyt
            $ parceiro2 = falas_python
        "Lua":
            $ parceiro2 = falas_lua
        "Java":
            $ falas_java[0] = jav
            $ parceiro2 = falas_java
        "Ruby":
            $ parceiro2 = falas_ruby
    if parceiro1[0].name == parceiro2[0].name:
        "Você não pode escolher a mesma pessoa duas vezes."
        "Vamos lá, mais uma vez"
        jump escolhendo_grupo
return
