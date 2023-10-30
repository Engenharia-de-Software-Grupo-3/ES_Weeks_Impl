label semana1_dia3:
    show escola with dissolve

    "Você percebe ao chegar na Academia que ainda está com a bola da professora Lovelace, 
        então decide ir procurar ela pelos corredores"
    
    if sala_recreacao_dia_2:
        jump bifurcacao_dia_3_a_1
    else:
        jump bifurcacao_dia_3_b_1

label bifurcacao_dia_3_a_1:

    "Enquanto você anda pela Academia, percebe uma situação estranha no corredor"

    scene luaXcobol with fade

    lua "O QUE É QUE VOCÊ DISSE, VISCONDE DE SABUGOSA COPYRIGHT FREE!?"

    cob "Não me faça repetir 2 vezes, pequena inconsequente: você e aquele seu amigo são exemplos cabais 
        do motivo de que tais práticas tornam estúpidos os envolvidos nelas"

    lua "Ok, ok. Eu vou deixar essa passar caso você deixe seu preconceito de lado e dê uma chance ao que eu 
        sugeri. É claro que você só está dizendo isso por pura ignorância"
    
    cob "Ficarei ignorante mesmo se de fato tomar parte em tal atividade sem sentido."

    lua "Eu vou arrancar teu bigode!"

    cob "Faça e terei a certeza de que a receita federal perceba o desfalque no seu imposto de renda!"

    "Isso parece uma situação que vai escalar rapidamente."

    "Pra ser bem sincero, você não tem certeza se deveria fazer algo sobre."

    scene corredor with dissolve

    show cobol 3 at right

    cob "Deixe-me ser bem claro."

    show cobol at right

    cob "O hobbie que você tanto idolatra não passa de uma forma infantil de escapismo."

    cob "Não importa se usares belas palavras para descrever ele, é apenas uma técnica de 
        redirecionamento do real problema."

    show lua 31 at left
    
    lua "Isso não é-"

    cob "Potencial desperdiçado. Você continua focando em coisas fúteis e ignorando suas 
        responsabilidades como uma criança."
    
    lua "Criança é teu ***-"

    cob "Ruby não fica fora disso. Ele é deveras admirável em inúmeros pontos, mas o problema dele é 
        diferente do seu."
    
    cob "Seus vícios não afetam sua integridade física, mas mentalmente lhe tiram a paz. E você sabe 
        que a culpa é sua."
    
    show lua 30 at left

    lua "Cala a boca e para de envolver ele nisso!"

    show cobol 5 at right

    cob "Não. Você precisa entender isso: cada dia que você passa investindo nisso é um desperdício."

    cob "E se não mudar como age, ao chegar no fim da linha, seu único companheiro será o remorso."

    "Ok, ele já tá começando a pegar pesado. Você não vai conseguir ficar parado vendo isso, mas também 
    não saber se quer problemas para si."

    "O que fará?"

menu escolha_B3A1:

    "Interromper a discussão":
        jump interrompe_discussao
    
    "Ir embora":
        jump nao_interrompe_discussao

label interrompe_discussao:

    "Não importa se isso te causar mais dor de cabeça, você sabe que vai se arrepender depois se não 
        fizer nada naquela situação."
    
    show lua 23 at left
    
    show cobol at right

    "Você defenestra a bola de basquete pela janela mais próxima e se apressa em direção aos dois para 
        a surpresa dos mesmos."
    
    mc "Ei, você pode parar com isso?"

    cob "Olá meu caro [mc], acho que não nos introduzimos direito até o presente momento."

    "Você se lembra de ter visto ele durante a chamada em sua classe, por isso ele devia saber o seu 
        nome também."
    
    mc "Verdade, e acho que a primeira impressão não foi muito boa para nenhum dos dois"

    show cobol 8 at right

    cob "Não se preocupe com as peculiaridades da senhorita Ada. É algo costumeiro da parte dela, mas de 
        fato ela tem nossos melhores interesses em mente."
    
    mc "Não estou falando disso. Você não acha que está sendo rude demais com ela?"

    show lua 21 at left

    lua "Isso mesmo, um completo Babaca."

    show cobol 7 at right

    cob "Ah..."
    
    show cobol 3 at right
    
    cob "..."

    show cobol 10 at right

    cob "Compreendo. Realmente aparenta ser isso."

    mc "O que isso significa?"

    show lua 26 at left

    lua "Deixa eu explicar. Eu vim tirar satisfação com esse cara sobre um certo assunto trivial..."

    show cobol 4 at right

    cob "Não é trivial..."

    show lua 24 at left

    lua "E então ele pediu pra eu “elaborar justificativas plausíveis para tal problemática”..."

    cob "O que não foi atendido devido ao caráter esdrúxulo de suas alegações."

    show lua 30 at left

    lua "E de repente ele começou a me cuspir ofensas com a cara mais limpa do mundo!"

    show cobol at right

    cob "Não eram ofensas, era uma observação pontual em relação ao cerne de seus problemas."

    show lua 19 at left

    lua "Mentiras e falácias!"

    show cobol 11 at right

    cob "Hipérboles e Imposto de renda!"

    mc "ALGUÉM POR FAVOR ME DÁ UM CONTEXTO!"

    cob "..."

    lua "..."

    "O silêncio reinou por alguns segundos até um deles falar algo."

    jump bifurcacao_dia_3_a_2

