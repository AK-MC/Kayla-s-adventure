frases = {
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
            'continuar': 14
        }
    },
    
partidas = {}
