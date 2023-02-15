en_to_morse = {
    'A': '.-',     'B': '-...',   'C': '-.-.',
    'D': '-..',    'E': '.',      'F': '..-.',
    'G': '--.',    'H': '....',   'I': '..',
    'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',
    'S': '...',    'T': '-',      'U': '..-',
    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',

    '0': '-----',  '1': '.----',  '2': '..---',
    '3': '...--',  '4': '....-',  '5': '.....',
    '6': '-....',  '7': '--...',  '8': '---..',
    '9': '----.'
}

morse_to_en = {
    '.-': 'A',    '-...': 'B',  '-.-.': 'C',
    '-..': 'D',   '.': 'E',     '..-.': 'F',
    '--.': 'G',   '....': 'H',  '..': 'I',
    '.---': 'J',  '-.-': 'K',   '.-..': 'L',
    '--': 'M',    '-.': 'N',    '---': 'O',
    '.--.': 'P',  '--.-': 'Q',  '.-.': 'R',
    '...': 'S',   '-': 'T',     '..-': 'U',
    '...-': 'V',  '.--': 'W',   '-..-': 'X',
    '-.--': 'Y',  '--..': 'Z',
    
    '-----': '0', '.----': '1', '..---': '2',
    '...--': '3', '....-': '4', '.....': '5',
    '-....': '6', '--...': '7', '---..': '8',
    '----.': '9'
}

morse_code = input('Input Morse code: ')

# Split the Morse code input into individual symbols
morse_list = morse_code.split()

# Translate each Morse symbol to its corresponding English letter/number using the morse_to_en dictionary
english_list = [morse_to_en.get(x, '') for x in morse_list]

# Join the English letters/numbers into a single string and print to the console
english_word = ''.join(english_list)
print(english_word)

print(' '.join(en_to_morse.get(x, '') for x in input('Input a word: ').upper()))
