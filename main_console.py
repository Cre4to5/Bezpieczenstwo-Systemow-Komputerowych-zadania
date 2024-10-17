from ciphers import caesar_cipher, caesar_key, polybius_square_cipher, polybius_key, message_cleaner

def console_menu(cipher, key_generate): 
    key = input("Podaj Klucz: ")
    if key == "":
        key = key_generate()
    match input("Co chcesz zrobić?\n1.Zaszyfruj\n2.Odszyfruj\n"):
        case "1":
            print(f"Oto zaszyfrowana wiadomość: {cipher(message_cleaner(input("Podaj wiadomość do zaszyfrowania: ")), key, False)}")
        case "2":
            print(f"Oto odszyfrowana wiadomość: {cipher(input("Podaj wiadomość do odszyfrowania: "), key, True)}")
def main():
    match input("Jaki Szyfr?\n1.Caesara\n2.Szachownica Polibiusza\n"):
        case "1":
            console_menu(caesar_cipher, caesar_key)
        case "2":
            console_menu(polybius_square_cipher, polybius_key)
if __name__ == '__main__':
    main()