def partOne():
    with open("input.txt", "r") as inputFile:
        lines = inputFile.read()
        points,  folds = lines.split('\n\n')
        points = set(tuple(map(int, line.split(','))) for line in points.split('\n'))
        for fold in folds.split('\n'):
            if '=' in fold:
                index = int(fold.split('=')[-1])
            else:
                continue
            if 'y' in fold:
                newPoints = set()
                while points:
                    point = points.pop()
                    if point[1] > index:
                        point = (point[0], index - (point[1] - index))
                    newPoints.add(point)
                points = newPoints

            elif 'x' in fold:
                newPoints = set()
                while points:
                    point = points.pop()
                    if point[0] > index:
                        point = (index - (point[0] - index), point[1])
                    newPoints.add(point)
                points = newPoints
            break
        return len(points)


def partTwo():
    with open("input.txt", "r") as inputFile:
        lines = inputFile.read()
        points,  folds = lines.split('\n\n')
        points = set(tuple(map(int, line.split(','))) for line in points.split('\n'))
        for fold in folds.split('\n'):
            if '=' in fold:
                index = int(fold.split('=')[-1])
            else:
                continue
            if 'y' in fold:
                newPoints = set()
                while points:
                    point = points.pop()
                    if point[1] > index:
                        point = (point[0], index - (point[1] - index))
                    newPoints.add(point)
                points = newPoints

            elif 'x' in fold:
                newPoints = set()
                while points:
                    point = points.pop()
                    if point[0] > index:
                        point = (index - (point[0] - index), point[1])
                    newPoints.add(point)
                points = newPoints

        for y in range((max(points, key = lambda k: k[1])[1] + 1)):
            l = ''
            for x in range(max(points, key = lambda k: k[0])[0] + 1):
                if (x, y) in points:
                    l += '#'
                else:
                    l += ' '
            print(l)

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
partTwo()
