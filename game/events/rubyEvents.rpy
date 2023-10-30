#Primeira
label rubyEvent0:
    scene corredor with fade
    show ruby with dissolve
    ruby 2 '[player_name]! Como vai?'
    show ruby
    menu:
        mc 'Ruby!' 
        "Eu vou bem, e você?":
            ruby 3 'Eu vou bem, eu vou bem…'
            ruby 2 'Mas você está bem mesmo?'
            show ruby 
            mc 'Huh? Como assim?'
            ruby 2 'É só que pode ser difícil se adaptar a vida na Academia. Tem tantas coisas diferentes…'
            show ruby 
            mc 'Bem, não são tantas assim….'
            ruby 3 'Bem, no começo parece mesmo normal, mas com o passar do tempo…'
        "Ainda estou me acostumando com a vida na Academia.": 
            ruby 2 'Eu sei como é! Tem tanta coisa nova, mas eu prometo que fica melhor com o tempo. '
            show ruby 
            mc 'Quanto tempo levou para você se adaptar?'
            ruby 2 'Bem…. Dois anos? Três, talvez….'
            ruby 3 'M-mas aposto que você irá bem mais rápido!'
        'Eu quero me jogar pela janela.':
            ruby 14 'Oh….'
            ruby 16 'Não é tão ruim assim, logo você vai se acostumar... '
            ruby 17 'Mas no meio-tempo, quer meu gancho de alpinismo?'
    #Junção
    ruby 17 'A maioria das atividades mais incomuns vão sendo introduzidas ao longo do tempo, para dar todo mundo tempo de se acostumar. '
    ruby 'Você começa tendo aula flexíveis, professores bizarros….'
    ruby 'Depois passamos para as competições esportivas de paintball, a inteligência artificial que quer tomar conta do sistema da escola….'
    ruby 19 'Você nem teve sua primeira invasão ninja ainda!'
    show ruby 
    mc 'E é para eu ter?'
    ruby 3 'Acontece mais do que deveria. '
    ruby 2 'Enfim, também não é como se você fosse passar por essas mudanças sozinho.'
    ruby 'Próximo ano, por exemplo, vamos finalmente ser alocados aos dormitórios da Academia. Nesse todo mundo vai estar no mesmo barco. '
    show ruby 
    mc 'Obrigado Ruby. Você parece ter bastante experiência.'
    ruby 5 'P-pareço? Hehe….'
    '' with hpunch
    ruby 3 'Oooops, esse é o sinal. Tenho que ir para a aula.'
    ruby 'Se quiser, a gente se fala no caminho. '
    scene black with dissolve
    'Vocês conversaram por pouco tempo, e Ruby estava claramente nervoso explicando os conceitos mais inventivos da Academia.'
    'Mas, de toda forma, você se sente que os dois se tornaram mais próximos.'
    $ rubyEventsCounter = 1
    return

label rubyEvent1:
    scene corredor with fade
    ruby '[player_name]!' 
    show ruby with dissolve
    ruby 3 'Eu sabia que eu tinha em algum lugar. Aqui. '
    'Ruby lhe entrega um caderno velho, mas bem cuidado.' 
    show ruby 
    'Folheando rapidamente, você percebe que todas as folhas foram usadas.'
    mc 'O que é isso?'
    ruby 2 'Foi meu caderno para quando eu entrei na Academia! Ele possui toda dica, informação ou guia necessário para sobreviver aqui. '
    show ruby 
    mc 'Capítulo 7: Como Sobreviver a Guerra do Bolo de Milho?'
    ruby 3 'Elas costumam acontecer em Junho. '
    show ruby 
    mc 'Por que vocês tem tantos eventos com nomes vagos e levemente ameaçadores?'
    ruby 2 'É, nunca fomos bons na convenção de nomes… é basicamente que em Junho tem um Bolo de Milho muito bom, e todos os alunos lutam por ele. '
    show ruby 
    mc 'Tem uma sessão inteira sobre quais as melhores armas não letais para se usar….'
    ruby 2 'O bolo é muito bom...'
    show ruby 
    mc '...'
    mc 'Ruby, esse caderno é incrivelmente detalhado. Deve ter levado anos para juntar tanta informação assim, tem certeza que não tem problema que eu fique com ele?'
    ruby 3 'Oh, sem dúvida! Eu tenho outro.' 
    ruby 'Na verdade, eu tenho o hábito de ficar escrevendo cadernos para coisas. '
    ruby 5 'Se eu puder ajudar o novo aluno a ter uma experiência um pouco melhor que a minha, então vale a pena. '
    show black with fade
    'Você e Ruby conversam por mais um tempo, tirando dúvidas e debatendo as estratégias de sobrevivência.' 
    'Mas logo, o sinal toca e vocês trocam despedidas.' 
    'De toda forma, você se sente que aprendeu um pouco mais sobre seu colega ruivo. '
    $ rubyEventsCounter = 2
    return

