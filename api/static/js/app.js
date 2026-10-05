/* ============================================================
   GUARDIA OVERLAY
   JAVASCRIPT PRINCIPAL
   ============================================================ */


/* ============================================================
   VARIÁVEIS
   ============================================================ */

let historicoAlertas = [];

let ultimaAnalise = null;


/* ============================================================
   INICIALIZAÇÃO
   ============================================================ */

document.addEventListener("DOMContentLoaded", function () {

    carregarHistorico();

    atualizarPainel();


    const sobreOverlay =
        document.getElementById(
            "sobreProjetoOverlay"
        );


    if (sobreOverlay) {

        sobreOverlay.addEventListener(
            "click",
            function (evento) {

                if (
                    evento.target ===
                    sobreOverlay
                ) {

                    fecharSobreProjeto();

                }

            }
        );

    }


    document.addEventListener(
        "keydown",
        function (evento) {

            if (
                evento.key === "Escape"
            ) {

                fecharSobreProjeto();

            }

        }
    );

});


/* ============================================================
   NAVEGAÇÃO
   ============================================================ */

function mostrarTela(tela) {

    const telas =
        document.querySelectorAll(
            ".tela"
        );


    telas.forEach(
        function (elemento) {

            elemento.classList.remove(
                "ativa"
            );

        }
    );


    const telaSelecionada =
        document.getElementById(
            "tela" +
            capitalizar(tela)
        );


    if (telaSelecionada) {

        telaSelecionada.classList.add(
            "ativa"
        );

    }


    const botoes =
        document.querySelectorAll(
            ".nav-button"
        );


    botoes.forEach(
        function (botao) {

            botao.classList.remove(
                "ativo"
            );

        }
    );


    if (
        tela === "conversa"
    ) {

        const botao =
            document.getElementById(
                "btnConversa"
            );

        if (botao) {

            botao.classList.add(
                "ativo"
            );

        }

    }


    if (
        tela === "analisador"
    ) {

        const botao =
            document.getElementById(
                "btnAnalisador"
            );

        if (botao) {

            botao.classList.add(
                "ativo"
            );

        }

    }


    if (
        tela === "painel"
    ) {

        const botao =
            document.getElementById(
                "btnPainel"
            );

        if (botao) {

            botao.classList.add(
                "ativo"
            );

        }


        atualizarPainel();

    }

}


/* ============================================================
   CAPITALIZAR
   ============================================================ */

function capitalizar(texto) {

    return (
        texto.charAt(0).toUpperCase() +
        texto.slice(1)
    );

}


/* ============================================================
   USAR EXEMPLO
   ============================================================ */

function usarExemplo(botao) {

    const mensagem =
        botao.innerText.trim();


    const campo =
        document.getElementById(
            "mensagem"
        );


    if (!campo) {

        return;

    }


    campo.value =
        mensagem;


    campo.focus();

}


/* ============================================================
   ENVIAR MENSAGEM DA CONVERSA
   ============================================================ */

async function enviarMensagemConversa() {

    const campo =
        document.getElementById(
            "mensagem"
        );


    if (!campo) {

        return;

    }


    const mensagem =
        campo.value.trim();


    if (!mensagem) {

        alert(
            "Digite uma mensagem antes de enviar."
        );


        campo.focus();


        return;

    }


    const botao =
        document.getElementById(
            "botaoEnviar"
        );


    if (botao) {

        botao.disabled =
            true;


        botao.innerText =
            "🔄 ANALISANDO...";

    }


    adicionarMensagemUsuario(
        mensagem
    );


    try {

        const resposta =
            await fetch(
                "/analisar",
                {

                    method:
                        "POST",

                    headers:
                        {

                            "Content-Type":
                                "application/json"

                        },

                    body:
                        JSON.stringify(
                            {

                                mensagem:
                                    mensagem

                            }
                        )

                }
            );


        const dados =
            await resposta.json();


        if (!resposta.ok) {

            throw new Error(
                dados.erro ||
                "Erro na API."
            );

        }


        const analise =
            dados.resultado;


        ultimaAnalise =
            analise;


        mostrarResultadoAnalisador(
            analise
        );


        mostrarTela(
            "analisador"
        );


        if (
            analise.categoria !==
            "Nenhum risco identificado"
        ) {

            registrarAlerta(
                analise,
                mensagem
            );


            mostrarCelular(
                analise
            );

        }


        campo.value =
            "";


    } catch (erro) {

        console.error(
            erro
        );


        alert(
            "Não foi possível analisar a mensagem.\n\n" +
            erro.message
        );

    }


    if (botao) {

        botao.disabled =
            false;


        botao.innerText =
            "➤ ENVIAR PARA O GUARDIA";

    }

}


