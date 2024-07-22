def generate_soundex(name):
    if not name:
        return ""

    soundex = name[0].upper()  # Start with the uppercase first letter
    prev_code = get_soundex_code(name[0])  # Get initial Soundex code
    
    for char in name[1:]:
        code = get_soundex_code(char)
        
        if should_add_code(code, prev_code) and len(soundex) < 4:
            soundex += code
            prev_code = code
        
        if len(soundex) == 4:
            break
    
    return pad_soundex(soundex)

def should_add_code(code, prev_code):
    return code != '0' and code != prev_code

def pad_soundex(soundex):
    return soundex.ljust(4, '0')

def get_soundex_code(char):
    vowels = 'aeiouyhw'
    if char.lower() in vowels:
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




