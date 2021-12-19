from itertools import combinations
from itertools import permutations
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


def partOne():
    '''
    rotations = [

        lambda a, b, c: (+a, +b, +c),
        lambda a, b, c: (+b, +c, +a),
        lambda a, b, c: (+c, +a, +b),
        lambda a, b, c: (+c, +b, -a),
        lambda a, b, c: (+b, +a, -c),
        lambda a, b, c: (+a, +c, -b),
        lambda a, b, c: (+a, -b, -c),
        lambda a, b, c: (+b, -c, -a),
        lambda a, b, c: (+c, -a, -b),
        lambda a, b, c: (+c, -b, +a),
        lambda a, b, c: (+b, -a, +c),
        lambda a, b, c: (+a, -c, +b),
        lambda a, b, c: (-a, +b, -c),
        lambda a, b, c: (-b, +c, -a),
        lambda a, b, c: (-c, +a, -b),
        lambda a, b, c: (-c, +b, +a),
        lambda a, b, c: (-b, +a, +c),
        lambda a, b, c: (-a, +c, +b),
        lambda a, b, c: (-a, -b, +c),
        lambda a, b, c: (-b, -c, +a),
        lambda a, b, c: (-c, -a, +b),
        lambda a, b, c: (-c, -b, -a),
        lambda a, b, c: (-b, -a, -c),
        lambda a, b, c: (-a, -c, -b)
        ]

    '''
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
            scannersList.append(Scanner(int(s[0].split(' ')[-2]), [list(map(int, x.strip().split(','))) for x in s[1:]]))

        #matched = {0:0}
        matched = set()
        matchedDistanceFromZero = {0:(0, 0, 0)}
        beacons = set()
        #matchedDist = {0 : (0, 0, 0)}
        allpointsFromZero = set()
        prevPickS = None
        pickCurS = None
        scannersList[0].pos = (0, 0, 0)
        picked = [ scannersList[0]]
        while len(matched) < len(scannersList):
            if pickCurS and pickCurS == picked[-1]:
                picked.pop()
                if not picked:
                    break
            pickCurS = picked[-1]
            print(pickCurS.id)
            for rot in rotations:
                dx = defaultdict(list)
                for p in pickCurS.detectedPoints:
                    for scanner in scannersList:
                        if scanner.id not in matched:# and scanner.id != pickCurS.id:
                            for j, p2 in enumerate(scanner.detectedPoints):
                                    cp = rot(*p2)
                                    dp = subtractPointBfromA(p, cp)
                                    dx[dp].append((j))

                                    if len(dx[dp]) >= 12:
                                        print("matched ", pickCurS.id, scanner.id, dp)
                                        #scanner.pos = subtractPointBfromA(dp , pickCurS.pos)
                                        scanner.pos = addPoints(dp , pickCurS.pos)
                                        #scanner.pos = subtractPointBfromA(pickCurS.pos, dp)
                                        print(scanner.pos)
                                        matched.add(scanner.id)
                                        for k in scanner.detectedPoints:
                                            r = rot(*k)
                                            allpointsFromZero.add(addPoints(r, scanner.pos))
                                            #allpointsFromZero.add(addPoints(k, scanner.pos))
                                        picked.append(scanner)
        print(len(allpointsFromZero))
        print((allpointsFromZero))
        print(matched)
        print(matchedDistanceFromZero)







def partTwo():
    return 'unknown'

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
