#image lua_parca = "images/Sprites Lua/lua 1.png"
#image java_parca = "images/Sprites Java/java 1.png"
#image python_parca = "images/Sprites Python/python 1.png"
#image ruby_parca = "images/Sprites Ruby/ruby 1.png"


#default falas_java = [jav, "Seria um prazer.", "Uma aspirante a detetive que resolveu inúmeros casos, contribuindo para a melhora da sociedade...", 'E então, vamos começar?', 'Seria uma boa ideia eu procurar informações do funcionamento intrínseco de tecnologias da área de computação, não apenas de computadores propriamente ditos.','Posso fazer isso com o próprio material existente aqui na biblioteca.', 'Acredito que você consegue concluir essa árdua tarefa?', ' Se você não sabia sobre, é melhor correr pra recuperar o tempo perdido. Posso ajudar se quiser.', 'Me dê 2 dias e garanto que tudo estará completo.', 'Aproveitando a deixa, vou pra biblioteca começar minha parte no trabalho. Até amanhã.']
#default falas_python = [pyt, "Claro que sim!", 'Uma garota maravilhosa que está sempre ajudando os outros... ', 'Olha eles aí', 'Eu posso entrevistar os professores da academia.', 'A maior parte deles teve muita importância sobre como a história dessa área progrediu.', 'Você vai ficar bem?', 'Ué, eu te falei sobre no primeiro dia sobre isso', 'Vou fazer as entrevistas ainda hoje, e amanhã vocês podem ir a sala de recreação pegar', 'Eu também vou indo, preciso preparar algumas coisas para amanhã. Tchau, pessoal!']
#default falas_lua = [lua, "Olha só, não é uma má ideia.", 'Uma garota cujo Deus errou na hora de fazer a ficha de personagem e de alguma forma nasceu com parafusos a mais e a menos...', 'Já era hora de aparecerem', 'Você não deve subestimar fóruns onlines alternativos. Se você for alguém habilidosa como eu e conseguir filtrar o que é útil, o que é inútil...', 'e o que é propaganda com vírus sobre mães solteiras na sua cidade, dá pra achar coisas muito impressionantes no meio desse garimpo. Vou procurar informações por ali.', 'Que deus te tenha', 'Não se preocupa, eu também ainda não comecei a estudar porque ainda falta tempo.', 'Não deve ser difícil pegar as coisas da net, então vai ser rápido.', 'Essa garota nunca para de surpreender. Bem não é da minha conta, tenho que ir pra casa começar o novo evento do Destination 2.']
#default falas_ruby = [rub, "Sim, pode contar comigo!", 'Uma mulher determinada que vai até o fim quando decide fazer algo...', 'O que você queria discutir?', 'A professora também mencionou sobre a etapa de avaliação de custos para a criação de tecnologias.', 'A parte de planilhas, planejamento e coleta de valores podem confiar em mim para fazer. Garanto que não vão se arrepender.', 'Você não pode se sobrecarregar com tantas atividades assim', 'Eu espero que eu seja capaz de acertar tudo. Sempre fico nervoso antes desse tipo de coisa.', 'Tenho que fazer algumas coisas amanhã, mas até lá termino as planilhas e podem ir pegar comigo na sala de recreação.', '- Muito obrigado pela chance de trabalhar com você! Vou para casa começar a análise de custos, então até mais.']
#default parceiro1 = []
#default parceiro2 = []
#default imagem_parceiro1 = "images/prolog  bird.png"
#default imagem_parceiro2 = "images/prolog  bird.png"




label semana2_dia10:
    call primeira_conversa_dia10 from _call_primeira_conversa_dia10
    if grupoJavaLua:
        call continua_dia10_parte1 from _call_continua_dia10_parte1
        call vai_pra_diretoria_dia10 from _call_vai_pra_diretoria_dia10
    else:
        call fim_simples_dia10 from _call_fim_simples_dia10
return



label primeira_conversa_dia10:
    scene black
    show text "Dia 10" at truecenter
    pause 2
    scene sala 1 with dissolve
    play music "audio/music (2).mp3" volume 0.5
    
    "Mais um dia comum naquela academia. Ada apresentava as aulas de forma estranha, mas elas não eram ruins pra ser sincero. Ela era uma professora bastante competente e não menosprezava as dúvidas dos alunos (ou talvez o fizesse, mas de forma tão erudita que ninguém que se importaria conseguia entender)."
    "Enquanto escutava a professora, você sente uma bolinha de papel lhe acertando. Olhando para o ponto de origem dela, você vê Prolog segurando uma folha na qual estava escrito: 'Abre as pernas'."
    "Você olha pra garota com estranheza enquanto balança a cabeça negativamente. 'Abra, para sua segurança', ela escreve na folha. 'Isso é assédio e coerção', você responde numa folha de caderno e a mostra."
    "Prolog parece um pouco incomodada com sua resposta e depois de um suspiro, a coruja dela começa a vir em sua direção e entra embaixo da sua mesa."
    "Num susto, você abre as pernas para evitar se machucar nas hélices dela. Irritado, você pega a folha novamente e manifesta nela sua indignação"
    
    mc "O que foi isso!?"
    show prolog  with moveinleft
     
    show prolog 13
    pro "Uma escuta, responde a folha da garota enquanto a sua coruja sai de debaixo da mesa levando um pequeno objeto consigo"
    mc " Por que você me grampeou!?"
    show prolog 27
    pro "Who, me?"
    mc "Sim, você"
    show prolog 26
    pro "Couldn't be"
    mc "Pode me levar a sério?"
    show prolog 28
    pro "Não, [player_name], a música continua com você dizendo 'then who'. Dessa forma nunca saberemos quem roubou o pão!"

    "Você desiste de seguir prolog nessa loucura e vira novamente para prestar atenção na aula"
    
    show black with dissolve
    pause 2.0
    return

    label continua_dia10_parte1:

    scene sala 1 with dissolve    
    "As aulas chegam ao intervalo e, com isso, uma figura inesperada se apresenta diante de sua mesa."
    show swift 3 with moveinleft
    swi "- [player_name], não é? Eu preciso ter uma conversa com você. Vem aqui fora um segundo."        
    show swift
    "Era Swift com a cara deslavada de esnobe dele. Você mal o conhece e já consegue dizer que ele não é peça boa, talvez o melhor seja se manter longe dele."
    
    mc "- Pode falar aqui mesmo."
    show swift 4
    swi "Hum, parece que você não entendeu. Eu que dou as ordens aqui, vocês pobretões apenas precis-"
    mc "Até mais"
    show swift 7
    swi "Eieieieiei, você vai realmente só me deixar aqui falando só!?"
    hide swift
    scene corredor with dissolve   
    "Swift começa a te seguir pelo corredor tentando iniciar a conversa"
    show swift 8 with moveinleft
    swi "Ei, [player_name], é rude deixar alguém falando só, principalmente se esse alguém possui uma posição tão elevada quanto eu, afinal de contas..."
    show swift 9    
    "Você acelera o passo."
    
    "Ele acelera junto."
    show swift 9
    swi "[player_name], escuta aqui, eu não me importo o que você pensa sobre mim, mas você tá com algo meu e eu preciso de volta, afinal..."
    show swift 8
    "Você começa a correr."
    
    "Ele começa a correr junto"
    
    mc "Larga do meu pé, peste!"
    show swift 8
    swi "Volta aqui, trombadinha! Ser pobre não vai te salvar das autoridades!"
    mc "Do que é que você tá falando!?"
    show swift 9
    "Vocês se aproximam da esquina do corredor. Você vê aquela como uma chance de despistar aquele loiro prepotente usando uma rápida curva fechada. Ela estava chegando."
        
    "10 metros."
    show swift 7    
    "5 metros."
    show swift 9
    "1 metro."
    show swift 9    
    swi "Eu tô mandando você devolver minha escuta!"
    show swift 8
    "Você freia bruscamente ao ouvir aquilo."
        
    mc "Então foi você!?"

    hide swift with moveoutright
    "Swift não tem o mesmo potencial de desaceleração que você, o que o faz passar direto e dar de cara com a parede."

    show swift 24 with moveinbottom
    mc "Por que você me grampeou!?"
    show swift 22
    swi "A resposta é óbvia! Você tem se metido demais em meus planos, então decidi te monitorar de perto pra evitar mais uma ocorrência."
    mc "Cara, a gente mal trocou palavras até agora, o que é que você quer dizer com 'se meter nos seus planos'?"
    show swift 17
    swi "Não se faça de idiota! Você me atrapalhou em ao menos uma ocasião. Não só isso, como me jogou do 4° andar!"
    mc "Ah..."
        
    "É, você se lembra disso."
        
    mc "Eu não me lembro disso"
    show swift 15
    swi "Isso é uma mentira descarada! Você- ah, quer saber, não tô com saco de lidar com gentalha como você, então só me devolve minha escuta. Essas coisas são caras e eu não quero ter o prejuízo de 3 escutas quebradas em 1 mês."
    mc "Por que você tá sequer espionando os outros?"
    show swift 13
    swi "Não é da sua conta. Agora, cadê minha escuta?"
    mc "Prolog pegou."
    show swift 8
    swi "O queeeeeeeeee!? E por que você deixou!?"
    mc "Você tá ouvindo a si mesmo?"
    show swift 7
    swi " Ótimo, agora por sua culpa eu"
        
    "Um barulho começa a sair dos autofalantes do corredor."
    show swift 5 
    
    jav "Depurando, depurando. 1, 2, 3. Todos escutam seu rei?"
        
    "Você reconhecia aquela voz. Era Java, mas ele parecia diferente"

    show swift 10    
    jav "Muito bem. Caros súditos, a corte real lamenta interromper o decorrer de seu dia, no entanto, existe um assunto urgente do qual é preciso tratar: a existência de um transgressor em nosso feudo"
    show swift 11 
    swi "Me fala, seu amigo escorreu o café em pano mofado?"
    mc "Você tá pedindo pra ser atirado do 4° andar de novo."
    jav "Swift... Seus dias de malícia acabam hoje! Suas atividades nocivas ao cidadãos, em especial ao vassalo nomeado Ruby, incluem extorsão, coerção, violência física e psicológica, uso indevido de títulos de nobreza e suborno. Hoje, um monarca vai ao chão"
    show swift 8
    mc "E-ei, o que diabos é isso?"
    show swift 15
    swi "C-c-certamente apenas ameaças infundada"
    jav "Meus pinguins entrarão em contato. Cambio desligo."
    show swift 24 at left
    swi "OS PINGUINS!? ISSO É MAL!"
    show prolog 6 at right with moveintop
    pro "Isso é muito mal!"
    show swift 23 at left
    show prolog 7 at right
    "reiterou Prolog que acabara de sair da ventilação."
    
    mc "Você tem essa mania de sair de todo e qualquer buraco, né?"
    show swift 15 at left
    swi "ESQUEÇA ELA, [player_name]. VOCÊ PRECISA ME AJUDAR, PELA NOSSA AMIZADE!"
    show swift 9 at left
    
    mc "Desde quando essa amizade existe? Deixando isso de lado, o que são esses pinguins que ele tá falando?"
    show prolog 6 at right
    pro "São literalmente pinguins"
    show prolog 13 at right
    show swift 10 at left
    pro "Essa é uma história que data de alguns meses atrás. Alguém trocou o café de Java pra descafeinado como brincadeira."
    show prolog 15 at right
    pro " No dia seguinte ele apareceu com um exercito de pinguins para proteger a academia."
    show prolog 7 at right
    show swift 7 at left
    mc "Isso é super estranho, mas pelo menos os pinguins tão apenas protegendo coisas, ao invés de fazer algo ruim."
    show swift 8 at left
    show prolog 12 at right
    swi "NÃO, VOCÊ NÃO SABE DO QUE TÁ FALANDO!"
    show swift 7 at left
    show prolog 13 at right
    pro "Parece que a ideia de proteger a academia se estendia um pouco longe demais."
    show prolog 28 at right
    pro "Os pinguins começaram a interditar áreas como os banheiros para evitar superlotação. Fizeram um cerco ao redor do mercado pra impedir a aquisição de itens possivelmente perigosos. Perseguiam estudantes que não seguiam as normas da escola..."
    show prolog 10 at right
    mc "Existem normas nessa escola?"
    show prolog 13 at right
    pro "Além disso, digamos que os pinguins iam um pouco além da conta no tratamento contra transgressores."
    show swift 15 at left
    show prolog 14 at right
    swi "UM POUCO ALÉM?!"
    show swift 6 at left
    swi "- AQUELES SEREM EMPLUMADOS ME DERRUBARAM, ME ARRASTARAM PARA A SALA DE RECREAÇÃO E ME USARAM DE CHOCADEIRA!"
    show swift 1 at left
    mc "- Oh, ok. Isso é mau"
    show prolog 13 at right
    pro "Sim"
    show prolog 6 at right
    show swift 5 at left
    pro "Provavelmente aconteceu porque Java ficou muito tempo sem dormir. Chuto 72 horas."
    mc "72?!"
    show prolog 7 at right
    show swift 11 at left
    swi "Ok, então tudo que precisamos fazer pra parar o maluco é pôr, ele para ninar, não é?? Isso vai ser fácil"
     
    "O garoto então tira um celular extremamente reluzente do bolso e começa a fazer uma ligação"
    
    show swift 4 at left
    swi "Alô?"
    show swift 8 at left
    swi " É claro que sou eu! Quem mas poderia ser?"
    show swift 12 at left
    swi "Isso não importa, o que importa é que os pinguins voltaram e eu preciso da ajuda de vocês pra resolver essa situação."
    show swift 13 at left
    swi "Preciso que apaguem alguém."
    show swift 11 at left
    swi "O ex-presidente"
    show swift 24 at left
    swi " Não, não o do país, animal! Eu tô falando de Java."
    show swift 4 at left
    swi "Isso. Ele tá..."
    show swift 5 at left
    show prolog 6 at right
    pro "Na sala do diretor"
    show prolog 7 at right
    show swift 13 at left
    swi "Na sala do diretor!"
    show swift 14 at left
    swi "Isso. Agora vão! Minha integridade está em risco aqui!"
    show swift 18 at left
    swi "Problema resolvido."
    show swift 19 at left
    show prolog 25 at right
    pro "Você ligou pros seus seguranças?"
    show prolog 5 at right
    show swift 20  at left
    swi "- É claro que sim. Agora eu não preciso mais me preocupar, as coisas serão resolvidas num estalar de..."
    "*HONK*"
    show swift 23  at left
    show prolog 7 at right
    "Vocês olham para o outro lado do corredor, e então veem vindo em alta velocidade na sua direção, 2..."

    show swift 24  at left
    show prolog 6 at right 
    show pinguins at truecenter with moveoutbottom
    swi "PINGUINS!"
    show prolog 28 at right
    show swift 23  at left
    pro " Eles nos acharam rápido. [player_name], preciso que você vá para a sala do diretor para parar Java. Tenho a impressão que apenas a guarda de Swift não vai ser o bastante."
    mc " E por que você acha que eu vou ser, então?"
    show prolog 27 at right
    pro "Só um pressentimento. Agora vai rápido, eu cuido de proteger Swift dos pinguins"
    mc "Certo..."
    hide swift with dissolve
    hide prolog with dissolve
    hide pinguins with dissolve
    #escurecer
    show black with dissolve
    pause 2.0
    return

