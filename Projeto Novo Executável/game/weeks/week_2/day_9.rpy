label semana2_dia9:
    call conversa_com_prolog_antes_aula from _call_conversa_com_prolog_antes_aula
    if grupoPythonRuby:
        call conversa_com_prolog_depois_aula from _call_conversa_com_prolog_depois_aula
        call casa_de_ruby from _call_casa_de_ruby
        call sala_de_estar_ruby from _call_sala_de_estar_ruby
        call evento from _call_evento
    return


label conversa_com_prolog_antes_aula:
    scene black
    show text "Dia 1" at truecenter
    play music "audio/music.mp3" volume 0.5
    scene sala 1 with dissolve
    scene sala 1 with dissolve


    "Mais uma vez, você estava na sala de aula, um pouco entediado."
    "Você repara que nem Ruby nem Python chegaram ainda, o que não é muito do feitio de nenhum dos dois."
    show prolog with moveinleft
    pro "Distraído, meu caro?"
    "Diz Prolog ao se esgueirar ao lado de sua mesa."
    mc "Ah!"
    show prolog 7
    "Você dá um grito assustado."
    mc "Você me assustou!"
    show prolog 6
    pro "Não sou uma assombração nem uma criminosa."
    show prolog 2
    pro "Não há necessidade para ficar tão arisco."
    "Disse ela antes de se virar para sua coruja novamente."
    show prolog 6
    pro "Gepeto, você já deve ter deduzido isso, mas só por garantia: [player_name] se surpreende fácil."
    "Você ainda não entende o por quê daquela garota constantemente com aquela coruja robótica, mas decide se abster de perguntar para evitar algum tipo de explicação maluco que ela provavelmente daria."
    show prolog 5
    pro "..."
    "E a garota fica ali de pé lhe encarando."
    "Algum tempo se passa..."
    "... e ela permanece lhe encarando ..."
    "..., em silêncio, ..."
    "Até que você fica desconfortável e decide perguntar."
    show prolog 7
    mc "Você quer alguma coisa?"
    show prolog 2
    pro "Não, agradeço a preocupação."
    show prolog 8
    pro "..."
    pro "..."
    show prolog 7
    mc "Então... Porque está me encarando assim?"
    show prolog 16
    pro "Análise, [player_name]."
    show prolog 2
    pro "Eu conheço a todos nessa sala, menos você."
    show prolog 16
    pro "Então estou te observando pra mudar isso."
    show prolog 2
    pro "Foi por isso que eu sabia seu nome."
    show prolog 16
    pro "Seu nome era o único do quadro que eu não reconhecia."
    show prolog 2
    pro " O fato propriamente dito de você não possuir conhecimento sobre algo é conhecimento por si só."
    show prolog 7
    mc "Isso é meio desconfortável."
    show prolog 6
    pro "Oh, mil desculpas!"
    show prolog 13
    pro "Vou começar a ser mais discreta!"
    show prolog 7
    mc "O ponto não é esse..."
    "A cortina de um profundo azure é levantada, dando espaço para que o holofote que chamamos de sol privilegiar seus escolhidos sob esse palco de mogno, queimando-os ao longo de suas performances."
    hide prolog 13 with moveoutleft
    show ada at left with moveinleft
    ada "Com lágrimas, sangue e suor, cantem e dancem, roubando o holofote um dos outros."
    "Dizia Ada que adentrara a sala e lentamente andava ao centro do quadro"
    ada "Isso é o Starlight!"
    show prolog 2 at right with moveinright
    pro "Bom dia pra senhora também, professora Ada!"
    hide prolog with moveoutright
    hide ada with moveoutleft
    "E assim, o dia foi passando..."
    scene black with dissolve
    return
    # Escurece a tela por alguns segundos pra dar a impressão de passagem de tempo.
    # Se o jogador tiver escolhido Ruby ou Python como um dos seus colegas de grupo, o dia 
    # 9 continua, caso contrário, ele acaba e vai direto para o dia 10.
    

label conversa_com_prolog_depois_aula:
    scene black
    show text "Dia 1" at truecenter
    play music "audio/music (2).mp3" volume 0.5
    scene sala 1 with dissolve
    scene sala 1 with dissolve

    show prolog 9 with moveinleft
    "No intervalo das aulas, Prolog veio até você com uma expressão preocupada."
    show prolog 6
    pro "Notícias de Python e Ruby?"
    show prolog 7
    mc "Não os vi o dia inteiro."
    show prolog 9
    pro "..."
    "Ela parecia pensativa."
    show prolog 6
    pro "Vem comigo."
    hide prolog 6 with moveoutright
    "Prolog agarra seu braço e começa a te arrastar pra fora da sala."

    scene black with dissolve
    mc "Ei, ei, ei. O que é isso?"

    scene corredor with dissolve
    show prolog 7 with moveinleft
    "Você questiona, enquanto a garota ouxa o seu braço e lhe força a andar apressadamente."
    show prolog 15
    pro "Vamos logo, não temos tempo à perder!"
    show prolog 7
    "Prolog começa a correr pelo corredor."
    "Sem entender o que está acontecendo, você decide acompanhá-la."
    mc "Você pode por favor me explicar o que estamos fazendo?"
    show prolog 6
    pro "Sala de recreação."
    show prolog 7
    mc "O que?"

    scene black with dissolve
    "Passando pela porta da dita sala, Prolog entra nela rapidamente e vai checar os registros de entrada e saída da sala."
    scene sala_recreacao with dissolve
    show prolog 18 with moveinleft
    pro "Sabia!"
    show prolog 7
    "Prolog então vai até a fonte dos desejos e põe a mão na água e de lá tira..."
    show prolog 19
    pro "Um fio elástico cortado, um balão estourado e uma argola!"
    show prolog 7
    mc "Daí já saiu coisa muito mais impressionante, não sei porque isso te chocou."
    hide prolog 7 with moveoutleft
    "Prolog começou a checar cada ar-condicionado da sala, e fechou os olhos pensativa."
    mc "O que é que você tá fazendo aqui? A gente não ia procurar Ruby e Python?"
    show prolog 21 with moveinleft
    pro "Por que eu procuraria alguém que já sei onde estão?"
    show prolog 22
    mc "?"
    show prolog 21
    pro "Eu estou apressada por outro motivo. Tenho que fazerem adiar o evento."
    show prolog 22
    mc "Você pode parar de fazer pulos de raciocínio, por favor?"
    show prolog 21
    pro "Ambos adoeceram e estão atualmente na casa de Ruby."
    show prolog 22
    mc "E como é que você sabe disso?"
    show prolog 21
    pro "Porque é a única explicação."
    show prolog 22
    pro "Eu tenho que fazer algo ainda então você poderia ir checar Python e Ruby pra mim?"
    pro "Eu não te envolveria nisso normalmente, mas como essa confusão envolve gente que tá no seu grupo pro trabalho da professora Ada, você também pode ser prejudicado."
    hide prolog with moveoutleft
    "Prolog puxa um caderno da roupa e escreve algo, arrancando a página e lhe entrega a página em seguida."
    show prolog 21 with moveinleft
    pro "O endereço é esse."
    show prolog 19
    pro "Agora, se me der licença, preciso ir pegar um projetor."
    mc "Mas e as aulas?"
    show prolog 21
    pro "Vamos faltar por um bom motivo."
    show prolog 19
    pro "Pare de incerteza e vá checar os doentes, Watson!"
    hide prolog with moveoutright
    "Prolog mais uma vez sai em disparada deixando você só."
    mc "O que acabou de acontecer?"
    scene black with dissolve
    return

    # Escurece a tela por alguns segundos pra dar a impressão de passagem de tempo.