/* ============================================================
   ADICIONAR MENSAGEM
   ============================================================ */

function adicionarMensagemUsuario(
    mensagem
) {

    const area =
        document.getElementById(
            "mensagensConversa"
        );


    if (!area) {

        return;

    }


    const mensagemElemento =
        document.createElement(
            "div"
        );


    mensagemElemento.className =
        "mensagem-usuario";


    mensagemElemento.innerHTML = `

        <div class="mensagem-label">
            Você
        </div>

        <div class="mensagem-conteudo">
            ${escaparHTML(mensagem)}
        </div>

    `;


    area.appendChild(
        mensagemElemento
    );


    area.scrollTop =
        area.scrollHeight;

}


/* ============================================================
   LIMPAR CONVERSA
   ============================================================ */

function limparConversa() {

    const area =
        document.getElementById(
            "mensagensConversa"
        );


    const campo =
        document.getElementById(
            "mensagem"
        );


    if (!area) {

        return;

    }


    const confirmar =
        confirm(
            "Deseja realmente apagar o histórico desta conversa?"
        );


    if (!confirmar) {

        return;

    }


    area.innerHTML = `

        <div class="mensagem-sistema">

            🛡️

            <span>
                Digite uma mensagem abaixo para
                iniciar a análise.
            </span>

        </div>

    `;


    if (campo) {

        campo.value = "";

    }


    ultimaAnalise =
        null;


    const resultado =
        document.getElementById(
            "resultadoAnalise"
        );


    if (resultado) {

        resultado.innerHTML = `

            <div class="resultado-vazio">

                🛡️

                <h2>
                    Aguardando mensagem
                </h2>

                <p>
                    Envie uma mensagem pela área
                    <strong>Conversa</strong>.
                </p>

            </div>

        `;

    }


    mostrarTela(
        "conversa"
    );


    if (campo) {

        campo.focus();

    }

}


/* ============================================================
   RESULTADO DO ANALISADOR
   ============================================================ */

