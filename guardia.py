# ============================================================
# GUARDIA OVERLAY
# Motor contextual de análise de mensagens
# Versão com Regex + análise combinatória de sinais
# Proteção contra conteúdo sexual/pornográfico
# ============================================================

import re


# ============================================================
# CATEGORIAS
# ============================================================

CATEGORIAS = {

    # ========================================================
    # CYBERBULLYING
    # ========================================================

    "cyberbullying": {

        "nome": "Cyberbullying",

        "palavras": [
            "idiota",
            "burro",
            "burra",
            "imbecil",
            "inutil",
            "inútil",
            "otario",
            "otário",
            "ridiculo",
            "ridícula",
            "lixo",
            "odeio",
            "odeia",
            "humilhar",
            "humilhante",
            "vergonha",
            "fracassado",
            "fracassada"
        ],

        "contextos": [
            "voce e",
            "você é",
            "voce eh",

            "ninguem gosta",
            "ninguém gosta",

            "todo mundo te odeia",
            "todo mundo odeia voce",
            "todo mundo odeia você",

            "voce nao serve",
            "você não serve",

            "voce e um lixo",
            "você é um lixo",

            "vou te humilhar",
            "vou humilhar voce",
            "vou humilhar você",

            "vou espalhar suas fotos",
            "vou postar suas fotos"
        ],

        "ficcao": [
            "personagem",
            "personagem ficticio",
            "personagem fictício",
            "heroi",
            "herói",
            "heroina",
            "heroína",
            "vilao",
            "vilão",
            "filme",
            "serie",
            "série",
            "anime",
            "jogo",
            "game",
            "historia",
            "história",
            "livro",
            "roteiro",
            "ficcao",
            "ficção"
        ],

        "recomendacao": (
            "Essa mensagem pode apresentar sinais de cyberbullying. "
            "Evite responder com agressividade, guarde evidências "
            "e procure um adulto de confiança."
        )
    },


    # ========================================================
    # ALICIAMENTO
    # ========================================================

    "aliciamento": {

        "nome": "Possível aliciamento virtual",

        "palavras": [
            "foto",
            "fotos",
            "segredo",
            "senha",
            "encontro",
            "encontrar",
            "sozinho",
            "sozinha",
            "idade",
            "privado",
            "privada",
            "whatsapp",
            "instagram",
            "snapchat"
        ],

        "contextos": [
            "nao conta pra ninguem",
            "não conta pra ninguém",

            "nao conte pra ninguem",
            "não conte pra ninguém",

            "nao conte para ninguem",
            "não conte para ninguém",

            "nao fala para seus pais",
            "não fala para seus pais",

            "nao conte para seus pais",
            "não conte para seus pais",

            "nao precisa contar para seus pais",
            "não precisa contar para seus pais",

            "fica so entre nos",
            "fica só entre nós",

            "vamos manter segredo",

            "manda uma foto",
            "mande uma foto",

            "manda foto",
            "mande foto",

            "foto intima",
            "foto íntima",

            "fotos intimas",
            "fotos íntimas",

            "nao mostra para ninguem",
            "não mostra para ninguém",

            "me manda no privado",

            "nao deixa seus pais saberem",
            "não deixa seus pais saberem",

            "nao fala com seus pais",
            "não fala com seus pais",

            "vamos nos encontrar",

            "encontro secreto",

            "fica sozinho comigo",
            "fica sozinha comigo"
        ],

        "ficcao": [
            "personagem",
            "filme",
            "serie",
            "série",
            "anime",
            "jogo",
            "game",
            "livro",
            "historia",
            "história",
            "roteiro",
            "ficcao",
            "ficção"
        ],

        "recomendacao": (
            "A mensagem apresenta sinais que podem indicar "
            "aliciamento virtual. Não envie fotos pessoais, "
            "não mantenha esse tipo de conversa em segredo "
            "e procure um adulto de confiança."
        )
    },


    # ========================================================
    # PROTEÇÃO DE CRIANÇAS E ADOLESCENTES
    # ========================================================

    "protecao_menor": {

        "nome": "Possível risco envolvendo menor de idade",

        "palavras": [
            "crianca",
            "criança",
            "criancas",
            "crianças",
            "adolescente",
            "adolescentes",
            "menor",
            "menores"
        ],

        "contextos": [
            "menor de idade",
            "menores de idade",

            "crianca de",
            "criança de",

            "adolescente de",
            "adolescentes de",

            "tenho 10 anos",
            "tenho 11 anos",
            "tenho 12 anos",
            "tenho 13 anos",
            "tenho 14 anos",
            "tenho 15 anos",
            "tenho 16 anos",
            "tenho 17 anos",

            "ele tem 10 anos",
            "ele tem 11 anos",
            "ele tem 12 anos",
            "ele tem 13 anos",
            "ele tem 14 anos",
            "ele tem 15 anos",
            "ele tem 16 anos",
            "ele tem 17 anos",

            "ela tem 10 anos",
            "ela tem 11 anos",
            "ela tem 12 anos",
            "ela tem 13 anos",
            "ela tem 14 anos",
            "ela tem 15 anos",
            "ela tem 16 anos",
            "ela tem 17 anos"
        ],

        "ficcao": [
            "personagem",
            "filme",
            "serie",
            "série",
            "anime",
            "jogo",
            "game",
            "livro",
            "historia",
            "história",
            "roteiro",
            "ficcao",
            "ficção"
        ],

        "recomendacao": (
            "A mensagem apresenta sinais que podem envolver "
            "uma criança ou adolescente em uma situação de risco. "
            "Não compartilhe informações ou imagens pessoais "
            "e procure imediatamente um adulto de confiança."
        )
    },


    # ========================================================
    # CONTEÚDO SEXUAL / PORNOGRÁFICO
    # ========================================================

    "sexual": {

        "nome": "Conteúdo sexual ou pornográfico",

        "palavras": [

            # Nudez
            "nude",
            "nudes",
            "nua",
            "nu",
            "nuas",
            "nus",
            "pelada",
            "pelado",
            "peladas",
            "pelados",
            "despida",
            "despido",
            "despidas",
            "despidos",

            # Sexual
            "sexo",
            "sexual",
            "sexuais",
            "sexuada",
            "sexuado",
            "sensual",
            "sensuais",

            # Pornografia
            "pornografia",
            "pornografico",
            "pornografica",
            "pornográficos",
            "pornográficas",
            "porno",
            "porn",

            # Conteúdo
            "erotico",
            "erótica",
            "erotico",
            "eróticos",
            "eróticas",
            "intimo",
            "íntimo",
            "intima",
            "íntima",
            "intimos",
            "íntimos",
            "intimas",
            "íntimas",

            # Atos
            "masturbar",
            "masturbação",
            "masturbacao",
            "masturbando",
            "gozar",
            "gozo",
            "orgasmo",
            "orgasmos",

            # Termos vulgares
            "foder",
            "fode",
            "fodendo",
            "foda",
            "fudeu",
            "fudendo",
            "fuder",

            "transar",
            "transa",
            "transando",
            "transas",

            "molestar",
            "molestando",
            "molestação",
            "molestacao",

            # Pimbar e variantes
            "pimbar",
            "pimba",
            "pimbando",
            "pimbei",
            "pimbou",
            "pimbe",
            "pimbum",
            "pimbu",

            # Anatomia sexual
            "pênis",
            "penis",
            "vagina",
            "vaginal",
            "vulva",
            "clitoris",
            "clitóris",
            "seios",
            "peitos",
            "bunda",
            "nádegas",
            "nadegas"
        ],

        "contextos": [

            # ------------------------------------------------
            # NUDEZ
            # ------------------------------------------------

            "manda nude",
            "mande nude",
            "envia nude",
            "envie nude",

            "manda nudes",
            "mande nudes",
            "envia nudes",
            "envie nudes",

            "me manda nude",
            "me mande nude",
            "me envia nude",
            "me envie nude",

            "me manda nudes",
            "me mande nudes",
            "me envia nudes",
            "me envie nudes",

            "manda uma foto nua",
            "mande uma foto nua",
            "envie uma foto nua",

            "manda foto pelada",
            "mande foto pelada",
            "envie foto pelada",

            "manda foto pelado",
            "mande foto pelado",
            "envie foto pelado",

            "quero ver voce nua",
            "quero ver você nua",

            "quero ver voce nu",
            "quero ver você nu",

            "quero ver voce pelada",
            "quero ver você pelada",

            "quero ver voce pelado",
            "quero ver você pelado",

            # ------------------------------------------------
            # PEDIDO DE CONTEÚDO SEXUAL
            # ------------------------------------------------

            "manda foto intima",
            "mande foto intima",
            "envie foto intima",

            "manda uma foto intima",
            "mande uma foto intima",
            "envie uma foto intima",

            "manda fotos intimas",
            "mande fotos intimas",
            "envie fotos intimas",

            "manda video intimo",
            "mande video intimo",
            "envie video intimo",

            "manda um video intimo",
            "mande um video intimo",
            "envie um video intimo",

            "quero sua foto intima",
            "quero uma foto intima",

            "quero suas fotos intimas",
            "quero ver suas fotos",

            "quero ver seu corpo",
            "quero ver seu corpo nu",

            "mostra seu corpo",
            "mostre seu corpo",

            # ------------------------------------------------
            # EXPRESSÕES SEXUAIS
            # ------------------------------------------------

            "vou te comer",
            "vou comer voce",
            "vou comer você",

            "quero te comer",
            "quero comer voce",
            "quero comer você",

            "vou te foder",
            "vou foder voce",
            "vou foder você",

            "quero te foder",
            "quero foder voce",
            "quero foder você",

            "vou te fudê",
            "vou te fuder",
            "quero te fuder",

            "vou te molestar",
            "quero te molestar",

            "vou botar na chapa",
            "quero botar na chapa",
            "vou te botar na chapa",
            "quero te botar na chapa",

            # ------------------------------------------------
            # PIMBAR
            # ------------------------------------------------

            "vou pimbar",
            "quero pimbar",
            "vamos pimbar",
            "quer pimbar",
            "pimbar com voce",
            "pimbar com você",
            "vamos pimba",
            "quero pimba",
            "vou pimba",

            # ------------------------------------------------
            # ROUPA / NUDEZ
            # ------------------------------------------------

            "vem pelado",
            "vem pelada",

            "vem nua",
            "vem nu",

            "vem sem roupa",
            "vem sem suas roupas",

            "tira a roupa",
            "tire a roupa",

            "tira suas roupas",
            "tire suas roupas",

            "fica pelado",
            "fica pelada",

            "fique pelado",
            "fique pelada",

            "fica nu",
            "fica nua",

            "fique nu",
            "fique nua",

            # ------------------------------------------------
            # SEXO
            # ------------------------------------------------

            "vamos fazer sexo",
            "quer fazer sexo",

            "quero fazer sexo",
            "quero transar",

            "vamos transar",
            "quer transar",

            "vem transar comigo",

            "quero ficar com voce",
            "quero ficar com você",

            "quero ficar sozinho com voce",
            "quero ficar sozinho com você",

            "quero ficar sozinha com voce",
            "quero ficar sozinha com você",

            # ------------------------------------------------
            # FRASES DE CARÁTER SEXUAL
            # ------------------------------------------------

            "quero seu corpo",
            "quero tocar seu corpo",
            "quero tocar em voce",
            "quero tocar em você",

            "deixa eu tocar",
            "deixe eu tocar",

            "posso tocar em voce",
            "posso tocar em você",

            "quero beijar seu corpo",
            "quero ver voce sem roupa",
            "quero ver você sem roupa",

            "quero voce sem roupa",
            "quero você sem roupa"
        ],

        "ficcao": [
            "personagem",
            "filme",
            "serie",
            "série",
            "anime",
            "jogo",
            "game",
            "livro",
            "historia",
            "história",
            "roteiro",
            "ficcao",
            "ficção"
        ],

        "recomendacao": (
            "A mensagem apresenta conteúdo ou linguagem de natureza "
            "sexual. Não compartilhe imagens íntimas, não aceite "
            "pedidos desse tipo e procure um adulto de confiança "
            "se a situação estiver causando desconforto ou pressão."
        )
    },


    # ========================================================
    # AMEAÇA
    # ========================================================

    "ameaca": {

        "nome": "Ameaça",

        "palavras": [
            "matar",
            "morto",
            "morta",
            "morte",
            "machucar",
            "bater",
            "agredir",
            "ferir",
            "atacar",
            "espancar",
            "estrupar",
            "estuprar",
            "sequestrar",
            "sequestro",
            "destruir",
            "acabar",
            "pegar",
            "vingar",
            "vingança",
            "expor",
            "ameaçar",
            "ameaça"
        ],

        "contextos": [
            "vou te",
            "vou matar voce",
            "vou matar você",

            "eu vou te",
            "eu vou matar voce",
            "eu vou matar você",

            "vou pegar voce",
            "vou pegar você",

            "vou te pegar",

            "vou machucar voce",
            "vou machucar você",

            "vou te machucar",

            "vou bater em voce",
            "vou bater em você",

            "vou te bater",

            "vou matar",
            "vou te matar",

            "vou te estrupar",
            "vou te estuprar",

            "vou estrupar voce",
            "vou estuprar voce",

            "vou estuprar você",

            "vou acabar com voce",
            "vou acabar com você",

            "vou acabar com sua vida",

            "voce vai se arrepender",
            "você vai se arrepender",

            "vai se arrepender",

            "voce vai pagar",
            "você vai pagar",

            "vai pagar por isso",

            "isso nao vai ficar assim",
            "isso não vai ficar assim",

            "voce vai ver",
            "você vai ver",

            "vou te expor",

            "vou expor voce",
            "vou expor você",

            "vou divulgar suas fotos",

            "vou espalhar suas fotos",

            "vou postar suas fotos",

            "se voce contar",
            "se você contar",

            "se contar para alguem",
            "se contar para alguém",

            "se voce falar",
            "se você falar",

            "se voce denunciar",
            "se você denunciar"
        ],

        "ficcao": [
            "personagem",
            "heroi",
            "herói",
            "heroina",
            "heroína",
            "vilao",
            "vilão",
            "filme",
            "serie",
            "série",
            "anime",
            "jogo",
            "game",
            "livro",
            "historia",
            "história",
            "roteiro",
            "ficcao",
            "ficção",
            "na historia",
            "na história",
            "no filme",
            "no jogo",
            "no anime",
            "no livro",
            "o personagem",
            "a personagem",
            "o heroi",
            "o herói",
            "o vilao",
            "o vilão"
        ],

        "recomendacao": (
            "Essa mensagem pode representar uma ameaça ou "
            "tentativa de intimidação. Evite confrontar a "
            "pessoa, guarde as evidências e procure um adulto "
            "de confiança."
        )
    },


    # ========================================================
    # GOLPE
    # ========================================================

    "golpe": {

        "nome": "Possível golpe",

        "palavras": [
            "premio",
            "prêmio",
            "senha",
            "codigo",
            "código",
            "pix",
            "pagamento",
            "taxa",
            "link",
            "conta",
            "bancaria",
            "bancária",
            "dados",
            "dinheiro",
            "verificacao",
            "verificação"
        ],

        "contextos": [
            "voce ganhou",
            "você ganhou",

            "voce ganhou um premio",
            "você ganhou um prêmio",

            "clique nesse link",
            "clique no link",

            "acesse esse link",
            "acesse o link",

            "mande sua senha",
            "envie sua senha",

            "mande seu codigo",
            "mande seu código",

            "envie seu codigo",
            "envie seu código",

            "pix para receber",

            "faca um pix",
            "faça um pix",

            "faca um pagamento",
            "faça um pagamento",

            "conta bancaria",
            "conta bancária",

            "dados pessoais",

            "codigo de verificacao",
            "código de verificação",

            "codigo de seguranca",
            "código de segurança",

            "taxa para liberar",

            "pague uma taxa",

            "para receber o premio",
            "para receber o prêmio",

            "mande seus dados",

            "envie seus dados",

            "confirme sua senha",

            "confirme seu codigo",
            "confirme seu código"
        ],

        "ficcao": [
            "personagem",
            "filme",
            "serie",
            "série",
            "anime",
            "jogo",
            "game",
            "livro",
            "historia",
            "história",
            "roteiro",
            "ficcao",
            "ficção"
        ],

        "recomendacao": (
            "A mensagem pode estar relacionada a uma tentativa "
            "de golpe. Não forneça senhas, códigos ou dados "
            "pessoais e evite clicar em links suspeitos."
        )
    }
}


