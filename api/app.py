# ============================================================
# GUARDIA
# API Flask
# ============================================================

from flask import Flask, request, jsonify, render_template
import sys
import os


# ============================================================
# PERMITE ENCONTRAR O guardia.py
# ============================================================

PASTA_PRINCIPAL = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.insert(0, PASTA_PRINCIPAL)


# ============================================================
# IMPORTA O CÉREBRO DO GUARDIA
# ============================================================

from guardia import analisar_mensagem


# ============================================================
# CRIA A APLICAÇÃO
# ============================================================

app = Flask(__name__)


# ============================================================
# ROTA PRINCIPAL
# ============================================================

@app.route("/")
def inicio():

    return render_template("index.html")


# ============================================================
# ROTA DE ANÁLISE
# ============================================================

@app.route("/analisar", methods=["POST"])
def analisar():

    # Tenta receber JSON
    dados = request.get_json(silent=True)


    # Verifica se recebeu dados
    if not dados:

        return jsonify({
            "erro": "Nenhum dado foi enviado."
        }), 400


    # Obtém a mensagem
    mensagem = dados.get("mensagem")


    # Verifica se existe mensagem
    if not mensagem:

        return jsonify({
            "erro": "O campo 'mensagem' é obrigatório."
        }), 400


    # Verifica se é texto
    if not isinstance(mensagem, str):

        return jsonify({
            "erro": "O campo 'mensagem' deve ser um texto."
        }), 400


    # Remove espaços extras
    mensagem = mensagem.strip()


    # Verifica mensagem vazia
    if not mensagem:

        return jsonify({
            "erro": "A mensagem não pode estar vazia."
        }), 400


    # ========================================================
    # ANALISA A MENSAGEM
    # ========================================================

    resultado = analisar_mensagem(mensagem)


    # ========================================================
    # DEVOLVE O RESULTADO
    # ========================================================

    return jsonify({
        "mensagem_analisada": mensagem,
        "resultado": resultado
    })


# ============================================================
# ROTA DE TESTE
# ============================================================

@app.route("/status")
def status():

    return jsonify({
        "status": "online",
        "servico": "GuardIA API",
        "versao": "1.0"
    })


# ============================================================
# INICIAR SERVIDOR
# ============================================================

if __name__ == "__main__":

    print()
    print("=" * 60)
    print("🛡️ GUARDIA OVERLAY - API")
    print("=" * 60)
    print()
    print("Servidor iniciando...")
    print()
    print("Acesse:")
    print("http://127.0.0.1:5000")
    print()
    print("Para encerrar: CTRL + C")
    print()
    print("=" * 60)
    print()

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )