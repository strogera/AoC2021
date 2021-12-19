from itertools import combinations
from collections import defaultdict

class Scanner:
    def __init__(self, id, listOfPoints):
        self.detectedPoints = listOfPoints
        self.pos = None
        self.id = id

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
            scannersList.append(Scanner(int(s[0].split(' ')[-2]), set(tuple(list(map(int, x.strip().split(',')))) for x in s[1:])))

        matched = set()
        pickCurS = scannersList[0]
        scannersList[0].pos = (0, 0, 0)
        partTwo = []
        while len(matched) < len(scannersList):
            for rot in rotations:
                dx = defaultdict(int)
                found = False
                for p in pickCurS.detectedPoints:
                    for scanner in scannersList:
                        if scanner.id not in matched:
                            for p2 in scanner.detectedPoints:
                                cp = rot(*p2)
                                dp = subtractPointBfromA(p, cp)
                                dx[dp] += 1
                                if dx[dp] >= 12:
                                    matched.add(scanner.id)
                                    partTwo.append(dp)
                                    found = True
                                    break
                        if found:
                            break
                    if found:
                        break
                if found:
                    for k in scanner.detectedPoints:
                        r = rot(*k)
                        pickCurS.detectedPoints.add(addPoints(r, dp))
        if partOne:
            return len(pickCurS.detectedPoints)

        maxx = 0
        for x,y in combinations(partTwo, 2):
            maxx = max(manhattan(x,y), maxx)
        return maxx


print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partOne(False))
