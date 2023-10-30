label semana2_dia13:
    "Hoje é dia de prova"
    call prepare_battle_1 from _call_prepare_battle_1
    "Após a prova..."
    call conversa_dia13 from _call_conversa_dia13
return

label conversa_dia13:
    scene black
    show text "Dia 13" at truecenter
    pause 2
    scene library with dissolve
    play music "audio/music (2).mp3" volume 0.5
    
    "Você se encontra com Prolog na biblioteca para enfim terminar o trabalho passado por Ada."
    
    show prolog 5 with moveinleft
    mc "E então, o resto do grupo já entregou o que precisava?"
    show prolog 2
    pro "Mas é claro que sim! Agora, cabe a nós colocar a mão na massa."
    show prolog
    mc "Certo, então vamos começar com isso. Quanto mais cedo começarmos, mais cedo acabamos."
    show prolog 10
    pro "Não diga isso, até parece que não quer passar seu sábado comigo."
    show prolog 7
    mc "O problema não é você, e sim o que estamos fazendo."
    show prolog 25
    pro "Então tá decidido, da próxima vez que formos passar a tarde juntos vamos para um lugar mais legal. Eu me diverti bastante trabalhando com você nessa semana, então seria legal fazermos algo junto que não seja resolver uma emergência."
    show prolog 26
    "Aquela conversa começava a lhe deixar um pouco envergonhado."
    show prolog 7
    mc "C-claro, e aonde você gostaria de ir?"
    show prolog 26
    pro "Ao jardim botânico."
    show prolog 6
    mc "Não esperava ouvir isso."
    show prolog 2
    pro "Eu acho que você ainda tem uma imagem errada sobre mim"
    show prolog 26
    pro "Enfim, chega de enrolação e vamos lá começar isso!"
    mc "De acordo."
    show prolog 5
    "Você passa o resto do dia trabalhando na documentação do projeto com Prolog. É uma tarefa árdua, mas, sinceramente, ter aquela garota como sua companhia fez com que o tempo passasse assustadoramente rápido. Ao terminar tudo, uma certa melancolia lhe atingiu enquanto vocês se despediam."
    hide prolog with dissolve
    scene black with dissolve
    mc "Na verdade, ela é bem mais do que todos dizem..."

    return

