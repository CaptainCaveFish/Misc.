x = 0
pixel = 0
step = []
step2 = []
final = []
line = []
symbols = [

["00"," "],
["01","%"],
["10","="],
["11","@"],

]
bitmap = str(input("Please enter your characters."))
for bit in bitmap:
    step.append(bit)
while x < len(step):
    twobit = str(step[x]) + str(step[x+1])
    step2.append(twobit)
    x += 2
for x in range(3):
    for y in range(3):
        for symbol in symbols:
            if step2[pixel] == symbol[0]:
                line.append(symbol[1])
                pixel += 1
    print(line)
    line = []


