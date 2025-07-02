def soft_aesthetic(text):
    mapa = {
        'a': 'ᥲ', 'b': 'ᥒ', 'c': 'ᥴ', 'd': 'ძ', 'e': 'ᥱ', 'f': 'ƒ', 'g': 'ɠ',
        'h': 'ђ', 'i': 'Ꭵ', 'j': 'ʝ', 'k': 'ƙ', 'l': 'ᥣ', 'm': 'ᥒ', 'n': 'ᥒ',
        'o': '᥆', 'p': 'ρ', 'q': 'զ', 'r': 'r', 's': '᥉', 't': 't', 'u': 'ᥙ',
        'v': 'ⱴ', 'w': 'ᥕ', 'x': '᥊', 'y': 'ყ', 'z': 'ʐ',
        'A': 'ᴀ', 'B': 'ʙ', 'C': 'ᴄ', 'D': 'ᴅ', 'E': 'ᴇ', 'F': 'ғ', 'G': 'ɢ',
        'H': 'ʜ', 'I': 'ɪ', 'J': 'ᴊ', 'K': 'ᴋ', 'L': 'ʟ', 'M': 'ᴍ', 'N': 'ɴ',
        'O': 'ᴏ', 'P': 'ᴘ', 'Q': 'ǫ', 'R': 'ʀ', 'S': 's', 'T': 'ᴛ', 'U': 'ᴜ',
        'V': 'ᴠ', 'W': 'ᴡ', 'X': 'x', 'Y': 'ʏ', 'Z': 'ᴢ', ' ': ' '
    }
    return ''.join(mapa.get(c, c) for c in text)

def tinycaps(text):
    mapa = { 
        'a':'ᵃ','b':'ᵇ','c':'ᶜ','d':'ᵈ','e':'ᵉ','f':'ᶠ','g':'ᵍ','h':'ʰ','i':'ᶦ','j':'ʲ','k':'ᵏ','l':'ˡ','m':'ᵐ','n':'ⁿ','o':'ᵒ','p':'ᵖ','q':'ᑫ','r':'ʳ','s':'ˢ','t':'ᵗ','u':'ᵘ','v':'ᵛ','w':'ʷ','x':'ˣ','y':'ʸ','z':'ᶻ',
        ' ':' '
    }
    return ''.join(mapa.get(c.lower(), c) for c in text)

def boxed(text):
    return ''.join(chr(ord('🄰') + (ord(c) - 65)) if c.isupper() else c for c in text)

def apply_custom_fonts(text):
    return {
        "soft_aesthetic": soft_aesthetic(text),
        "tiny_caps": tinycaps(text),
        "boxed_uppercase": boxed(text)
    }