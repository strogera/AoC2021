def partOne():
    with open("input.txt", "r") as inputFile:
        directions = map(lambda k: (k[0], int(k[1])), [x.strip().split() for x in inputFile.readlines()])
        posx = 0
        posy = 0
        for d, x in directions:
            if d == 'forward':
                posx += x
            elif d == 'up':
                posy -= x
            elif d == 'down':
                posy += x
        return abs(posx*posy)



def partTwo():
    with open("input.txt", "r") as inputFile:
        directions = map(lambda k: (k[0], int(k[1])), [x.strip().split() for x in inputFile.readlines()])
        hor = 0
        depth = 0
        aim = 0
        for d, x in directions:
            if d == 'forward':
                hor += x
                depth += aim * x
            elif d == 'up':
                aim -= x
            elif d == 'down':
                aim += x
        return hor*depth

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
