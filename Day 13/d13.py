def partOne():
    with open("input.txt", "r") as inputFile:
        lines = inputFile.read()
        elems,  folds = lines.split('\n\n')
        elems = [ tuple(map(int, line.split(','))) for line in elems.split('\n')]
        grid = []
        for x in range(max(elems, key = lambda k: k[0])[0] + 1):
            grid.append([' ']*(max(elems, key = lambda k: k[1])[1] + 1))

        for marked in elems:
            grid[marked[0]][marked[1]] = '#'

        gridXLength = len(grid)
        gridYLength = len(grid[0])
        for fold in folds.split('\n'):
            if '=' in fold:
                index = int(fold.split('=')[-1])
            else:
                continue
            if 'y' in fold:
                for xx in range(gridXLength):
                    for yy in range(gridYLength):
                        if yy > index:
                            if grid[xx][yy] == '#':
                                grid[xx][index - (yy - index)]  = '#'
                                grid[xx][yy] = ' '
                gridYLength = index

            elif 'x' in fold:
                for xx in range(gridXLength):
                    for yy in range(gridYLength):
                        if xx > index:
                            if grid[xx][yy] == '#':
                                grid[index - (xx - index)][yy] = '#'
                                grid[xx][yy] = ' '
                gridXLength = index
            break
        count = 0
        for x in range(gridXLength):
            for y in range(gridYLength):
                if grid[x][y] == '#':
                    count += 1
        return count


def partTwo():
    with open("input.txt", "r") as inputFile:
        lines = inputFile.read()
        elems,  folds = lines.split('\n\n')
        elems = [ tuple(map(int, line.split(','))) for line in elems.split('\n')]
        grid = []
        for x in range(max(elems, key = lambda k: k[0])[0] + 1):
            grid.append([' ']*(max(elems, key = lambda k: k[1])[1] + 1))

        for marked in elems:
            grid[marked[0]][marked[1]] = '#'

        gridXLength = len(grid)
        gridYLength = len(grid[0])
        for fold in folds.split('\n'):
            if '=' in fold:
                index = int(fold.split('=')[-1])
            else:
                continue
            if 'y' in fold:
                for xx in range(gridXLength):
                    for yy in range(gridYLength):
                        if yy > index:
                            if grid[xx][yy] == '#':
                                grid[xx][index - (yy - index)]  = '#'
                                grid[xx][yy] = ' '
                gridYLength = index

            elif 'x' in fold:
                for xx in range(gridXLength):
                    for yy in range(gridYLength):
                        if xx > index:
                            if grid[xx][yy] == '#':
                                grid[index - (xx - index)][yy] = '#'
                                grid[xx][yy] = ' '
                gridXLength = index
        for y in range((gridYLength)):
            l = ''
            for x in range((gridXLength)):
                l += grid[x][y]
            print(l)
        print()

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
partTwo()