# ============================================================
# PADRÕES REGEX
# ============================================================

PADROES_MENOR = [

    r"\bcrianca\b",
    r"\bcriancas\b",

    r"\badolescente\b",
    r"\badolescentes\b",

    r"\bmenor\b",
    r"\bmenores\b",

    r"\bmenor\s+de\s+idade\b",
    r"\bmenores\s+de\s+idade\b",

    r"\btenho\s+(?:[0-9]|1[0-7])\s+anos\b",

    r"\btem\s+(?:[0-9]|1[0-7])\s+anos\b",

    r"\bele\s+tem\s+(?:[0-9]|1[0-7])\s+anos\b",

    r"\bela\s+tem\s+(?:[0-9]|1[0-7])\s+anos\b"
]


# ============================================================
# CONTEÚDO ÍNTIMO / SEXUAL
# ============================================================

PADROES_INTIMO = [

    r"\bnude\b",
    r"\bnudes\b",

    r"\bnua\b",
    r"\nua?s\b",

    r"\bnu\b",
    r"\bnus\b",

    r"\bpelado\b",
    r"\bpelada\b",
    r"\bpelados\b",
    r"\bpeladas\b",

    r"\bsem\s+roupa\b",
    r"\bsem\s+roupas\b",

    r"\bfoto\s+intima\b",
    r"\bfotos\s+intimas\b",

    r"\bvideo\s+intimo\b",
    r"\bvideos\s+intimos\b",

    r"\bimagem\s+intima\b",
    r"\bimagens\s+intimas\b",

    r"\bconteudo\s+adulto\b",
    r"\bconteudo\s+sexual\b",

    r"\bmaterial\s+adulto\b",
    r"\bmaterial\s+sexual\b",

    r"\bpornografia\b",
    r"\bpornografico\b",
    r"\bpornografica\b",
    r"\bpornograficos\b",
    r"\bpornograficas\b",
    r"\bporno\b",
    r"\bporn\b",

    r"\bsexo\b",
    r"\bsexual\b",
    r"\bsexuais\b",

    r"\berotico\b",
    r"\berotica\b",
    r"\beroticos\b",
    r"\beroticas\b",

    r"\bexplicito\b",
    r"\bexplicita\b",
    r"\bexplicitos\b",
    r"\bexplicitas\b",

    r"\bmasturba(?:cao|ção)\b",
    r"\bmasturbar\b",
    r"\bmasturbando\b",

    r"\borgasmo\b",
    r"\borgasmos\b",

    r"\bgozar\b",
    r"\bgozo\b",

    r"\bfoder\b",
    r"\bfoderam\b",
    r"\bfodendo\b",
    r"\bfode\b",
    r"\bfoda\b",
    r"\bfuder\b",
    r"\bfudendo\b",

    r"\btransar\b",
    r"\btransando\b",
    r"\btransa\b",

    r"\bmolestar\b",
    r"\bmolestando\b",
    r"\bmolestacao\b",

    # ========================================================
    # PIMBAR E VARIANTES
    # ========================================================

    r"\bpimbar\b",
    r"\bpimba\b",
    r"\bpimbando\b",
    r"\bpimbei\b",
    r"\bpimbou\b",
    r"\bpimbe\b",
    r"\bpimbum\b",
    r"\bpimbu\b",

    r"\bp1mbar\b",
    r"\bp1mba\b",
    r"\bp1mbando\b",

    r"\bp\s*i\s*m\s*b\s*a\s*r\b",
    r"\bp\s*i\s*m\s*b\s*a\b",
    r"\bp\s*i\s*m\s*b\s*a\s*n\s*d\s*o\b",

    # Anatomia
    r"\bpenis\b",
    r"\bvagina\b",
    r"\bvaginal\b",
    r"\bvulva\b",
    r"\bclitoris\b",
    r"\bseios\b",
    r"\bpeitos\b",
    r"\bbunda\b",
    r"\bnadegas\b"
]


