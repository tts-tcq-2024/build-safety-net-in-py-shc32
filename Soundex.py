def generate_soundex(name):
    if not name:
        return ""

    soundex = name[0].upper()
    prev_code = get_soundex_code(name[0])
    
    for char in name[1:]:
        code = get_soundex_code(char)
        if should_add_code(code, prev_code) and len(soundex) < 4:
            soundex += code
            prev_code = code
        elif len(soundex) == 4:
            break
        else:
            prev_code = code

    soundex = pad_soundex(soundex)
    return soundex

def pad_soundex(soundex):
    return soundex.ljust(4, '0')

def get_soundex_code(char):
    if char.lower() in 'aeiouyhw':
        return '0'
    
    mapping = {
        'b': '1', 'f': '1', 'p': '1', 'v': '1',
        'c': '2', 'g': '2', 'j': '2', 'k': '2', 'q': '2',
        's': '2', 'x': '2', 'z': '2',
        'd': '3', 't': '3',
        'l': '4',
        'm': '5', 'n': '5',
        'r': '6'
    }
    return mapping.get(char.lower(), '0')



