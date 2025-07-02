from flask import Flask, request, jsonify
from text_fancipy import fancy as fancipy_fancy
import fancytext
from fontes_custom import apply_custom_fonts

app = Flask(__name__)

@app.route("/fonte")
def gerar_fontes():
    texto = request.args.get("texto", "")
    if not texto:
        return jsonify({"erro": "Parâmetro 'texto' é obrigatório"}), 400

    resultado = {
        "original": texto
    }

    # Fontes da text-fancipy
    fancipy_estilos = [
        "bubble", "bold", "italic", "outline", "wide", "strike", "slash",
        "flip", "parenthesis", "small", "square", "mirror", "tiny", "dark"
    ]
    for estilo in fancipy_estilos:
        try:
            resultado[f"text_fancipy_{estilo}"] = fancipy_fancy(texto, estilo)
        except:
            pass

    # Fontes do fancytext (via GitHub)
    try:
        fancy_variantes = fancytext.fancy_all(texto)
        for estilo, convertido in fancy_variantes.items():
            resultado[f"fancytext_{estilo}"] = convertido
    except:
        resultado["fancytext_error"] = "Erro ao aplicar fancytext"

    # Fontes manuais (soft aesthetic e mais)
    resultado.update(apply_custom_fonts(texto))

    return jsonify(resultado)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)