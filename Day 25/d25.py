def partOne():
    with open("input.txt", "r") as inputFile:
        lines = inputFile.readlines()
        east, south = set(), set()
        maxx, maxy = len(lines), len(lines[0].strip())
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                if lines[i][j] == '>':
                    east.add((i, j))
                elif lines[i][j] == 'v':
                    south.add((i, j))
    count = 0
    changed = True
    while changed:
        changed = False
        count += 1
        newEast = set()
        newSouth = set()
        for i, j in east:
            if j + 1 < maxy:
                if (i, j+1) not in south and (i, j+1) not in east:
                    changed = True
                    newEast.add((i, j+1))
                else:
                    newEast.add((i, j))
            else:
                if (i, 0) not in south and (i, 0) not in east:
                    changed = True
                    newEast.add((i, 0))
                else:
                    newEast.add((i, j))
        for i, j in south:
            if i + 1 < maxx:
                if (i+1, j) not in south and (i+1, j) not in newEast:
                    changed = True
                    newSouth.add((i+1, j))
                else:
                    newSouth.add((i, j))
            else:
                if (0, j) not in south and (0, j) not in newEast:
                    changed = True
                    newSouth.add((0, j))
                else:
                    newSouth.add((i, j))
        east = newEast
        south = newSouth
    return count


def partTwo():
    return 'Click the button on the site after getting all the previous stars'

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