# Terceira
label rubyEvent2:
    scene corredor with fade
    rub "Como eu queria aquela JPEG SSR Plus..."
    rub "Oh, [player_name]!"
    show ruby 
    mc 'Ruby, eu estava imaginando….'
    mc 'Que outros tipos de cadernos você tem?'
    ruby 3 'Oh, eu tenho vários. Eu tenho um para cada matéria que eu já estudei.' 
    ruby 'Um para cada ano acadêmico, eu tenho alguns falando sobre a administração….'
    show ruby 
    mc 'São todos acadêmicos? Você não tem nenhum pessoal?'
    ruby 2 'Oh, eu tenho alguns desses também.'
    ruby 3 'Vem, eu te mostro os que eu guardo no meu armário. '
    show ruby
    menu:
        "Um dos cadernos chama sua atenção."
        'Caderno de Verde.':
            ruby 3 'Oh, esse é o meu Caderno Guia para Jogos Gacha!'
            ruby 17 'Ele vai ter todas as informações que você precisa para atingir o máximo de sucesso e eficiência em mais de 30 diferentes jogos de Gacha. '
            show ruby 15
            mc 'Oh, você joga tantos Gachas assim?'
            ruby 6 'E-eu? Não, não, não. Eles são para…. Para Python! Sim, eu escrevi para ela. '
            show ruby 29
            mc 'Mas está a sua assinatura. '
            ruby 28 'Eu que escrevi...' 
            show ruby 29
            mc 'E eu nunca vi Python jogando algo. '
            ruby 28 'E-ela tem vergonha.' 
            show ruby 29
            mc 'Ei, se você está mentindo sobre isso, Lua teria feito mais sentido. '
            ruby 25 'Droga, é mes-'
            ruby 28 'Espera! Não! Eu não estou mentindo!'
            show ruby 29
            mc 'Claro….'
            ruby 28 'Enfim…. Esse caderno deve lhe ensinar todos os meios para conseguir os cinco-estrelas que você quer!'
            ruby 8 'Mesmo que ele quase nunca funciona para mim….'
        'Caderno Azul.':
            ruby 2 'Esse é o meu Caderno de Escrita de Cadernos!'
            show ruby 
            mc 'Caderno de Escrita de Caderno?'
            ruby 3 'Isso aí! Ele lhe dá todas as estratégias para conseguir condensar qualquer assunto que você queira em um ou múltiplos cadernos!'
            show ruby 1
            mc 'E como você escreveu ele?'
            ruby 2 'Bem, primeiro eu escrevi o Caderno de Escrita de Cadernos de Escrita, mas esse foi mais um livreto….'
            ruby 'O resto foi só prática e experiência mesmo. '
            ruby 3 'Todo ano eu escrevo uma nova edição, sabe? Para sempre me manter no topo. '
        'Caderno Roxo.':
            ruby 2 'Esse é o meu Caderno de Chás.'
            show ruby 
            mc 'Você gosta de chás?'
            ruby 3 'Chás são fantásticos! E eles tem uma longa história também, sabia?'
            ruby 'Nesse caderno, você vai encontrar tudo, desde diferentes tipos e métodos de preparações de chá, até instruções para como realizar uma cerimônia!'
            show ruby 
            mc 'Você já realizou uma cerimônia?'
            ruby 2 'Bem….'
            ruby 'Eu já pratiquei algumas vezes, mas eu nunca realizei uma de verdade. '
            ruby 16 'Não tinha quem convidar, sabe?'
            ruby 18 'Mas um dia, eu sei que vou preparar uma de verdade!'
    # Junção
    scene corredor with fade
    "Após certo tempo olhando a imensa coleção de cadernos..."
    mc 'E esse caderno vermelho?'
    show ruby 31
    ruby 'NÃO TOCA!'
    'Ruby se joga para frente, tomando o caderno das suas mãos. '
    ruby 32 'Esse- huh….'
    ruby 'Esse caderno foi envenenado!'
    show ruby 
    mc 'Envenenado?'
    ruby 31 'Sim! Qualquer um que tocar nele será afligido por uma paralisação severa!'
    show ruby  32
    mc 'Mas você está tocando.'
    ruby 24 'Eu, hum….'
    ruby 32 'Eu desenvolvi tolerância! Isso!'
    mc 'E eu toquei agora a pouco.'
    ruby 31 'Mas foi por pouco tempo. '
    show ruby 32
    mc 'E eu tenho quase certeza que-'
    ruby 31 'Mas você ainda tocou! Você precisa lavar as mãos rapidamente antes que os efeitos tomem conta. '
    ruby 32 'Vamos, vamos, eu te levo!'
    'Ruby praticamente te arrasta para o banheiro, puxando o Caderno de Lavar Mãos e lhe dando um rápido curso de como fazer. '
    'Depois disso, ele gagueja uma desculpa e diz que precisa ir embora. '
    'Por mais estranho que esse encontro tenha sido, você ainda sente que conhece Ruby um pouco melhor agora….'
    $ rubyEventsCounter = 3
    return

