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

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def add_accent(phrase):
    accents = ['\u0301', '\u0300', '\u0302']
    
    new_phrase = ''
    for char in phrase:
        if char.isalpha():
            new_phrase += char + random.choice(accents)
        else:
            new_phrase += char
    
    return new_phrase

def main():
    while True:
        try:
            obf = int(input("obf level: "))
            clear_screen()
            break
        except ValueError:
            input("\nInvalid input. Please enter a valid integer.")
            clear_screen()

    print("Type a phrase and press 'Enter'. The accented phrase will be copied to the clipboard.")
    print("Press 'Ctrl+C' to exit.")
    while True:
        try:
            phrase = input("\nYour phrase: ")
            phrase_accent = phrase
            for _ in range(obf):
                phrase_accent = add_accent(phrase_accent)
            pyperclip.copy(phrase_accent)
            input(f"\nPhrase copied to clipboard")
            clear_screen()
        except KeyboardInterrupt:
            print("\nProgram completed.")
            break

if __name__ == "__main__":
    main()
