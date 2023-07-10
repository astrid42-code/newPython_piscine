import sys

# https://geekflare.com/fr/python-morse-code-translator/
# only space and alphanumeric chars 
CHARS_TO_MORSE_CODE_MAPPING = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    # '.': '.-.-.-',
    # ',': '--..--',
    # '?': '..--..',
    # '\'': '· − − − − ·',
    # '!': '− · − · − −',
    # '/': '− · · − ·',
    # '(': '− · − − ·',
    # ')': '− · − − · −',
    # '&': '· − · · ·',
    # ':': '− − − · · ·',
    # ';': '− · − · − ·',
    # '=': '− · · · −',
    # '+': '· − · − ·',
    # '-': '− · · · · −',
    # '_': '· · − − · −',
    # '"': '· − · · − ·',
    # '$': '· · · − · · −',
    # '@': '· − − · − ·',
}

str = ''
if (len(sys.argv) == 1):
    sys.exit(1)
elif (len(sys.argv) > 2):
    sys.argv.pop(0)
    str = ' '.join(sys.argv)
else:
    str = sys.argv[1]

def to_morse_code(str):
    morse_code = ''
    for char in str:
        if char.islower():
            char = char.upper()
        if char == ' ':
            morse_code += '/ '
        elif char not in CHARS_TO_MORSE_CODE_MAPPING.keys():
            print("ERROR")
            sys.exit(1)
        else:
            morse_code += CHARS_TO_MORSE_CODE_MAPPING[char] + ' '
    return morse_code

morse_code = str
res = to_morse_code(morse_code)
print(res)

sys.exit(1)