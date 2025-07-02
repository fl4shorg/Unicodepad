from flask import Flask, request, jsonify
from text_fancipy import fancy as fancipy_fancy
from fontes_custom import apply_custom_fonts

app = Flask(__name__)

@app.route("/fonte")
def gerar_fontes():
    texto = request.args.get("texto", "")
    if not texto:
        return jsonify({"erro": "Parâmetro 'texto' é obrigatório"}), 400

    resultado = {"original": texto}

    # Fontes do text-fancipy (~60 estilos)
    estilos = [
        "bubble", "bold", "italic", "outline", "wide", "strike", "slash",
        "flip", "parenthesis", "small", "square", "mirror", "tiny", "dark",
        "circled", "circled_white", "upside_down", "currency", "roman", 
        "superscript", "subscript", "block", "underline", "slash_through", 
        "invisible", "diacritical", "zalgo"
    ]

    for estilo in estilos:
        try:
            resultado[f"textfancipy_{estilo}"] = fancipy_fancy(texto, estilo)
        except Exception:
            pass

    # Fontes personalizadas (manuais)
    resultado.update(apply_custom_fonts(texto))

    return jsonify(resultado)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)