label casa_de_ruby:
    scene black
    play music "audio/music (3).mp3" volume 0.5
    "Você chega na casa de Ruby e toca a campainha."
    scene casa_ruby with dissolve
    "Pouco tempo depois o garoto ruivo abre a porta."
    show ruby 8 with moveinleft
    "Ele parecia acabado."
    show ruby 3
    rub "[player_name], o que você está fazendo aqui?"
    show ruby 9
    rub "*cough cough*"
    show ruby 11
    rub "Não deveria estar tendo aula agora?"
    show ruby
    mc "Prolog disse que você e Python estavam doentes e pediu pra vir vê-los."
    show ruby 2
    rub "Oh, não precisava. Sério."
    show ruby 2
    "Ruby parecia um pouco culpado por deixar vocês preocupados."
    mc "Pode ficar tranquilo, amigos servem pra esse tipo de coisa."
    show ruby
    rub "...Entendi."
    show ruby 2
    "Ruby respondeu um pouco satisfeito com sua colocação."
    mc "Posso entrar?"
    show ruby 3
    rub "Claro!"
    hide ruby 3 with moveoutleft
    mc "Perdão a intromissão."
    scene black with dissolve
    return

label sala_de_estar_ruby:
    scene sala_ruby
    play music "audio/music (3).mp3" volume 0.5
    show pyth ii 48 with moveinbottom
    "Python estava deitada no sofá com o cabelo desamarrado."
    "Suas duas cobras estavam ao lado dela."
    show pyth ii 43
    pyt "Ela nota sua chegada e dá um sorrido."
    pyt "Oi, [player_name]."
    show pyth ii 49
    pyt "*cough cough cough*"
    show pyth ii 43
    pyt "Como você está?"
    show pyth ii 45
    mc "Eu que devia estar peguntando isso."
    mc "O que aconteceu com vocês 2 pra ficarem doentes ao mesmo tempo de um dia para o outro?"
    mc "Prolog me disse que isso aconteceu, mas não disso como."
    show pyth ii 46
    pyt "Ah, foi Prolog que mandou você ver a gente?"
    show pyth ii 43
    "Python deu uma leve risada."
    pyt "Então vou deixar ela te explicar depois, afinal, a detetive que soluciona o caso deve ser quem explica ele."
    show pyth ii 45 at right
    mc "Ah, Prolog também falou sobre adiar algum tipo de evento."
    show ruby 6 at left with moveinleft
    rub "Oh! É sério mesmo!?"
    show pyth ii 46
    pyt "Se foi ela que disse, com certeza é sério."
    pyt "Se ela já conseguiu adiar o ataque ao campeonato acadêmico do ano passado, ela também consegue adiar isso."
    show pyth ii 45
    mc "Vocês têm essa mania de falar as coisas como se o novato soubesse o que está acontecendo.."
    show ruby 2
    rub "Certo, desculpa..."
    show ruby
    "Lamentou Ruby cabisbaixo."
    show ruby 16
    rub "Acontece que vai haver um evento de boas vindas para os novos estudantes da Academia."
    rub "Ele normalmente é realizado pelo presidente, mas já que Java abdicou, ainda não temos um. "
    rub "Então Python se ofereceu para fazer isso e eu queria acompanhar ela nessa tarefa, mas..."
    show ruby
    show pyth ii 49
    pyt "*Cough cough*"
    show pyth ii 46
    pyt "Aconteceram... Coisas... e agora estamos assim."
    show pyth ii 45
    mc "Isso é um grande problema mesmo."
    mc "Faz sentido Prolog ir pedir para adiarem já que os 2 organizadores estão doentes, sem vocês o evento não pode acontecer."
    show ruby 2
    rub "Na verdade não."
    show ruby 16
    rub "Existe gente pra substituir a gente pra caso isso acontecesse, Prolog vai fazer isso mais por consideração mesmo."
    show ruby
    show pyth ii 47
    pyt "Mesmo assim, ainda temos alguns problemas."
    pyt "O discurso de abertura ainda não ficou pronto."
    show pyth ii 45
    mc "Se esse é o problema, então eu posso ajudar."
    mc "Vocês não deveriam fazer esforço estando doentes."
    mc "E com Prolog adiando o evento, podemos trabalhar sem pressa."
    show pyth ii 46
    pyt "É, você tem razão"
    show pyth ii 49
    pyt "*cough cough*."
    show pyth ii 43
    hide ruby with moveoutright
    pyt "Deixarei essa tarefa com você, meu querido calouro!"
    hide pyth with moveoutbottom
    show ruby at left with moveinright
    show futon at top with moveinright
    "Ruby traz um futon pra sala e deita nele."
    hide futon with moveoutbottom
    hide ruby with moveoutbottom
    "Enquanto isso, você vai à mesa com uma caneta e papel para escrever o discurso."
    mc "..."
    mc "..."
    "Você termina de escrever o papel do discurso e mostra a ruby, acreditando que fez um bom trabalho."
    show ruby 16 at center with moveinbottom
    rub "Desculpa, mas tá tangente demais."
    show ruby 2
    rub "Realmente o discurso passa a energia da Academia, mas agora parece que o lado educacional dela é inexistente."
    show ruby
    mc "..."
    "Você dá um suspiro e faz uma cara de desapontado."
    show ruby 2
    rub "Certo, vamos refazer. Afinal de contas, Prolog adiou o evento então temos tempo."
    show ruby
    "Seu telefone então toca"
    hide ruby
    scene escola with dissolve
    show prolog 6
    pro "Alô, alô."
    pro "Prolog falando."
    pro "O evento foi adiado em 2 horas, até depois."
    hide prolog with moveoutright
    scene black with dissolve
    "E então ela desliga"
    scene sala_ruby with dissolve
    mc "..."
    "Você para por um instante"
    mc "2 HORAS!?"
    mc "Do que adianta adiar só duas horas se os apresentadores tão doentes?"
    mc "Pelo menos adiasse um dia!"
    show pyth ii 46 at right with moveinbottom
    pyt "Provavelmente..."
    show pyth ii 49
    pyt "*cough cough*"
    show pyth ii 46
    pyt "... ela fez o melhor que pôde."
    hide pyth with moveoutbottom
    mc "O quão ruim estão vocês dois?"
    show ruby 2 with moveinbottom
    rub "Eu não tô tão mal."
    rub "Apenas coriza, olhos ardendo e um pouco de dor nas articulações, já Python..."
    show pyth ii 46 at right with moveinbottom
    pyt "Tá ruim até pra eu me levantar."
    hide pyth with moveoutbottom
    "Disse ela como em um gemido, enquanto Pye e Tom lançavam um olhar preocupado sob a garota."
    mc "..."
    "Você hesita por um instante."
    mc "Ruby..."
    show ruby 2
    rub "O que foi?"
    show ruby
    mc "O quanto você quer fazer aquele discurso?"
    show ruby 24
    rub "Muito!"
    show ruby 2
    rub "Por... diversos motivos..."
    show ruby
    mc "O quão longe você está disposto a ir pra fazer seu trabalho?"
    show ruby 24
    rub "Disposto a muito!"
    show pyth ii 47 at right with moveinbottom
    pyt "Por que isso, [player_name]?"
    show pyth ii 45
    mc "Culinária médica experimental."
    show pyth ii 47
    show ruby 6
    pyt "Eh?"
    rub "Eh?"
    hide pyth with moveoutbottom
    show ruby 7
    mc "Medicações unidas à chás farmacêuticos usando alho e limão, canja de galinha milagrosa que leva antialérgicos como ingredientes, analgésicos triturados e misturados a sucos de vitamina c, entre outros artifícios."
    show ruby 2
    rub "E isso vai fazer eu melhorar rápido para terminar de escrever o discurso?"
    show ruby
    mc "Talvez. Elas foram receitas ensinadas à mim por minha avó e adaptadas ao meu corpo para garantir eficácia."
    show ruby 26
    rub "Tudo bem, pode fazer! Eu não tenho nada a perder!"
    show ruby 23
    mc "Tem sim."
    show ruby 28
    rub "?"
    show ruby 2
    mc "Se chama experimental por um motivo."
    mc "Na pior das hipóteses você pode ir parar no hospital por infecção intestinal."
    show ruby 6
    rub "Ehhhhhh!?"
    show pyth ii 52 at right with moveinbottom
    pyt "E você sugerindo uma medida dessas?!"
    "Python perguntou surpreendida."
    show pyth ii 43
    pyt "Enfim está se tornando um estudante da Academia Sem Nome Definido!"
    hide pyth with moveoutbottom
    "Você pega papel e começa a escrever uma lista."
    mc "Limão, alho, medicamentos analgésicos de diferentes marcas, laranja, acerola, peito de frango, vitamina c efervescente, antialérgicos e a lista continua. Após termina-la, você a entrega a Ruby e o questiona:"
    mc "Tem alergia a algo daqui?"
    mc "Por mais desnecessário que pareça questionar coisas como “você  é  alérgico  a  frango?” isso ̴é super  importante  para  evitar  a ocorrência de um choque anafilático inesperado."
    show ruby 7
    rub "Ãn? N-não, não tenho."
    show ruby 2
    "Diz ̴Ruby nitidamente preocupado ao ver que “itens para bebida” incluía alho e ̴arroz."
    "Aos poucos a determinação que o garoto havia mostrado minutos atrás estava escorrendo por entre seus dedos enquanto ouvia quantos riscos estavam envolvidos nessa bomba caseira diferenciada de [player_name]."
    hide ruby with moveoutbottom
    mc "Muito bem, nenhum de vocês se levanta até eu voltar."
    mc "Temos 2 horas, serei rápido nas compras e cozinhar tudo demorará uma meia hora dependendo do tamanho da sua cozinha."
    mc "Assim, com 40 minutos tudo estará pronto."
    show pyth ii 47 at right with moveoutbottom
    pyt "E quanto a mim aqui? Algum remédio milagroso ensinado por sua avó?."
    show pyth ii 45
    mc "Pra você a resposta é outra, mas depois falamos sobre."
    mc "Vou indo e já volto, enquanto isso, vão dormir."
    hide pyth with moveoutbottom
    scene black with dissolve
    "Você falou antes de sair da casa, disposto a por em pratica suas habilidades provenientes do fato de você não ter dinheiro para pagar um plano de saúde."
    scene casa_de_ruby with dissolve
    "Você nunca imaginou que as coisas malucas que você fazia com um fogão, um liquidificador e um furador de coco seriam capazes de ajudar outra pessoa."
    scene sala_de_estar_ruby with dissolve
    show pyth ii 45 at right with moveinbottom
    show ruby with moveinbottom
    "Após fazer as compras, você volta para a casa de Ruby e encontra o mesmo e Python ainda deitados."
    hide pyth with moveoutbottom
    hide ruby with moveoutbottom
    "“Ótimo”, você pensa antes de se dirigir a cozinha."
    scene black with dissolve
    scene cozinha_ruby with dissolve
    mc "Muito bem, tá na hora de trabalhar."
    "Você tira das sacolas as compras e pega os itens necessários para o inicio de seu projeto de transmutação alquimica que carinhosamente apelidou de Culinaria Esperimental Medicinal." 
    "CEM, para os mais próximos"
    mc "Cem dores, cem ganhos."
    "E agora começa a parte difícil: adaptar a receita."
    "Ao longo do processo de lapidação dessa habilidade, você acabou passando mal diversas vezes."
    "Ao longo do tempo, você foi conhecendo melhor seu corpo, podendo criar a melhor receita com os efeitos colaterais menos danosos."
    "Mas agora é diferente: você tá fazendo aquilo pra outra pessoa, pra um corpo que não é o seu."
    "Para isso, um processo de análise sobre a pessoa é necessário com o intuito de não mandar ela para o hospital."
    scene emptydnd with dissolve
    # Começo do tutorial do puzzle de drag and drop
    "Por vezes, você encontrará situações nas quais é necessária uma análise sobre o interior de uma pessoa."
    "Nesse tipo de situação será iniciado um mini-game no qual você deve arrastar pedaços de código e organizá-los para formar um algoritmo."
    "Ao acertar o espaço de um trecho do código, o mesmo se fixará no local e, quando todas as lacunas forem preenchidas, o mini-game terá sido concluído."
    "Não se preocupe, a história só continua após o algoritmo ser formado, no então, não há um limite de tempo nem penalidade por errar a ordem, então vá em seu próximo ritmo." 
    # Fim do tutorial.
    # Aqui é inserido o minigame de drag and drop de Ruby, e, após ele ser concluído, a história continua.
    stop music
    $setup_ruby_bs_puzzle()
    call screen ruby_bs_puzzle    