label nao_interrompe_discussao:

    "Talvez realmente não seja bom ficar metendo o nariz onde não é chamado quando você nem sequer sabe 
        como essa academia funciona."

    show lua 31 at left
    
    lua "Mesmo que isso aconteça eu pelo menos terei algo comigo no fim! E você o que terá!? Dinheiro?"

    show cobol at right

    cob "Paz."

    show lua 19 at left

    lua "Isso não é paz, é apatia!"
    
    lua "Uma vida sem significado!"

    cob "Uma vida sem sofrimento"

    "Você tinha razão, é melhor ir embora antes de ser arrastado para um debate filosófico 
        de \“qual o sentido da vida\”."
    
    "Mas uma brusca virada, você perde o equilíbrio e a bola de basquete é a única coisa que 
        impede você de bater a cara no chão."

    "Como nada é de graça nessa vida, aquilo te custa a própria bola já que após isso ela quicou 
        e saiu pela janela do corredor."
    
    "O barulho de sua quase queda alerta as duas pessoas que estavam discutindo."

    show lua 17 at left

    lua "Oh! Justo o que precisávamos: um juiz imparcial."
    
    lua "Vem aqui um instante."

    "Realmente o roteiro conspira contra você [mc]."

    "Não importa o que você faça, sempre vai acabar se envolvendo em problemas."
    
    jump bifurcacao_dia_3_a_2

label bifurcacao_dia_3_a_2:

    show lua 3 at left

    lua "O quão importante você considera jogos?"

    mc "Jogos? Tipo dominó?"

    lua "Não tô falando disso. Jogos digitais, vídeo games e coisas do tipo."

    mc "Oh, esse tipo de jogo."

menu escolha_B3A2:

    "Eu acho legal":
        
        lua "Então certeza que você vai entender o meu lado."
    
    "Eu não me importo muito":
        
        lua "Eh, sério? Você não sabe o que tá perdendo."

        show cobol 10 at right

        cob "Para a situação atual, isso é de fato o melhor caso."

        cob "Alguém não viesado capaz de ver a situação de forma logica"
    
    "Eu não gosto":

        show cobol at right

        cob "Se é assim, entenderá o problema em mãos de forma correta, meu caro."

