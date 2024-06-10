alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = (input("Type your message:\n").lower())
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
special_characters = "!@#$%^&*()-+={}[]|\;:'\"<>,.?/~"


def encode(text, shift):

    text1 = []
    for i in range(0, len(text)):
        if text[i] in special_characters:
            text1.append(text[i])
        elif text[i] == ' ':
            text1.append(" ")
        elif text[i] in alphabet:
            new_index = alphabet.index(text[i]) + shift
            if new_index > 25:
                new_index = new_index - 26
            text1.append(alphabet[new_index])

    return print(str(text1))


encode(text, shift)

def decode(text, shift):
    
    text1 = []
    for i in range(0, len(text)):
        if text[i] in special_characters:
            text1.append(text[i])
        elif text[i] == ' ':
            text1.append(" ")
        elif text[i] in alphabet:
            new_index = alphabet.index(text[i]) - shift
            if new_index < 0:
                new_index = 26 - new_index
            text1.append(alphabet[new_index])

    return print(str(text1))

decode(text, shift)