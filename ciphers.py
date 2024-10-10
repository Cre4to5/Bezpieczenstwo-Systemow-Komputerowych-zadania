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
    temp1 = ""
    if not mode:
        for l in to_process:
            index = table.find(l)
            temp += f"{index // 7 + 1}{index % 7 + 1}"
        for l in chop(temp,5):
            while len(l)<5:
                l += f"{random.randint(8,9)}"
            # print(l)
            # print(int(l))
            # print(int(l)*int(l))
            # print(a)
            # print(int(l)*int(l)*a)
            # print(b)
            # print(int(l)*int(l)*a+b)
            temp1 += f"{int(l)*int(l)*a+b} "
    else:
        for l in to_process.split(" "):
            # print(l)
            # print(int(l))
            # print(a)
            # print(int(l)/a)
            temp += str(int(math.sqrt((int(l)-b)/a)))
        print(temp)
        for cords in chop(temp,2):
            if len(cords) == 2 and int(cords[0]) - 1 < 5 and int(cords[1]) - 1 < 7:
                temp1 += key[(int(cords[0])-1) % 5 * 7 + int(cords[1]) - 1]
    return temp1
def polybius_key():
    return f"{random.shuffle(ALPHABET)}{random.randint(1,9)}{random.randint(1,9)}"

def chop(string, interval):
    return [string[i:i+interval] for i in range (0, len(string), interval)]
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