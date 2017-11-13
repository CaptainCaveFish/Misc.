bit = 0
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
y = int(input("Please enter the height of your bitmap."))
x = int(input("Please enter the width of your bitmap."))
bitmap = str(input("Please enter your characters."))
while bit < len(bitmap):
    step.append([bitmap[bit],bitmap[bit+1]])
    bit += 2
for bits in step:
    for symbol in symbols:
        if bits[0] == symbol[0] and bits[1] == symbol[1]:
            preline.append(symbol[2])
for a in range(y):
    for b in range(x):
        pixel = b + (a*x)
        line.append(preline[pixel])
    print(line)
    line = []