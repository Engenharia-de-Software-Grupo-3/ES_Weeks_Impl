image pyth perguntandoP = "images/Sprites Python/python 6.png"

image pyth perguntando = "images/Sprites Python/python 7.png"

image pyth escutando = "images/Sprites Python/python 8.png"

image pyth alegre1 = "images/Sprites Python/python 11.png"

image pyth alegre2 = "images/Sprites Python/python 13.png"

image pyth perguntaalegre2 = "images/Sprites Python/python 14.png"

image pyth impressionada =  "images/Sprites Python/python 23.png"

image pyth pesames1 =  "images/Sprites Python/python 36.png"

image pyth pesames2 =  "images/Sprites Python/python 37.png"

image pyth confusa = "images/Sprites Python/python 34.png"

image pyth semhumor =  "images/Sprites Python/python 35.png"
    
image pyth duvida =  "images/Sprites Python/python 17.png"

label pythonEvent0 :
    play music "audio/music.mp3" volume 0.5

    scene sala 1 with fade

    show pyth alegre2

    pyt "E então, como tem sido a sua experiência aqui até agora, [player_name]?"

    show pyth alegre1

    mc "Acho que ela tem tido seus altos e baixos"

    show pyth perguntandoP

    pyt "Entendi. É uma pena que esses baixos existam toda vez que eu pergunto pra alguém."

    mc "Pra quem tanto você faz essa pergunta?"

    show pyth alegre1

    pyt "Ué, pra todo novo estudante é claro. Mesmo que Java fosse o presidente e quem recepcionasse os novos alunos, eu sempre vou atrás do pessoal para ter certeza que terão uma vida alegre na instituição."

    mc "Você realmente se importa muito com todo mundo."

    show pyth alegre2

    pyt "Sim! Todos que vem aqui possuem suas próprias histórias e eu adoraria ouvi-las, assim como eu tenho ótimas que quero contar. Me diz, você sabe que essa é uma instituição famosa de grande prestígio, certo?"

    mc "Claro que sim, não existe ninguém que não saiba disso."

    show pyth perguntando

    pyt "E, seja sincero, você acha que faz sentido você estar nela?"

    mc "Ok, isso é meio rude de se perguntar."

    show pyth perguntaalegre2

    pyt "Vamos lá, não é o que você está pensando. Apenas diga o que sente"

    mc "(Essa de fato não é um questionamento que se deva fazer do nada pra alguém, mas, sinceramente, Python não parecia ter nenhuma malícia quando fez esse questionamento. Por isso, você decidiu ser sincero)"
    
    mc "Na verdade, eu não acho que eu tô no lugar certo. Quase todo mundo aqui parece ser tão habilidoso em tantas coisas diferentes que eu me sinto um pouco deslocado."

    show pyth perguntando 

    pyt "Sabia que é exatamente assim que quase todo novo estudante daqui se sente?"

    mc "É sério?!"

    show pyth impressionada

    pyt "Seríssimo. “Por que eu vim pra cá se não sou bom em nada”, “até no que eu sou bom eu não consigo fazer direito”, “todo mundo aqui deve achar que eu só um empecilho”, e por aí vai. Java é muito bom em tudo que faz e se importa muito com o bem estar dos colegas, mesmo que não pareça. Só que as vezes apenas uma boa intenção não é o bastante pra afastar os pensamentos tristes dos novatos, e por isso eu gostaria de ajudar nisso: dando a todos um mão amiga e um belo sorriso! Se você está aqui não é por sorte ou qualquer ironia do destino, você está aqui porque é onde deve estar e merece estar!"

    mc "Isso realmente é super legal de sua parte, se dedicando assim para acolher os outros"
    
    show pyth alegre1

    pyt "Que nada, apenas amo fazer novos amigos e me divertir com eles."

    mc "Eu adoraria ser tão disposto quanto você. Não acho que eu seja necessariamente ruim em me comunicar com as pessoas, é só que parece que todo mundo ao meu redor está em uma frequência diferente da minha, sabe?"

    show pyth alegre2

    pyt "Mas é claro que está. Você não pode esperar que todos gostem das mesmas coisas ou que ajam da mesma forma, e é por isso que fazer amigos é tão legal."

    mc "(Você consegue sente que um boneco de neve derreteria ao encontro de um sorriso que radia tanto calor. É, ela é realmente muito boa no que faz e parece que é naturalmente assim desde sempre. Sinceramente é bom ter com quem contar dentro dessa academia tão estranha e imprevisível, além disso, você tem certeza que se não fosse por aquela garota, você provavelmente teria levantado algumas paredes entre você e os outros estudantes.)"

    mc "Muito obrigado por tudo!"
    
    show pyth confusa

    pyt "Hum? Pelo que exatamente está agradecendo?"

    mc "N-não é nada!"

    mc "(Você se sente envergonhado assim que as palavras saem da sua boca. Você não normalmente seria tão aberto sobre o que pensa e sente, mas por algum motivo, Python parece ter a misteriosa habilidade de fazer as pessoas quererem ser o mais franca possível.)"

    mc "Algum criminoso já confessou os crimes pra você? – (Você fala isso na tentativa de fazer uma piada...)"
    
    show pyth duvida

    pyt "Oh, então você ouviu essa história? Aconteceu quando eu tinha 6 anos e..."

    mc "Pera, o que?!"
    
    show pyth escutando

    pyt "É isso mesmo. Oh! Você na verdade tá falando da do ano passado não é? Realmente essa ficou mais popular, achei que você se referia à primeira vez."

    mc "Primeira vez???? Isso já aconteceram 2 vezes???"

    show pyth perguntando

    pyt "37, para ser mais exata"

    mc "??????????"

    show pyth perguntandoP

    pyt "Eu me lembro da vez que uma gangue pegou Swift de refém e o prenderam dentro do mercado para o usarem como moeda de troca. No fim das contas, eles esperaram 12 horas e não receberam uma única resposta por parte dos chantageados."

    mc "Eu sei que é uma má prática dar à sequestradores o dinheiro que eles pedem, mas ainda assim me sinto um pouco mal por Swift."

    show pyth duvida

    pyt "Ah, eles não queriam exatamente dinheiro."

    mc "Não? E o eles estavam atrás do que?"
    
    show pyth perguntando

    pyt "Férias remuneradas."

    mc "O que?"

    show pyth escutando

    pyt "Acontece que eles eram uma gangue formada por assalariados, office boys, scrum teams, scrum masters, entre outros, que trabalhavam em algumas lojas e empresas cuja quais a família de Swift é dona. Os salários de muitos foram cortados durante suas férias, então eles se revoltaram. Mas os pais de Swift não deram o braço a torcer. O problema não era o dinheiro, aparentemente eles acharam que aquilo foi só uma birra dos empregados e ignoraram a situação."

    mc " Ok, agora eu me sinto ainda pior por Swift."

    show pyth alegre1

    pyt "É, foi muito triste. Mas os sequestradores foram tão educados! Mesmo invadindo o mercado eles não tocaram em nada. Percebi que eles tavam começando a ficar com fome, então levei uma cesta de comida pra Swift e eles, aí fizemos um piquenique no mercado e brincamos de mímica. No fim das contas eles se desculparam, se demitiram dos empregos e viraram zeladores da academia"

    mc "(Você está perplexo com tal informação) – E isso já aconteceu outras 36 vezes?"

    show pyth alegre2

    pyt "Isso mesmo."

    mc "..."
    
    show pyth duvida

    pyt "Ok, aquela garota aparentemente de fato possui algum tipo de poder místico. É a única explicação plausível."

    pyt "Na verdade, nos últimos anos a taxa de criminalidade diminuiu aqui na cidade e por algum motivo alguns criminalistas dizem que um fator principal foi a minha presença e a da minha amiga Prolog. Não entendo muito bem o que eles querem dizer com isso."
    mc "Eu entendo"

    show pyth impressionada

    pyt "Ah não, olha a hora, a gente vai se atrasar para a próxima aula! Temos que correr. Tchau DAVVI, foi legal conversar com você"
    
    hide pyth with moveoutright

    mc "(A garota sai correndo em disparada e você fica estático com o fato de que a segurança de nossa sociedade está pautada na existência de duas únicas jovens garotas)."
    
    $ pythonEventsCounter = 1
    return