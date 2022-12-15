frases = {
    'reiniciado': 'Jogo reiniciado (progresso do jogador apagado).',
    'inventario_insuficiente': 'Sem os recursos necessários para avançar.',
    'canal_privado': 'Por favor, envie mensagens para mim através de canal compartilhado de texto (não pvt).',
    'sem_canal_de_voz': 'Por favor, esteja em um canal de voz para ter a imersão necessária do jogo.',
    'erro': 'I\'m sorry Dave, I\'m afraid I can\'t do that.'
}

estados = {
    0: {
        'frases': ['Digite "iniciar" para começar o jogo.'],
        'proximos_estados': {
            'iniciar': 1
        }
    },
    1: {
        'frases': ['200 anos após a pandemia de 2019, o ser humano se vê novamente no meio de uma nova calamidade.  Dessa vez, é consenso entre a sociedade científica que a Terra se tornará inabitável nos próximos anos. Assim, uma nova missão de reconhecimento para o planeta Gj-504b é realizada. A nova equipe é composta pela comandante da missão, Kayla. Além dela, há também o engenheiro Alef e o senhor Otto, um idoso que participou de uma missão com o mesmo intuito anteriormente. Assim, os três partem atrás de uma garantia de futuro para a humanidade. \n Deseja iniciar a jornada? Digite "continuar" '],
        'proximos_estados': {
            'continuar': 2
        }
    },
    2: {
        'frases': ['Me sinto inquieta. Há barulho, são meus colegas conversando, como as pessoas conseguem interagir com as outras logo cedo? Minha noite de sono se resume em um sonho estranho, não consigo me lembrar. Será que devo conversar com eles? \n Digite "1" para se manter calada, "2" para conversar com alguém em específico ou "3" para interagir com os dois colegas ao mesmo tempo.'],
        'proximos_estados': {
            '1': 7,
            '2': 3,
            '3': 4
        }
    },
    3: {
        'frases': ['Digite "1" para conversar com Alef ou "2" para conversar com Otto.'],
        'proximos_estados':{
            '1': 5,
            '2': 6
        }   
    },
    4: {
        'frases': ['[ Otto lê um livro que parece ter uns 1000 anos, enquanto Alef toma      café ] \n -como vão as coisas ? \n -Alef estava me contando de forma super interessante de como ele ajustou a Lia - comentou Otto, visivelmente incomodado por interromperem sua leitura \n -Certo, qual o nome desse livr….\n Digite "continuar"'],
        'proximos_estados':{
            'continuar': 7
        }
    },
    5:{
        'frases': ['Levanto do meu lugar silencioso e me aproximo de Alef. Ele está empenhado em limpar o óculos, olhando de ângulos diferentes para ter certeza que não tem uma poeira sequer.  \n - Como está a Lia? Vi que estava ajustando os canais de comunicação com a Central. [ Ele põe o óculos, seus olhos castanhos claros me encaravam demoradamente. ] \n - Fiz uns ajustes nos parâmetros, ela está funcionando  perfeitamente. Não é Lia? \n - Sim senhor - responde o painel [ Alef da um sorriso satisfeito] \n - Você  está com uma cara ótima! -diz ele num tom sarcástico \n [Não durmo bem desde que a missão começou, a última coisa que estou é ótima.] \n -Estou nervosa com essa missão, sabemos o que está em risc… \n Digite "1" para continuar.'],
        'proximos_estados': {
            '1': 7
        }
    },

    6: {
        'frases': ['Vejo que Otto está sentado com um livro sob o colo e tento me aproximar, aqui de onde estou ele parece entediado, mas quanto mais me aproximo vejo que ele está ocupado com seus pensamentos, parece está divagando sobre algo, isso automaticamente faz com que eu me arrependa de tentar uma aproximação, perto demais para recuar, tento conversar com ele mesmo assim: - Senhor Otto, tudo ok? \n -… (silêncio) \n -Otto? \n -Oi?! Não escuto muito, quando precisar fala mais alto, comandante. [falou parecendo incomodado com a repentina interferência ao seu monólogo interno] \n -Apenas perguntei se estava tudo bem, o senhor parece preocupado… \n -Estava só pensando… Mas não se preocupe com um velho como eu, não tenho mais nada a perder desde que… Digite "1" para continuar.'],
        'proximos_estados': {
            '1':7
        }
    },
    7: {
        'frases': ['Um estrondo alto interrompeu a conversa, olho para meus colegas como quem pergunta se eles também escutaram. todos se levantaram, alertas. Otto sacou sua arma rapidamente, o barulho cessou, mas a tensão aumentou. Digite "continuar"'],
        'proximos_estados': {
            'continuar': 8
        }
    },
    8: {
        'frases': ['- O barulho parece ter vindo de lá - comenta Alef, apontando para o armazém \n -Vou ver o que foi isso  - disse Otto encaminhando-se para o armazém, onde está guardada as armas e equipamentos. \n -Por que ele tem uma arma? \n Encaro Alef com a mesma expressão confusa, mas determinada a descobrir \n -Deixa que eu vou com ele. \n Digite "continuar"'],
        'proximos_estados': {
            'continuar': 9
        }
    },
    9: {
        'frases': ['Fui atrás de Otto, quase correndo para tentar alcançá-lo, quando ele para bruscamente e levanta sua arma na altura do rosto. Olhando para a direção em que a arma está apontada vejo uma menina, digo menina pois o máximo que ela aparenta ter é 17 anos, com uma arma direcionada a Otto e, consequentemente, a mim também. Esforço-me para não demonstrar o misto de confusão e atordoamento em que me encontro, o esforço se torna inútil quando vejo ela alternar a mira entre eu e o Otto e, quase de forma automática, puxo a faca que estava comigo. A garota, percebendo a reação, grita: \n -Não tentem nada! \n -Por favor, calma! Calma.. está tudo bem. [Falo olhando para ela enquanto tento me aproximar] \n -Não dê ouvidos a essa criança Comandante. [Otto fala, ainda com os olhos cerrados na menina] Percebo que a garota aparenta mais medo do ódio que Otto demonstra que de qualquer outro sentimento, penso em uma alternativa mais arriscada.  \n Otto, abaixe a arma imediatamente! \n Ele tira os olhos da menina e começa a me olhar fixamente como se quisesse entender se havia algum truque. Começa a abaixar a arma lentamente contra a sua vontade ao perceber que minha decisão não mudaria. A menina direciona seu olhar diretamente para mim, compartilhando o mesmo semblante confuso de Otto. Começo a me aproximar dela enquanto falo: \n -Sua vez, garota. Ninguém aqui vai te machucar, tem a minha palavra, quer você acredite ou não. Minha fala parece funcionar, pois mesmo tremendo e assustada ela começa a largar a arma também. Aproveito nesse instante para correr para atrás dela e a imobilizo, ela se debate em uma tentativa de se livrar, mas é inútil pois consigo apertar seus pulsos facilmente já que sou maior.\n -Você me enganou, sua mentirosa! \n -Otto! Vai buscar uma corda. \n Otto pega sua arma e sai correndo da sala em busca da corda, enquanto Alef se aproxima perplexo com a situação que encontra. \n -O que está acontecendo aqui? \n - É o que vamos descobrir. \n Digite "1" para tentar conversar com a invasora, "2" para prende-la '],
        'proximos_estados': {
            '1': 10,
            '2': 11
        }
    },
    10: {
        'frases': ['[Levo a intrusa para o centro da nave, ela não aparenta estar assustada. Quem será ela? e o que faz aqui? Mando ela se sentar] \n -Quem é você e como entrou aqui? \n [ a garota permanece calada] \n fala garota ! - esbraveja otto sem paciência \n [ todos olhavam para ela com curiosidade. Como uma adolecente conseguiu entrar ali sem que ninguém visse? O olhar dela era de revolta. A menina era de origem asiática, e encarava todos sem medo.] \n -Meu nome é Yoko - revela a adolecente \n -Está perdida Yoko? meio longe de casa não? - ironiza Alef \n [ Yoko se mantém quieta, fica evidente que essa é a única informação que teremos.] \n Não quer falar, então não fale. Vamos entrar em contato com a central, eles sabem de tudo e de todos. \n- Abre conexão com a agência, alef. - comando \n [Alef passa alguns minutos tentando uma conexão] \n -Não sei o que está acontecendo, não estou conseguindo estabelecer conexão com a Terra. \n -A Lia não funciona? [Me aproximo dele levemente preocupada] \n -Não, eu tenho certeza que está funcionando, mas o canal de comunicação está apresentando instabilidade, não consigo encontrar a nossa frequência. \n -É melhor sairmos daqui, rápido.[Diz Otto de forma alarmante] \n -Você sabe o que está acontecendo? -Questiono \n -A nave deve está sofrendo interferência pelos asteroides que tem nessa região. Acreditem em mim, vocês não vão querer continuar aqui por muito tempo… \n Digite "1" para permanecer no mesmo lugar até os asteroides passarem ou "2" para sair dali.'],
        'proximos_estados': {
            '1': 12,
            '2': 13
        }
    },
    11: {
        'frases': [' Após me certificar que a menina estava bem amarrada, deixo ela em uma sala vazia e retomo a sala de comando onde meus colegas me aguardavam. \n -Temos que nos conectar com a agência, perguntar quem diabos é essa garota [Otto fala com irritação antes mesmo de eu me aproximar o suficiente. \n -Sim, vamos fazer isso imediatamente, ela não parece ser vinculada a nenhum grupo terrorista, mas precisamos entender como ela entrou na nave. \n -Vou abrir conexão com a Terra - Alef se dirige para o painel de controle. enquanto começo a andar inquietamente pela sala, pensando em tudo que acabou de acontecer. 10 minutos passam-se até que vendo Alef  desordenado, questiono se está tudo bem. \n-Estou tentando mas tem algo de estranho, tem uma frequência interferindo na conexão. \n -Mais isso agora, ótimo! - resmunga Otto \n -A Lia está com problema? - Me aproximo de Alef buscando entender. \n -Não,eu tenho certeza que está funcionando, mas o canal de comunicação está apresentando instabilidade, não consigo encontrar a nossa frequência. \n Percebo que a tensão toma conta do ambiente, principalmente pela expressão corporal de Otto que muda de irritado para aparentemente assustado, até que então fala de forma alarmante: \n -É melhor sairmos daqui,rápido! \n -Por que? - Questiono-o. \n -A nave deve estar sofrendo interferência por um aglomerado de asteroides. São muito comuns nessa região que estamos. Temos que sair daqui logo.\n Digite Digite "1" para permanecer no mesmo lugar até os asteroides passarem ou "2" para sair dali.'],
        'proximos_estados': {
            '1': 12,
            '2': 13
        }
    },
    12: {
        'frases': ['Vamos ficar parados até os asteroides irem para outra direção - ordeno \n -Acho uma péssima ideia - diz otto com arrogância \n -iremos permanecer- digo firmemente \n[ A nave foi atingida enquanto eles discutiam. A lateral da nave colidiu com diversos asteroides, que agitaram um pouco a nave. Na direção deles vinham muito mais asteroides. \n -Droga…temos que sair daqui agora, se não pode danificar mais. Vou redirecionar a nave.- diz Alef [ Alef corre até o painel, mas não consegue controlar. parece que a batida interferiu no sistema. \n Digite "continuar"]'],
        'proximos_estados': {
            'continuar': 14
        }
    },
    13: {
        'frases': ['- temos que sair desse lugar! Alef corre para o painel de controle da nave, quando de repente algo colide com a nave, automaticamente olham para o painel à frente e vêem as luzes de alerta piscando, a lateral foi atingida. Com isso, a sirene toca, olho para Alef, sua expressão é de alarme, tenho que fazer algo. Disparo em direção do painel de comando para tentar redirecionar a nave para outro lugar o mais rápido possível. Mas antes que eu consiga alcançar um asteroide colide com a nave me fazendo cair com a colisão. \n Digite "continuar"'],
        'proximos_estados': {
            'continuar':14
        }
    },
    14: {
        'frases': ['- Consegui consertar o painel para fazer a nave sair do lugar, mas o tanque e outras partes foram atingidas - anuncia Alef- Vamos tentar um pouso em algum planeta próximo, ou não conseguiremos chegar até o Gj-504b.- \n O único planeta dessa galáxia com condições aceitáveis para pouso é o Osíris, mas não acredito que seja uma boa alternativa, é um planeta muito hostil e desconhecido. [avisa Otto] \n - Na situação em que estamos, qualquer coisa pode ser considerada. Kayla? \n -Alef está certo, precisamos tentar! \n Digite "continuar"'],
        'proximos_estados': {
            'continuar': 15
        }
    },
    15: {
        'frases': ['- Conseguimos pousar sem grandes problemas, aviso aos colegas então que permaneceremos aqui até o Alef conseguir consertar a nave.\n -Eu li sobre esse planeta, existem elementos bons que podemos usar. Você deve ir em busca, Alef. Eu até iria mas já estou tão velho que duvido que teria alguma serventia - comenta otto \n Digite "continuar"'],
        'proximos_estados': {
            'continuar': 16
        }  
    },
    16: {
        'frases': ['Alef vai sair para explorar esse planeta, estou nervosa. Não quero que ele vá, estou com um pressentimento ruim. Ele anda de lá para cá pegando equipamentos para sua busca. \n -Toma bastante cuidado,  não sabemos o que tem lá fora \n -não se preocupe capitã, já estou crescidinho - ele fala de forma brincalhona. \n difícil não me preocupar, gosto de Alef. \n -Peguei tudo que preciso. Certo, até logo! \n  -Me mantenha informada, qualquer coisa que pudermos usar é bem vindo. -Nos olhamos no fundo dos olhos, ele parecia querer dizer alguma coisa \n -Eu… ele hesitou -   Eu não vou demorar  -Ele se afasta e dá um comando para Lia abrir a porta. \n Digite "continuar"'],
        'proximos_estados': {
            'continuar': 17
        }  
    },
    17: {
        'frases': ['Após a saída de Alef fico sozinha com otto \n -Verifique como está Yoko, leve algo para ela comer. -ordeno \n Ele sai de sua poltrona com uma rapidez impressionante. \n- Sim comandante \n Sento na minha cadeira, coloco o comunicador e logo escuto a respiração de Alef \n -consegue me escutar? -pergunto \n  sim - ele responde \n Pela visão que tenho  de sua câmera, percebo um ambiente estranho. A superfície cor arroxeada, o lugar é um breu absoluto.  \n -Vou seguir para o norte, talvez eu encontre metal por lá \n - Certo, não se afaste muito. \n  Escuto os sons de conversa, por que Otto está demorando? o barulho se intensifica, parece uma briga. \n -Ah droga! a garota \n - já volto Alef \n - Ok \n Digite "continuar"'],
        'proximos_estados': {
            'continuar': 18
        }  
    },
    18: {
        'frases': [' Me encaminho para onde eles estão. Quanto mais me aproximo, os sons ficam mais reconhecíveis. Escuto Otto falando evidentemente furioso: \n -Você realmente está me dizendo que a única evidência que você tem que eu sou culpado pelo o que aconteceu com seu pai é que eu também estava naquela nave? \n -Você sabe que não, a última ligação que meu pai fez foi comigo, ele disse o quanto estava preocupado com o rumo da missão e como você parecia estar interessado em pousar no Gj-504b, mesmo sem nenhuma grande necessidade \n -Não vou discutir o que era, ou não, necessário com uma criança, você não sabe nada sobre o que aconteceu, exatamente como seu pai não sabia [Otto interrompe o que estava falando ao me ver, os dois me encararam, provavelmente perguntando-se desde quando eu estava ali. Toda aquela conversa era confusa demais para mim, mas agora posso começar a entender o porquê dessa menina estar aqui, preciso conversar com Otto para saber o que ele descobriu. \n -Otto, me siga por favor. \n- Sim - diz enquanto confirma com a cabeça, quase de forma serviçal, algo incomum para a postura recorrente. Quando eu ia questionar o que aconteceu entre ele e a Yoko, o comunicador do Alef emite um sinal sonoro. Procuro entender se ele está tentando entrar em contato, mas o sinal para, tento então checar a câmera do seu uniforme, mas parece está desligada começo a me preocupar, o que será que está acontecendo com o Alef, ele deve estar precisando de ajuda. Busco falar isso para Otto, que agora me olha de forma bem mais tranquila do que quando o encontrei. \n -Preciso encontrar o Alef! \n -Ele vai voltar, não deve ser nada de mais \n -Como pode ter tanta certeza? ele pode estar machucado ou precisando de ajuda. \n -Precisamos esperar, não temos certeza de onde ele está. Vamos tentar contato novamente, se ele não responder, em algumas horas eu mesmo irei atrás dele \n Digite "continuar"'],
        'proximos_estados': {
            'continuar': 19
        }  
    },
    19:{
        'frases': [ ' A porta se abre, olhamos e lá estava Alef. corro em sua direção, para ver como ele está. Ele parece meio grogue. /n -O que aconteceu? Perdemos o contato com você. \n -Eu não sei. Estava muito escuro, algo pulou no meu pescoço. \n olho uma picada em seu pescoço, tem uma aparência esverdeada \n Conseguiu? temos que sair daqui. \n -Sim, consegui. Vou começar imediatamente. \n- Eu te ajudo, Alef! Mas antes eu tenho que falar algo com a Yoko. \n Digite "continuar"'],
        'proximos_estados':{
            'continuar':20
        }
    },
 20:{
        'frases': [ 'Chegando à sala em que Yoko está, vejo ela sentada no chão parecendo concentrada. \n -Ei menina, a essa altura você já deve saber que não conseguimos contato com a central, se quiser sair dessa sala vou precisar saber algumas informações sobre você. \n -Seu amigo já esteve aqui mais cedo, as informações de que precisa ele sabe. \n -Aquilo que presenciei não parecia muito com uma conversa. Vamos, estou tentando te ajudar, por que o Otto falou sobre seu pai? Vocês já se conheciam antes, não é mesmo? \n -Não, meu pai é quem conhecia ele. - A garota falou mostrando pouco interesse em continuar uma conversa. \n Não quer continuar falando, hum?! -Falo enquanto sento no chão ao lado dela, separadas pela porta de vidro da sala em que ela está retida. -Não sei quando sairemos daqui. Alef está tentando consertar a nave,isso pode levar horas ou dias, Vou te contar minha motivação para está aqui e talvez você me conte um pouco mais sobre você. \n Yoko se mantém calada, mas vejo que ela parece mais interessada. \n -Meu marido participou das últimas 3 missões, você é nova demais, mas deve saber que as missões AK-MC32 e AK-MC33 foram um fracasso completo, a última missão, porém, chegamos tão perto, nunca vou entender o que aconteceu, o porque não conseguimos. Você se lembra da última vez que a humanidade tentou, não é mesmo, 6 anos atrás. Meu marido era o capitão dessa missão, ele estava obcecado, tinha certeza que tudo daria certo, revisou todos os erros cometidos anteriormente, todas as rotas. No fim, todos sabemos como terminou a missão, Apenas Otto voltou,uma tripulação de 8 pessoas, mais treinadas e inteligentes do que minha equipe de agora, quase todos mortos. É por isso que estou aqui, quero continuar o que ele começou, não faço pelo futuro da humanidade, só quero dar sentido ao trabalho que ele dedicou a vida. \n -Sinto muito, meu pai estava nessa missão também. \n Digite "continuar" para descobrir um pouco mais sobre a históŕia de Yoko'],
        'proximos_estados':{
            'continuar':21
        }
    },
    21:{
        'frases': ['-Seu pai? - Olho para ela sem esconder minha surpresa. \n -Meu pai era o Astronauta Shin Takahashi, eu tinha  11 anos quando ele foi para essa missão, ele conversava comigo quase todos os dias, usando o painel de controle da nave em conexão a um dispositivo que ele mesmo construiu para mim antes de partir. Tenho motivos para acreditar que o fracasso inexplicável dessa missão não foi um acaso, meu pai não morreu por um erro técnico ou de cálculo, foi por interesse, é o que quero provar, vim aqui atrás disso. \nAchei você ! Alef enlouqueceu, ele tentou me agredir, acredito que ele esta tendo alucinações. - Otto interrompe a conversa e diz apavorado \n -Vamos lá ver - digo enqunato aperto o botão da "cela" e solto Yoko. -vamos Yoko, você vai com a gente. \n Otto parece não gostar da minha atitude mas nao diz nada. fomos a cabine de controle achamos Alef, ele está ainda soldando. ele não parecia nada bem \n -isso já está bom Alef, vamos decolar - diz otto \n Alef não responde. Ele olha ao redor, encarando cada um de nós como se tentasse nos reconhecer, seus olhos estavam vermelhos e seu rosto estava pálido \n Solta isso garoto! - Diz Otto, impaciente. Encaminha-se em direção ao Alef.'],
        'proximos_estados':{
            'continuar':22
        }
    },
    22:{
        'frases': ['Alef continua trabalhando como se não escutasse Otto que se aproxima e, forçando-o a parar o empurra, Alef então vira-se em direção ao senhor e possuído por uma fúria que nunca vi em seu rosto acerta Otto com um soco, me espanto com esse golpe, e sem tempo para pensar no que devo fazer tento me aproximar, mas yoko segura meu braço e me olha como se pedisse para que não tentasse nada, enquanto isso, Alef tenta se aproximar de Otto em mais uma tentativa de atingi-lo, Otto se desvia instintivamente e parece buscar a arma que tinha antes, Alef parece perceber isso e interrompe esse movimento com um chute na altura do estômago o que deixa o senhor, aparentemente, sem ar, se curvado até que cai com as duas mãos apoiadas no chão. Alef se aproxima dele e lhe direciona um soco no rosto, mesmo com Otto caído e sem reação, Alef continua a socar, nessa hora me solto de Yoko procuro minha arma de choque, me aproximo de Alef o máximo que consigo, pois sinto que nesse estado, nem mesmo eu conseguiria controlá-lo, aproximo meu dispositivo de choque em seu pescoço até que ele fique completamente inconsciente. Tiro ele de cima de Otto e me direciono para Yoko: \n -Busque uma corda para mim, por favor, você sabe onde encontrar. \n Ela sai, enquanto tenta ajudar Otto a se levantar. \n "Digite continuar"'],
        'proximos_estados':{
            'continuar': 23
        }
    },
    23: {
        'frases': ['Otto segura o pacote de gelo em seu rosto,depois de amarrar Alef deixamos no depósito onde Yoko ficou. \n -O que deu naquele cara? - questiona Yoko \n -Nao faco ideia, Alef nao é desse jeito. algo aconteceu enquanto ele foi lá fora que o deixou assim. - digo \n -Não venha defender seu namoradinho,você viu o que ele fez comigo ! - esbraveja otto \n -Ele não é meu namorado, e sim eu vi. Ele está fora de si,apresenta um risco a essa missão nesse momento. \n Vamos deixá-lo aqui e temos que partir. Ainda temos uma missão para concluir e nosso tempo está acabando, você sabe disso. - diz otto \n Digite "1" para deixar Alef no planeta e seguir com a missão ou "2" para leva-lo'],
        'proximos_estados':{
            '1':24,
            '2':26
        }
    },
    24: {
        'frases': ['Vocês vão abandonar ele aqui? Ele vai morrer. - comenta yoko \n -Eu não quero deixar Alef, sei que ele não é assim, ele nunca iria agredir otto. Mas eu jurei continuar o que o meu falecido marido começou \n -Ele vai ficar. - decido \n Saio da sala e volto ao trabalho que Alef estava fazendo antes de tudo começar. Investigo se a nave tem condições mínimas para decolar e, aparentemente, está tudo certo, Otto estava certo, se tivéssemos deixado o Alef naquele estado continuar a mexer aqui, poderíamos ter perdido tudo. Volto para onde deixamos o Alef decidida a acompanhar ele até fora da nave, nunca poderei me perdoar, sei que essa decisão significa deixá-lo para morrer, não posso fingir que não sei, mas não posso perder tudo agora, jurei que iria até às últimas consequências por essa missão. Encontro Alef acordando, meio confuso, sem entender o que está acontecendo. Ele me vê e parece tentar pronunciar meu nome, mas o som não sai, abro a sala em que ele está e ajudo-o a levantar, ele anda com dificuldade  e com as mãos ainda presas leva-as até a cabeça que parece estar doendo. \n -Alef, sei que você não está bem, e não espero que você me perdoe pelo que vou fazer, mas preciso que me acompanhe até a saída. -Falo tentando não chorar. \n Fora da nave, caminho com ele até uma distância segura, ele parece cansado da caminhada, falo para ele sentar. Sentado, Alef fecha os olhos. \n -Preciso ir, agora. -Falo enquanto desamarro suas mãos, e novamente aplico a arma de choque, dessa vez por menos tempo, só preciso voltar para a nave antes que ele acorde. Digite "continuar"'],
        'proximos_estados': {
            'continuar': 25
        }
    },
    25:{
        'frases':['A nave lança-se no espaço com certa dificuldade, estamos viajando há algumas horas, perdi a noção do tempo. \n -vou deixar o meu no automático, me chame se precisar. - digo para Otto, enquanto tiro meu cinto e vou em direção a Yoko. Dou alguns passos, até que escuto Lia falando: \n ERRO! ERRO! ATENÇÃO ERRO. \n Me volto para o painel e vejo que as luzes do painel estão piscando, volto correndo para meu lugar e tento entender o que está acontecendo, os níveis de energia estão diminuindo muito rapidamente. A pŕopria iluminação da nave diminui e Lia continua anunciando erros. Não sei o que fazer, peço para Otto assumir minha posição enquanto vou correndo a fonte de energia verificar se há algum problema na parte física que Alef estava tentando consertar ou se o sistema da nave não consegue identificar esse tipo de alimentação. Após procurar por qualquer coisa parecida com um vazamento, ou algo parecido, constato que é o sistema da nave. Esse sistema foi desenvolvido pelo Alef, nem mesmo Otto saberia comandar as funcionalidades. Percebendo isso, não me desespero, sei que não há mais nada que possamos fazer. Me encosto na parede e vou descendo com as mãos apoiadas na cabeça, até estar completamente sentada no chão. Nesse ponto, sorrio ao perceber que tive tanto medo que a missão falhasse por interferência de outra pessoa que deixei um homem para trás, e foi justamente isso que tornou impossível completar. Deseja voltar ao estado de decisão sobre deixar ou não Alef? Digite "1" para sim e "2" para não.'],
        'proximos_estados':{
            '1': 23,
            '2': 30
        }
    },
    26: {
        'frases':['Vocês vão abandonar ele aqui? Ele vai morrer. - comenta yoko \n Eu não quero deixar Alef, sei que ele não é assim.E ele é o engenheiro da tripulação, ele sabe melhor do que ninguem como essa nave funciona. \n -Não vamos abandonar ele. Ele faz parte da equipe, e sei que ele vai melhorar. - digo decidida \n saio da sala e vou vê Alef. Entro no depósito, ele está deitado na cama , amarrado ainda. Ele parece tão calmo dormindo, muito diferente de antes. volto para a cabine de controle, Yoko e otto já estão lá, acho que estão esperando uma atitude minha. \n Digite "continuar"'],
        'proximos_estados': {
         'continuar': 27
        }
    },
    27: {
        'frases': [''

        ]
    }
}



canais_de_voz = {}