label ruby_bs_complete:
    scene cozinha_ruby with dissolve
    play music "audio/music (3).mp3" volume 0.5
    "Enfim a análise foi concluída."
    "Sim, uma obra prima que une estatísticas, química e biologia."
    "Uma receita capaz de ajudar a curar aquela doença de Ruby, e exclusivamente aquela doença de Ruby."
    "Se dado à qualquer outra pessoa, poderiam haver consequências imprevisíveis."
    "Com a receita em mãos você começa a travar uma guerra dentro daquela cozinha."
    # Escurece a tela por alguns segundos pra dar a impressão de passagem de tempo.
    mc "Finalmente."
    mc "Finalmente está pronto."
    mc "O preparo inteiro demorou mais que o planejado, mas tudo bem, ainda faltava 1 hora e 10 minutos pro evento."

    scene sala_de_estar_ruby with dissolve
    "Você então vai até Ruby e delicadamente o acorda, evitando assustá-lo."
    mc "Ruby, tá aqui a comida."
    show ruby with moveinbottom
    mc "Eu preciso que você consuma da seguinte forma: primeiro coma esse pão, depois a canja de galinha e só aí o chá."
    show ruby 2
    rub "Certo."
    show ruby 8
    rub "Ruby estava surpreso, ele esperava algo com aparência muito pior, mas aquilo parecia só comida normal que você daria pra alguém que está doente. Ele come o pão, normal."
    show ruby
    "Ruby começa a achar que estava preocupado por nada e fica mais tran-"
    show ruby 8
    mc "Agora me escute Ruby: não importa se você achar que tem algo errado com essa canja de galinha, ela é só uma canja de galinha."
    mc "Não pare de toma-la até acabar a tigela."
    show ruby 13
    rub "C-c-c-certo..."
    show ruby 8
    "Ruby estava aterrorizado."
    show ruby 20
    "Ele pegou a colher, sua mão tremia, até que enfim a canja entrou em sua boca."
    show ruby 8
    "Algo estava errado."
    "Algo estava definitivamente errado, aquilo tinha um sabor diferente do que deveria ter."
    show ruby 14
    rub "Era doce- não..."
    rub "Era doce- não..."
    show ruby 7
    "Agora que Ruby percebeu, na verdade era salgado. A canja estava muito fria, parecia até ter saído do frezer- não, ela na verdade estava quente."
    show ruby 9
    "Quente, quase pelando. A consistência era viscos- não, era liquida. Tão líquida que descia por sua garganta como água."
    show ruby 13
    rub  "O que era aquilo? Aquele prato diabólico de características amórficas. Qual o sabor? Qual a textura? Qual o cheiro? Qual a cor? Qual o prato?"
    rub "Quem sou eu?"
    rub "Por que estou comendo isso?"
    rub "O que é isso? O que é isso? Oqueéissoqueéissoqueéissoqueéissoqueéissoqueéissoqueéissooqueéissoqueéissoqueéissooqueéissoqueéissoqueéissooqueéissoqueéissoqueéissooqueéissoqueéissoqueéissooqueéissoqueéissoqueéisso...!"
    rub  "O que era aquilo? Aquele prato diabólico de características amórficas. Qual o sabor? Qual a textura? Qual o cheiro? Qual a cor? Qual o prato?"
    rub "Quem sou eu?"
    rub "Por que estou comendo isso?"
    rub "O que é isso? O que é isso? Oqueéissoqueéissoqueéissoqueéissoqueéissoqueéissoqueéissooqueéissoqueéissoqueéissooqueéissoqueéissoqueéissooqueéissoqueéissoqueéissooqueéissoqueéissoqueéissooqueéissoqueéissoqueéisso...!"
    mc "Ruby!"
    show ruby 8
    "Você gritou, tirando-o do transe."
    mc "Não há nada de errado com a canja de galinha."
    mc "Apenas coma tudo."
    show ruby 7
    "Ruby estava soando frio."
    "Talvez ele tivesse cometido o pior erro de sua vida, mas era tarde demais."
    show ruby 9
    "Ele comeu uma colherada. E mais uma colherada. E mais uma colherada. E mais uma colherada. E mais uma colherada..."
    mc "Ruby, acabou."
    "Você disse enquanto o garoto tentava pegar uma canja que já não mais existia na tigela."
    show ruby 8
    "A névoa que cobria a mente do garoto começou a se dissipar, e nesse momento ele recobrou a consciência desesperado."
    show ruby 6
    rub "O-o-o-o-o-o-o-o que é essa canja amaldiçoada!?"
    show ruby 7
    mc "Tá tudo bem, já acabou. Agora só falta o chá."
    show ruby 9
    rub "Não! Não! Não quero mais saber disso!"
    show ruby 8
    mc "Ruby, falta uma hora pro evento. Se não terminar o processo da refeição, tudo terá sido inútil e você não conseguirá ficar num estado adequado para fazer o discurso."
    show ruby 9
    rub "... Droga."
    show ruby 8
    mc "Só falta o chá e você deve toma-lo numa única golada, caso contrario será pior."
    mc "Ele já está frio o bastante."
    show ruby 7
    "O garoto olha para o chá preocupado."
    show ruby 2
    rub "Depois disso acabou?"
    show ruby
    mc "Acabou."
    show ruby 2
    rub "Eu vou chegar a tempo no evento?"
    show ruby
    mc "Vai."
    show ruby 2
    rub "Ok, então."
    show ruby
    "Num ato de coragem, Ruby segura a alça da xicara e a aproxima da boca."
    "Não havia cheiro algum emanando do chá, o que causou uma enorme estranheza no garoto."
    "Seus ancestrais japoneses gritavam da cova: aquele será pior que o anterior e a falta de cheiro é prova de que o chá está tentando ocultar sua verdadeira essência."
    show ruby 8
    "E então a golada. Assim que ocorreu, Ruby percebeu que tinha razão."
    "Este não era como o anterior. É como se a Guerra da Cisplatina tivesse sido transformada em uma bebida."
    "O instinto natural foi cuspir, mas Ruby aguentou."
    "A medida que o chá se espalhava por sua boca, Ruby começava a sentir como se fosse parte da guerra."
    "Uma hora como pai que foi arrancado da família para segurar uma arma."
    "Uma hora como um desertor que precisa viver como vergonha da sociedade."
    "Uma hora como o próprio terreno, banhado por sangue de pessoas que choram por suas famílias e amigos."
    "O horror era incomparável."
    "Diferente do prato anterior que era a junção de antíteses de uma natureza incompreensível ao ser humano, aquele era..."
    show ruby 2
    rub "Um terror puramente humano"
    "Disse Ruby enquanto caia no Futon novamente."
    hide ruby with moveoutbottom
    "Ruby desmaiou."
    show pyth ii 52 at right with moveinbottom
    pyt "Você acabou de desmaiar o garoto!"
    show pyth ii 49
    pyt "Por que diabos você fez isso???????"
    hide pyth with moveoutbottom
    mc "Tratamento concluído. Ele tem 50 minutos de descanso."
    scene black with dissolve
    "Oh, eu espero MUITO que você tenha tenha frequentado as atividades do clube “How to get away with the murder (not the show)”."
    # Escurece a tela por alguns segundos pra dar a impressão de passagem de tempo
    scene sala_de_estar_ruby with dissolve
    "Ruby enfim acorda depois do seu tratamento duvidoso."
    show ruby 6 with moveinbottom
    rub "Eu estou vivo!?"
    mc "Sim, você está vivo. Não só isso. Se levanta."
    "Ruby então se levanta do futon e percebe algo."
    show ruby 21
    rub "Eu tô bem!?"
    show ruby 7
    mc "Sim, você está bem."
    mc "A receita foi um sucesso, e a cura é a recompensa por aguentar o processo infernal."
    "Ruby estava embasbacado com aquilo."
    "Ele estava sem conseguir olhar para uma luz sem que seus olhos lacrimejassem e agora todo resquício da doença havia sumido!"
    show ruby 6
    rub "Como você fez isso!?"
    show ruby 7
    mc "Não posso revelar o método."
    show ruby
    mc "Pessoas poderiam tentar imitar sem ter a capacidade disso e alguém provavelmente seria mandado para a UTI."
    show ruby 2
    rub "E-entendi."
    rub "Me desculpa duvidar de você."
    show ruby
    mc "Não se preocupa, qualquer um duvidaria desse tipo de coisa."
    mc "Além disso, foi uma aposta de risco alto que poderia te deixar ainda pior, só usei porque se não não daria tempo de você participar do evento."
    mc "O melhor sempre é deixar seu corpo curar por meios convencionais."
    "Com todo o barulho feito, Python também acorda."
    show pyth ii 49 at right with moveinbottom
    pyt "*Cough cough*"
    show pyth ii 47
    pyt "Quanto tempo ainda falta pro evento?"
    show pyth ii 48
    mc "Dez minutos."
    show pyth ii 52
    pyt "Dez minutos!?"
    show pyth ii 49
    pyt "Mas não vai dar tempo de escrever o discurso!"
    show pyth ii 48
    mc "Não, não vai. Você vai ter que fazer isso sem um roteiro."
    show pyth ii 47
    pyt "Não..."
    show pyth ii 49
    pyt "*cough cough*"
    show pyth ii 47
    pyt "... se preocupe..."
    show pyth ii 49
    pyt "*cough cough cough*"
    show pyth ii 47
    pyt "Ruby."
    show pyth ii 43
    pyt "Eu vou estar com você pra lhe ajudar."
    show pyth ii 44
    pyt "E aí [player_name], qual a ideia que você disse que tinha pra eu me curar?"
    show pyth ii 45
    mc "É bem simples: tome muita água e repouse. Evite esforço e se alimente bem."
    show pyth ii 47
    pyt "E é?"
    show pyth ii 46
    pyt "Mas como isso vai me curar até o evento?"
    show pyth 45
    mc "Não vai."
    show pyth ii 47
    show ruby 6
    pyt "O queeeeee!?"
    "Ruby e Python perguntaram juntos, surpresos."
    show pyth ii 45
    show ruby
    mc "A receita não pode ser compartilhada entre pessoas diferentes e só dava tempo de preparar uma única refeição."
    mc "A situação de Ruby era melhor, então havia mais chances dele melhorar a tempo."
    mc "E você não merece passar por aquela refeição amaldiçoada com uma probabilidade tão alta de ser inútil."
    show ruby 32
    rub "É! Você não quer aquilo, acredita em mim!"
    "Ruby disse isso, enquanto estremecia."
    show ruby 29
    show pyth ii 47
    pyt "Então você nunca planejou me deixar ir ao evento, não é?"
    show pyth ii 45
    mc "Isso mesmo."
    show pyth ii 52
    pyt "Você tá fazendo pouco de mim se acha que uma doença assim é o bastante pra me impedir de ajudar um amigo..."
    "Pye e Tom começam a subir pelo sofá e se entrelaçam cada uma em um dos braços da garota."
    mc "Ei, o que você tá fazendo?"
    "Você questiona confuso pela cena e de repente..."
    # Tem um sprite especifico pra isso (Python 53), a partir daqui é ele que deve ser usado para Python
    show pyth ii 51
    pyt "Guh!"
    "garota solta um gemido de dor quando suas cobras mordem seu pescoço e se fixam nele."
    show pyth ii 53
    mc "O que é isso!?"
    show ruby 21
    rub "Pye, Tom, soltem ela agora!"
    show ruby 15
    pyt "N-não, tão tudo bem, essa minha técnica especial: “Marionete de Peçonha”!"
    show ruby 21
    rub "Isso não é um battle shonen pra você fazer esse tipo de coisa!"
    rub "Para, se não você pode se machucar!"
    show ruby 15
    "Ruby ordena mais uma vez muito preocupado."
    pyt "Está tudo bem."
    "Afirma Python mais uma vez enquanto se levanta do sofá."
    pyt "Assim Tom e Pye podem mover meus braços e o veneno de dois serve como anestesia, permitindo que meu corpo se mova sem que eu sinta dor. Dessa forma eu vou poder subir com você no palco, Ruby."
    pyt "Ah, mas você terá que me levar até lá, eu não consigo mover minhas pernas sozinha."
    show ruby 32
    rub "Isso é só mais um motivo pra você não ir!"
    show ruby 29
    "Aquilo é uma péssima ideia, pode parecer hipocrisia vindo de você considerando sua técnica de CEM, mas um cuidado paliativo tão absurdo não pode fazer bem ao corpo."
    show ruby 21
    rub "Ela pode de fato não estar sentido a dor agora por causa do veneno, mas uma hora que isso passar, seu corpo vai desabar de dor."
    rub "Você precisa impedir ela de usar essa Beserk Armor Reptiliana antes que haja consequências graves, mas usar a segurança dela não vai convencê-la; estava claro que Python é o tipo de pessoa que se machuca para ajudar os outros."
    hide pyth with moveoutbottom
    hide ruby with moveoutbottom
    scene emptydnd with dissolve
    "Mais uma vez, você via como necessária uma análise."
    "Vamos, entenda aquela garota e descubra seus pontos fracos para criar um argumento que irá convencê-la!"
    # Aqui é inserido o minigame de drag and drop de Python, e, após ele ser concluído, a história continua.
    stop music
    $setup_python_bs_puzzle()
    call screen python_bs_puzzle