function mostrarResultadoAnalisador(
    analise
) {

    const resultado =
        document.getElementById(
            "resultadoAnalise"
        );


    if (!resultado) {

        return;

    }


    const nivel =
        String(
            analise.nivel ||
            "seguro"
        ).toLowerCase();


    let classeNivel =
        "resultado-" +
        nivel;


    let icone =
        "🛡️";


    if (
        nivel === "alto"
    ) {

        icone =
            "🚨";

    } else if (
        nivel === "moderado"
    ) {

        icone =
            "⚠️";

    } else if (
        nivel === "baixo"
    ) {

        icone =
            "🟢";

    }


    /* ========================================================
       CONFIANÇA
       ======================================================== */

    let confianca =
        Number(
            analise.confianca
        );


    if (
        isNaN(confianca)
    ) {

        confianca =
            0;

    }


    confianca =
        Math.max(
            0,
            Math.min(
                100,
                confianca
            )
        );


    /* ========================================================
       SINAIS IDENTIFICADOS
       ======================================================== */

    let sinaisHTML =
        "";


    if (
        analise.sinais &&
        analise.sinais.length > 0
    ) {

        sinaisHTML = `

            <div class="resultado-secao">

                <h3>
                    🔎 Sinais identificados
                </h3>

                <div class="sinais-lista">

                    ${analise.sinais
                        .map(
                            function (sinal) {

                                return `
                                    <span class="sinal">
                                        ${escaparHTML(
                                            sinal
                                        )}
                                    </span>
                                `;

                            }
                        )
                        .join("")
                    }

                </div>

            </div>

        `;

    }


    /* ========================================================
       OUTRAS CATEGORIAS
       ======================================================== */

    let categoriasHTML =
        "";


    if (
        analise.categorias_detectadas &&
        analise.categorias_detectadas.length > 1
    ) {

        categoriasHTML = `

            <div class="resultado-secao">

                <h3>
                    🧠 Outras categorias identificadas
                </h3>

                <div class="categorias-detectadas">

                    ${
                        analise.categorias_detectadas
                            .map(
                                function (item) {

                                    return `

                                        <div class="categoria-detectada">

                                            <span>
                                                ${escaparHTML(
                                                    item.categoria
                                                )}
                                            </span>

                                            <strong>
                                                ${escaparHTML(
                                                    item.nivel
                                                ).toUpperCase()}
                                            </strong>

                                        </div>

                                    `;

                                }
                            )
                            .join("")
                    }

                </div>

            </div>

        `;

    }


    /* ========================================================
       HTML DO RESULTADO
       ======================================================== */

    resultado.innerHTML = `

        <div class="
            resultado-card
            ${classeNivel}
        ">


            <!-- =================================================
                 CABEÇALHO
                 ================================================= -->

            <div class="resultado-topo">

                <div class="resultado-icone">

                    ${icone}

                </div>


                <div>

                    <div class="resultado-legenda">

                        RESULTADO DA ANÁLISE

                    </div>


                    <h2>

                        ${
                            analise.categoria ===
                            "Nenhum risco identificado"

                                ? "Mensagem analisada"

                                : "Possível risco identificado"
                        }

                    </h2>

                </div>

            </div>



            <!-- =================================================
                 STATUS
                 ================================================= -->

            <div class="resultado-status">

                <span class="status-bolinha"></span>

                ${
                    analise.categoria ===
                    "Nenhum risco identificado"

                        ? "MENSAGEM SEM RISCO EVIDENTE"

                        : "RISCO " +
                          nivel.toUpperCase() +
                          " IDENTIFICADO"
                }

            </div>



            <!-- =================================================
                 DADOS PRINCIPAIS
                 ================================================= -->

            <div class="resultado-dados">


                <div class="resultado-dado">

                    <span>
                        Categoria
                    </span>

                    <strong>
                        ${escaparHTML(
                            analise.categoria
                        )}
                    </strong>

                </div>


                <div class="resultado-dado">

                    <span>
                        Nível de risco
                    </span>

                    <strong>
                        ${nivel.toUpperCase()}
                    </strong>

                </div>


                <div class="resultado-dado">

                    <span>
                        Confiança
                    </span>

                    <strong>
                        ${confianca}%
                    </strong>

                </div>


            </div>



            <!-- =================================================
                 SINAIS
                 ================================================= -->

            ${sinaisHTML}



            <!-- =================================================
                 OUTRAS CATEGORIAS
                 ================================================= -->

            ${categoriasHTML}



            <!-- =================================================
                 ORIENTAÇÃO
                 ================================================= -->

            <div class="resultado-orientacao">

                <div class="orientacao-titulo">

                    💡 Orientação

                </div>


                <p>

                    ${escaparHTML(
                        analise.recomendacao
                    )}

                </p>

            </div>


        </div>

    `;

}


/* ============================================================
   REGISTRAR ALERTA
   ============================================================ */

function registrarAlerta(
    analise,
    mensagem
) {

    const agora =
        new Date();


    const alerta = {

        categoria:
            analise.categoria,

        nivel:
            analise.nivel,

        confianca:
            analise.confianca,

        /*
           A pontuação continua armazenada
           internamente, mas não é exibida
           no site.
        */

        pontuacao:
            analise.pontuacao,

        mensagem:
            mensagem,

        horario:
            agora.toLocaleTimeString(
                "pt-BR"
            ),

        data:
            agora.toLocaleDateString(
                "pt-BR"
            )

    };


    historicoAlertas.unshift(
        alerta
    );


    salvarHistorico();


    atualizarPainel();

}


/* ============================================================
   SALVAR HISTÓRICO
   ============================================================ */

function salvarHistorico() {

    localStorage.setItem(

        "guardia_historico",

        JSON.stringify(
            historicoAlertas
        )

    );

}


/* ============================================================
   CARREGAR HISTÓRICO
   ============================================================ */

function carregarHistorico() {

    const dados =
        localStorage.getItem(
            "guardia_historico"
        );


    if (dados) {

        try {

            historicoAlertas =
                JSON.parse(
                    dados
                );

        } catch {

            historicoAlertas =
                [];

        }

    }


    atualizarPainel();

}


/* ============================================================
   ATUALIZAR PAINEL
   ============================================================ */

