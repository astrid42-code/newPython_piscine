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

    """
    This function takes a single string argument,
    translate it in morse code
    then it prints the string in morse
    Punctuation marks and special characters result in an error
    """
    morse_code = ''
    print(str)
    for char in str:
        print(char)
        if char.islower():
            char = char.upper()
            # print(char)
        
        elif char not in NESTED_MORSE.keys():
            assert False, "the arguments are bad"
        morse_code += NESTED_MORSE[char] + ' '
        # print(morse_code)
    return morse_code


morse_code = str
res = to_morse_code(morse_code)
print(res)

sys.exit(1)

# ATTENTION : le $ coupe la string !! c est malefique