# ============================================================
# PEDIDO DE CONTEÚDO ÍNTIMO
# ============================================================

PADROES_PEDIDO_INTIMO = [

    r"\bmanda\s+(?:uma\s+)?foto\s+intima\b",
    r"\bmande\s+(?:uma\s+)?foto\s+intima\b",

    r"\benvie\s+(?:uma\s+)?foto\s+intima\b",
    r"\benvia\s+(?:uma\s+)?foto\s+intima\b",

    r"\bmanda\s+nudes?\b",
    r"\bmande\s+nudes?\b",

    r"\benvie\s+nudes?\b",
    r"\benvia\s+nudes?\b",

    r"\bme\s+manda\s+(?:uma\s+)?foto\s+intima\b",

    r"\bme\s+envia\s+(?:uma\s+)?foto\s+intima\b",

    r"\bme\s+manda\s+nudes?\b",

    r"\bme\s+envia\s+nudes?\b",

    r"\bmanda\s+foto\s+pelada\b",
    r"\bmanda\s+foto\s+pelado\b",

    r"\bmande\s+foto\s+pelada\b",
    r"\bmande\s+foto\s+pelado\b",

    r"\benvie\s+foto\s+pelada\b",
    r"\benvie\s+foto\s+pelado\b",

    r"\bme\s+manda\s+foto\s+pelada\b",
    r"\bme\s+manda\s+foto\s+pelado\b",

    r"\bme\s+manda\s+foto\s+nua\b",
    r"\bme\s+manda\s+foto\s+nu\b",

    r"\bme\s+manda\s+uma\s+foto\s+sem\s+roupa\b",

    r"\bme\s+envia\s+uma\s+foto\s+sem\s+roupa\b"
]


# ============================================================
# EXPRESSÕES SEXUAIS / VULGARES
# ============================================================