function atualizarPainel() {

    const total =
        historicoAlertas.length;


    let alto =
        0;

    let moderado =
        0;

    let baixo =
        0;


    let cyber =
        0;

    let aliciamento =
        0;

    let ameaca =
        0;

    let golpe =
        0;


    historicoAlertas.forEach(
        function (alerta) {

            const nivel =
                String(
                    alerta.nivel || ""
                ).toLowerCase();


            if (
                nivel === "alto"
            ) {

                alto++;

            }


            if (
                nivel === "moderado"
            ) {

                moderado++;

            }


            if (
                nivel === "baixo"
            ) {

                baixo++;

            }


            const categoria =
                String(
                    alerta.categoria || ""
                ).toLowerCase();


            if (
                categoria.includes(
                    "cyberbullying"
                )
            ) {

                cyber++;

            }


            if (
                categoria.includes(
                    "aliciamento"
                )
            ) {

                aliciamento++;

            }


            if (
                categoria.includes(
                    "ameaça"
                )
            ) {

                ameaca++;

            }


            if (
                categoria.includes(
                    "golpe"
                )
            ) {

                golpe++;

            }

        }
    );


    definirTexto(
        "totalAlertas",
        total
    );


    definirTexto(
        "totalAlto",
        alto
    );


    definirTexto(
        "totalModerado",
        moderado
    );


    definirTexto(
        "totalBaixo",
        baixo
    );


    definirTexto(
        "categoriaCyber",
        cyber
    );


    definirTexto(
        "categoriaAliciamento",
        aliciamento
    );


    definirTexto(
        "categoriaAmeaca",
        ameaca
    );


    definirTexto(
        "categoriaGolpe",
        golpe
    );


    let porcentagemAlto =
        0;

    let porcentagemModerado =
        0;

    let porcentagemBaixo =
        0;


    if (total > 0) {

        porcentagemAlto =
            Math.round(
                alto /
                total *
                100
            );


        porcentagemModerado =
            Math.round(
                moderado /
                total *
                100
            );


        porcentagemBaixo =
            Math.round(
                baixo /
                total *
                100
            );

    }


    definirTexto(
        "porcentagemAlto",
        porcentagemAlto + "%"
    );


    definirTexto(
        "porcentagemModerado",
        porcentagemModerado + "%"
    );


    definirTexto(
        "porcentagemBaixo",
        porcentagemBaixo + "%"
    );


    definirLargura(
        "barraAlto",
        porcentagemAlto
    );


    definirLargura(
        "barraModerado",
        porcentagemModerado
    );


    definirLargura(
        "barraBaixo",
        porcentagemBaixo
    );


    atualizarHistoricoVisual();

}


/* ============================================================
   HISTÓRICO VISUAL
   ============================================================ */

function atualizarHistoricoVisual() {

    const lista =
        document.getElementById(
            "listaAlertas"
        );


    if (!lista) {

        return;

    }


    if (
        historicoAlertas.length === 0
    ) {

        lista.innerHTML = `

            <div class="sem-alertas">

                🛡️

                <br><br>

                Nenhum alerta registrado ainda.

                <br>

                As análises realizadas aparecerão aqui.

            </div>

        `;

        return;

    }


    lista.innerHTML =
        historicoAlertas
            .map(
                function (alerta) {

                    return `

                        <div class="alerta-historico">

                            <div class="alerta-topo">

                                <span class="categoria">

                                    ${escaparHTML(
                                        alerta.categoria
                                    )}

                                </span>

                                <span class="horario">

                                    ${escaparHTML(
                                        alerta.data
                                    )}

                                    —

                                    ${escaparHTML(
                                        alerta.horario
                                    )}

                                </span>

                            </div>


                            <div class="texto-mensagem">

                                ${escaparHTML(
                                    alerta.mensagem
                                )}

                            </div>


                            <div class="informacoes">

                                <span class="tag">

                                    Nível:
                                    ${escaparHTML(
                                        alerta.nivel
                                    ).toUpperCase()}

                                </span>


                                <span class="tag">

                                    Confiança:
                                    ${alerta.confianca}%

                                </span>

                            </div>

                        </div>

                    `;

                }
            )
            .join("");

}


/* ============================================================
   LIMPAR HISTÓRICO
   ============================================================ */

function limparHistorico() {

    if (
        historicoAlertas.length === 0
    ) {

        return;

    }


    const confirmar =
        confirm(
            "Deseja realmente limpar o histórico de alertas?"
        );


    if (!confirmar) {

        return;

    }


    historicoAlertas =
        [];


    salvarHistorico();


    atualizarPainel();

}


/* ============================================================
   SIMULAÇÃO DO CELULAR
   ============================================================ */

