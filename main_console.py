from ciphers import messageCleaner, caesarCipher, caesarKey, isCaesarKey, polybiusCipher, polybiusKey, isPolybiusKey, vigenereCipher, vigenereKey, isVigenereKey, playfairCipher, playfairKey, isPlayfairKey

def console_menu(cipher, keyGenerate, isKey): 
    key = ""
    while not isKey(key):
        key = input("Podaj Klucz lub zosaw puste pole aby wygenerować: ")
        if key == "":
            key = keyGenerate()
            print(f"Oto wygenerowany klucz: {key}")
    match input("Co chcesz zrobić?\n1.Zaszyfruj\n2.Odszyfruj\n"):
        case "1":
            print(f"Oto zaszyfrowana wiadomość: {cipher(messageCleaner(input("Podaj wiadomość do zaszyfrowania: ")), key, False)}")
        case "2":
            print(f"Oto odszyfrowana wiadomość: {cipher(input("Podaj wiadomość do odszyfrowania: "), key, True)}")
def main():
    match input("Jaki Szyfr?\n1.Caesara\n2.Szachownica Polibiusza\n3.Vigenera\n4.Szyfr Playfair\n"):
        case "1":
            console_menu(caesarCipher, caesarKey, isCaesarKey)
        case "2":
            console_menu(polybiusCipher, polybiusKey, isPolybiusKey)
        case "3":
            console_menu(vigenereCipher, vigenereKey, isVigenereKey)
        case "4":
            console_menu(playfairCipher, playfairKey, isPlayfairKey)
if __name__ == '__main__':
    main()