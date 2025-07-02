from flask import Flask, request, jsonify
from text_styler import TextStyler
from flask_cors import CORS
import os

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

    estilos = [
        'bold', 'italic', 'bold italic',
        'monospace', 'double-struck', 'script',
        'bold script', 'fraktur', 'bold fraktur',
        'sans', 'bold sans', 'italic sans', 'bold italic sans',
        'circled', 'circled negative', 'squared', 'squared negative',
        'upside down', 'mirrored', 'fullwidth'
    ]

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
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)