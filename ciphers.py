import random
import math

ALPHABET = "aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż"
ROWS, COLLUMNS = 5, 7#rows * collumns needs to equal length of alphabet
BATCHES = 5#batch size of numbers to do operations with
RARE = ["x", "v", "ź", "q"]#rarest letters in polish language (so they are easy to spot after decription)

#region Caesar Cipher
def shift(toBeShifted, n):
    processedMsg = ""
    for l in toBeShifted:
        processedMsg += singleShift(l, n)
    return processedMsg
def caesarCipher(toProcess, key, isDeciphering):
    key = int(key)#key should always be a str
    if isDeciphering:#which way we are shifting
        key = -key
    return shift(toProcess, key)
def caesarKey():
    return str(random.randint(0, len(ALPHABET)))#key is random positive int smaller than alphabets length
def isCaesarKey(s):
    if type(s) == str and str.isnumeric(s):#key needs to be a string and be composed of numbers
        return int(s) >= 0 and int(s) <= len(ALPHABET)#key needs to be positive int smaller than alphabets length
    return False
#endregion
#region Polybius Square Cipher
def polybiusCipher(toProcess, key, mode):
    table = key[0:len(ALPHABET)]#decomposing key to variables
    a = int(key[len(ALPHABET)])
    b = int(key[len(ALPHABET) + 1])
    firstProcesing = ""
    processedMsg = ""
    if not mode:
        for l in toProcess:
            x, y = indexToCordinates(table.find(l))
            firstProcesing += f"{x}{y}"#convert index into cordinates in polybius square
        for l in chop(firstProcesing,BATCHES):#split so numbers won't get too big
            while len(l) < BATCHES:#for the last number if it isn't multiple of 5
                l += f"{random.randint(max(ROWS, COLLUMNS) + 1,9)}"#random numbers that are unused by cipher
            processedMsg += f"{int(l)*int(l)*a+b} "#performing math operations on segmented numbers to jumble them up
    else:
        for l in toProcess.split(" "):
            firstProcesing += str(int(math.sqrt((int(l)-b)/a)))#undoing math operations
        for coords in chop(firstProcesing,2):#indecies are in pairs of two
            if len(coords) == 2 and int(coords[0]) - 1 < 5 and int(coords[1]) - 1 < 7:#filtering random mumbo jumbo possibly done to fill last group of five
                processedMsg += key[cordinatesToIndex(int(coords[0]),int(coords[1]))]#converting cordinates to index and then to deciphered letter
    return processedMsg
def polybiusKey():
    return f"{playfairKey()}{random.randint(1,9)}{random.randint(1,9)}"#every polibious key is jumbled alphabet and two non zero digits
def isPolybiusKey(s):
    return isPlayfairKey(s[0:35]) and str.isdigit(s[35]) and str.isdigit(s[36]) and int(s[35]) > 0 and int(s[36]) > 0
#endregion
#region Vigenere Cipher
def vigenereCipher(toProcess, key, isDeciphering):
    processedMsg = ""
    while len(key) < len(toProcess):
        key += key
    for l, k in zip(toProcess, key):
        shiftBy = ALPHABET.index(k)
        if isDeciphering:
            shiftBy = -shiftBy
        processedMsg += singleShift(l, shiftBy)
    return processedMsg
def vigenereKey():
    f = open(file="./PlWords.txt",mode="r",encoding="utf8")
    lines = f.readlines()
    # print(lines)
    return random.choice(list(x.strip() for x in lines))
def isVigenereKey(s):
    if len(s) == 0:
        return False
    for l in s:
        if l not in ALPHABET:
            return False
    return True
#endregion
#region Playfair Cipher
def noDoubleLetters(toProcess):
    processedMsg = ""
    for i in range(0,len(toProcess),2):
        processedMsg += toProcess[i]
        if i+1 < len(toProcess):
            if toProcess[i] == toProcess[i + 1]:
                if toProcess[i] in RARE:
                    processedMsg += random.choice([x for x in RARE if x != toProcess[i]])
                else:
                    processedMsg += random.choice(RARE)[0]
            processedMsg += toProcess[i + 1]
        else:
            processedMsg += random.choice(RARE)
    print(processedMsg)
    return processedMsg
def playfairCipher(toProcess, key, isDeciphering):
    processedMsg = ""
    for pair in chop(noDoubleLetters(toProcess), 2):
        row1, collumn1 = indexToCordinates(key.index(pair[0]))
        row2, collumn2 = indexToCordinates(key.index(pair[1]))
        if isDeciphering:
            shiftBy = -1
        else:
            shiftBy = 1
        
        if row1 == row2:
            collumn1 = (collumn1 + shiftBy) % COLLUMNS
            collumn2 = (collumn2 + shiftBy) % COLLUMNS
        elif collumn1 == collumn2:
            row1 = (row1 + shiftBy) % ROWS
            row2 = (row2 + shiftBy) % ROWS
        else:
            collumn1 , collumn2 = collumn2, collumn1
        processedMsg += key[cordinatesToIndex(row1,collumn1)]
        processedMsg += key[cordinatesToIndex(row2,collumn2)]
    return processedMsg
def playfairKey():
    processedKey = ""
    for letter in random.sample(ALPHABET, len(ALPHABET)):
        processedKey += letter
    return processedKey
def isPlayfairKey(s):
    if len(s) == 0:
        return False
    return list(s).sort() == list(ALPHABET).sort()
#endregion
def indexToCordinates(index):
    return index // COLLUMNS + 1, index % COLLUMNS + 1
def cordinatesToIndex(x,y):
    return (x - 1) % ROWS * COLLUMNS + y - 1
def chop(s, interval):
    return [s[i:i+interval] for i in range (0, len(s), interval)]#suprisingly useful method to split str in constant intervals
def messageCleaner(msg):
    temp = ""
    for l in msg.lower():#whole message needs to be lowercase
        if l in ALPHABET:#only supported caracters go through
            temp += l
    return temp
def singleShift(letter, n):
    return ALPHABET[(ALPHABET.index(letter) + n) % len(ALPHABET)]#shift the letter by specified amount