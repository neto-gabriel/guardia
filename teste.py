# ============================================================
# TESTES AUTOMÁTICOS DO GUARDIA
# ============================================================

from guardia import analisar_mensagem


def executar_teste(numero, mensagem, categoria_esperada):

    resultado = analisar_mensagem(mensagem)

    categoria_obtida = resultado["categoria"]

    if categoria_esperada.lower() in categoria_obtida.lower():

        print(f"✅ Teste {numero}: PASSOU")

    else:

        print(f"❌ Teste {numero}: FALHOU")

        print(f"   Mensagem: {mensagem}")
        print(f"   Esperado: {categoria_esperada}")
        print(f"   Obtido:   {categoria_obtida}")

    print()


def iniciar_testes():

    print()
    print("=" * 60)
    print("🛡️ TESTES AUTOMÁTICOS DO GUARDIA")
    print("=" * 60)
    print()


    # --------------------------------------------------------
    # TESTE 1
    # --------------------------------------------------------

    executar_teste(
        1,
        "Vamos jogar?",
        "Nenhum risco identificado"
    )


    # --------------------------------------------------------
    # TESTE 2
    # --------------------------------------------------------

    executar_teste(
        2,
        "Você é inútil",
        "Cyberbullying"
    )


    # --------------------------------------------------------
    # TESTE 3
    # --------------------------------------------------------

    executar_teste(
        3,
        "Não conta pra ninguém, manda foto",
        "aliciamento"
    )


    # --------------------------------------------------------
    # TESTE 4
    # --------------------------------------------------------

    executar_teste(
        4,
        "Vou te expor",
        "Ameaça"
    )


    # --------------------------------------------------------
    # TESTE 5
    # --------------------------------------------------------

    executar_teste(
        5,
        "Você ganhou um prêmio, clique nesse link",
        "golpe"
    )


    # --------------------------------------------------------
    # TESTE 6
    # --------------------------------------------------------

    executar_teste(
        6,
        "Você é inútil, ninguém gosta de você e vou te expor",
        "Cyberbullying"
    )


    print("=" * 60)
    print("🏁 TESTES FINALIZADOS")
    print("=" * 60)
    print()


# ------------------------------------------------------------
# EXECUTAR TESTES
# ------------------------------------------------------------

if __name__ == "__main__":

    iniciar_testes()