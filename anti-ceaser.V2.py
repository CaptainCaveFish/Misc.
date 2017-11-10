def decrypt():
    encrypt = []
    common = open('common','r')
    answers = open('output.txt','r+')
    message = input('Please enter the encrypted message.')
    for spaces in range(26):
        answer = []
        encrypt = []
        script = list(message)
        for letter in script:
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
        matches = 0
        lot = list(encrypt)
        words = list(common)
        for letter in lot:
            print(letter)
            y = 0 + (lot.index(letter))
            print(words)
            for x in words:
                b = x.rstrip()
                print(b)
                for sign in b:
                    print(sign)
                    if y < len(encrypt):
                        if str(encrypt[y]) == str(sign):
                            y += 1
                    if y == len(words):
                        matches += 1
                print(matches)
        answer = [encrypt,matches]
        answers.write(str(answer)+'/')
    commons = list(common)
    for line in commons:
        x += 2
    print(x)
    for a in range(x):
        for line in answers:
            k = []
            print(line)
            e = line.split('/')
            print(e)
            for f in e:
                g = f.split(',')
                print(g)
                for h in g:
                    i = h.replace('[','')
                    j = i.replace(']','')
                    k.append(j)
                if int(k[(len(k)-1)]) == (x-a):
                    print(line)
    answers.close()
decrypt()