label bifurcacao_dia_3_a_3:

    show lua 17 at left

    lua "Jogos são algo muito importante. Eles são a cristalização dos sonhos e esperanças daqueles que os 
        fazem!"
    
    lua "Podemos dizer que uma obra de arte."

    lua "Jogos conseguem criar sonhos dentro daqueles que o jogam e torna-los pessoas melhores."

    lua "É nisso que eu acredito e queria que todos também pudessem entender e sentir o que eu sinto."

    "Quando ela coloca assim, jogos de fato começam a ganhar uma maior relevância não papel 
        maior das coisas."
    
    show cobol 5 at right

    cob "Mais hipérboles de caráter eufemista são lançadas por essa dama."

    cob "Mesmo que eu considerasse jogos como algo tão importante assim, é necessário parcimônia."

    cob "Repetições originam hábitos. Hábitos originam vícios."

    cob "Você está nesse estado e se nega a sair dele."

    show lua 5 at left

    lua "Isso não importa se não me prejudicar. É como pedir pra alguém que joga futebol o tempo 
        todo parar de fazer isso porque deveria fazer mais coisas."

    show cobol 6 at right
    
    cob "Primeiramente, sim, mas você está desviando do real problema que deu origem à toda essa discussão."

    mc "É verdade até agora não me disseram o motivo da briga de vocês ter começado."

    lua "Se jogos são tão bons, não seria legal ter eles em qualquer lugar?"

    mc "Acho que sim?"

    show lua 7 at left

    lua "Tá vendo! Eu sabia que ia ficar do meu lado!"

    show cobol 9 at right

    cob "Negativado."

    mc "?"

    cob "O CPF dela está negativado."

    show lua 11 at left

    lua "..."

    cob "Ela fez um empréstimo no banco do qual sou representante à 3 meses atrás."

    cob "Apenas a primeira parcela foi paga. Então houve um reajuste no valor das mesmas 
        para o futuro, e ela veio fazer uma reclamação para minha pessoa."
    
    show lua 19 at left

    lua "Claro que eu fui reclamar! Um reajuste assim do nada é só extorsão!"

    show cobol 5 at right

    cob "Não foi do nada. O banco tentou contatar a senhora 8 vezes em diferentes ocasiões para avisar."

    cob "Mas você achava que eram ligações de cobrança e desligou todas as vezes."

    show lua 11 at left

    lua "..."

    mc "..."

    show lua 14 at left

    lua "Foi por uma boa causa."

    lua "Foi um investimento."

    lua "A Microtendo lançou uma nova versão de seu console portátil DXphere e eu não consegui 
        juntar todo o dinheiro a tempo pra comprar ele  day-one."
    
    lua "Por isso eu fiz o empréstimo."

    mc "Porque você não passou no cartão? Se você pode fazer empréstimo, provavelmente tem um cartão."

    show lua 22 at left

    lua "Usei o limite dele pra comprar todos os jogos do novo console."

    mc "TODOS!?"

    lua "Só são 3."

    mc "..."

    mc "Você fez um empréstimo pra comprar um console que só tem 3 jogos?"

    lua "Foi."

    mc "E ao invés de comprar só um, fez ainda mais dividas comprando os 3 de uma vez?"

    show lua 14 at left

    lua "Diversidade é o tempero da vida."

    "Você estava completamente pasmo. Como alguém poderia agir de forma tão 
        inconsequente assim com sua saúde financeira?"

    show lua 28 at left
    
    lua "Mas foi um investimento!"

    lua "A nova versão tem retrocompatibilidade com os jogos da anterior, então 
        eu posso jogar nela os jogos que já tenho e assim-"

    mc "Você se endividou pra comprar um vídeo-game pra jogar coisas que já podia antes?"

    show lua 11 at left

    lua " É que a resolução da nova tela é tão boa"

    mc "..."

    mc "Muito prazer meu nome é [mc]."

    show lua 19 at left

    lua "Ei, não fuja da discussão"

    show cobol at right

    cob "Cobol, à seu dispor. Aquela senhorita se chama Lua. É um prazer lhe conhecer."

    show lua 3 at left

    lua "É, claro, tudo maravilha, mas no fim das contas, quem você acha que tem razão nessa briga?"

    mc "Precisa perguntar mesmo? É claro que-"

    alan "[mc]."

    "Você olha para trás e vê Alan segurando a bola de basquete com uma mão e 
        pondo gelo na cabeça com a outra."
    
    show alan
    hide lua 3
    hide cobol
    with fade
    
    alan "Já te disseram que você tem um ótimo arremesso?"

    mc "Eu posso explicar."

    alan "Adoraria ouvir na minha sala."

    alan "Venha comigo."

    hide alan
    with dissolve

    scene black
    with fade

    # "Recomenda-se que você salve o jogo neste ponto."

    show sala_diretoria
    show alan
    with dissolve

    alan "Então....."

    alan "Você jogou ele do 4º andar?"

    mc "Foi um acidente, senhor."

    alan "Você acidentalmente jogou sua bola de basquete..." 
    alan 'que por acidente ocorreu em acertar Swift...'
    alan 'que por acidente estava retornando um carrinho de compras para a loja...' 
    alan "fazendo que ele acidentalmente caísse dentro do carrinho, perdesse o controle, fosse até as escadarias, se chocasse contra a parede e jogasse o inocente aluno pela janela do 4º andar?"

    mc "Quando você fala desse jeito, faz parecer pior do que realmente foi."

    alan "Alan Turing, o pai da Ciência da Computação, esfrega os dedos contra as 
        próprias têmporas, soltando um longo suspiro."
    
    alan "[mc], você se lembra de quando eu lhe convidei para essa instituição?"

    mc "Você quer dizer quando você me atropelou com o seu carro?"

    alan "Bem, sim, mas quando eu lhe atropelei, eu me desculpei logo em seguida. 
        Esse é um exemplo que acho sábio em se seguir."
    
    mc "Foi um acidente! Isso só aconteceu porque Lua estava sofrendo bullying de COBOL!"

    alan "Lua sofre bullying de COBOL todo dia meu caro rapaz, isso não lhe servirá 
        como uma boa justificativa."

    mc "Você sabia do bullying?"

    alan "Está ocorrendo já há algum tempo, sim."

    mc "E você fez nada? COBOL sequer foi chamado para a diretoria."

    alan "Nós, na academia, tentamos fazer o melhor para garantir o bem-estar 
        físico e mental de nossos alunos, a todo momento."
    
    alan "De novo, nos conhecemos com você me atropelando."

    alan "Você não era um aluno naquela época."

    alan "COBOL tem uma personalidade difícil, não negarei o fato. Mas seus comentários 
        vêm de um lugar de verdadeira preocupação e motivo. Esse motivo sendo que o vício de Lua por 
        jogos fizesse com que ela se tornasse uma fugitiva da Receita Federal."
    
    alan "Portanto, assim como nos esforçamos para limpar a ficha dela, você deve se 
        esforçar em corrigir seus erros."
    
    alan "Seu erro sendo ter defenestrado Swift pela janela do 4º andar."

    mc "Acidentalmente."

    alan "Acidentalmente defenestrar Swift pelo 4º andar, é claro. Você é um bom garoto, 
        com um forte coração e ainda mais fortes, resistentes a atropelamentos ossos. Por isso, 
        preciso que seja forte o suficiente para reconhecer..."
    
    alan "Que o COBOL pagou pelas computadores do laboratório, então não queremos aborrecê-lo."

    alan "Agora, se me dá licença, eu tenho outros negócios a atender. Você será liberado com 
        apenas um aviso, mas na próxima vez que cometer uma ofensa federal nas premissas, terei 
        que ser mais severo."
    
    return

