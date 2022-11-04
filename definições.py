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
            'iniciar': 1,
        }
    },
    1: {
        'frases': ['200 anos após a pandemia de 2019, o ser humano se vê novamente no meio de uma nova calamidade.  Dessa vez, é consenso entre a sociedade científica que a Terra se tornará inabitável nos próximos anos. Assim, uma nova missão de reconhecimento para o planeta Gj-504b é realizada. A nova equipe é composta pela comandante da missão, Kayla. Além dela, há também o engenheiro Alef e o senhor Otto, um idoso que participou de uma missão com o mesmo intuito anteriormente. Assim, os três partem atrás de uma garantia de futuro para a humanidade. \n Deseja iniciar a jornada? Digite "Iniciar" '],
        'proximos_estados': {
            '[i]Iniciar': 2,
        }
    },
    2: {
        'frases': ['Me sinto inquieta. Há barulho, são meus colegas conversando, como as pessoas conseguem interagir com as outras logo cedo? Minha noite de sono se resume em um sonho estranho, não consigo me lembrar. Será que devo conversar com eles? \n Digite "1" para se manter calada, "2" para conversar com alguém em específico ou "3" para interagir com os dois colegas ao mesmo tempo.'],
        'proximos_estados': {
            '1': 7,
            '2': 3,
            '3': 4,
        }
    },
    3: {
        'frases': ['Digite "1" para conversar com Alef ou "2" para conversar com Otto.'],
        'proximos_estados':{
            '1': 5,
            '2': 6,
        }   
    },
    4: {
        'frases': ['conversa com os dois'],
        'proximos_estados':{
            '1': 5,
            '2': 6,
        }
    },

    5:{
        'frases': ['Levanto do meu lugar silencioso e me aproximo de Alef. Ele está empenhado em limpar o óculos, olhando de ângulos diferentes para ter certeza que não tem uma poeira sequer.  \n - Como está a Lia? Vi que estava ajustando os canais de comunicação com a Central. [ Ele põe o óculos, seus olhos castanhos claros me encaravam demoradamente. ] \n - Fiz uns ajustes nos parâmetros, ela está funcionando  perfeitamente. Não é Lia? \n - Sim senhor - responde o painel [ Alef da um sorriso satisfeito] \n - Você  está com uma cara ótima! -diz ele num tom sarcástico \n [Não durmo bem desde que a missão começou, a última coisa que estou é ótima.] \n -Estou nervosa com essa missão, sabemos o que está em risc… \n Digite "1" para continuar.'],
        'proximos_estados': {
            '1': 7,
        }
    },

    6: {
        'frases': ['Vejo que Otto está sentado com um livro sob o colo e tento me aproximar, aqui de onde estou ele parece entediado, mas quanto mais me aproximo vejo que ele está ocupado com seus pensamentos, parece está divagando sobre algo, isso automaticamente faz com que eu me arrependa de tentar uma aproximação, perto demais para recuar, tento conversar com ele mesmo assim: - Senhor Otto, tudo ok? \n -… (silêncio) \n -Otto? \n -Oi?! Não escuto muito, quando precisar fala mais alto, comandante. [falou parecendo incomodado com a repentina interferência ao seu monólogo interno] \n -Apenas perguntei se estava tudo bem, o senhor parece preocupado… \n -Estava só pensando… Mas não se preocupe com um velho como eu, não tenho mais nada a perder desde que… Digite "1" para continuar.'],
        'proximos_estados': {
            '1':7
        }
    },
    7: {
        'frases': ['Fim do jogo!'],
        'proximos_estados': {
            'reiniciar': 1
        }
    }
}

partidas = {}
