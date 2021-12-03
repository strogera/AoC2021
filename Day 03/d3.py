from functools import reduce

def partOne():
    with open("input.txt", "r") as inputFile:
        elems = list(map(lambda k: [int(x) for x in k.strip()], inputFile.readlines()))
        mostc = (['1' if f > (len(elems) - f) else '0'
                  for f in reduce(
                      lambda a, b :
                          [a[i] + b[i] for i in range(len(elems[0]))],
                      elems,
                      [0]*len(elems[0]))
                  ])
        leastc = [str(1-int(x)) for x in mostc]
        return int(''.join(mostc), 2)*int(''.join(leastc), 2)

def partTwo():
    with open("input.txt", "r") as inputFile:
        elems = list(map(lambda k: k.strip(), inputFile.readlines()))
        genElems = [x for x in elems]
        scrubElems = [x for x in elems]
        for i in range(len(elems[0])):
            if len(genElems) > 1:
                countOnes = [x[i] for x in genElems].count('1')
                if countOnes >= (len(genElems) - countOnes):
                    genElems = [x for x in genElems if x[i] == '1']
                else:
                    genElems = [x for x in genElems if x[i] == '0']
            if len(scrubElems) > 1:
                countOnes = [x[i] for x in scrubElems].count('1')
                if countOnes >= (len(scrubElems) - countOnes):
                    scrubElems = [x for x in scrubElems if x[i] == '0']
                else:
                    scrubElems = [x for x in scrubElems if x[i] == '1']
        return int(genElems[0], 2) * int(scrubElems[0], 2)

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