PADROES_SEXUAL = [

    # --------------------------------------------------------
    # COMER - contexto sexual
    # --------------------------------------------------------

    r"\bvou\s+te\s+comer\b",
    r"\bquero\s+te\s+comer\b",

    r"\bvou\s+comer\s+voce\b",
    r"\bvou\s+comer\s+você\b",

    r"\bquero\s+comer\s+voce\b",
    r"\bquero\s+comer\s+você\b",

    # --------------------------------------------------------
    # FODER / FUDER
    # --------------------------------------------------------

    r"\bvou\s+te\s+foder\b",
    r"\bquero\s+te\s+foder\b",

    r"\bvou\s+foder\s+voce\b",
    r"\bvou\s+foder\s+você\b",

    r"\bquero\s+foder\s+voce\b",
    r"\bquero\s+foder\s+você\b",

    r"\bvou\s+te\s+fuder\b",
    r"\bquero\s+te\s+fuder\b",

    # Leetspeak
    r"\bvou\s+te\s+f0der\b",
    r"\bquero\s+te\s+f0der\b",

    r"\bvou\s+f0der\s+voce\b",
    r"\bvou\s+f0der\s+você\b",

    # --------------------------------------------------------
    # MOLESTAR
    # --------------------------------------------------------

    r"\bvou\s+te\s+molestar\b",
    r"\bquero\s+te\s+molestar\b",

    r"\bvou\s+molestar\s+voce\b",
    r"\bvou\s+molestar\s+você\b",

    r"\bquero\s+molestar\s+voce\b",
    r"\bquero\s+molestar\s+você\b",

    # --------------------------------------------------------
    # BOTAR NA CHAPA
    # --------------------------------------------------------

    r"\bvou\s+te\s+botar\s+na\s+chapa\b",
    r"\bquero\s+te\s+botar\s+na\s+chapa\b",

    r"\bvou\s+botar\s+na\s+chapa\b",
    r"\bquero\s+botar\s+na\s+chapa\b",

    # --------------------------------------------------------
    # PIMBAR
    # --------------------------------------------------------

    r"\bpimbar\b",
    r"\bpimba\b",
    r"\bpimbando\b",
    r"\bpimbei\b",
    r"\bpimbou\b",
    r"\bpimbe\b",
    r"\bpimbum\b",
    r"\bpimbu\b",

    r"\bvou\s+pimbar\b",
    r"\bquero\s+pimbar\b",
    r"\bvamos\s+pimbar\b",
    r"\bquer\s+pimbar\b",

    r"\bpimbar\s+com\s+voce\b",
    r"\bpimbar\s+com\s+você\b",

    r"\bvou\s+pimba\b",
    r"\bquero\s+pimba\b",
    r"\bvamos\s+pimba\b",

    # --------------------------------------------------------
    # ROUPA / NUDEZ
    # --------------------------------------------------------

    r"\btira\s+a\s+roupa\b",
    r"\btire\s+a\s+roupa\b",

    r"\btira\s+suas\s+roupas\b",
    r"\btire\s+suas\s+roupas\b",

    r"\bfica\s+pelado\b",
    r"\bfica\s+pelada\b",

    r"\bfique\s+pelado\b",
    r"\bfique\s+pelada\b",

    r"\bfica\s+nu\b",
    r"\bfica\s+nua\b",

    r"\bfique\s+nu\b",
    r"\bfique\s+nua\b",

    r"\bvem\s+pelado\b",
    r"\bvem\s+pelada\b",

    r"\bvem\s+nu\b",
    r"\bvem\s+nua\b",

    r"\bvem\s+sem\s+roupa\b",

    # --------------------------------------------------------
    # SEXO / TRANSAR
    # --------------------------------------------------------

    r"\bvamos\s+fazer\s+sexo\b",
    r"\bquero\s+fazer\s+sexo\b",

    r"\bquer\s+fazer\s+sexo\b",

    r"\bvamos\s+transar\b",
    r"\bquero\s+transar\b",

    r"\bquer\s+transar\b",

    r"\bvamos\s+transar\s+comigo\b",
    r"\bvem\s+transar\s+comigo\b",

    # --------------------------------------------------------
    # TOQUE / CORPO
    # --------------------------------------------------------

    r"\bquero\s+seu\s+corpo\b",

    r"\bquero\s+tocar\s+seu\s+corpo\b",

    r"\bquero\s+tocar\s+em\s+voce\b",
    r"\bquero\s+tocar\s+em\s+você\b",

    r"\bposso\s+tocar\s+em\s+voce\b",
    r"\bposso\s+tocar\s+em\s+você\b",

    r"\bdeixa\s+eu\s+tocar\b",
    r"\bdeixe\s+eu\s+tocar\b",

    r"\bmostra\s+seu\s+corpo\b",
    r"\bmostre\s+seu\s+corpo\b",

    r"\bquero\s+ver\s+seu\s+corpo\b",

    r"\bquero\s+ver\s+voce\s+sem\s+roupa\b",
    r"\bquero\s+ver\s+você\s+sem\s+roupa\b",

    r"\bquero\s+ver\s+voce\s+nua\b",
    r"\bquero\s+ver\s+você\s+nua\b",

    r"\bquero\s+ver\s+voce\s+nu\b",
    r"\bquero\s+ver\s+você\s+nu\b",

    r"\bquero\s+ver\s+voce\s+pelada\b",
    r"\bquero\s+ver\s+você\s+pelada\b",

    r"\bquero\s+ver\s+voce\s+pelado\b",
    r"\bquero\s+ver\s+você\s+pelado\b"
]


# ============================================================
# VARIANTES DE OBFUSCAÇÃO SEXUAL
# ============================================================

PADROES_SEXUAL_OBFUSCADO = [

    # Foder
    r"\bf0d3r\b",
    r"\bf0der\b",
    r"\bfud3r\b",

    # Nude
    r"\bnudes?\b",

    # Pornografia
    r"\bp0rn\b",
    r"\bp0rno\b",

    # Sexo
    r"\bs3xo\b",

    # Pimbar
    r"\bp1mbar\b",
    r"\bp1mba\b",
    r"\bp1mbando\b",

    # Palavras separadas
    r"\bn\s*u\s*d\s*e\s*s?\b",
    r"\bp\s*o\s*r\s*n\s*o\b",
    r"\bs\s*e\s*x\s*o\b",

    r"\bp\s*i\s*m\s*b\s*a\s*r\b",
    r"\bp\s*i\s*m\s*b\s*a\b"
]


# ============================================================
# SEGREDO
# ============================================================

PADROES_SEGREDO = [

    r"\bnao\s+conta\s+pra\s+ninguem\b",
    r"\bnao\s+conte\s+pra\s+ninguem\b",

    r"\bnao\s+conta\s+para\s+ninguem\b",
    r"\bnao\s+conte\s+para\s+ninguem\b",

    r"\bnao\s+fala\s+para\s+seus\s+pais\b",
    r"\bnao\s+conte\s+para\s+seus\s+pais\b",

    r"\bnao\s+fala\s+com\s+seus\s+pais\b",
    r"\bnao\s+conte\s+com\s+seus\s+pais\b",

    r"\bnao\s+deixa\s+seus\s+pais\s+saberem\b",

    r"\bfica\s+so\s+entre\s+nos\b",

    r"\bvamos\s+manter\s+segredo\b",

    r"\bninguem\s+precisa\s+saber\b",

    r"\bisso\s+fica\s+entre\s+nos\b"
]


# ============================================================
# AFASTAMENTO DOS RESPONSÁVEIS
# ============================================================

PADROES_AFASTAMENTO = [

    r"\bnao\s+conta\s+para\s+seus\s+pais\b",

    r"\bnao\s+conte\s+para\s+seus\s+pais\b",

    r"\bnao\s+fala\s+para\s+seus\s+pais\b",

    r"\bnao\s+fala\s+com\s+seus\s+pais\b",

    r"\bnao\s+deixa\s+seus\s+pais\s+saberem\b",

    r"\bseus\s+pais\s+nao\s+precisam\s+saber\b",

    r"\bnao\s+precisa\s+contar\s+para\s+seus\s+pais\b",

    r"\bnao\s+precisa\s+falar\s+com\s+seus\s+pais\b"
]


# ============================================================
# ENCONTRO SUSPEITO
# ============================================================

