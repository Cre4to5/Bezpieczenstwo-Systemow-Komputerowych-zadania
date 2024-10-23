import random
import math

ALPHABET = "aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż"

def shift(to_be_shifted, n):
    processedMsg = ""
    for l in to_be_shifted:
        INDEX = ALPHABET.index(l)#check where the character is in an alphabet
        processedMsg += ALPHABET[(INDEX + n) % len(ALPHABET)]#next character index shifted by a key
    return processedMsg
def caesarCipher(to_process, key, isDeciphering):
    key = int(key)#key should always be a str
    if isDeciphering:#which way we are shifting
        key = -key
    return shift(to_process, key)
def caesarKey():
    return str(random.randint(0, len(ALPHABET)))#key is random positive int smaller than alphabets length
def isCaesarKey(s):
    if type(s) == str and str.isnumeric(s):#key needs to be a string and be composed of numbers
        return int(s) >= 0 and int(s) <= len(ALPHABET)#key needs to be positive int smaller than alphabets length
    return False

def polybiusCipher(to_process, key, mode):
    table = key[0:35]#decomposing key to variables
    a = int(key[35])
    b = int(key[36])
    firstProcesing = ""
    processedMsg = ""
    if not mode:
        for l in to_process:
            index = table.find(l)#check where the character is in an alphabet
            firstProcesing += f"{index // 7 + 1}{index % 7 + 1}"#convert index into cordinates in polybius square
        for l in chop(firstProcesing,5):#split so numbers won't get too big
            while len(l)<5:#for the last number if it isn't multiple of 5
                l += f"{random.randint(8,9)}"#random numbers that are unused by cipher
            processedMsg += f"{int(l)*int(l)*a+b} "#performing math operations on segmented numbers to jumble them up
    else:
        for l in to_process.split(" "):
            firstProcesing += str(int(math.sqrt((int(l)-b)/a)))#undoing math operations
        for cords in chop(firstProcesing,2):
            if len(cords) == 2 and int(cords[0]) - 1 < 5 and int(cords[1]) - 1 < 7:
                processedMsg += key[(int(cords[0])-1) % 5 * 7 + int(cords[1]) - 1]
    return processedMsg
def polybiusKey():
    return f"{random.shuffle(ALPHABET)}{random.randint(1,9)}{random.randint(1,9)}"
def isPolybiusKey(s):
    return True#TODO

def chop(string, interval):
    return [string[i:i+interval] for i in range (0, len(string), interval)]
def messageCleaner(msg):
    temp = ""
    for l in msg.lower():
        if l in ALPHABET:
            temp += l
    return temp