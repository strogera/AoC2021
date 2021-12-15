from collections import defaultdict

def partOne(loopSize = 10):
    with open("input.txt", "r") as inputFile:
        lines = inputFile.read()
        curString, rulesStr = lines.split('\n\n')
        rules = {}
        for line in rulesStr.split('\n'):
            if ' -> ' in line:
                fromStr , toStr = line.strip().split(' -> ')
                rules[fromStr] = toStr
        countOccurances = defaultdict(int)

        pairsInString = defaultdict(int)
        for i in range(len(curString) - 1):
            pairsInString[(curString[i] , curString[i+1])] += 1
            countOccurances[curString[i]] += 1
        countOccurances[curString[-1]] += 1

        for _ in range(loopSize):
            newPairsInString = defaultdict(int)
            for pair in pairsInString:
                charToAdd = rules[pair[0] + pair[1]]
                newPair1 = (pair[0], charToAdd)
                newPair2 = (charToAdd, pair[1])
                newPairsInString[newPair1] += pairsInString[pair]
                newPairsInString[newPair2] += pairsInString[pair]
                countOccurances[charToAdd] += pairsInString[pair]
            pairsInString = newPairsInString
        return max(countOccurances.values()) - min(countOccurances.values())

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partOne(40))