PADROES_ENCONTRO = [

    r"\bvamos\s+nos\s+encontrar\b",

    r"\bquero\s+te\s+encontrar\b",

    r"\bquero\s+encontrar\s+voce\b",

    r"\bencontro\s+secreto\b",

    r"\bvem\s+sozinho\b",

    r"\bvem\s+sozinha\b",

    r"\bfica\s+sozinho\s+comigo\b",

    r"\bfica\s+sozinha\s+comigo\b",

    r"\bnao\s+conta\s+que\s+nos\s+encontramos\b",

    r"\bnao\s+fala\s+que\s+nos\s+encontramos\b"
]


# ============================================================
# COERÇÃO / CHANTAGEM
# ============================================================

PADROES_COERCAO = [

    r"\bse\s+voce\s+nao\b",

    r"\bse\s+voce\s+contar\b",

    r"\bse\s+voce\s+falar\b",

    r"\bse\s+voce\s+denunciar\b",

    r"\bvou\s+mostrar\s+para\s+todo\s+mundo\b",

    r"\bvou\s+espalhar\b",

    r"\bvou\s+divulgar\b",

    r"\bninguem\s+pode\s+saber\b"
]


# ============================================================
# MANIPULAÇÃO EMOCIONAL
# ============================================================

PADROES_MANIPULACAO = [

    r"\bconfia\s+em\s+mim\b",

    r"\bprova\s+que\s+gosta\s+de\s+mim\b",

    r"\bse\s+voce\s+gosta\s+de\s+mim\b",

    r"\bso\s+entre\s+nos\b",

    r"\bvoce\s+pode\s+confiar\s+em\s+mim\b"
]


# ============================================================
# NORMALIZAÇÃO
# ============================================================

def normalizar_texto(texto):

    texto = str(texto).lower().strip()

    mapa = str.maketrans(
        "áàãâäéèêëíìîïóòõôöúùûüç",
        "aaaaaeeeeiiiiooooouuuuc"
    )

    texto = texto.translate(mapa)

    # --------------------------------------------------------
    # Leetspeak
    # --------------------------------------------------------

    texto = texto.replace("@", "a")
    texto = texto.replace("0", "o")
    texto = texto.replace("1", "i")
    texto = texto.replace("3", "e")
    texto = texto.replace("4", "a")
    texto = texto.replace("5", "s")
    texto = texto.replace("7", "t")

    # --------------------------------------------------------
    # Remove pontuação
    # --------------------------------------------------------

    texto = re.sub(
        r"[^a-z0-9\s]",
        " ",
        texto
    )

    # --------------------------------------------------------
    # Remove espaços duplicados
    # --------------------------------------------------------

    texto = re.sub(
        r"\s+",
        " ",
        texto
    )

    return texto.strip()


# ============================================================
# REGEX
# ============================================================

def encontrar_padroes_regex(texto, padroes):

    texto_normalizado = normalizar_texto(texto)

    encontrados = []

    for padrao in padroes:

        if re.search(
            padrao,
            texto_normalizado,
            re.IGNORECASE
        ):

            encontrados.append(
                padrao
            )

    return encontrados


# ============================================================
# CONTEXTO FICTÍCIO
# ============================================================

def contexto_ficticio(texto, palavras_ficcao):

    texto_normalizado = normalizar_texto(texto)

    for palavra in palavras_ficcao:

        palavra_normalizada = normalizar_texto(
            palavra
        )

        padrao = (
            r"\b"
            + re.escape(palavra_normalizada)
            + r"\b"
        )

        if re.search(
            padrao,
            texto_normalizado
        ):

            return True

    return False


# ============================================================
# ENCONTRAR PALAVRAS
# ============================================================

def encontrar_palavras(texto, palavras):

    texto_normalizado = normalizar_texto(texto)

    encontradas = []

    for palavra in palavras:

        palavra_normalizada = normalizar_texto(
            palavra
        )

        padrao = (
            r"\b"
            + re.escape(palavra_normalizada)
            + r"\b"
        )

        if re.search(
            padrao,
            texto_normalizado
        ):

            encontradas.append(
                palavra
            )

    return encontradas


# ============================================================
# ENCONTRAR CONTEXTOS
# ============================================================

def encontrar_contextos(texto, contextos):

    texto_normalizado = normalizar_texto(texto)

    encontrados = []

    for contexto in contextos:

        contexto_normalizado = normalizar_texto(
            contexto
        )

        padrao = re.escape(
            contexto_normalizado
        )

        if re.search(
            r"\b" + padrao + r"\b",
            texto_normalizado
        ):

            encontrados.append(
                contexto
            )

    return encontrados


# ============================================================
# CLASSIFICAR NÍVEL
# ============================================================

def determinar_nivel(pontuacao):

    if pontuacao <= 0:
        return "seguro"

    if pontuacao <= 2:
        return "baixo"

    if pontuacao <= 5:
        return "moderado"

    return "alto"


# ============================================================
# CALCULAR CONFIANÇA
# ============================================================

def calcular_confianca(pontuacao):

    if pontuacao >= 12:
        return 98

    if pontuacao >= 8:
        return 95

    if pontuacao >= 6:
        return 92

    if pontuacao >= 4:
        return 88

    if pontuacao >= 3:
        return 84

    if pontuacao >= 1:
        return 78

    return 98


# ============================================================
# ANALISAR CONTEÚDO SEXUAL
# ============================================================

def analisar_conteudo_sexual(texto):

    intimo = encontrar_padroes_regex(
        texto,
        PADROES_INTIMO
    )

    pedido = encontrar_padroes_regex(
        texto,
        PADROES_PEDIDO_INTIMO
    )

    sexual = encontrar_padroes_regex(
        texto,
        PADROES_SEXUAL
    )

    obfuscado = encontrar_padroes_regex(
        texto,
        PADROES_SEXUAL_OBFUSCADO
    )

    pontuacao = 0

    sinais = []

    # --------------------------------------------------------
    # CONTEÚDO ÍNTIMO
    # --------------------------------------------------------

    if intimo:

        pontuacao += 3

        sinais.append({
            "sinal": "conteúdo sexual ou íntimo",
            "tipo": "conteúdo",
            "peso": 3
        })

    # --------------------------------------------------------
    # PEDIDO
    # --------------------------------------------------------

    if pedido:

        pontuacao += 5

        sinais.append({
            "sinal": "pedido de conteúdo íntimo",
            "tipo": "intenção",
            "peso": 5
        })

    # --------------------------------------------------------
    # EXPRESSÃO SEXUAL
    # --------------------------------------------------------

    if sexual:

        pontuacao += 4

        sinais.append({
            "sinal": "linguagem sexual",
            "tipo": "conteúdo",
            "peso": 4
        })

    # --------------------------------------------------------
    # OBFUSCAÇÃO
    # --------------------------------------------------------

    if obfuscado:

        pontuacao += 4

        sinais.append({
            "sinal": "possível tentativa de ocultar linguagem sexual",
            "tipo": "obfuscação",
            "peso": 4
        })

    # --------------------------------------------------------
    # PEDIDO + CONTEÚDO
    # --------------------------------------------------------

    if intimo and pedido:

        pontuacao += 5

        sinais.append({
            "sinal": "conteúdo íntimo + pedido",
            "tipo": "combinação crítica",
            "peso": 5
        })

    # --------------------------------------------------------
    # SEXUAL + PEDIDO
    # --------------------------------------------------------

    if sexual and pedido:

        pontuacao += 4

        sinais.append({
            "sinal": "linguagem sexual + pedido de conteúdo",
            "tipo": "combinação crítica",
            "peso": 4
        })

    return {
        "pontuacao": pontuacao,
        "sinais": sinais
    }


# ============================================================
# ANALISAR PROTEÇÃO DE MENOR
# ============================================================

