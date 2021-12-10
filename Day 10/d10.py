from math import floor
from functools import reduce

def partOne():
    with open("input.txt", "r") as inputFile:
        lines = inputFile.readlines()
        matchingBraces = {'[': ']', '{': '}', '(': ')', '<': '>'}
        score = {')': 3, ']': 57, '}': 1197, '>': 25137}
        finalScore = 0
        for line in lines:
            stack = []
            for brace in line.strip():
                if stack == [] or matchingBraces[stack[-1]] != brace:
                    if brace in matchingBraces.keys():
                        stack.append(brace)
                    else:
                        finalScore += score[brace]
                        break
                else:
                    stack.pop()
        return finalScore


def partTwo():
    with open("input.txt", "r") as inputFile:
        lines = inputFile.readlines()
        matchingBraces = {'[': ']', '{': '}', '(': ')', '<': '>'}
        score = {')': 1, ']': 2, '}': 3, '>': 4}
        finalScores = []
        for line in lines:
            stack = []
            for brace in line.strip():
                if stack == [] or matchingBraces[stack[-1]] != brace:
                    if brace in matchingBraces.keys():
                        stack.append(brace)
                    else:
                        stack = []
                        break
                else:
                    stack.pop()
            if stack != []:
                finalScores.append(reduce(lambda a, b: a * 5 +  score[matchingBraces[b]], stack[::-1], 0))
        return sorted(finalScores)[floor(len(finalScores)/2)] if len(finalScores) > 0 else 0

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
