def decrypt():
    message = input('Please the encrypted message.')
    for spaces in range(26):
        encrypt = []
        for letter in message:
            ASCII = ord(letter)
            if 65 < ASCII < 90:
                ASCII -= int(spaces)
                if ASCII < 65:
                    ASCII += 26
                symbol = chr(ASCII)
                encrypt.append(symbol)
            elif ASCII == 32:
                symbol = chr(ASCII)
                encrypt.append(symbol)
            else:
                print("Unsupported character entered. Please revise your message and try again.")
        print(encrypt)
decrypt()