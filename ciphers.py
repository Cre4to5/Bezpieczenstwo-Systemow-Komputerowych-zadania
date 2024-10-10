import random
import math
ALPHABET = "aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż"
def shift(to_be_shifted, n):
    pass#TODO
def caesar_cipher(to_process, key, mode):
    pass#TODO
def caesar_key():
    return random.randint(0, 33)

def polybius_square_cipher(to_process, key, mode):
    table = key[0:35]
    a = int(key[35])
    b = int(key[36])
    temp = ""
    if not mode:
        for l in to_process:
            index = table.find(l)
            temp += f"{index // 7 + 1}{index % 7 + 1}"
        for l in [temp[i:i+5] for i in range (0, len(temp), 5)]:
            while len(l)<5:
                l += f"{random.randint(1,7)}"
            temp += f"{int(l)*int(l)*a+b} "
    else:
        for l in to_process.split(" "):
            (math.sqrt(int(l)/a)-b)#TODO
    return temp
def polybius_key():
    return f"{random.shuffle(ALPHABET)}{random.randint(1,9)}{random.randint(1,9)}"

def message_cleaner(msg):
    temp = ""
    for l in msg.lower():
        if l in ALPHABET:
            temp += l
    return temp
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