label vai_pra_diretoria_dia10:
    #transição para diretoria
    "Você segue a ordem de Prolog e vai para a diretoria. Não é como se você se importasse com aquele esnobe em apuros, mas ver Java agindo de forma tão desconexa com sigo mesmo era algo que lhe deixava triste. Por isso, era sua função ajudar seu amigo a recobrar os sensos."
    scene corredor with dissolve
    show lua 34 with moveinbottom
    "Ao chegar na frente da sala, você vê uma cena absurda. Os guardas de Swifts, todos em ternos preto e branco, estavam jogados pelo chão. Era realmente impressionante o fato de que todos aqueles profissionais treinados foram derrotados, mas o mais impressionante era quem havia feito aquilo."
    show lua 27 
    mc "Lua?"
    
    "Ela parecia cansada. Faz sentido, derrubar todas aquelas pessoas demandaria muito esforço. Não, não era isso. Ela parecia... Com sono?"
    show lua 26 
    
    lua "Oh, é você, [player_name]. Como é que vão as coisas?"
    show lua 25 
    mc "O que aconteceu aqui!?"
    show lua 15 
    lua "Nada de demais. Eles tentaram invadir a sala de Java, então eu tô aqui para dar uma coça neles."
    mc "Como diabos você derrubou todos eles?"
    show lua 5 
    lua "Capoeira."
    show lua 6
    mc "Desde quando você luta!?"
    show lua 13
    lua "Ei, nem toda gamer é sedentária, tá certo? Isso aí é preconceito de sua parte"
    show lua 26
    lua "Qual é, é só um pequeno acerto de contas por Ruby. Aquele magrelo é gentil demais para empatar o placar com o filhinho de papai, então tô ajudando Java com isso."
    show lua 25
    mc "Uma vingança não deixaria Ruby feliz! Além disso, nada vai mudar. Swift já foi feito de chocadeira e continua sendo uma praga."
    show lua 33
    lua "Isso é verdade também, mas tem outro motivo."
    mc "E qual seria?"
    show lua 31
    lua "Eu vendi uma conta pra Swift em um jogo popular hoje em dia, porque ele achou que se fosse melhor que Ruby em algum jogo, ele aumentaria suas chances de vencer a eleição que vai haver"
    mc "Isso não faz o menor sentido."
    show lua 25
    lua "Nope, mas a forma como aquele a mente daquele cara funciona é um mistério. Então convenientemente, eu tinha uma conta de um jogo que joguei um pouco e não goste, então vendi ela pra Swift"
    
    "Era visivel que ela estava caindo de sono"
    
    mc "Certo, qual o problema?"
    show lua 10
    lua "Eu mudei a senha da conta."
    mc "Que?"
    show lua 9
    lua "Eu mudei a senha ontem e esqueci qual pus"
    mc "A quanto tempo você tá acordada?"
    show lua 5
    lua "37 horas."
    mc "Tá explicado"
    show lua 15
    lua "De qualquer forma, eu não sei qual a senha da conta e eu preciso esperar 48 horas pra muda-la novamente"
    mc "E como isso leva você a ajudar Java"
    show lua 19
    lua "Se Swift descobre o que aconteceu ele me põe no PROCOM por venda e propaganda ilegítima."
    show lua 14
    lua "Se eu... distrair... ele durante... o dia... ele não..."
    show lua
    "Lua bate com as duas palmas no rosto para manter-se acordada"
    show lua 3
    lua "vai perceber o problema e eu vou poder alterar a conta!"
    mc "Eu não sei se isso é ou não uma piada."
    show lua 30
    lua "Depende se você acharia ou não engraçado eu ter minha casa confiscada pelo PROCOM para custear a dívida."
    mc "PELO AMOR DE DEUS, POR QUANTO VOCÊ VENDEU ESSA CONTA!?"
    show lua 32
    lua "Pelo suficiente para desnegativar meu CPF."
    
    "Você começa a pensar que talvez Swift não seja tão ruim quanto parece"
    show lua 26
    lua "Tendo isso em mente, eu não posso deixar você passar"
    show lua 25 
    "É, o dialogo estava fora de cogitação para resolver aquele problema. Além disso, se Lua conseguiu varrer o chão com todos os seguranças de Swift, você nunca conseguiria passar por ela usando de força bruta."
    
    " Olha, talvez Swift esteja apenas colhendo o que plantou? No fim das contas, ele se dar mal parece que beneficiaria mais pessoas do que causaria estragos."
    
    "Então seu telefone toca."
    show lua 25 at left
    show prolog  at right with moveinbottom
    pro "Alô, alô, minha Campina Grande... (Cantando)"
    show prolog 2 at right
    pro "Aquele abraço! (Cantando)"
    show prolog 5 at right
    mc "O que foi, Prolog?"
    show prolog 28 at right
    pro "Por que os pinguins ainda não se dispersaram?"
    mc "Lua tá guardando a porta."
    show prolog 6 at right
    pro "Oh... Isso é um problema maior ainda. Ela extorquiu Swift recentemente?"
    mc "Sim"
    show prolog 14 at right
    pro "Deixa eu pensar por um segundo..."
    show prolog 13 at right
    pro "Ok, pode deixar que eu resolvo o problema dela mais tarde, mas de qualquer forma você ainda vai ter que arrumar um jeito de passar por ela?"
    mc "E como é que eu faço isso!?"
    show prolog 2 at right
    pro "Se vira aí, meu caro Watson. Tenho que desligar, a barricada de caixas do cereal Gatilhos que Haskell fez não vai aguentar, vamos ter que pular pela janela. Falo com você depois!"
    hide prolog with dissolve
    mc "Mas que droga!"
    show lua 27 at center
    lua "Discussão com a colega de grupo?"
    mc "Mais ou menos. Ei, Prolog disse que vai te ajudar com o problema do PROCOM, então você poderia me deixar passar?"
    show lua 19
    lua "Nem a pau. Se eu te deixar passar vai ser como uma medalha de bronze no Kinect Adventures. Quando eu tô jogando, só miro no ouro"
    show black with dissolve
    show lua 19
    "Ótimo, ela não vai ceder. Você realmente vai ter que pensar numa forma de passar, mas como? "
    
    "Você precisa entender sua oponente."
    
    "Forçar a passagem é impensável, então você precisa ser sagaz. Entre na mentalidade dela. Torne-se um Gamer e derrote-a em seu próprio jogo!"
    
    
    "Por vezes, você encontrará situações nas quais é necessária uma análise sobre o interior de uma pessoa."
    
    "Nesse tipo de situação será iniciado um mini-game no qual você deve arrastar pedaços de código e organizá-los para formar um algoritmo."
    
    "Ao acertar o espaço de um trecho do código, o mesmo se fixará no local e, quando todas as lacunas forem preenchidas, o mini-game terá sido concluído. "
    
    "Não se preocupe, a história só continua após o algoritmo ser formado, no então, não há um limite de tempo nem penalidade por errar a ordem, então vá em seu próximo ritmo."
    # Inicia tutorial Drag and Drop
    #Fim Tutorial
    hide lua with dissolve
    $setup_lua_bs_puzzle()
    call screen lua_bs_puzzle








