from itertools import combinations
from collections import defaultdict


def addPoints(a , b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])

def subtractPointBfromA(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])

def manhattan(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

def partOne(partOne = True):
    rotations = [
        lambda x, y, z : (x, y, z),
        lambda x, y, z : (x, -y, -z),
        lambda x, y, z : (x, z, -y),
        lambda x, y, z : (x, -z, y),
        lambda x, y, z : (y, x, -z),
        lambda x, y, z : (y, -x, z),
        lambda x, y, z : (y, z, x),
        lambda x, y, z : (y, -z, -x),
        lambda x, y, z : (z, x, y),
        lambda x, y, z : (z, -x, -y),
        lambda x, y, z : (z, y, -x),
        lambda x, y, z : (z, -y, x),
        lambda x, y, z : (-x, y, -z),
        lambda x, y, z : (-x, -y, z),
        lambda x, y, z : (-x, z, y),
        lambda x, y, z : (-x, -z, -y),
        lambda x, y, z : (-y, x, z),
        lambda x, y, z : (-y, -x, -z),
        lambda x, y, z : (-y, z, -x),
        lambda x, y, z : (-y, -z, x),
        lambda x, y, z : (-z, x, -y),
        lambda x, y, z : (-z, -x, y),
        lambda x, y, z : (-z, y, x),
        lambda x, y, z : (-z, -y, -x)
    ]

    with open("input.txt", "r") as inputFile:
        scanners = inputFile.read().split('\n\n')
        scannersList = []
        for s in scanners:
            s = s.strip().split('\n')
            scannersList.append(set(tuple(list(map(int, x.strip().split(',')))) for x in s[1:]))
        matched = set()
        curScanner = set(scannersList[0])
        matched.add(0)
        partTwo = []
        while len(matched) < len(scannersList):
            for rotate in rotations:
                inCommon = defaultdict(int)
                for point1 in list(curScanner):
                    for id, scanner in enumerate(scannersList):
                        if id not in matched:
                            for point2 in scanner:
                                diff = subtractPointBfromA(point1, rotate(*point2))
                                inCommon[diff] += 1
                                if inCommon[diff] >= 12:
                                    matched.add(id)
                                    partTwo.append(diff)
                                    for k in scanner:
                                        curScanner.add(addPoints(rotate(*k), diff))
                                    break
        if partOne:
            return len(curScanner)

        maxx = 0
        for x,y in combinations(partTwo, 2):
            maxx = max(manhattan(x,y), maxx)
        return maxx


print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partOne(False))
