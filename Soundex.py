def get_soundex_code(c):
    c = c.upper()
    mapping = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }
    return mapping.get(c, '0')  # Default to '0' for non-mapped characters

def generate_soundex(name):
    if not name:
        return ""

    # Step 1: Start with the first letter (capitalized)
    soundex = name[0].upper()
    prev_code = get_soundex_code(soundex)

    # Step 2: Iterate through the remaining characters in the name
    for char in name[1:]:
        code = get_soundex_code(char)
        if code != '0' and code != prev_code:
            soundex += code
            prev_code = code
        
        # Step 3: Break loop if the soundex is already 4 characters long
        if len(soundex) == 4:
            break

    # Step 4: Pad with zeros if necessary
    soundex = soundex.ljust(4, '0')

    return soundex

