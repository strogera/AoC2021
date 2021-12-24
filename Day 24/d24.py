def partOne(partTwo = False):
    with open("input.txt", "r") as inputFile:
        blocks = [x for x in inputFile.read().split('inp w\n')[1:]]
        maxx = [x for x in '00000000000000']
        minn = [x for x in '00000000000000']
        stack = []
        for i, block in enumerate(blocks):
            block = block.split('\n')
            if block[3] == 'div z 1':
                y = int(block[14].split(' ')[-1])
                stack.append((i, y))
            elif block[3] == 'div z 26':
                j, value = stack.pop()
                x = int(block[4].split(' ')[-1])
                value += x
                if value > 0:
                    maxx[i] = '9'
                    maxx[j] = str(9 - value)
                    minn[i] = str(1 + value)
                    minn[j] = '1'
                else:
                    maxx[i] = str(9 - abs(value))
                    maxx[j] = '9'
                    minn[i] = '1'
                    minn[j] = str(1 + abs(value))
            else:
                assert(False)
    if partTwo:
        return ''.join(minn)
    return ''.join(maxx)


print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partOne(True))
