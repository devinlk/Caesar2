#This is a tutorial from the book Invent Your
#Own Computer Games with Python

#Caesar cipher
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_KEY_SIZE = len(SYMBOLS)

def getMode(): #defines the integer getmode for the rest of the code
    while True: #starts a do while loop
        print('Do you wish to encrypt or decrypt a message?')#asks the user a question
        mode = input().lower()
        if mode in ['encrypt', 'e', 'decrypt', 'd']:
            return mode
        else:#gives the alternative prompt if the users response does not follow the restrictions
            print('Enter either "encrypt" or "e" or "decrypt" or "d".')#gives the user alternative response

def getMessage():#defines previous integer
    print('Enter your message: ')#prompts user for given response
    return input()#returns to first step

def getKey():#defines different integer
    key = 0#gives the frame for where the numbers can range
    while True:#do while loop
        print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))#asks user for key response
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):#gives key for users response
            return key#return to key prompt

def getTranslatedMessage(mode, message, key):#defines function
    if mode[0] == 'd':#looks for incrept looks for d to decrypt
        key = -key
    translated = ''

    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex == -1: #Symbol not found in SYMBOLS
            #Just add this symbol without any change
            translated += symbol
        else:#either going to have to add a specific number of letters or subtract
            #Encrypt or decrypt
            symbolIndex += key
        if symbolIndex >= len(SYMBOLS):
            symbolIndex -= len(SYMBOLS)
        elif symbolIndex < 0:
            symbolIndex += len(SYMBOLS)

        translated += SYMBOLS[symbolIndex]
    return translated

mode = getMode()
message = getMessage()
key = getKey()
print('Your translated text is: ')
print(getTranslatedMessage(mode, message, key))