def partOne(day = 80):
    with open("input.txt", "r") as inputFile:
        lines = inputFile.readlines()
        gen = [int(x) for x in lines[0].strip().split(',')]
        fish = [0] * 9
        for g in gen:
            fish[g] += 1
        for _ in range(day):
            newFish = [0] * 9
            for f in range(9):
                if f > 0:
                    newFish[f-1] += fish[f]
                else:
                    newFish[8] += fish[0]
                    newFish[6] += fish[0]
            fish = newFish
        return sum(fish)

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partOne(256))
