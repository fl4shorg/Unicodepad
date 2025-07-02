from flask import Flask, request, jsonify
from text_styler import TextStyler
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

styler = TextStyler()

@app.route('/')
def home():
    return '✨ API Unicode Text Styler Online ✨'

@app.route('/estilizar', methods=['GET'])
def estilizar():
    texto = request.args.get('texto')
    if not texto:
        return jsonify({"erro": "Texto não fornecido. Use ?texto=seu_texto"}), 400

    estilos = styler.get_available_styles()
    resposta = {}

    for estilo in estilos:
        try:
            resposta[estilo] = styler.convert(texto, estilo)
        except Exception:
            resposta[estilo] = None

    return jsonify({
        "original": texto,
        "estilos": resposta
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)