label bifurcacao_dia_3_b_1:

    "Você percorre os corredores, ainda ponderando sobre sua nova vida."

    "Tudo aqui é tão grande, desde os prédios até as pessoas, maiores que a própria vida, maiores que você."

    "Um calafrio corre por sua espinha, cobrindo seu corpo com um sentimento claustrofóbico."

    "\"É assim que vai ser?\", seu coração bate forte como uma bola de ping pong bate na mesa, 
        sua mente gira como uma pedra rolando ladeira abaixo,"

    "e um barulho dentro de sua cabeça são como o de chutes numa parede acertam sua cabeça como 
        se fosse uma tela de bloqueio para uma área de trabalho vazia."
    
    "Pera, não. O barulho tá ficando mais alto."

    swi "Ora, ora, ora… Olha o que o gato arrastou até aqui."

    "Diz uma voz de forma fina e vil."

    "Como uma cobra, caso cobras aprendessem a falar assistindo filmes da Barbie."

    "Você vira na esquina do corredor e vê duas figura, um jovem ruivo no 
        chão contra a parede e um outro loire de pé."
    
    scene swiftXruby
    with fade

    "Você imagina que o de pé é a Barbie com bolsa de couro de cobra, o qual está tentando posar de 
        forma ameaçadora, e falhando miseravelmente nessa tarefa."
    
    "É visível que o loiro tá se esforçando muito para não perder o equilíbrio, como um 
        graveto extremamente determinado à não cair da árvore."
    
    "A semelhança com uma árvore fica ainda maior devido às notas verdes de dólares 
        caindo da boca de sua calça."
    
    rub "Oh legal, vintinho!"

    rub "Sabe, é bem irresponsável guardar dinheiro assim, se alguém mal intencionado encon-"

    swi "Me dá isso de volta!"

    rub "Claro, desculpa!"

    swi "Eu tô fazendo bullying com você! Porque está me dando conselhos financeiros ao 
        invés de se sentir insignificante e pequeno?!"
    
    rub "Eu não sou pequeno! Não sou!"

    swi "Me desculpa, pode repitir? Eu não consigo te escutar daí de baixo!"

    rub "Tá tudo bem. Deixa eu só levantar aqui rapindinho pra fa-"

    swi "Não! Isso foi uma piada sobre sua altura. \"Aí de baixo\" não porque você tá no 
        chão, mas porque você é pequeno!"
    
    rub "Eunãosoupequeno!"

    "Aquela certamente é a cena de bullying mais patética que você já viu."

    scene corredor
    show ruby 30 at left
    show swift 14 at right
    with fade

    rub "Porque você tá sequer me fazendo bullying?"

    swi "Porque vi seu caderno. Eu sei seus planos…"

    show ruby 28 at left

    rub "O-o que? Me devolve meu caderno."

    swi "Só se você desistir da ideia"

    show ruby 8 at left

    rub "Mas eu… Eu…"

    "Parece que aquilo atingiu um impasse. Você quer ajudar, mas nem sabe direito o que tá 
        acontecendo. O que vai fazer?"
    