label python_bs_complete:
    scene sala_de_estar_ruby with dissolve
    play music "audio/music (3).mp3" volume 0.5
    show pyth ii 53 at right
    show ruby 7
    mc "Python, nesse exato momento você está assustadora."
    mc "Aparecer assim para os novatos não vai passar sua imagem calorosa de sempre; eles não se sentirão acolhidos, mas sim aterrorizados!"
    pyt "Mesmo assim eu não posso abandonar Ruby..."
    mc "Confie no seu amigo. Mesmo que as condições estejam desfavoráveis, ele será capaz de superar elas. Ruby tem muita determinação, e o fato de que ele completou o tratamento da minha técnica CEM prova isso."
    pyt "Você tem certeza que consegue, Ruby? – questionou garota."
    show ruby 20
    rub "Sim, mesmo que não tenha um discurso prévio, eu consigo!"
    "Afirmou Ruby como quem quer convencer a si mesmo."
    pyt "... – Python permanece quieta por um tempo."
    # A partir daqui volta pros sprites de Python com cabelo solto.
    show pyth ii 49
    pyt "Tudo bem..."
    "Diz a garota, desanimada."
    show pyth ii 47
    pyt "Desculpe por não poder ajudar."
    show pyth ii 48
    show ruby 25
    rub "Isso não é verdade."
    show ruby 26
    rub "Ver você se esforçando tanto assim me deixa ainda mais decidido."
    show ruby 23
    mc "Isso tudo é muito legal, mas a gente precisa ir rápido pro evento Ruby."
    show ruby 24
    rub "Verdade! Até mais Python, se cuida, tá?"
    hide ruby with moveoutright
    show pyth ii 47
    pyt "Claro."
    hide pyth with moveoutbottom
    scene black with dissolve
    "E assim lá fomos nós."
    return

