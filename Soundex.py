def remove_vowels_except_first_letter(word):
    if not word:
        return ''
    
    first_letter = word[0]
    return first_letter + ''.join(char for char in word[1:] if char not in 'aeiouyhw')

def encode_consonants(word):
    mapping = {
        'b': '1', 'f': '1', 'p': '1', 'v': '1',
        'c': '2', 'g': '2', 'j': '2', 'k': '2', 'q': '2',
        's': '2', 'x': '2', 'z': '2',
        'd': '3', 't': '3',
        'l': '4',
        'm': '5', 'n': '5',
        'r': '6'
    }
    
    first_letter = word[0]
    encoded = [first_letter]
    for char in word[1:]:
        digit = mapping.get(char)
        if digit and (not encoded or digit != encoded[-1]):
            encoded.append(digit)
    
    return encoded

def remove_duplicate_adjacent_digits(encoded):
    return [char for i, char in enumerate(encoded) if i == 0 or char != encoded[i-1]]

def soundex(word):
    if not word:
        return None
    
    word = word.lower()
    word = remove_vowels_except_first_letter(word)
    encoded = encode_consonants(word)
    encoded = remove_duplicate_adjacent_digits(encoded)
    encoded = (encoded + ['0', '0', '0'])[:4]
    
    return ''.join(encoded)
