def generate_soundex(name):
    if not name:
        return ""

    soundex = initialize_soundex(name)
    soundex = process_name_for_soundex(name, soundex)
    soundex = pad_soundex(soundex)

    return soundex

def initialize_soundex(name):
    # Start with the first letter (capitalized)
    return name[0].upper() if name else ""

def process_name_for_soundex(name, soundex):
    if not soundex:
        return soundex
    
    prev_code = get_soundex_code(soundex)
    for char in name[1:]:
        prev_code = add_code_and_update_prev_code(char, soundex, prev_code)
        if is_soundex_complete(soundex):
            break
    
    return soundex

def add_code_and_update_prev_code(char, soundex, prev_code):
    code = get_soundex_code(char)
    if should_add_code(code, prev_code) and not is_soundex_complete(soundex):
        soundex = append_code(soundex, code)
        prev_code = update_prev_code(prev_code, code)
    return prev_code

def append_code(soundex, code):
    return soundex + code

def update_prev_code(prev_code, code):
    return code if should_add_code(code, prev_code) else prev_code

def should_add_code(code, prev_code):
    return code != '0' and code != prev_code

def is_soundex_complete(soundex):
    return len(soundex) == 4

def pad_soundex(soundex):
    # Pad with zeros if necessary
    return soundex.ljust(4, '0')

def get_soundex_code(char):
    # Define your logic here to get the Soundex code for a given character
    # Example implementation:
    # (For simplicity, assuming all non-'a-z' characters return '0')
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