label lua_bs_complete:
    scene corredor with dissolve
    #transicao
    "Sim, é isso! Você sabe a resposta para aquilo."
    show lua 34 at center with moveinbottom
    mc "Lua, me deixe passar, caso contrário, terei que usar algo que não gostaria."
    show lua 30
    lua "Sinto muito, meu chapa, mas você não vai me derrubar tão fácil assim"
    mc "Certo, então lá vai:"
    show lua 23
    "você puxa o celular para preparar seu golpe"
    
    "Uma música começa a ser reproduzida..."
    
    mc "~Gohda-san and the others laid out the beautifully adorned dessert. I guess it's true when they say you have another stomach for dessert. I'd thought that being fed all that delicious food had totally filled me up, but as soon as I laid eyes on the dessert, my stomach started yelling 'More!'~"
    show lua 24
    lua "Pera, o que... você tá fazendo?"
    show lua 27
    mc "~I don't know much about desserts, but this looked really good. A white pudding-like substance was garnished with two shades of red sauce, and elegant rose petals adorned the dish. With such magnificent food distributed in front of everybody, it was time for the chef to extol the virtues of his creation. However, Maria, who was completely indifferent to this strict rule, got excited by this beautiful and delicious looking dessert and jumped into the fray as soon as it was placed before her. Aunt Rosa scolded her, calling it bad manners, but George responded by saying 'Now, now, it's alright.'~"
    show lua 26
    lua "Ah... Entendi... Fui enganada..."
    
    hide lua with moveoutbottom
    "Lua então apaga a vai ao chão. Ela estava com sono após passar 37 horas acordada, além disso, parar os guarda costas deve ter sido cansativo. A garota estava a beira de desmaiar, precisava apenas de um empurrãozinho"
    
    mc "É, o início de Umineko nunca falha em fazer alguém dormir."
    show black with dissolve
    pause 1.0
    "Você coloca Lua escorada na parede e adentra na sala do diretor. E lá sentado na cadeira de Alan Turing estava sentado Java."
    scene sala diretoria with dissolve
    show java 13 with moveinleft
    jav "O que traz você aos aposentos reais, jovem camarada?"
    mc "Onde está Turing?"
    show java 12
    jav "Os pinguins o levaram para a sala de entretenimento. Aquele que recebe o suborno de um transgressor também é um transgressor."
    mc "Java, isso é loucura! Você precisa voltar aos seus sensos."
    show java 15
    jav "Nunca estive mais lúcido, meu amigo. Sinto informar-lhe, mas aqueles que ficam no caminho do Rei, também serão tratados como transgressores. Não tem jeito, você precisará por ele para dormir assim como fez com lua. Analise-o e descubra como!"
    
    show black with dissolve
    pause 1.0
    
    #transição drag and drop java
    $setup_java_bs_puzzle()
    call screen java_bs_puzzle