menu escolha_B3B1:

    "Ignore, aquilo não é sa sua conta":

        "Você decide ignorar e continuar procurando a professora. Você já percebeu que nessa 
            Academia nem tudo é o que parece ser."
        
        "Talvez eles estejam apenas atuando, certamente existe certa energia homoafetiva emanando da cena."

        "É, deve ser isso. Agora você só precisa forcar no que veio fa- Desde quando seu 
            cadarço tá desamarrado?"
        
        "O chão se aproxima rapidamente à medida que você cai, mas a bola de basquete 
            para sua cara antes dela beijar o chão."
        
        "Sua natureza elastica amortece o impacto e à lança diretamente contra o 
            nariz do porcelana do rapaz loiro."
        
        jump bifurcacao_dia_3_b_2
    
    "Interromper a cena":

        mc "Ei, você pode parar com isso."

        "Não importa o lugar: um babaca sempre é um babaca. E você consegue reconhecer um quando vê."

        show swift 12 at right

        swi "O que você quer?"

        mc "Deixa o garoto em paz."

        show swift 19 at right

        swi "Ohhhhh, você é o cara novo, não é?"

        swi "Então você não sabe como as coisas funcionam por aqui. Deixa eu te expli-"

        mc "Solta."

        mc "O."

        mc "Garoto."

        "Você não é uma pessoa muito intimidadora, mas como suspeitava, 
            aquele loirinho é muito mais covarde do que parece."

        "Ele começa a ficar nervoso e tira o pé da parede"

        show swift 10 at right

        "Ele levanta um pouco a perna e pega da boca da calça o dinheiro ali guardado."

        swi "Pra você. Pega, finja que nunca viu o que aconteceu e dá o fora."

        mc "Você vai realmente tentar comprar o direito de encher o saco desse garoto?"

        show swift 3 at right

        swi "Não, eu vou tentar comprar o direito de você não encher o MEU saco."

        swi "Agora vaza."

        mc "Eu não quero seu dinheiro!"

        show swift 8 at right

        swi "Você quer! Você não é imune ao capitalismo!"

        "O rapaz começa a quase esfregar o dinheiro na sua cara."

        "Irritado, você usa a bola de basquete pra afastar a mão dele."

        mc "Eu já disse que não quero!"

        "Acabou que você pôs força demais no empurrão e a bola acaba acertando diretamente a cara de Swift."

        jump bifurcacao_dia_3_b_2