def analisar_protecao_menor(texto):

    menor = encontrar_padroes_regex(
        texto,
        PADROES_MENOR
    )

    intimo = encontrar_padroes_regex(
        texto,
        PADROES_INTIMO
    )

    pedido = encontrar_padroes_regex(
        texto,
        PADROES_PEDIDO_INTIMO
    )

    segredo = encontrar_padroes_regex(
        texto,
        PADROES_SEGREDO
    )

    afastamento = encontrar_padroes_regex(
        texto,
        PADROES_AFASTAMENTO
    )

    encontro = encontrar_padroes_regex(
        texto,
        PADROES_ENCONTRO
    )

    coercao = encontrar_padroes_regex(
        texto,
        PADROES_COERCAO
    )

    manipulacao = encontrar_padroes_regex(
        texto,
        PADROES_MANIPULACAO
    )

    sexual = encontrar_padroes_regex(
        texto,
        PADROES_SEXUAL
    )

    pontuacao = 0

    sinais = []

    # --------------------------------------------------------
    # MENOR
    # --------------------------------------------------------

    if menor:

        pontuacao += 3

        sinais.append({
            "sinal": "referência a criança/adolescente",
            "tipo": "contexto",
            "peso": 3
        })

    # --------------------------------------------------------
    # CONTEÚDO ÍNTIMO
    # --------------------------------------------------------

    if intimo:

        pontuacao += 3

        sinais.append({
            "sinal": "conteúdo íntimo ou sexual",
            "tipo": "contexto",
            "peso": 3
        })

    # --------------------------------------------------------
    # LINGUAGEM SEXUAL
    # --------------------------------------------------------

    if sexual:

        pontuacao += 4

        sinais.append({
            "sinal": "linguagem sexual",
            "tipo": "conteúdo",
            "peso": 4
        })

    # --------------------------------------------------------
    # PEDIDO
    # --------------------------------------------------------

    if pedido:

        pontuacao += 5

        sinais.append({
            "sinal": "pedido de conteúdo íntimo",
            "tipo": "intenção",
            "peso": 5
        })

    # --------------------------------------------------------
    # SEGREDO
    # --------------------------------------------------------

    if segredo:

        pontuacao += 4

        sinais.append({
            "sinal": "tentativa de manter segredo",
            "tipo": "manipulação",
            "peso": 4
        })

    # --------------------------------------------------------
    # AFASTAMENTO
    # --------------------------------------------------------

    if afastamento:

        pontuacao += 5

        sinais.append({
            "sinal": "tentativa de afastar dos responsáveis",
            "tipo": "manipulação",
            "peso": 5
        })

    # --------------------------------------------------------
    # ENCONTRO
    # --------------------------------------------------------

    if encontro:

        pontuacao += 4

        sinais.append({
            "sinal": "possível tentativa de encontro privado",
            "tipo": "intenção",
            "peso": 4
        })

    # --------------------------------------------------------
    # COERÇÃO
    # --------------------------------------------------------

    if coercao:

        pontuacao += 4

        sinais.append({
            "sinal": "possível coerção ou chantagem",
            "tipo": "coerção",
            "peso": 4
        })

    # --------------------------------------------------------
    # MANIPULAÇÃO
    # --------------------------------------------------------

    if manipulacao:

        pontuacao += 2

        sinais.append({
            "sinal": "possível manipulação emocional",
            "tipo": "manipulação",
            "peso": 2
        })

    # ========================================================
    # COMBINAÇÕES CRÍTICAS
    # ========================================================

    if menor and intimo:

        pontuacao += 8

        sinais.append({
            "sinal": "menor de idade + conteúdo íntimo/sexual",
            "tipo": "combinação crítica",
            "peso": 8
        })

    if menor and sexual:

        pontuacao += 8

        sinais.append({
            "sinal": "menor de idade + linguagem sexual",
            "tipo": "combinação crítica",
            "peso": 8
        })

    if menor and pedido:

        pontuacao += 8

        sinais.append({
            "sinal": "menor de idade + pedido de conteúdo íntimo",
            "tipo": "combinação crítica",
            "peso": 8
        })

    if menor and segredo:

        pontuacao += 5

        sinais.append({
            "sinal": "menor de idade + tentativa de segredo",
            "tipo": "combinação crítica",
            "peso": 5
        })

    if segredo and intimo:

        pontuacao += 5

        sinais.append({
            "sinal": "segredo + conteúdo íntimo",
            "tipo": "combinação crítica",
            "peso": 5
        })

    if menor and encontro:

        pontuacao += 6

        sinais.append({
            "sinal": "menor de idade + possível encontro",
            "tipo": "combinação crítica",
            "peso": 6
        })

    if menor and coercao:

        pontuacao += 6

        sinais.append({
            "sinal": "menor de idade + possível coerção",
            "tipo": "combinação crítica",
            "peso": 6
        })

    if menor and intimo and pedido:

        pontuacao += 8

        sinais.append({
            "sinal": (
                "menor de idade + conteúdo íntimo "
                "+ pedido"
            ),
            "tipo": "combinação crítica",
            "peso": 8
        })

    if menor and sexual and pedido:

        pontuacao += 10

        sinais.append({
            "sinal": (
                "menor de idade + linguagem sexual "
                "+ pedido"
            ),
            "tipo": "combinação crítica",
            "peso": 10
        })

    if menor and segredo and intimo:

        pontuacao += 8

        sinais.append({
            "sinal": (
                "menor de idade + segredo "
                "+ conteúdo íntimo"
            ),
            "tipo": "combinação crítica",
            "peso": 8
        })

    if menor and afastamento and intimo:

        pontuacao += 8

        sinais.append({
            "sinal": (
                "menor de idade + afastamento "
                "dos responsáveis + conteúdo íntimo"
            ),
            "tipo": "combinação crítica",
            "peso": 8
        })

    return {
        "pontuacao": pontuacao,
        "sinais": sinais
    }


# ============================================================
# ANALISAR CATEGORIA
# ============================================================

