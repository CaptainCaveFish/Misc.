def ceaser():
    encrypt = []
    message = input('Please enter your message(upper case only).')
    spaces = input('Please enter the number of spaces to move the message along.')
    for letter in message:
        ASCII = ord(letter)
        if 65 < ASCII < 90:
            ASCII += int(spaces)
            if ASCII > 90:
                ASCII -= 26
            symbol = chr(ASCII)
            encrypt.append(symbol)
        elif ASCII == 32:
            symbol = chr(ASCII)
            encrypt.append(symbol)
        else:
            print("Unsupported character entered. Please revise your message and try again.")
    print(encrypt)
ceaser()