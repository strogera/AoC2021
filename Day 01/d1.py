def partOne():
    with open("input.txt", "r") as inputFile:
        elems = []
        for line in inputFile:
            elems.append(int(line.strip()))
        count = 0
        for i in range(1, len(elems)):
            if elems[i] > elems[i-1]:
                count += 1
        return count


def partTwo():
    with open("input.txt", "r") as inputFile:
        elems = []
        for line in inputFile:
            elems.append(int(line.strip()))
        count = 0
        for i in range(len(elems) - 3):
            if sum(elems[i:i+3]) < sum(elems[i+1:i+4]):
                count += 1
        return count

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
