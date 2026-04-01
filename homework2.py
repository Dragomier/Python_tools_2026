latin_to_morse = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',
    'E': '.',     'F': '..-.',  'G': '--.',   'H': '....',
    'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',
    'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',
     ' ': ''
}

def create_reversed_dict(dictionary: dict) -> dict:
    return {v:k for k, v in dictionary.items()}

def encode(text: str) -> str:
    text = text.upper()
    letters_to_translate = []
    for letter in text:
        if (ord(letter) >= ord("A") and ord(letter) <= ord("Z")) or letter == " ":
            letters_to_translate.append(letter)
    translated_letters = [latin_to_morse[letter] + '/' for letter in letters_to_translate]

    return "".join(translated_letters)[:-1]

def decode(text: str) -> str:
    morse_to_latin = create_reversed_dict(latin_to_morse)
    letters = text.split('/')
    translated_letters = [morse_to_latin[letter] for letter in letters]

    return "".join(translated_letters).lower()

ans = input("Encode text -- click e \nDecode text -- click d\n")
text = input("Give a text to translate: ")
if ans == 'e':
    print(encode(text))
elif ans == 'd':
    print(decode(text))
else:
    print("Incorrect input, try again!")