# Quarto (Final)
label rubyEvent3:
    scene corredor with fade
    show ruby with fade
    ruby '...'
    mc '...'
    mc '.... Está um belo clima hoje, né? Parece-'
    ruby 31 'OKAY EU MENTI PARA VOCÊ!'
    show ruby 
    mc '....'
    show ruby 
    mc 'Okay, elabore.'
    ruby 'O caderno não estava envenenado....'
    show ruby 23
    mc 'Eu imaginei isso.'
    ruby 24 'O caderno envenenado é o caderno azul com rosa e roxo, o Caderno Apossematismo.'
    show ruby 23
    mc 'Você realmente tem-'
    ruby 2 'O caderno vermelho é o meu Caderno Presidencial...'
    show ruby 
    mc 'Caderno Presidencial? Tipo, com os diferentes presidentes da república?'
    ruby 2 'Não, com diferentes planos e estratégias para se tornar Presidente de Classe.'
    show ruby
    mc 'Oh....'
    ruby 2 'Eu não fico falando isso para muita gente, mas eu sempre quis ser Presidente de Classe.'
    ruby 16 'Desde que eu entrei na Academia, alguns alunos nunca acharam que eu era bom o suficiente...'
    ruby 'Parecia que só a minha presença aqui era o suficiente para manchar o nome da instituição.'
    ruby 'Nem todo mundo pensava assim, claro. A maioria nem ligava.' 
    ruby 'Como também não faziam nada para impedir que os poucos que pensavam assim me atormentassem todo dia....'
    ruby 2 'Mas Java era uma exceção. Ele fez de tudo para que eu conseguisse me encaixar aqui.'
    ruby 'E, desde então, eu sonhei em um dia ser Presidente de Classe e retribuir o favor.'
    show ruby
    mc 'E por que esconder isso?'
    ruby 2 'Um pouco tempo atrás um cara descobriu o caderno. Ele queria se candidatar, e me ameaçou a menos que eu o entregasse....'
    ruby 'Eu consegui fugir por pouco. Mas acho que ainda estou um pouco inseguro em mostrar para mais gente....'
    show ruby 
    mc 'Ruby, desde que eu cheguei aqui, você foi o que mais se esforçou para me fazer sentir acolhido.' 
    mc 'Você é organizado e caridoso, e daria um excelente presidente. '
    show ruby 37
    'Foram poucas e simples palavras, mas você percebe que foram o suficiente para emocionar Ruby.'
    'Você e Ruby se tornam mais próximos. '
    if itens_estado[4] == True:
        mc "Ruby..." 
        rub 23 "?"
        mc "Eu tenho um presente para você."
        rub 24 "Isso é..."
        rub 25 "UM JPEG SSS+?!"
        rub 37 "Pra mim?"
        $ itens_estado[4] = False
        $ rubyLoveCounter += 3
    $ rubyLoveCounter += 3
    $ rubyEventsCounter = 4
    ruby 36 'Obrigado, [player_name].'
    return