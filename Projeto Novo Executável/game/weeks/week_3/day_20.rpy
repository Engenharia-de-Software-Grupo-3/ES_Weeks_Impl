default love_final = 0
default elegiveis = []

label semana3_dia20:
    "Hoje é dia de prova"
    call prepare_battle_2 from _call_prepare_battle_2_1
    "Após a prova..."
    python:
        if pythonLoveCounter >= 6 and pythonEventsCounter >= 4:
            elegiveis.append(pythonLoveCounter)
        if javaLoveCounter >= 6 and javaEventsCounter >= 4:
            elegiveis.append(javaLoveCounter)
        if luaLoveCounter >= 6 and luaEventsCounter >= 4:
            elegiveis.append(luaLoveCounter)
        if rubyLoveCounter >= 6 and rubyEventsCounter >= 4:
            elegiveis.append(rubyLoveCounter)
        
        if len(elegiveis) != 0:
            love_final = max(elegiveis)
    
    scene escola
    mc "O sol está brilhando, o céu está azul, os pássaros estão cantando, e eu venci o perigo iminente da minha ansiedade debilitadora de ser o aluno novo em um mundo novo...."
    mc "Por enquanto...."
   
    if love_final == 0:
        call bad_end from _call_bad_end
    else:
        mc "Eu até fiz alguns novos amigos...."
        mc "E talvez eu devesse investir mais nessas amizades, já que terminamos as provas..."
        mc "E eu economizei dinheiro o suficiente para ter uma pequena folga..."
        mc "Eu deveria passar tempo com algum deles mais tarde. E eu seu exatamente com qual deles."
        if love_final == pythonLoveCounter:
            call python_end from _call_python_end
        elif love_final == rubyLoveCounter:
            call ruby_end from _call_ruby_end
        elif love_final == luaLoveCounter:
            call lua_end from _call_lua_end
        else:
            call java_end from _call_java_end  
return

label python_end:
    mc "Eu acho que vou chamar Python...."
    mc "E sei exatamente para onde deveríamos ir!"
    mc "Hey, Python, um minuto!"
    show pyth 13
    pyt "Oh! Oi [player_name]! Está tudo bem?"
    mc "Tudo está ótimo...."
    mc "Hum...."
    mc "Na verdade, eu queria falar com você sobre uma coisa."
    show pyth 2
    pyt "Tem certeza de que você está bem? Você está meio vermelho."
    mc "Sim, sim, tenho certeza."
    "[player_name] - pensamento" "É melhor eu só falar logo...."
    mc "Então, abriu um parque de diversões aqui na cidade, e eu soube que ele é muito bom."
    mc "E eu queria saber se você gostaria de ir comigo? Podemos ir na Roda Gigante juntos."
    "Por um momento, seu coração para. Você não consegue ler a expressão dela, com os 3 pares de olhos (dois humanos, quatro reptilianos) lhe encarando firmemente...."
    "Na sua cabeça, uma eternidade passa, mas quando ela responde...."
    show pyth 13
    pyt "Eu adoraria ir com você!"
    mc "Sério?"
    "Ela segura sua mão e um arrepio corre pela sua coluna."
    show pyth 9
    pyt "Hehe."
    show pyth 12
    pyt "Acho que lhe vejo mais tarde!"
    hide pyth 12
    "E sem esperar uma resposta, ela saiu saltitando para casa."
    scene black with dissolve
    "Algumas horas se passam e enfim vocês se encontram no parque."
    scene python_hotdog
    pyt "UAU! Realmente é incrível!"
    mc "Obrigado por aceitar o convite."
    pyt "Nada disso, [player_name]. Eu que agradeço. Para mim é como um banho de nostalgia."
    mc "Fico feliz que tenha gostado. "
    mc "Mas e então, vamos na roda gigante? Garanto que dessa vez você sairá mais de um metro do chão."
    "A garota dá um leve sorriso antes de lhe responder."
    pyt "Se você realmente vai levar pra esse lado, precisa de mais uma coisa para completar a cena."
    mc "E o que seria essa coisa."
    "A garota então estende os braços em sua direção."
    pyt "Você segurando minha mão."
    "Sua cara fica vermelha e sua mente embranquece, assim como já acontecera muitas vezes."
    "Mas dessa vez era diferente. Aquela garota havia se tornado para você alguém importante demais."
    "Você se recusar a deixar que algo tão bobo como sua vergonha estrague o momento dela."
    mc "Se realmente é o que quer..."
    "Você gentilmente segura as mãos dela. Ela responde com um sorriso, o qual você também retribui. Meio sem jeito, mas retribui."
    scene black with dissolve
    "E assim, Python e você entram de mãos dadas na roda gigante. Vocês sentam no assento um ao lado do outro, ainda com as mãos entrelaçadas."
    "Não parecem que elas serão soltas antes do brinquedo parar e, sinceramente, você não poderia estar mais feliz."
return

label java_end:
    mc "Java?"
    show java 13
    jav "Sim?"
    mc "Quer sair mais tarde?"
    show java 10
    jav "Sim. Não precisa nem ser mais tarde. Tem uma cafeteria nova que abriu perto daqui, poderíamos ir lá agora?."
    mc "Claro, por que não?"
    scene black
    "Então você java se direcionam a cafeteria"
return