label evento:
    scene auditorio with dissolve
    play music "audio/music (2).mp3" volume 0.5
    "O evento aconteceria num local dentro da Academia e Ruby me indicou o caminho."
    "Quando chegamos lá, faltava pouco pra ele precisar entrar em cena."
    show ruby with moveinleft
    mc "Nervoso?"
    show ruby 2
    rub "Um pouco... Mas agora não é hora pra isso."
    show ruby
    mc "Vai lá, você consegue."
    "Você disse dando um tapinha nas costas dele."
    rub "Obrigado."
    hide ruby with moveoutleft
    scene black with dissolve
    # Escurece a tela
    "Você decide ficar pra ver como as coisas vão se suceder e percebe que assim que ele começa a falar, toda o nervosismo de Ruby pareceu sumir."
    "Não só isso, na verdade você se surpreende com o garoto; ele passava uma impressão confiante e responsável, grandioso de certa forma."
    "Você enfim entendeu o que ele e Python queriam no discurso: algo que fizesse você pensar ̴“caramba, ̴ainda bem que ̴eu ̴estou ̴aqui”."
    "Certamente ̴era uma impressão diferente da de Python, mas sinceramente, talvez aquela fosse a impressão perfeita"
    scene auditorio with dissolve
    # Desescurece a tela
    "O evento enfim acaba e Ruby vem até você."
    show ruby with moveinleft
    mc "Parece que deu tudo certo com o evento, você foi incrível."
    show ruby 3
    rub "Muito obrigado, mas isso foi graças a você."
    show ruby 5
    rub "O primeiro agradecimento foi por cordialidade, mas esse leva meus sinceros sentimentos: muito obrigado mesmo!"
    show ruby
    "Alguns estudantes parecem se aproximar de Ruby para perguntar coisas."
    hide ruby with moveoutright
    "Você acha melhor deixar ele continuar sobre holofotes, então decide ir embora pra não atrapalhar."
    mc "Ah, é verdade. Minhas coisas ainda estão na sala."
    scene black with dissolve
    "A essa altura você já havia perdido todo o resto das aulas, mas valeu a pena."
    scene sala 1 with dissolve
    "Você caminha até a sala para pegar suas coisas, entra nela e começa a se organizar."
    scene sala_janela with dissolve 
    "Nesse momento, uma brisa entra pela janela, fazendo você instintivamente olhar para ela."
    scene sala 1 with dissolve
    "Ao retornar seu olhar para suas coisas, você percebe que..."
    mc "Sumiram!"
    show prolog with moveinright
    pro "Sacrebleu! Quem poderia ter feito algo do tipo?"
    show prolog 5
    "Questionou Prolog de forma cínica enquanto segurava suas coisas em mãos."
    mc "Desde quando você está aqui?"
    show prolog 19
    pro "Eu disse que seria mais discreta ao te observar."
    show prolog 5
    "A garota devolve a você suas coisas e continua."
    show prolog 6
    mc "Ruby adoeceu?"
    show prolog 7
    pro "Adoeceu."
    show prolog 3
    pro "Impressionante! Não faço ideia de como ele fez pra ficar de pé no evento."
    show prolog 4
    pro "Aposto que tem dedo seu nisso daí."
    show prolog 5
    mc "Você também assistiu?"
    show prolog 3
    pro "Claro que assisti, mas isso são outros quinhentos."
    show prolog
    pro "E então, o que você fez?"
    show prolog 7
    mc "Opa, opa, opa. Você não acha que tem que me responder algumas coisas primeiro?"
    show prolog
    pro "Hehe, acho que te devo isso, não é, meu caro assistente?"
    show prolog 7
    mc "Eu não sou seu- Quer saber, deixa pra lá."
    mc "Vamos começar de forma cronológica:" 
    mc "Por que você foi correndo para a sala de recreação naquela hora?"
    show prolog 6
    pro "Você se lembra da reunião de ontem sobre o projeto?"
    pro "Alguém disse que iria para sala de recreação no hoje."
    show prolog 7
    mc "Lembro disso, mas não foram porque estavam doentes."
    pro "Você está vendo as coisas da forma errada, [player_name]."
    show prolog 6
    pro "De fato, eles não foram hoje porque adoeceram, mas eles adoeceram porque foram para a sala de recreação."
    show prolog 7
    mc "Do que você tá falando?"
    show prolog 19
    pro "Elementar, [player_name]."
    show prolog 20
    pro "Os eventos de hoje foram uma arapuca criada para prejudicar Python e Ruby."
    show prolog 7
    mc "Mas como seria possível alguém fazer eles adoecerem assim?"
    show prolog 21
    pro "A resposta está na sala de recreação, ela foi manipulada para causar isso."
    show prolog 23
    pro "O culpado provavelmente ouviu a reunião do nosso grupo e sabia que seu alvo iria para a sala de recreação no dia seguinte, então ele preparou uma armadilha."
    show prolog 20
    pro "Com isso em mente, me diga [player_name]-san:"
    show prolog 21
    pro "Por que o culpado fez isso?"
    mc "Para impedir Ruby e Python de virem ao evento."
    show prolog 19
    pro "Bingo!"
    show prolog 20
    pro "Mesmo que ele soubesse que os dois iriam pra sala, não havia como garantir que eles iriam ao mesmo tempo."
    show prolog 7
    mc "Então a armadilha, seja lá qual foi só atingiria um deles."
    show prolog 27
    pro "Non! Um erro amador [player_name]."
    show prolog 21
    pro "Eles iriam juntos pra sala, pois o que eles iam fazer lá envolvia ambos."
    show prolog 7
    "Você começa a se perguntar sobre o que ela estava dizendo."
    "Então, uma lembrança cruza sua mente."
    "Em pensamento, você pondera..."
    "O que é que Python e Ruby precisavam fazer para o evento hoje pela manhã que ainda não estava pronto quando você foi à casa de Ruby?"
    mc "Preparar o discurso!"
    show prolog 17
    pro "Magnifique!"
    show prolog 21
    pro "Isso mesmo, Python e Ruby iriam terminar os preparos para o discurso do evento que aconteceria logo em seguida."
    pro "Mas ainda temos alguns problemas: Ruby e Python não pisaram naquela sala hoje e ainda assim adoeceram."
    pro "Além disso, você fica falando que o culpado fez uma armadilha, mas não explica que armadilha foi essa."
    show prolog 6
    pro "Vamos por partes."
    pro "Quem é culpado, [player_name]?"
    show prolog 7
    mc "Você pulou todas as partes do início e foi direto pra conclusão!"
    show prolog
    pro "Claro!"
    show prolog 2
    pro "Porque você já não é capaz de descobrir quem é?"
    show prolog 3
    pro "Assim como eu descobri o culpado antes mesmo de sair para fora da sala de aula hoje de manhã."
    show prolog 25
    pro "Pense, o que aconteceria se Ruby e Python não pudessem comparecer ao evento?"
    pro "Ele seria cancelado?"
    show prolog 29
    mc "Não, pois haveria um substit- !"
    "Você para por um segundo ao entender o que a garota queria dizer."
    show prolog 26
    pro "Parece que você já percebeu."
    show prolog 25
    pro "O culpado precisava ser alguém que soubesse que Python e Ruby seriam os responsáveis para o evento."
    show prolog 26
    pro "Além disso, precisava ser alguém que ganharia algo com caso os dois não aparecessem no evento."
    show prolog 21
    pro "Então foi o substituto dos dois que fez isso, mas quem ele é?"
    pro "Eu tinha um palpite, mas a certeza só veio após ver os últimos 6 registros de entrada e saída da sala de recreação ontem."
    show prolog 22
    "Prolog lhe entregou um papel com nomes em uma ordem específica: Swift, Ruby, Python, Swift, Python e Ruby."
    "Duas das 3 pessoas foram, as vítimas o que só deixava um nome como possível culpado: "
    mc "Swift"
    show prolog 19
    pro "Bingo."
    show prolog 21
    pro "Você talvez não saiba, mas Swift se candidatará para o cargo de presidente que foi desocupado por Java e muito provavelmente Ruby fará o mesmo."
    show prolog 23
    pro "O evento de hoje era uma ótima oportunidade para cair no gosto dos novatos e conseguir mais votos."
    show prolog 21
    pro "Ruby provavelmente nem pensou nisso, mas Swift com certeza via isso como uma chance de ouro."
    show prolog 22
    mc "Como diabos você sabia disso antes de chegar na sala de recreação?"
    show prolog 21
    pro "Python pode parecer uma cabeça de vento às vezes, mas sempre está presente nas aulas."
    show prolog 22
    pro "Ruby é um estudante exemplar. Os dois desaparecem, justamente no dia do evento pelo qual estavam responsáveis."
    show prolog 21
    pro "Isso tinha que estar relacionado."
    show prolog 22
    pro "Eles não estariam matando aula para organizar as coisas, então alguém devia estar envolvido."
    show prolog 21
    pro "O evento seria uma boas vindas para os novatos, o culpado precisava ganhar algo com a falta de Ruby e Python."
    show prolog 22
    mc "Se os organizadores faltam, o substituto entra."
    mc "O que o substituto teria a ganhar com a apresentação?"
    mc "Reconhecimento."
    mc "Apenas por ego?"
    mc "Não, deve ter outra coisa."
    show prolog 21
    pro "Votos."
    show prolog 22
    pro "Quem é que vai se candidatar e usaria técnicas baixas para conseguir?"
    show prolog 21
    pro "Swift."
    show prolog 22
    pro "E foi assim que eu descobri o culpado."
    "Impressionante. Aquela sucessão de deduções fazia sentido, mas é surpreendente que ela conseguisse fazer isso em tão pouco tempo."
    "Mas você sentia que havia algo de errado."
    "O registro de entrada e saída da sala é de ontem."
    "Isso significa que a armadilha foi armada e ativada ontem."
    "Swift sabia que Python e Ruby iriam para a sala no dia do evento, mas como ele sabia que eles também iriam no dia anterior?"
    show prolog 21
    pro "Ele não sabia."
    show prolog 22
    mc "O que?"
    show prolog 21
    pro "Como eu disse, ele não sabia. Provavelmente foi uma grande coincidência pro azar dele."
    show prolog 22
    pro "E o motivo é..."
    show prolog 21
    pro "Qual a ordem de entrada e saída da sala?"
    show prolog 22
    mc "Swift entra, e um tempo depois vêm Ruby e Python. Daí Swift sai, e então saem depois Ruby e Python."
    show prolog 21
    pro "Com isso em mente, me diga: quando a armadilha foi armada?"
    show prolog 22
    mc "...!"
    show prolog 21
    pro "Quando Ruby e Python entraram, Swift ainda não havia terminado a armadilha."
    show prolog 22
    pro "Não há outro motivo pra ele ainda estar na sala."
    show prolog 21
    pro "Mas se ele fosse embora, Ruby e Python provavelmente notariam a armadilha sendo preparada e a desarmariam."
    show prolog 22
    mc "Então significa que essa armadilha precisava ter sido terminada e ativada ontem mesmo!"
    show prolog 26
    pro "Exactement!"
    show prolog 21
    pro "Swift provavelmente terminou a armadilha sorrateiramente pouco depois dos dois chegarem e fugiu de lá sem que eles percebessem."
    pro "Ao sair da sala, ele ativou a armadilha."
    show prolog 22
    mc "Mas no fim das contas, o que era a armadilha?"
    show prolog 21
    pro "Essencialmente era bem simples, tudo que ele usou foram TOKENS, um fio elástico, um balão, uma argola, a fonte e o ar condicionado."
    show prolog 22
    mc "Não foram essas coisas que você encontrou na fonte?"
    show prolog 21
    pro "Tirando o ar condicionado e os TOKENS, sim."
    show prolog 22
    pro "Swift pôs TOKENS dentro do balão e o amarrou na argola."
    show prolog 21
    pro "Por dentro da argola ele passou um elástico, cuja uma das pontas foi presa na fonte e outra nas pás do ar condicionado desligado."
    show prolog 22
    pro "A argola com o balão também foi presa usando as pás do ar condicionado, dessa forma, quando o ar condicionado fosse ligado, a argola deslizaria pelo fio como numa tirolesa, fazendo o balão acertar a fonte e estourar."
    show prolog 21
    pro "Quando o balão estourasse, TOKENS caíram na fonte, e assim, o gacha foi ativado, molhando Python e Ruby que estavam na sala."
    pro "O ar condicionado esfriou a sala e os dois, que estavam molhados, acabaram adoecendo por causa disso."
    show prolog 22
    mc "Mas então Ruby e Python poderiam evitar de adoecer se abrissem as janelas para esquentar a sala, desligar o ar condicionado ou simplesmente sair da sala."
    show prolog 21
    pro "Eles não podiam desligar o ar, porque Swift quebrou o botão de desligar manual deles."
    show prolog 22
    pro "Confirmei isso quando fomos para a sala de recreação."
    show prolog 21
    pro "Além disso, as janelas têm um mecanismo para reduzir o gasto de energia: se o ar estiver ligado, elas não podem ser abertas."
    show prolog 22
    pro "O último ponto que você citou é fácil de explicar: Swift tinha a chave pra trancar a sala, afinal, essa era a única maneira de garantir que ninguém entraria na sala antes de Python e Ruby e acabaria estragando a armadilha."
    show prolog 21
    pro "Ele talvez tenha pegado a chave com o diretor no dia ou tenha conseguido ela há tempo atrás, não importa."
    show prolog 22
    pro "O que importa é que assim Swift poderia trancar as duas vítimas ensopadas dentro da sala fria, o que fez elas adoecerem."
    show prolog 21
    pro "Provavelmente eles conseguiram eventualmente falar com alguém fora da sala pra pegar outra chave com Alan Turing para abrir a sala, mas, até lá, o estrago já havia sido feito."
    show prolog 22
    mc "Faz sentido."
    "Isso explica as coisas estranhas que vimos na sala e a situação de Ruby e Python."
    "Swift também conseguiria ativar a armadilha depois de sair da sala caso ele levasse o controle do ar condicionado."
    mc "Mesmo assim, ir tão baixo apenas por causa de um evento pra ganhar votos é absurdo!"
    mc "É claro que o evento seria adiado quando o diretor soubesse disso."
    show prolog 21
    pro "Na verdade não."
    show prolog 22
    pro "Eu nem mesmo comuniquei a ele isso."
    show prolog 21
    mc "Ué, por que não?"
    show prolog 22
    pro "Suborno."
    mc "Ah..."
    "Você relembra os eventos de sua primeira semana."
    pro "É, você consegue ver como Swift poderia se safar com um pouco de dinheiro."
    mc "Então como é que você fez com que adiassem o evento?"
    show prolog 21
    pro "Vandalismo."
    show prolog 22
    mc "???????"
    show prolog 21
    pro "Pedi a ajuda de Lua para criar uma distração e tirar todos do local utilizando o alarme de incêndio e o Gepeto."
    show prolog 22
    pro "Aproveitando que todos saíram do local, eu baguncei todo o local e escondi parte da decoração dele, então, eles não tiveram outra escolha a não ser postergar o início do evento."
    mc "Mas isso não vai por você e Lua em problemas?"
    show prolog 21
    pro "Não sou descuidada a ponto de ser descoberta por algo tão trivial."
    show prolog 22
    "Aquela garota podia ser meio estranha, mas visto o que ela fez hoje, também era extremamente confiável."
    "Os elogios de seus colegas de grupo faziam total sentido."
    mc "No fim das contas, você de fato é tudo isso que as pessoas dizem não é?"
    show prolog 26
    pro "Non! Sou apenas Prolog, uma estudante da Academia-Sem-Nome-Definido! – Disse ela com um sorriso no rosto."
    "A esse ponto você não sabia se aquilo era modéstia ou só uma piada, mas decidiu não ficar mais batendo nessa tecla."
    mc "Muito obrigado pela ajuda, mas agora se me der licença, vou ind-"
    show prolog 28
    pro "Espere um segundo! Você ainda não respondeu minha pergunta."
    show prolog 7
    mc "Que pergunta?"
    show prolog 6
    pro "O que você fez para Ruby conseguir vir apresentar o evento?"
    show prolog 7
    mc "Ah..."
    mc "Você provavelmente consegue deduzir, não?"
    show prolog 6
    pro "Em parte."
    show prolog 7
    pro "Imagino que tenha sido algum tipo de tratamento paliativo alternativo usando conhecimento popular, mas não consigo apontar exatamente qual."
    mc "Talvez seja melhor assim."
    show prolog 6
    pro "Por que?"
    show prolog 7
    mc "Você provavelmente tentaria deduzir o processo usado no tratamento, e eu não posso deixar isso acontecer."
    show prolog 15
    pro "Que monopólio medicinal é esse seu, hein?"
    show prolog 6
    pro "Achei que tínhamos nos tornado companheiros."
    show prolog 7
    mc "Em resumo, foi Culinária Experimental Medicinal, CEM, pra encurtar."
    mc "Não posso falar mais, já que isso poderia ter mandado Ruby pra o hospital devido a um choque anafilático."
    show prolog 6
    pro "O que diabos você fez com aquele garoto?"
    show prolog 10
    mc "Pergunte a ele e terá a experiência do paciente."
    mc "Se eu falar da minha você vai acabar tentando imitar isso em algum momento e não quero ser o cara que te ensinou a mandar alguém para 7 palmos abaixo da terra."
    mc "E agora, me despeço novamente."
    show prolog 17
    pro "... Certo. Até mais, [player_name]!"
    hide pro with moveoutright
    pro "Foi divertido trabalhar com você."
    mc "Você não sabe se divertido era a palavra certa, mas de fato no fim das contas, trabalhar com a jovem detetive não foi algo ruim."
    mc "Você consegue ver o porque dos estudantes serem tão grato a ela, de repente todas as histórias absurdas sobre ela parecem ter embasamento."
    scene black with dissolve
    
    # -------------------------------------------------------------------------------------
    scene rua_qualquer with dissolve
    "Você volta para casa e no meio do caminho percebe que esqueceu de perguntar algo."
    mc "Ah, esqueci de perguntar sobre como ela sabia que Python está na casa de Ruby."
    "Minutos depois, seu celular toca. Ao atender, você escuta uma garota nele, quase que cantarolando as palavras que dizia."
    pro "Alô, alô, Doutor. Doutor Daminh-"
    mc "O que você quer, Prolog?"
    
    scene casa_prolog with dissolve
    show prolog 6
    pro "Que frieza! Eu vim responder sua pergunta."
    hide prolog
    
    scene rua_qualquer with dissolve
    mc "Que pergunta?"
    
    scene casa_prolog with dissolve
    show prolog 6
    pro "O porquê de Python estar casa de Ruby."
    hide prolog
    
    scene rua_qualquer with dissolve
    mc "...!"
    
    scene casa_prolog with dissolve
    show prolog 6
    pro "Isso aconteceu porque provavelmente eles não conseguiram trabalhar nada na sala de recreação, então estavam meio atrasados com as atividades."
    show prolog 7
    pro "Python deve ter ido se trocar em casa e ido para casa de Ruby, o qual mora com os seus pais."
    show prolog 6
    pro "Ruby é tímido, então se sentiria desconfortável na casa de outra pessoa com a qual não tem muito contato."
    show prolog 7
    pro "Python sabia disso, por isso ela que foi para a casa dele, não o contrário."
    show prolog 6
    pro "Mesmo não se sentindo muito bem, eles continuaram trabalhando, e foi aí que provavelmente a situação de Python piorou."
    show prolog 7
    pro "Vendo a garota naquele estado, os pais de Ruby provavelmente decidiram deixar ela dormir lá pra descansar e cuidar dela."
    show prolog 6
    pro "Você não encontrou os pais do garoto quando foi lá porque eles passam o dia trabalhando."
    show prolog 7
    pro "É claro, isso tudo é só uma suposição, mas provavelmente é o bastante para suprir sua curiosidade."
    show prolog 6
    pro "Câmbio, desligo."
    hide prolog with moveoutright
    
    scene rua_qualquer with dissolve
    "E assim a ligação termina."
    mc "É, ela realmente é tudo o que dizem."
    scene black with dissolve

    return