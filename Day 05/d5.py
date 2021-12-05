from collections import defaultdict

def partOne():
    with open("input.txt", "r") as inputFile:
        lines = inputFile.readlines()
        grid = defaultdict(int)
        elems = [[[int(z) for z in y.split(',')] for y in x.strip().split('->')] for x in lines]
        for point1, point2 in elems:
            if point1[1] != point2[1] and point1[0] != point2[0]:
                continue
            i = point1[0]
            j = point1[1]
            while i != point2[0] or j != point2[1]:
                grid[(i,j)] += 1
                if point2[0] < i:
                    i -= 1
                elif point2[0] > i:
                    i += 1
                if point2[1] < j:
                    j -= 1
                elif point2[1] > j:
                    j += 1
            grid[(i,j)] += 1
        return len(list(filter(lambda k : k > 1,grid.values())))


def partTwo():
    with open("input.txt", "r") as inputFile:
        lines = inputFile.readlines()
        grid = defaultdict(int)
        elems = [[[int(z) for z in y.split(',')] for y in x.strip().split('->')] for x in lines]
        for point1, point2 in elems:
            i = point1[0]
            j = point1[1]
            while i != point2[0] or j != point2[1]:
                grid[(i,j)] += 1
                if point2[0] < i:
                    i -= 1
                elif point2[0] > i:
                    i += 1
                if point2[1] < j:
                    j -= 1
                elif point2[1] > j:
                    j += 1
            grid[(i,j)] += 1
        return len(list(filter(lambda k : k > 1, grid.values())))


print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
