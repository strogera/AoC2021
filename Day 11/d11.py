def flash(grid, octPos):
    adjList = {1j, -1j, 1, -1, -1-1j, 1+1j, -1+1j, 1-1j}
    exploded = [octPos]
    grid[int(octPos.real)][int(octPos.imag)] = 0
    countFlashes = 0
    while exploded:
        octPos = exploded.pop()
        countFlashes += 1
        for adj in adjList:
            adjPos = octPos + adj
            adjx, adjy = int(adjPos.real), int(adjPos.imag)
            if adjx in range(len(grid)) and adjy in range(len(grid[adjx])):
                if grid[adjx][adjy] != 0:
                    grid[adjx][adjy] += 1
                    if grid[adjx][adjy] > 9:
                        grid[adjx][adjy] = 0
                        exploded.append(adjPos)
    return countFlashes


def partOne():
    with open("input.txt", "r") as inputFile:
        lines = inputFile.readlines()
        grid = [[int(x) for x in line.strip()] for line in lines]

        countFlashes = 0
        for _ in range(100):
            for x in range(len(grid)):
                for y in range(len(grid[x])):
                    grid[x][y] += 1
            for x in range(len(grid)):
                for y in range(len(grid[x])):
                    if grid[x][y] > 9:
                        countFlashes += flash(grid, complex(x, y))
        return countFlashes


def partTwo():
    with open("input.txt", "r") as inputFile:
        lines = inputFile.readlines()
        grid = [[int(x) for x in line.strip()] for line in lines]

        countFlashes = 0
        countSteps = 0
        while countFlashes != len(grid) * len(grid[0]):
            countFlashes = 0
            countSteps += 1
            for x in range(len(grid)):
                for y in range(len(grid[x])):
                    grid[x][y] += 1
            for x in range(len(grid)):
                for y in range(len(grid[x])):
                    if grid[x][y] > 9:
                        countFlashes += flash(grid, complex(x, y))
        return countSteps


print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