label java_bs_complete: 
    scene corredor with dissolve
    show java 8
    "Sim, essa é a forma correta de parar Java!"
    show java 17
    mc "Eu desafio vossa majestade à um duelo!"
    show java 15
    jav "Quanta ousadia de sua parte. Muito bem, como ele procederá? "
    mc "Java Puzzlers. Aquele que resolver os 95 quebra cabeças do livro será declarado o vencedor."
    show java 12
    jav "Me desafiar em minha própria área? Não sei se isso é bravura ou tolice, mas aceito sua proposta. Para a biblioteca! "
    
    #transição para biblioteca
    "Você e Java seguem para a biblioteca, seguidos por uma marcha de pinguins. No meio do caminho, você manda uma mensagem para Prolog, explicando seu plano. Não demora muito até que vocês chegam ao seu destino."
    hide java with dissolve
    show black with dissolve
    pause 1.0
    scene library with dissolve
    show java 2 at left with moveinleft
    show prolog at right with moveinright
    pro "Estão prontos para o duelo que abalará a monarquia!?"
    mc "Você chegou rápido"
    show prolog 6
    mc "Além disso, porque você é a anunciadora se só tem nós 3 aqui dentro?"
    show prolog 20
    pro "Nunca subestime a velocidade do paradigma lógico. E para a segunda pergunta: uma competição fica mais legal com uma comentarista."
    show prolog 10
    show java 15
    jav "Deixem de enrolação. Viemos aqui para travar uma batalha."
    show prolog 3
    show java 16
    pro "Certo, certo, meu rei."
    show prolog 4
    pro "Aqui estão as regras: vocês responderão as perguntas, mas as respostas serão corrigidas apenas no fim. Podem usar o tempo que quiserem, mas assim que um terminar as 95 questões, o outro só terá mais 10 minutos para fazer questões. "
    show prolog 27
    pro " Cada questão acertada lhe dar um ponto. Cada questão errada ou em branco lhe tira 1 ponto. Quem estiver com mais pontos no fim será o vencedor."
    show prolog 22
    "A garota pegou da estante e deu a cada um uma cópia de Java Puzzlers."
    show prolog 18
    pro "Eeeeeeeee... Comecem!"
    hide prolog with moveoutright
    show java 15 at center
    "Java estava frenético. Mesmo com as 72 horas sem sono, ele ainda era uma máquina movida à café. Movida a café, e essa era sua fraqueza. "
    
    "Toda vez que resolvia uma questão, ele tomava uma xicara de café feito por sua cafeteira portátil e mandava ela preparar outra para que nunca lhe faltasse uma ao terminar a questão."
    
    "Ele tinha a confiança de que nunca demoraria o bastante numa questão a ponto do café na xicara esfriar, por isso, valia mais a pena ele preparar outra assim que tomasse uma do que ter que esperar uma ficar pronta para ir para a próxima questão."
    
    "Java estava na liderança, mas o você estava logo atrás. Enquanto ele estava na questão 20, você estava na 10. E então..."
    show prolog at right with moveinright
    pro "[player_name] ultrapassa Java no número de questões!"
    
    "A garota comentava tudo e qualquer coisa de forma extremamente escandalosa, quase incomoda, mas foi só nesse momento que Java pareceu se alterar. "
    hide prolog with moveoutright
    "Você escrevia no livro rapidamente e passava as páginas, seu ritmo era insano. Isso acendeu uma chama nos olhos de Java, fazendo-o acelerar ainda mais, lhe ultrapassando."
    
    "Mas isso não era o bastante para abalar você, pois, quando Java lhe ultrapassou, você aumentou novamente a velocidade, seguindo-o de perto!"
    show java 12 
    jav "[player_name], você é forte, mas ainda não é páreo para mim! "
    
    "E então, vocês entravam no ultimo terço das questões. E, nesse momento, a velocidade de Java atingiu níveis sobre-humanos, completando as 30 questões restantes em 3 minutos, e concluindo a prova"
    show prolog 2 at right with moveinright
    show java 25 at left 
    pro "E Java cruza a linha de chegada! Mas não podemos garantir sua vitória ainda, porque seu oponente ainda possui 10 minutos para responder suas 25 questões restantes"
    show prolog 6
    "E ao ouvir isso, você abriu um sorriso malicioso. Sua velocidade caiu drasticamente, voltando a de uma pessoa normal. Isso causou estranheza em Java. E então, o tempo foi passando."
    
    "1 minuto"
    
    "2 minutos"
    
    "4 minutos"
    
    "8 minutos"
    
    "Você seguia num caminhar lento e sereno, isso fez Java se irritar."
    show java 17 
    jav "O que está acontecendo, [player_name]?! Você desistiu de lutar depois que terminei as questões? Onde está sua garra de agora há pouco!?"
    mc "Não preciso de garra."
    show java 11 
    jav "O que?"
    mc "Nem mesmo preciso terminar as 95 questões."
    show java 15 
    jav "Você está caçoado de mim!? Acha que a minha pressa fez eu errar questões? Hahahahaha! Tolice, eu estou muito além de erros tão amadores."
    mc "Ah, não, não. Você entendeu errado. Acontece que eu não preciso terminar as questões porque eu já venci"
    show java 11 
    jav "O que você..."
    
    "E nesse momento, a mente de Java embranquece."
    show java 14
    jav "Desgraçado..."
    hide java with moveoutbottom
    "*POW*"
    
    "O corpo de Java cai sobre a mesa"
    
    "O silencio toma a sala por alguns instantes, até que você pergunta:"
     
    mc "Quantos saches?"
    show prolog 3 at center with moveinleft
    pro "37 saquinhos de camomila concentrada. Cortesia de Haskell, ele aparentemente ficou tão irritado com os pinguins bagunçando sua loja que decidiu nem me cobrar por eles. Mas me diz, como pensou nesse plano?"
    show prolog 6
    mc "Java é movido à café. Significa que ele passou as ultimas 72 horas se afogando em café para manter-se acordado. Por causa disso, seu paladar já estava anestesiado por causa do calor do café, o que não o permitiria notar a presença da camomila."
    mc "Além disso, não é preciso ser um gênio pra saber que após tanto tempo acordado, a pessoa está prestes a dormir de pé, então tudo que Java precisava para dormir era um empurrãozinho."
    show prolog 5
    mc "Fico feliz que você conseguiu encontrar uma abertura para trocar as xicaras de café dele para o nosso chá de camomila feito com café ao invés de água."
    show prolog 2
    pro "Foi fácl."
    show prolog 
    pro "Todo o barulho que eu estava fazendo disfarçou o som da maquina de café que escondi embaixo da mesa. Java estava tão concentrado que nem percebia quando eu trocava as xicaras."
    show prolog 3
    pro "Mas foi por isso que você começou a acelerar, não é? Pra forçar Java a se concentrar apenas nas questões e não notar a xicara sendo trocada 37 vezes ao longo do duelo. "
    show prolog 14
    mc "Então você percebeu."
    show prolog 16
    pro "Claro que percebi. E então, quantas perguntas você acertou?"
    mc "Zero, é claro"
    pro "Você tava escrevendo violentamente para assustar Java, né?"
    mc "Novamente, é claro."
    show prolog 2
    pro "Guwahahahahahaha"
    show prolog 
    pro "Magnifique! [player_name], meu caro, você realmente é coisa de outro mundo."
    mc "Você me dá crédito demais"
    show prolog 5
    "Você dizia isso, mas na verdade sentia certo orgulho de ter vencido Java, de uma forma ou de outra. E com essa satisfação, você volta para ver o restante das aulas do dia."
    hide prolog with moveoutbottom
    show black with dissolve
    pause 1.0
    return

label fim_simples_dia10:
    "E assim mais um dia chega ao fim."
    return
    
return
