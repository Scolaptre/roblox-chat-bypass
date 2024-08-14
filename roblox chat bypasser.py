import os
from os import system
import random
try:
    import pyperclip
except:
    os.system("pip install pyperclip")
try:
    import keyboard
except:
    os.system("pip install keyboard")

def add_accent(phrase):
    accents = {
        'a': ['á', 'à', 'â'], 'b': ['b́', 'b̀', 'b̂'], 'c': ['ć', 'c̀', 'ĉ'], 'd': ['ḋ', 'd̀', 'd̂'], 'e': ['é', 'è', 'ê'],
        'f': ['f́', 'f̀', 'f̂'], 'g': ['ǵ', 'g̀', 'ĝ'], 'h': ['h́', 'h̀', 'ĥ'], 'i': ['í', 'ì', 'î'], 'j': ['j́', 'j̀', 'ĵ'],
        'k': ['ḱ', 'k̀', 'k̂'], 'l': ['ĺ', 'l̀', 'l̂'], 'm': ['ḿ', 'm̀', 'm̂'], 'n': ['ń', 'ǹ', 'n̂'], 'o': ['ó', 'ò', 'ô'],
        'p': ['ṕ', 'p̀', 'p̂'], 'q': ['q́', 'q̀', 'q̂'], 'r': ['ŕ', 'r̀', 'r̂'], 's': ['ś', 's̀', 'ŝ'], 't': ['t́', 't̀', 't̂'],
        'u': ['ú', 'ù', 'û'], 'v': ['v́', 'v̀', 'v̂'], 'w': ['ẃ', 'ẁ', 'ŵ'], 'x': ['x́', 'x̀', 'x̂'], 'y': ['ý', 'ỳ', 'ŷ'], 'z': ['ź', 'z̀', 'ẑ'],
        'A': ['Á', 'À', 'Â'], 'B': ['B́', 'B̀', 'B̂'], 'C': ['Ć', 'C̀', 'Ĉ'], 'D': ['Ḋ', 'D̀', 'D̂'], 'E': ['É', 'È', 'Ê'],
        'F': ['F́', 'F̀', 'F̂'], 'G': ['Ǵ', 'G̀', 'Ĝ'], 'H': ['H́', 'H̀', 'Ĥ'], 'I': ['Í', 'Ì', 'Î'], 'J': ['J́', 'J̀', 'Ĵ'],
        'K': ['Ḱ', 'K̀', 'K̂'], 'L': ['Ĺ', 'L̀', 'L̂'], 'M': ['Ḿ', 'M̀', 'M̂'], 'N': ['Ń', 'Ǹ', 'N̂'], 'O': ['Ó', 'Ò', 'Ô'],
        'P': ['Ṕ', 'P̀', 'P̂'], 'Q': ['Q́', 'Q̀', 'Q̂'], 'R': ['Ŕ', 'R̀', 'R̂'], 'S': ['Ś', 'S̀', 'Ŝ'], 'T': ['T́', 'T̀', 'T̂'],
        'U': ['Ú', 'Ù', 'Û'], 'V': ['V́', 'V̀', 'V̂'], 'W': ['Ẃ', 'Ẁ', 'Ŵ'], 'X': ['X́', 'X̀', 'X̂'], 'Y': ['Ý', 'Ỳ', 'Ŷ'], 'Z': ['Ź', 'Z̀', 'Ẑ']
    }

    new_phrase = ''
    for char in phrase:
        if char in accents:
            new_phrase += random.choice(accents[char])
        elif char == ' ':
            new_phrase += ' '
        else:
            new_phrase += char
    
    return new_phrase

def main():
    obf = int(input("obf level: "))
    print("Type a phrase and press 'Enter'. The accented phrase will be copied to the clipboard.")
    print("Press 'Ctrl+C' to exit.")
    while True:
        try:
            phrase = input("\nYour phrase: ")
            phrase_accent = phrase
            for _ in range(obf):
                phrase_accent = add_accent(phrase_accent)
            pyperclip.copy(phrase_accent)
            print(f"\nphrase copied to clipboard\n")
        except KeyboardInterrupt:
            print("\nProgram completed.")
            break

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()

