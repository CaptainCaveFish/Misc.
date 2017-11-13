file = open("heyMr.txt","r")# Opens Target File
def compress(file):
    unique = []
    final = []
    for line in file:
        sentence = line.split()
        for word in sentence:
            if word not in unique:
                unique.append(word)
            for x in range(0,len(unique)):
                if word == unique[x]:
                    final.append(x)
    print(final)
    print (unique)

