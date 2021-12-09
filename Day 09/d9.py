from functools import reduce
from collections import deque

def checkListRange(x, y, grid):
    return x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0])

def isLowestPoint(grid, pos):
    num = grid[int(pos.real)][int(pos.imag)]
    for z in [1j, -1j, 1, -1]:
        adjNumIndex = pos + z
        x, y = int(adjNumIndex.real), int(adjNumIndex.imag)
        if checkListRange(x, y, grid) and grid[x][y] <= num:
            return False
    return True


def bfs(grid, lowPoint):
    q = deque()
    q.append(lowPoint)
    discovered = set()
    discovered.add(lowPoint)
    count = 0
    while q:
        v = q.popleft()
        count += 1
        for adj in [1j, 1, -1j, -1]:
            adjIndex = v + adj
            x, y = int(adjIndex.real), int(adjIndex.imag)
            if checkListRange(x, y, grid) and grid[x][y] != 9 and adjIndex not in discovered:
                q.append(adjIndex)
                discovered.add(adjIndex)
    return count

def partOne():
    with open("input.txt", "r") as inputFile:
        elems = [[int(y) for y in x.strip()] for x in inputFile.readlines()]
        count = 0
        for x in range(len(elems)):
            for y in range(len(elems[x])):
                if isLowestPoint(elems, complex(x, y)):
                    count += elems[x][y] + 1
        return count

def partTwo():
    with open("input.txt", "r") as inputFile:
        elems = [[int(y) for y in x.strip()] for x in inputFile.readlines()]
        basins = []
        for x in range(len(elems)):
            for y in range(len(elems[x])):
                numIndex = complex(x, y)
                if isLowestPoint(elems, numIndex):
                    basins.append(bfs(elems, numIndex))
        return reduce(lambda x, y: x*y, sorted(basins)[-3:])

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
