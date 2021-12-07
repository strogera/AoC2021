def partOne():
    with open("input.txt", "r") as inputFile:
        lines = inputFile.readlines()
        elems = [int(x) for x in lines[0].split(',')]
        summs = []
        for i in range(len(elems)):
            summs.append(sum([abs(x - i) for x in elems]))
        return int(min(summs))



def partTwo():
    with open("input.txt", "r") as inputFile:
        lines = inputFile.readlines()
        elems = [int(x) for x in lines[0].split(',')]
        summs = []
        for i in range(len(elems)):
            summs.append(sum([(abs(x - i)*(abs(x - i) + 1))/2 for x in elems]))
        return int(min(summs))

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