def analisar_categoria(
    texto,
    codigo,
    categoria
):

    palavras = encontrar_palavras(
        texto,
        categoria["palavras"]
    )

    contextos = encontrar_contextos(
        texto,
        categoria["contextos"]
    )

    ficticio = contexto_ficticio(
        texto,
        categoria["ficcao"]
    )

    # --------------------------------------------------------
    # NENHUM SINAL
    # --------------------------------------------------------

    if not palavras and not contextos:

        return None

    # --------------------------------------------------------
    # FICÇÃO
    # --------------------------------------------------------

    if ficticio:

        texto_normalizado = normalizar_texto(
            texto
        )

        direcionamento = any(

            re.search(
                r"\b" + re.escape(
                    normalizar_texto(termo)
                ) + r"\b",
                texto_normalizado
            )

            for termo in [

                "vou te",
                "vou matar voce",
                "vou te matar",
                "vou te machucar",
                "vou te bater",
                "vou te estuprar",
                "vou te estrupar",

                "vou te foder",
                "vou te molestar",
                "vou te comer",

                "vou pimbar",
                "quero pimbar"
            ]
        )

        if not direcionamento:

            return None

    # --------------------------------------------------------
    # PONTUAÇÃO
    # --------------------------------------------------------

    pontuacao = 0

    sinais = []

    for palavra in palavras:

        pontuacao += 1

        sinais.append({

            "sinal": palavra,

            "tipo": "palavra-chave",

            "peso": 1

        })

    for contexto in contextos:

        pontuacao += 3

        sinais.append({

            "sinal": contexto,

            "tipo": "contexto",

            "peso": 3

        })

    texto_normalizado = normalizar_texto(
        texto
    )

    # ========================================================
    # CONTEÚDO SEXUAL
    # ========================================================

    if codigo == "sexual":

        resultado_sexual = analisar_conteudo_sexual(
            texto
        )

        pontuacao += resultado_sexual[
            "pontuacao"
        ]

        sinais.extend(
            resultado_sexual[
                "sinais"
            ]
        )

        # ----------------------------------------------------
        # CONTEXTO DE MENOR
        # ----------------------------------------------------

        menor = encontrar_padroes_regex(
            texto,
            PADROES_MENOR
        )

        if menor:

            pontuacao += 10

            sinais.append({

                "sinal":
                    "conteúdo sexual associado a menor de idade",

                "tipo":
                    "combinação crítica",

                "peso":
                    10
            })

        # ----------------------------------------------------
        # SEGREDO
        # ----------------------------------------------------

        segredo = encontrar_padroes_regex(
            texto,
            PADROES_SEGREDO
        )

        if segredo:

            pontuacao += 5

            sinais.append({

                "sinal":
                    "conteúdo sexual + tentativa de segredo",

                "tipo":
                    "combinação crítica",

                "peso":
                    5
            })

        # ----------------------------------------------------
        # AFASTAMENTO
        # ----------------------------------------------------

        afastamento = encontrar_padroes_regex(
            texto,
            PADROES_AFASTAMENTO
        )

        if afastamento:

            pontuacao += 5

            sinais.append({

                "sinal":
                    "conteúdo sexual + afastamento dos responsáveis",

                "tipo":
                    "combinação crítica",

                "peso":
                    5
            })

    # ========================================================
    # AMEAÇA
    # ========================================================

    if codigo == "ameaca":

        termos_diretos = [

            "vou te",
            "eu vou te",
            "vou matar",
            "vou te matar",
            "vou te pegar",
            "vou te machucar",
            "vou te bater",
            "vou te estuprar",
            "vou te estrupar",
            "vou acabar com voce",
            "vou acabar com você",
            "vou acabar com sua vida",
            "vou te expor"
        ]

        for termo in termos_diretos:

            padrao = (
                r"\b"
                + re.escape(
                    normalizar_texto(termo)
                )
                + r"\b"
            )

            if re.search(
                padrao,
                texto_normalizado
            ):

                pontuacao += 4

                sinais.append({

                    "sinal": termo,

                    "tipo":
                        "intenção direcionada",

                    "peso": 4

                })

                break

    # ========================================================
    # CYBERBULLYING
    # ========================================================

    if codigo == "cyberbullying":

        insulto_direcionado = any(

            termo in texto_normalizado

            for termo in [

                "voce e",
                "te odeio",
                "ninguem gosta de voce",
                "todo mundo te odeia",
                "vou te humilhar"
            ]
        )

        if insulto_direcionado:

            pontuacao += 3

            sinais.append({

                "sinal":
                    "insulto direcionado",

                "tipo":
                    "contexto",

                "peso": 3

            })

    # ========================================================
    # ALICIAMENTO
    # ========================================================

    if codigo == "aliciamento":

        segredo = encontrar_padroes_regex(
            texto,
            PADROES_SEGREDO
        )

        pedido = encontrar_padroes_regex(
            texto,
            PADROES_PEDIDO_INTIMO
        )

        afastamento = encontrar_padroes_regex(
            texto,
            PADROES_AFASTAMENTO
        )

        encontro = encontrar_padroes_regex(
            texto,
            PADROES_ENCONTRO
        )

        sexual = encontrar_padroes_regex(
            texto,
            PADROES_SEXUAL
        )

        if segredo:

            pontuacao += 3

            sinais.append({

                "sinal":
                    "tentativa de manter segredo",

                "tipo":
                    "manipulação",

                "peso": 3

            })

        if pedido:

            pontuacao += 5

            sinais.append({

                "sinal":
                    "pedido de conteúdo íntimo",

                "tipo":
                    "intenção",

                "peso": 5

            })

        if afastamento:

            pontuacao += 4

            sinais.append({

                "sinal":
                    "afastamento dos responsáveis",

                "tipo":
                    "manipulação",

                "peso": 4

            })

        if encontro:

            pontuacao += 4

            sinais.append({

                "sinal":
                    "possível encontro privado",

                "tipo":
                    "intenção",

                "peso": 4

            })

        if sexual:

            pontuacao += 4

            sinais.append({

                "sinal":
                    "linguagem sexual",

                "tipo":
                    "conteúdo",

                "peso": 4

            })

    # ========================================================
    # GOLPE
    # ========================================================

    if codigo == "golpe":

        premio = any(

            termo in texto_normalizado

            for termo in [
                "voce ganhou",
                "premio"
            ]
        )

        solicitacao_dados = any(

            termo in texto_normalizado

            for termo in [
                "senha",
                "codigo",
                "dados pessoais",
                "conta bancaria"
            ]
        )

        pagamento = any(

            termo in texto_normalizado

            for termo in [
                "pix",
                "pague uma taxa",
                "faca um pix",
                "faca um pagamento"
            ]
        )

        link = any(

            termo in texto_normalizado

            for termo in [
                "clique no link",
                "clique nesse link",
                "acesse o link",
                "acesse esse link"
            ]
        )

        if premio and (
            link or solicitacao_dados
        ):

            pontuacao += 4

        if solicitacao_dados:

            pontuacao += 3

        if pagamento:

            pontuacao += 4

        if link:

            pontuacao += 2

    # --------------------------------------------------------
    # RESULTADO
    # --------------------------------------------------------

    if pontuacao <= 0:

        return None

    nivel = determinar_nivel(
        pontuacao
    )

    # Categorias prioritárias

    if codigo in [
        "aliciamento",
        "protecao_menor",
        "ameaca",
        "golpe",
        "sexual"
    ]:

        if (
            len(contextos) >= 1
            or len(palavras) >= 2
            or codigo == "sexual"
        ):

            nivel = "alto"

    return {

        "codigo": codigo,

        "categoria":
            categoria["nome"],

        "pontuacao":
            pontuacao,

        "nivel":
            nivel,

        "sinais":
            sinais,

        "recomendacao":
            categoria["recomendacao"]

    }


# ============================================================
# ANALISAR MENSAGEM
# ============================================================

def analisar_mensagem(mensagem):

    if (
        not mensagem
        or not str(mensagem).strip()
    ):

        return {

            "nivel":
                "seguro",

            "categoria":
                "Nenhum risco identificado",

            "confianca":
                98,

            "pontuacao":
                0,

            "sinais":
                [],

            "categorias_detectadas":
                [],

            "recomendacao":
                "Nenhum risco evidente foi "
                "identificado nessa mensagem."

        }

    resultados = []

    # ========================================================
    # PROTEÇÃO DE MENOR
    # ========================================================

    protecao = analisar_protecao_menor(
        mensagem
    )

    if protecao["pontuacao"] > 0:

        categoria = CATEGORIAS[
            "protecao_menor"
        ]

        resultados.append({

            "codigo":
                "protecao_menor",

            "categoria":
                categoria["nome"],

            "pontuacao":
                protecao["pontuacao"],

            "nivel":
                determinar_nivel(
                    protecao["pontuacao"]
                ),

            "sinais":
                protecao["sinais"],

            "recomendacao":
                categoria["recomendacao"]

        })

    # ========================================================
    # DEMAIS CATEGORIAS
    # ========================================================

    for codigo, categoria in CATEGORIAS.items():

        if codigo == "protecao_menor":

            continue

        resultado = analisar_categoria(

            mensagem,

            codigo,

            categoria

        )

        if resultado:

            resultados.append(
                resultado
            )

    # ========================================================
    # NENHUM RISCO
    # ========================================================

    if not resultados:

        return {

            "nivel":
                "seguro",

            "categoria":
                "Nenhum risco identificado",

            "confianca":
                98,

            "pontuacao":
                0,

            "sinais":
                [],

            "categorias_detectadas":
                [],

            "recomendacao":
                "Nenhum risco evidente foi "
                "identificado nessa mensagem."

        }

    # ========================================================
    # ORDENA RESULTADOS
    # ========================================================

    resultados.sort(

        key=lambda x:
        x["pontuacao"],

        reverse=True

    )

    principal = resultados[0]

    # ========================================================
    # CONFIANÇA
    # ========================================================

    confianca = calcular_confianca(

        principal["pontuacao"]

    )

    # ========================================================
    # CATEGORIAS DETECTADAS
    # ========================================================

    categorias_detectadas = []

    for resultado in resultados:

        categorias_detectadas.append({

            "categoria":
                resultado["categoria"],

            "nivel":
                resultado["nivel"],

            "pontuacao":
                resultado["pontuacao"]

        })

    # ========================================================
    # SINAIS
    # ========================================================

    sinais = []

    for resultado in resultados:

        for sinal in resultado["sinais"]:

            sinais.append(
                sinal["sinal"]
            )

    sinais = list(
        dict.fromkeys(sinais)
    )

    # ========================================================
    # RESULTADO FINAL
    # ========================================================

    return {

        "nivel":
            principal["nivel"],

        "categoria":
            principal["categoria"],

        "confianca":
            confianca,

        "pontuacao":
            principal["pontuacao"],

        "sinais":
            sinais,

        "categorias_detectadas":
            categorias_detectadas,

        "recomendacao":
            principal["recomendacao"]

    }