label bifurcacao_dia_3_b_2:

    swi "Wah!"

    show swift 6 at right

    "O rapaz tropeça para trás, caindo dentro de um carrinho de compras vazio deixado no corredor, 
        propelindo o mortífero veículo de supermercado escadaria abaixo no fim do corredor, 
        acertando a parede e defenestrando o loiro."
    
    hide swift 6
    with fade
    
    swi "Waaaaaaaaaaaaaaah!"

    play sound "audio/Smashing.mp3" fadein 1.0

    hide ruby 8
    show ruby 26
    with dissolve

    rub "Você me salvou!"

    mc "Eu acho que ele morreu…"

    rub "Muito obrigado!"

    mc "Foi uma queda do 4° andar…"

    rub "Oi, eu me chamo Ruby."

    mc "Ah, eu me chamo [mc]."

    show ruby 3

    rub "Você é o cara novo! Lua me pediu pra te entregar isso como desculpa por ter te largado com Haskell."

    "Você recebe 2x Energéticos!"

    $ itens_estado[0] = itens_estado[0] + 2

menu escolha_B3B2:

    "Porque aquele cara tava te incomodando?":

        show ruby 2

        rub "Oh, ele faz isso. Estamos na mesma classe, mas por algum motivo ele sempre 
            tá tentando competir comigo."
        
    "O que tinha no seu caderno?":

        show ruby 16

        rub "Ah… Então você ouviu. Não é nada… Sério, só uma ideia boba."
    
    "Sério, a gente tem que checar como aquele cara tá":
        
        show ruby 16

        rub "Oh, é. Isso é uma boa ideia, deixa só eu guardar essas coisas e…"

label bifurcacao_dia_3_b_3:

    swi "Aí está ele!"

    show ruby 16 at left with move
    show swift 8 at right with zoomin
    "O rapaz volta ao 4° andar com uma rapidez assustadora."
    show alan with zoomin
    "E ele não está sozinho. Ao seu lado está Allan Turing, o qual vem andando 
        lentamente em sua direção (ele ainda está em preto e branco?)." 

    mc "..."

    alan "..."

    mc "Eu posso explicar."

    alan "Adoraria ouvir na minha sala."

    alan "Venha comigo."

    scene black
    with fade

    # "Recomenda-se que você salve o jogo neste ponto."

    scene sala_diretoria
    show alan
    with dissolve

    alan "Então....."

    alan "Você jogou ele do 4º andar?"

    mc "Foi um acidente, senhor."

    alan "Você acidentalmente jogou ele do 4º andar, estou correto?"

    mc "Quando você fala desse jeito, faz parecer pior do que realmente foi."

    "Alan Turing, o pai da Ciência da Computação, esfrega os dedos contra as 
        próprias têmporas, soltando um longo suspiro."
    
    alan "[mc], você se lembra de quando eu lhe convidei para essa instituição?"

    mc "Você quer dizer quando você me atropelou com o seu carro?"

    alan "Bem, sim, mas quando eu lhe atropelei, eu me desculpei logo 
        em seguida. Esse é um exemplo que acho sábio em se seguir."
    
    mc "Swift estava fazendo bullying com Ruby."

    alan "De um jeito meio homoafetivo, sim, mas isso não significa que o que você fez foi certo."

    mc "Você sabia do bullying homoafetivo?"

    alan "Está ocorrendo já há algum tempo, sim."

    mc "E você fez nada? Swift sequer foi chamado para a diretoria."

    alan "Nós, na academia, tentamos fazer o melhor para garantir o bem-estar físico e 
        mental de nossos alunos, a todo momento."

    mc "De novo, nos conhecemos com você me atropelando."

    alan "Você não era um aluno naquela época."

    alan "Swift tem uma personalidade difícil, não negarei o fato. Mas seu desenvolvimento 
        acadêmico é excelente, e ele fez diversas contribuições para a Academia. Já estamos 
        arranjando reparações para o pobre Ruby, mas também devemos corrigir seu erro."
    
    alan "Seu erro sendo defenestrar um aluno pelo 4º andar."

    mc "Acidentalmente."

    alan "Acidentalmente defenestrar um aluno pelo 4º andar, é claro. Você é um bom garoto, 
        com um forte coração e ainda mais fortes, resistentes a atropelamentos ossos. Por isso, 
        preciso que seja forte o suficiente para reconhecer..."
    
    alan "Que o pai de Swift pagou pelas reformas no refeitório, então não queremos aborrecê-lo."

    alan "Agora, se me dá licença, eu tenho outros negócios a atender. Você será liberado com apenas 
        um aviso, mas na próxima vez que cometer uma ofensa federal nas premissas, 
        terei que ser mais severo."
    
    return