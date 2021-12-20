def partOne(iterations = 2):
    with open("input.txt", "r") as inputFile:
        lines = inputFile.readlines()
        imageEnhancement = lines[0].strip()
        lines = [x.strip() for x in lines[2:]]
        litPixels = set()
        for i in range(len(lines)):
            for j, y in enumerate(lines[i]):
                if y == '#':
                    litPixels.add(complex(i, j))

        for index in range(iterations):
            newLitPixels = set()
            minx = int(min(list(litPixels), key = lambda k: k.real).real)
            maxx = int(max(list(litPixels), key = lambda k: k.real).real)
            miny = int(min(list(litPixels), key = lambda k: k.imag).imag)
            maxy = int(max(list(litPixels), key = lambda k: k.imag).imag)
            if index % 2 == 1 and imageEnhancement[0] == '#':
                for step in range(1, 4):
                    for i in range(minx-3, maxx+4):
                        litPixels.add(complex(i, miny-step))
                        litPixels.add(complex(i, maxy+step))
                    for j in range(miny-3, maxy+4):
                        litPixels.add(complex(minx-step, j))
                        litPixels.add(complex(maxx+step, j))
                minx -= 1
                maxx += 1
                miny -= 1
                maxy += 1

            for i in range(minx - 1, maxx + 2):
                for j in range(miny - 1, maxy + 2):
                    pixel = complex(i, j)
                    binaryNumber = []
                    for adj in [-1-1j, -1, -1+1j, -1j, 0j, 1j, 1-1j, 1, 1+1j]:
                        binaryNumber.append('1' if (pixel + adj) in litPixels else '0')
                    if imageEnhancement[int(''.join(binaryNumber), 2)] == '#':
                        newLitPixels.add(pixel)
            litPixels = newLitPixels
        return len(litPixels)


print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partOne(50))