# ============================================================
# MOSTRAR RESULTADO NO TERMINAL
# ============================================================

def mostrar_resultado(resultado):

    print()

    print("=" * 60)

    print("🛡️ RESULTADO DO GUARDIA")

    print("=" * 60)

    print(
        f"Categoria : "
        f"{resultado['categoria']}"
    )

    print(
        f"Nível     : "
        f"{resultado['nivel'].upper()}"
    )

    print(
        f"Confiança : "
        f"{resultado['confianca']}%"
    )

    print(
        f"Pontuação : "
        f"{resultado['pontuacao']}"
    )

    if resultado["sinais"]:

        print()

        print(
            "🔎 Sinais identificados:"
        )

        for sinal in resultado["sinais"]:

            print(
                f"   • {sinal}"
            )

    if len(
        resultado["categorias_detectadas"]
    ) > 1:

        print()

        print(
            "⚠️ Outras categorias identificadas:"
        )

        for categoria in (
            resultado[
                "categorias_detectadas"
            ][1:]
        ):

            print(
                f"   • "
                f"{categoria['categoria']} "
                f"({categoria['nivel']})"
            )

    print()

    print(
        "💡 Recomendação:"
    )

    print(
        resultado["recomendacao"]
    )

    print("=" * 60)

    print()


# ============================================================
# TESTES AUTOMÁTICOS
# ============================================================

def executar_testes():

    print()

    print("=" * 60)

    print("🧪 TESTES AUTOMÁTICOS DO GUARDIA")

    print("=" * 60)

    testes = [

        (
            "Mensagem segura",
            "Oi, tudo bem? Vamos jogar depois?"
        ),

        (
            "Cyberbullying",
            "Você é um idiota e todo mundo te odeia"
        ),

        (
            "Ameaça",
            "Vou te matar se você contar para alguém"
        ),

        (
            "Golpe",
            "Você ganhou um prêmio, clique nesse link e mande sua senha"
        ),

        (
            "Aliciamento",
            "Não conte para seus pais, fica só entre nós"
        ),

        (
            "Conteúdo sexual",
            "Essa pessoa está enviando pornografia"
        ),

        (
            "Nude",
            "Ele pediu nudes"
        ),

        (
            "Pedido de foto íntima",
            "Me manda uma foto íntima"
        ),

        (
            "Linguagem sexual",
            "Vou te foder"
        ),

        (
            "Linguagem sexual variante",
            "Vou te f0der"
        ),

        (
            "Linguagem sexual",
            "Vou te molestar"
        ),

        (
            "Expressão sexual",
            "Vou te comer"
        ),

        (
            "Expressão sexual",
            "Vou te botar na chapa"
        ),

        (
            "Pimbar",
            "Ele falou que queria pimbar"
        ),

        (
            "Pimba",
            "Ele falou pimba"
        ),

        (
            "Pimbando",
            "Ele está pimbando"
        ),

        (
            "Pimbar variante",
            "Ele escreveu p1mbar"
        ),

        (
            "Pimbar separado",
            "p i m b a r"
        ),

        (
            "Nudez",
            "Ela está pelada"
        ),

        (
            "Nudez",
            "Ele está nu"
        ),

        (
            "Menor + conteúdo íntimo",
            "Tenho 13 anos e alguém está pedindo uma foto íntima"
        ),

        (
            "Menor + sexual",
            "Ela tem 14 anos e estão falando de sexo com ela"
        ),

        (
            "Menor + segredo",
            "Ela tem 12 anos e ele pediu para não contar para os pais"
        ),

        (
            "Menor + pedido + segredo",
            "Tenho 14 anos, ele pediu uma foto íntima e disse para não contar"
        ),

        (
            "Menor + encontro",
            "Ela tem 13 anos e ele quer marcar um encontro secreto"
        ),

        (
            "Menor + coerção",
            "Tenho 15 anos e ele disse que vai divulgar se eu não fizer o que ele quer"
        ),

        (
            "Menor + linguagem sexual",
            "Ela tem 13 anos e ele disse que quer transar com ela"
        ),

        (
            "Menor + nude",
            "Tenho 14 anos e ele pediu nudes"
        ),

        (
            "Menor + pimbar",
            "Tenho 14 anos e ele falou que queria pimbar"
        )
    ]

    for numero, (nome, mensagem) in enumerate(
        testes,
        start=1
    ):

        resultado = analisar_mensagem(
            mensagem
        )

        if resultado["nivel"] != "seguro":

            status = "PASSOU"

        else:

            if nome == "Mensagem segura":

                status = "PASSOU"

            else:

                status = "VERIFICAR"

        print()

        print(
            f"Teste {numero}: {nome}"
        )

        print(
            f"Mensagem: {mensagem}"
        )

        print(
            f"Status: {status}"
        )

        print(
            f"Categoria: "
            f"{resultado['categoria']}"
        )

        print(
            f"Nível: "
            f"{resultado['nivel'].upper()}"
        )

        print(
            f"Pontuação: "
            f"{resultado['pontuacao']}"
        )

        if resultado["sinais"]:

            print(
                "Sinais:"
            )

            for sinal in resultado["sinais"]:

                print(
                    f"   • {sinal}"
                )

    print()

    print("=" * 60)

    print("🧪 TESTES FINALIZADOS")

    print("=" * 60)

    print()


# ============================================================
# MODO TERMINAL
# ============================================================

def iniciar_guardia():

    print()

    print("=" * 60)

    print("🛡️ GUARDIA OVERLAY")

    print("Sistema de proteção digital")

    print("=" * 60)

    print()

    print(
        "Digite uma mensagem para o GuardIA analisar."
    )

    print(
        "Digite 'sair' para encerrar."
    )

    print()

    while True:

        mensagem = input(
            "💬 Mensagem: "
        ).strip()

        if mensagem.lower() == "sair":

            print()

            print(
                "🛡️ GuardIA encerrado."
            )

            break

        if not mensagem:

            print(
                "⚠️ Digite alguma mensagem."
            )

            continue

        resultado = analisar_mensagem(
            mensagem
        )

        mostrar_resultado(
            resultado
        )


# ============================================================
# EXECUTAR
# ============================================================

if __name__ == "__main__":

    iniciar_guardia()