function mostrarCelular(
    analise
) {

    const overlay =
        document.getElementById(
            "celularOverlay"
        );


    const celular =
        document.getElementById(
            "celular"
        );


    const notificacao =
        document.getElementById(
            "notificacao"
        );


    if (!overlay || !notificacao) {

        return;

    }


    /* ========================================================
       DADOS
       ======================================================== */

    const celularCategoria =
        document.getElementById(
            "celularCategoria"
        );


    if (celularCategoria) {

        celularCategoria.innerText =
            analise.categoria || "-";

    }


    const celularNivel =
        document.getElementById(
            "celularNivel"
        );


    if (celularNivel) {

        celularNivel.innerText =
            String(
                analise.nivel || "-"
            ).toUpperCase();

    }


    const celularConfianca =
        document.getElementById(
            "celularConfianca"
        );


    if (celularConfianca) {

        celularConfianca.innerText =
            String(
                analise.confianca ?? "-"
            ) +
            "%";

    }


    /* ========================================================
       HORA
       ======================================================== */

    atualizarHoraCelular();


    /* ========================================================
       CLASSE DO NÍVEL
       ======================================================== */

    notificacao.classList.remove(
        "nivel-alto",
        "nivel-moderado",
        "nivel-baixo",
        "nivel-seguro"
    );


    const nivel =
        String(
            analise.nivel || "seguro"
        ).toLowerCase();


    if (
        nivel === "alto"
    ) {

        notificacao.classList.add(
            "nivel-alto"
        );

    } else if (
        nivel === "moderado"
    ) {

        notificacao.classList.add(
            "nivel-moderado"
        );

    } else if (
        nivel === "baixo"
    ) {

        notificacao.classList.add(
            "nivel-baixo"
        );

    } else {

        notificacao.classList.add(
            "nivel-seguro"
        );

    }


    /* ========================================================
       ÍCONE
       ======================================================== */

    const emoji =
        document.getElementById(
            "notificacaoEmoji"
        );


    const titulo =
        document.getElementById(
            "notificacaoTitulo"
        );


    const resumo =
        document.getElementById(
            "notificacaoResumo"
        );


    if (
        nivel === "alto"
    ) {

        if (emoji) {

            emoji.innerText =
                "🚨";

        }


        if (titulo) {

            titulo.innerText =
                "Risco alto identificado";

        }


        if (resumo) {

            resumo.innerText =
                "O GuardIA detectou sinais que podem representar uma situação de alto risco.";

        }

    } else if (
        nivel === "moderado"
    ) {

        if (emoji) {

            emoji.innerText =
                "⚠️";

        }


        if (titulo) {

            titulo.innerText =
                "Risco moderado identificado";

        }


        if (resumo) {

            resumo.innerText =
                "O GuardIA identificou sinais que merecem atenção.";

        }

    } else {

        if (emoji) {

            emoji.innerText =
                "🛡️";

        }


        if (titulo) {

            titulo.innerText =
                "Alerta do GuardIA";

        }


        if (resumo) {

            resumo.innerText =
                "O sistema identificou sinais que merecem atenção.";

        }

    }


    /* ========================================================
       REINICIA ANIMAÇÃO
       ======================================================== */

    if (celular) {

        celular.style.animation =
            "none";

        celular.offsetHeight;

        celular.style.animation =
            "";

    }


    notificacao.style.animation =
        "none";

    notificacao.offsetHeight;

    notificacao.style.animation =
        "";


    /* ========================================================
       ABRE O CELULAR
       ======================================================== */

    overlay.style.display =
        "flex";


    /* ========================================================
       PEQUENO EFEITO DE NOTIFICAÇÃO
       ======================================================== */

    setTimeout(
        function () {

            notificacao.classList.add(
                "notificacao-nova"
            );


            setTimeout(
                function () {

                    notificacao.classList.remove(
                        "notificacao-nova"
                    );

                },
                700
            );

        },
        500
    );

}


/* ============================================================
   ATUALIZAR HORA DO CELULAR
   ============================================================ */

function atualizarHoraCelular() {

    const elemento =
        document.getElementById(
            "celularHora"
        );


    const hora =
        new Date().toLocaleTimeString(
            "pt-BR",
            {

                hour:
                    "2-digit",

                minute:
                    "2-digit"

            }
        );


    if (elemento) {

        elemento.innerText =
            hora;

    }


    const horaNotificacao =
        document.getElementById(
            "notificacaoHora"
        );


    if (horaNotificacao) {

        horaNotificacao.innerText =
            hora;

    }

}


