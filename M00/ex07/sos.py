import sys

# https://geekflare.com/fr/python-morse-code-translator/
# only space and alphanumeric chars
NESTED_MORSE = {
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
    ' ': '/ '
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
    assert False, "the arguments are bad"
else:
    str = sys.argv[1]


def to_morse_code(str):
    morse_code = ''
    for char in str:
        if char.islower():
            char = char.upper()
        elif char not in NESTED_MORSE.keys():
            assert False, "the arguments are bad"
        morse_code += NESTED_MORSE[char] + ' '
    return morse_code


morse_code = str
res = to_morse_code(morse_code)
print(res)

sys.exit(1)
