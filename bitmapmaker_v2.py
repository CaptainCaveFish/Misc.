x = 0
step = []
mainline = []
line1 = []
line2 = []
line3 = []
symbols = [

["0","0"," "],
["0","1","%"],
["1","0","="],
["1","1","@"],

]
bitmap = str(input("Please enter your characters."))
while x < len(bitmap):
    step.append([bitmap[x],bitmap[x+1]])
    x += 2
for bits in step:
    for symbol in symbols:
        if bits[0] == symbol[0] and bits[1] == symbol[1]:
            mainline.append(symbol[2])
for a in range(3):
    line1.append(mainline[a])
for a in range(3):
    line2.append(mainline[a+3])
for a in range(3):
    line3.append(mainline[a+6])
print(line1)
print(line2)
print(line3)
line = []

