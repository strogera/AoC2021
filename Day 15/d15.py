import heapq

def isInRange(grid, x, y):
    return x in range(len(grid)) and y in range(len(grid[x]))

def findPath(grid, start, end):
    # Dijkstra
    dist = {}
    queue = [(0, start)]
    heapq.heapify(queue)
    dist[start] = 0
    visited = set()
    while queue:
        d, v = heapq.heappop(queue)
        if v == end:
            return d
        if v in visited:
            continue
        visited.add(v)
        for x, y in [(v[0] + 1, v[1]), (v[0], v[1] + 1), (v[0] - 1, v[1]), (v[0], v[1] - 1)]:
            if isInRange(grid, x, y):
                alt = d + grid[x][y]
                if (x,y) not in dist or alt < dist[(x,y)]:
                    dist[(x,y)] = alt
                    heapq.heappush(queue, (alt, (x,y)))

def partOne():
    with open("input.txt", "r") as inputFile:
        lines = inputFile.readlines()
        grid = [[int(x) for x in line.strip()] for line in lines]
        return findPath(grid, (0, 0), (len(grid) - 1, len(grid[0]) - 1))


def partTwo():
    with open("input.txt", "r") as inputFile:
        lines = inputFile.readlines()
        grid = [[int(x) for x in line.strip()] for line in lines]
        grid2 = [[0]*len(grid[0])*5 for _ in range(len(grid)* 5)]
        for i in range(len(grid2)):
            for j in range(len(grid2[i])):
                grid2[i][j] = (grid[i%len(grid)][j%len(grid[0])] + i//len(grid) + j//len(grid[0]))
                if grid2[i][j] > 9:
                    grid2[i][j] %= 9
        return findPath(grid2, (0, 0), (len(grid2) - 1, len(grid2[0]) - 1))

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
