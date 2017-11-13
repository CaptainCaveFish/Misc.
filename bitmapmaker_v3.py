import math
x = 0
step = []
preline = []
mainline = []
line = []
symbols = [

["0","0"," "],
["0","1","%"],
["1","0","="],
["1","1","@"],

]
bitmap = str(input("Please enter your characters."))
size = int(math.sqrt(len(bitmap)/2))
while x < len(bitmap):
    step.append([bitmap[x],bitmap[x+1]])
    x += 2
for bits in step:
    for symbol in symbols:
        if bits[0] == symbol[0] and bits[1] == symbol[1]:
            preline.append(symbol[2])
for a in range(size):
    for b in range(size):
        pixel = b + (3*a)
        line.append(preline[pixel])
    print(line)
    line = []