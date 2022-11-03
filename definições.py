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
            '2': 6
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
