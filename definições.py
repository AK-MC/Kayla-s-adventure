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
        'frases': ['200 anos após a pandemia de 2019, o ser humano se vê novamente no meio de uma nova calamidade.  Dessa vez, é consenso entre a sociedade científica que a Terra se tornará inabitável nos próximos anos. Assim, uma nova missão de reconhecimento para o planeta Gj-504b é realizada. A nova equipe é composta pela comandante da missão, Kayla. Além dela, há também o engenheiro Alef e o senhor Otto, um idoso que participou de uma missão com o mesmo intuito anteriormente. Assim, os três partem atrás de uma garantia de futuro para a humanidade. \n Assim que iniciou a viagem, Kayla sentiu-se inquieta. Em meio ao barulho da conversa de seus colegas de missão, pensou em suas motivações para estar ali. Kayla então decide: \n Digite: \n "1" para  manter-se calada; \n  "2" para conversar com um deles; \n "3" para conversar com os dois simultaneamente;'],
        'proximos_estados': {
            '1': 2,
            '2': 3,
            '3': 4
        }
    },
    2: {
        'frases': ['Um estrondo alto interrompeu a conversa, Kayla olha para os colegas como quem pergunta se eles também escutaram. todos se levantaram, alertas. Otto saca uma arma rapidamente, o barulho cessa mas a tensão aumenta.\n o barulho parece ter vindo de lá - comenta Alef, apontando para o armazém.\n Deixa que eu veja o que foi isso  - disse Otto encaminhando-se para o armazém, onde estão guardadas as armas e os equipamentos. \n Por que ele tem uma arma? \n Kayla encara alef, seu olhar fazia a mesma pergunta \n -deixa que eu vou com ele. \n Kayla vinha atrás de Otto, ele para bruscamente e levanta sua arma na altura do rosto. Olhando para a mesma direção que a arma está apontada, Kayla vê uma menina com uma arma apontada em sua direção. Tenta não parecer atordoada, mas quase de forma automática puxa sua faca, pronta para um possível confronto. A menina, percebendo a reação, começa a intercalar a mira da arma entre os dois. \n-Não tentem nada! [ diz a menina] \n- Calma, calma … - comenta a comandante \n- Eu sei quem voce é, fale para o velhote abaixar a arma! \n- Você primeiro, criança. [responde Otto] \n Ela parece avançar com ódio da provocação, Kayla percebendo que nenhum ali está disposto a baixar a arma, tenta tomar o controle da situação.] \n- Larga a arma Otto! É uma ordem!  - grita Kayla. \n Otto,  como contra sua vontade, desce a arma lentamente.] \n -Sua vez garota! [Tremendo e assustada ela larga também] \n Kayla aproveita e corre para trás da jovem, com a faca em seu pescoço. A invasora se debate na tentativa inútil de escapar. Porém, kayla aperta seus pulsos facilmente. \n -já esperava isso vindo de voce, sua mentirosa! \n Fica calada! \n Alef se aproxima surpreso. \n O que está acontecendo aqui? -pergunta Alef \n Otto vai em direção da garota que se agitava e amarra seus pulsos] \n -também queremos saber - diz kayla \n Digite "1" para tentar conversar com a menina ou "2" para manter-la presa.'], 
        'próximos_estados':{
            '1': 5,
            '2': 6
        }
    },
    3: {
        'frases': ['Digite "1" para conversar com o Sr. Otto ou "2" para conversar com Alef.'],
        'proximos_estados': {
            '1': 5,
            '2': 6
        
        }
    },
    5: {
        'frases': ['Senhor Otto, tudo ok? … \n (silêncio) \n Senhor Otto? \n Oi?! Não escuto muito, quando precisar, pode falar mais alto. [falou parecendo incomodado com a repentina interferência ao seu monólogo interno] \n Apenas perguntei se estava tudo bem, o senhor parece preocupado… \n Estava só pensando… Mas não se preocupe com um velho como eu, não tenho mis nada a perder desde que… \n Deseja continuar? Digite "continuar"'],
        'proximos_estados': {
        'continuar':2
        
        }
    },
    6: {
        'frases': ['-Alef, como vai o rádio? vi que você estava verificando os canais de comunicação. [ele tinha um rosto amigável, apesar de seus olhos cansados] \n -Ajustei os parâmetros das frequências, está tudo funcionando. Como você está? Está com uma cara ótima! \n [Kayla não dormia bem há dias, a última coisa que ela estava era ótima] \n -Boa piada ha ha. Estou nervosa com essa missão, tem muitas coisas em risc….\n Deseja continuar? Digite "continuar"'],
        'proximos_estados': {
        'continuar':2
        }
    },
    4: {
        'frases': ['Fim do jogo!'],
        'proximos_estados': {
            'reiniciar': 1
        }
    }
}

partidas = {}
