from flask import Flask, request, jsonify
from fancify_text import bold, italic, bubble, wide
from text_fancipy import fancy as fancipy_fancy

app = Flask(__name__)

soft_map = {
    'a': 'ᥲ', 'b': 'ᥒ', 'c': 'ᥴ', 'd': 'ძ', 'e': 'ᥱ', 'f': 'ƒ', 'g': 'ɠ',
    'h': 'ђ', 'i': 'Ꭵ', 'j': 'ʝ', 'k': 'ƙ', 'l': 'ᥣ', 'm': 'ᥒ', 'n': 'ᥒ',
    'o': '᥆', 'p': 'ρ', 'q': 'զ', 'r': 'r', 's': '᥉', 't': 't', 'u': 'ᥙ',
    'v': 'ⱴ', 'w': 'ᥕ', 'x': '᥊', 'y': 'ყ', 'z': 'ʐ',
    'A': 'ᴀ', 'B': 'ʙ', 'C': 'ᴄ', 'D': 'ᴅ', 'E': 'ᴇ', 'F': 'ғ', 'G': 'ɢ',
    'H': 'ʜ', 'I': 'ɪ', 'J': 'ᴊ', 'K': 'ᴋ', 'L': 'ʟ', 'M': 'ᴍ', 'N': 'ɴ',
    'O': 'ᴏ', 'P': 'ᴘ', 'Q': 'ǫ', 'R': 'ʀ', 'S': 's', 'T': 'ᴛ', 'U': 'ᴜ',
    'V': 'ᴠ', 'W': 'ᴡ', 'X': 'x', 'Y': 'ʏ', 'Z': 'ᴢ',
    ' ': ' '
}

def soft_aesthetic(text):
    return ''.join(soft_map.get(c, c) for c in text)

@app.route('/fonte')
def fonte():
    texto = request.args.get('texto', '')
    if not texto:
        return jsonify({'erro': 'Parâmetro "texto" é obrigatório'}), 400
    
    resultado = {
        'original': texto,
        'fancify_bold': bold(texto),
        'fancify_italic': italic(texto),
        'fancify_bubble': bubble(texto),
        'fancify_wide': wide(texto),
        'fancipy_bubble': fancipy_fancy(texto, 'bubble'),
        'fancipy_cursive': fancipy_fancy(texto, 'cursive'),
        'soft_aesthetic': soft_aesthetic(texto),
    }
    return jsonify(resultado)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)