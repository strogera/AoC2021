class Cube:
    def __init__(self, xrange, yrange, zrange, mode):
        self.xrange = (min(*xrange), max(*xrange))
        self.yrange = (min(*yrange), max(*yrange))
        self.zrange = (min(*zrange), max(*zrange))
        self.mode = mode

    def getVolume(self):
        return  ((self.xrange[1] - self.xrange[0]) *
                 (self.yrange[1] - self.yrange[0]) *
                 (self.zrange[1] - self.zrange[0]))

def getXYZfrom(line):
    temp = line.strip().split(' ')[-1]
    xrange, yrange, zrange = temp.split(',')
    xrange = xrange.split('=')[-1].split('..')
    yrange = yrange.split('=')[-1].split('..')
    zrange = zrange.split('=')[-1].split('..')
    xr = (int(xrange[0]), int(xrange[1]) + 1)
    yr = (int(yrange[0]), int(yrange[1]) + 1)
    zr = (int(zrange[0]), int(zrange[1]) + 1)
    return (xr, yr, zr)

def partOne():
    with open("input.txt", "r") as inputFile:
        lines = inputFile.readlines()
        cubes = []
        for l in lines:
            mode = l.split(' ')[0]
            xr, yr, zr = getXYZfrom(l)
            if not (xr[0] in range(-50, 51) and xr[1] in range(-50, 51) and
               yr[0] in range(-50, 51) and yr[1] in range(-50, 51) and
               zr[0] in range(-50, 51) and zr[1] in range(-50, 51)):
                 continue
            cubes.append(Cube(xr, yr, zr, mode))
        return getVolume(cubes)


def intersectionAxis(range1, range2):
    if ((range1[1] >= range2[0] and range1[1] <= range2[1]) or
        (range1[0] >= range2[0] and range1[0] <= range2[1]) or
        (range2[1] >= range1[0] and range2[1] <= range1[1]) or
        (range2[0] >= range1[0] and range2[0] <= range1[1])) :
        return (max(range1[0], range2[0]), min(range1[1], range2[1]))
    else:
        return None

def getIntersectionCube(cube1, cube2):
    xr = intersectionAxis(cube1.xrange, cube2.xrange)
    yr = intersectionAxis(cube1.yrange, cube2.yrange)
    zr = intersectionAxis(cube1.zrange, cube2.zrange)
    if xr and yr and zr:
        return Cube(xr, yr, zr, "")
    else:
        return None

def getVolume(cubes):
    onCubes = []
    offCubes = []
    volume = 0
    for c in cubes:
        newOnCubes = []
        newOffCubes = []
        if c.mode == 'on':
            volume += c.getVolume()
            newOnCubes.append(c)
        for c2 in onCubes:
            intersectionCube = getIntersectionCube(c,c2)
            if intersectionCube:
                volume -= intersectionCube.getVolume()
                newOffCubes.append(intersectionCube)
        for c2 in offCubes:
            intersectionCube = getIntersectionCube(c,c2)
            if intersectionCube:
                volume += intersectionCube.getVolume()
                newOnCubes.append(intersectionCube)
        onCubes += newOnCubes
        offCubes += newOffCubes
    return volume

def partTwo():
    with open("input.txt", "r") as inputFile:
        lines = inputFile.readlines()
        cubes = []
        for l in lines:
            mode = l.split(' ')[0]
            xr, yr, zr = getXYZfrom(l)
            cubes.append(Cube(xr, yr, zr, mode))
        return getVolume(cubes)

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
