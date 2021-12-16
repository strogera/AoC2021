from functools import reduce

def operation(op, listOfOperants):
    if op == 0:
        return sum(listOfOperants)
    elif op == 1:
        return reduce(lambda a, b : a*b, listOfOperants, 1)
    elif op == 2:
        return min(listOfOperants)
    elif op == 3:
        return max(listOfOperants)
    elif op == 4:
        return listOfOperants[0]
    elif op == 5:
        return  1 if listOfOperants[0] > listOfOperants[1] else 0
    elif op == 6:
        return 1 if listOfOperants[0] < listOfOperants[1] else 0
    elif op == 7:
        return 1 if listOfOperants[0] == listOfOperants[1] else 0


def consumePackets(curBitString, limitPacketsConsumed = None):
    partOneResult = 0
    resultOfEvaluation = []
    while len(curBitString) > 7:
        partOneResult += int(curBitString[:3], 2) # += packet's Version
        packetTypeId = int(curBitString[3:6], 2)
        if packetTypeId == 4:
            literalValue = ''
            countGroups = 0
            for x in range(6, len(curBitString), 5):
                countGroups += 1
                literalValue += curBitString[x+1:x+5]
                if curBitString[x] == "0":
                    break
            countBits = len(literalValue) + len(literalValue)%4 + 6 + countGroups
            resultOfEvaluation.append(int(literalValue, 2))
            curBitString = curBitString[countBits:]
        else:
            if curBitString[6] == '0':
                lengthOfSubPackets = int(curBitString[7:7+15], 2)
                p1, _, p2 = consumePackets(curBitString[7 + 15 : 7 + 15 + lengthOfSubPackets])
                partOneResult += p1
                curBitString = curBitString[7 + 15 + lengthOfSubPackets:]
            elif curBitString[6] == '1':
                numberOfSubPackets = int(curBitString[7:7+11], 2)
                p1, curBitString , p2 = consumePackets(curBitString[7+11:], numberOfSubPackets)
                partOneResult += p1
            resultOfEvaluation.append(operation(packetTypeId, p2))

        if limitPacketsConsumed :
            limitPacketsConsumed -= 1
            if limitPacketsConsumed == 0:
                break
    return partOneResult, curBitString, resultOfEvaluation




def partOne():
    with open("input.txt", "r") as inputFile:
        lines = inputFile.readlines()
        bitString = ''.join([(str(bin(int(x, 16)))[2:].zfill(4)) for x in lines[0].strip()])
        return consumePackets(bitString)[0]

def partTwo():
    with open("input.txt", "r") as inputFile:
        lines = inputFile.readlines()
        bitString = ''.join([(str(bin(int(x, 16)))[2:].zfill(4)) for x in lines[0].strip()])
        return consumePackets(bitString)[2][0]

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