/* ============================================================
   ABRIR ALERTA PELO CELULAR
   ============================================================ */

function abrirAlertaPeloCelular() {

    const overlay =
        document.getElementById(
            "celularOverlay"
        );


    if (overlay) {

        overlay.style.display =
            "none";

    }


    mostrarTela(
        "analisador"
    );

}


/* ============================================================
   FECHAR CELULAR
   ============================================================ */

function fecharCelular() {

    const overlay =
        document.getElementById(
            "celularOverlay"
        );


    if (!overlay) {

        return;

    }


    overlay.style.display =
        "none";


    mostrarTela(
        "conversa"
    );

}


/* ============================================================
   ALERTA PRINCIPAL
   ============================================================ */

function mostrarAlertaPrincipal() {

    if (!ultimaAnalise) {

        return;

    }


    const analise =
        ultimaAnalise;


    const overlay =
        document.getElementById(
            "overlay"
        );


    const alerta =
        document.getElementById(
            "alerta"
        );


    if (!overlay || !alerta) {

        return;

    }


    const alertaCategoria =
        document.getElementById(
            "alertaCategoria"
        );


    if (alertaCategoria) {

        alertaCategoria.innerText =
            analise.categoria;

    }


    const alertaNivel =
        document.getElementById(
            "alertaNivel"
        );


    if (alertaNivel) {

        alertaNivel.innerText =
            String(
                analise.nivel
            ).toUpperCase();

    }


    const alertaConfianca =
        document.getElementById(
            "alertaConfianca"
        );


    if (alertaConfianca) {

        alertaConfianca.innerText =
            analise.confianca +
            "%";

    }


    const mensagemAlerta =
        document.getElementById(
            "mensagemAlerta"
        );


    if (mensagemAlerta) {

        mensagemAlerta.innerText =
            "O GuardIA identificou sinais que podem representar um risco em uma conversa.";

    }


    const alertaRecomendacao =
        document.getElementById(
            "alertaRecomendacao"
        );


    if (alertaRecomendacao) {

        alertaRecomendacao.innerText =
            analise.recomendacao;

    }


    alerta.classList.remove(
        "nivel-alto",
        "nivel-moderado",
        "nivel-baixo",
        "nivel-seguro"
    );


    const nivel =
        String(
            analise.nivel || "seguro"
        ).toLowerCase();


    alerta.classList.add(
        "nivel-" +
        nivel
    );


    const iconeAlerta =
        document.getElementById(
            "iconeAlerta"
        );


    if (iconeAlerta) {

        if (
            nivel === "alto"
        ) {

            iconeAlerta.innerText =
                "🚨";

        } else if (
            nivel === "moderado"
        ) {

            iconeAlerta.innerText =
                "⚠️";

        } else {

            iconeAlerta.innerText =
                "🟢";

        }

    }


    overlay.style.display =
        "flex";

}


/* ============================================================
   FECHAR ALERTA
   ============================================================ */

function fecharOverlay() {

    const overlay =
        document.getElementById(
            "overlay"
        );


    if (overlay) {

        overlay.style.display =
            "none";

    }

}


/* ============================================================
   SOBRE O PROJETO
   ============================================================ */

function mostrarSobreProjeto() {

    const overlay =
        document.getElementById(
            "sobreProjetoOverlay"
        );


    if (!overlay) {

        return;

    }


    overlay.classList.add(
        "aberto"
    );


    document.body.style.overflow =
        "hidden";

}


/* ============================================================
   FECHAR SOBRE O PROJETO
   ============================================================ */

function fecharSobreProjeto() {

    const overlay =
        document.getElementById(
            "sobreProjetoOverlay"
        );


    if (!overlay) {

        return;

    }


    overlay.classList.remove(
        "aberto"
    );


    document.body.style.overflow =
        "";

}


/* ============================================================
   FUNÇÕES AUXILIARES
   ============================================================ */

function definirTexto(
    id,
    texto
) {

    const elemento =
        document.getElementById(
            id
        );


    if (elemento) {

        elemento.innerText =
            texto;

    }

}


function definirLargura(
    id,
    porcentagem
) {

    const elemento =
        document.getElementById(
            id
        );


    if (elemento) {

        elemento.style.width =
            porcentagem +
            "%";

    }

}


function escaparHTML(
    texto
) {

    const div =
        document.createElement(
            "div"
        );


    div.innerText =
        texto ?? "";


    return div.innerHTML;

}