label lua_end:
    mc "Vou chamar Lua...."
    mc "Só espero que ela não esteja ocupada...."
    mc "Hum.... Lua, você teria um minuto para conversar?"
    show lua
    lua "Huh? Seja rápido, eu tenho que voltar para casa logo e fazer minha dailies. "
    mc "Oh, certo."
    mc "Então. Sabe. Tipo. Assim. Meio que. Não, pera. Deixa eu começar de novo. Então. Tipo. Sabe-"
    show lua 20
    lua "Vai looooooooooooogo!"
    mc "Okok!"
    mc "Você está livre mais tarde? Você quer sair comigo?"
    "Por um momento, seu coração para. Você não consegue ler a expressão dela, com seus olhos estrelado tão distantes quanto o próprio espaço...."
    "Na sua cabeça, uma eternidade passa, mas quando ela responde...."
    show lua 3
    lua "Como assim?"
    mc "Oh. A gente poderia sair para algum lugar e-"
    lua "Mais tarde é a competição de New Super Street Kombat Bros 2 – Ultra Instinct – Neo Challengers Anniversary Edition HD Remix 64.... & Knuckles!"
    mc "Oh. É mesmo.... eu tinha esquecido. Desculpa, eu-"
    lua "E você está vindo comigo."
    mc "Huh?"
    show lua 7
    lua "Eu esqueci de te contar?"
    lua "A competição vai acontecer em uma daquelas convenções de cultura pop que tem uma vez por ano."
    lua "Vai ter um palco gigante, vai ser incrível."
    show lua 22
    lua "E eu meio que preciso de alguém para me segurar caso eu tente pular em algum gamer idiota que tente me irritar antes da competição."
    lua "Então você vai comigo. Eu já até consegui suas credenciais. Aqui, toma sua identidade de volta."
    mc "Oh, obrigado, e-"
    mc "Você pegou minha identidade?"
    lua "E também...."
    show lua 24
    lua "Vai ser uma convenção longa, e esses tipos de coisa são mais divertidas com alguém especial, então...."
    show lua 22
    lua "Bem, não importa. Você está vindo comigo."
    show lua 3
    lua "Te pego as cinco?"
    mc "Cinco?"
    show lua 6
    lua "Ótimo. Até depois!"
    hide lua 6
    mc "...."
    mc "O que acabou de acontecer...?"
    mc "E essa não é a minha identidade...."
    "Mas, mesmo com pensamentos de falsidade ideológica afligem sua mente, eles não são o suficiente para tirar o sorriso em seu rosto...."
    "E quanto a sua identidade.... agora você pode pegar mais tarde."
    scene black
    "O relógio bate as 5 e você se encontra com Lua no evento."
    scene lua_miku
    lua "E então, vamos ver as coisas? Ainda tem tempo até o início do torneiro"
    mc "Claro. Não esperava que você viesse de cosplay."
    lua "É claro que eu viria. Esse é meu primeiro cosplay, então quero sua opinião sincera: o que achou?"
    mc "Sinceramente, incrível."
    lua "Eu sabia! Afinal, se fui eu que fiz não podia dar errado."
    scene black
    "Você e Lua começam a andar pelo evento lotado."
    "Você não tem tanto interesse assim naquele evento, mas a sua companhia faz com que você não quisesse estar em qualquer outro lugar além daquele."
return

label ruby_end:
    mc "Vou chamar Ruby...."
    mc "Mas onde que ele está? Eu não vi ele até agora...."
    rub "[player_name]! [player_name]!"
    "Antes que você consiga se virar, um garoto ruivo e animado se joga com os braços ao redor do seu pescoço, praticamente girando."
    scene ruby_winner
    rub "EU GANHEI!"
    rub "Você está olhando, neste momento, para o mais novo Presidente Estudantil da Academia!"
    mc "Você ganhou?"
    rub "Eu ganhei!"
    mc "VOCÊ GANHOU?!"
    rub "EU GANHEI!"
    mc "PARABÉNS!"
    rub "Eu estou.... Eu estou tão feliz...."
    rub "Vai ter uma cerimônia de vitória mais tarde."
    rub "Você, por acaso, estaria livre...?"
    mc "Você...."
    mc "Você está me convidando para a cerimônia?"
    rub "Sim. Você foi meu Consultor para a campanha. Sem você, eu não acho que conseguiria ter sido eleito."
    mc "Eu...."
    mc "Eu estaria honrado em te acompanhar na cerimônia."
    rub "!"
    rub "O-okay! Então vamos juntos amanhã! Eu posso te buscar em casa."
    rub "Vai ser um passeio presidencial! Hahá!"
    rub "Eu tenho que ir embora agora.... Tenho assuntos presidenciais para cuidar. Te vejo amanhã, okay!"
    scene black
    "E, com isso, ele vai embora, com um sorriso no rosto, lhe deixando com uma estranha mistura de orgulho e animação. "

return

label bad_end:
    mc "Adoraria passar o resto do dia de hoje com alguns dos meus colegas."
    mc "Mas não me sinto proximo o bastante deles para isso."
    mc "Quer saber? Vou só pra casa dormir. Mereço uma tarde sem fazer nada depois de tudo que passei."
    "E assim, você volta para casa sozinho. Não é algo necessariamente ruim, todos precisam de um tempo consigo mesmo."
return