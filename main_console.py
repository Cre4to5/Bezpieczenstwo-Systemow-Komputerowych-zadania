from ciphers import messageCleaner, caesarCipher, caesarKey, isCaesarKey, polybiusCipher, polybiusKey, isPolybiusKey

def console_menu(cipher, keyGenerate, isKey): 
    key = input("Podaj Klucz: ")
    if key == "":
        key = keyGenerate()
    while not isKey(key):
        key = input("Błędny Klucz!\nPodaj Prawidłowy Klucz lub zosaw puste pole: ")
    match input("Co chcesz zrobić?\n1.Zaszyfruj\n2.Odszyfruj\n"):
        case "1":
            print(f"Oto zaszyfrowana wiadomość: {cipher(messageCleaner(input("Podaj wiadomość do zaszyfrowania: ")), key, False)}")
        case "2":
            print(f"Oto odszyfrowana wiadomość: {cipher(input("Podaj wiadomość do odszyfrowania: "), key, True)}")
def main():
    match input("Jaki Szyfr?\n1.Caesara\n2.Szachownica Polibiusza\n"):
        case "1":
            console_menu(caesarCipher, caesarKey, isCaesarKey)
        case "2":
            console_menu(polybiusCipher, polybiusKey, isPolybiusKey)
if __name__ == '__main__':
    main()