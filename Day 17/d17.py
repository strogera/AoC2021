def partOne(partOne = True):
    with open("input.txt", "r") as inputFile:
        lines = inputFile.readlines()
        targetx, targety = lines[0].strip().split(':')[1].split(',')
        targetMinx , targetMaxx = list(map(int, targetx.split('=')[1].split('..')))
        targetMiny , targetMaxy = list(map(int, targety.split('=')[1].split('..')))
        startPos = (0, 0)
        drag = gravity = 1
        maxY = count = 0

        for startingVelocityx in range(max(abs(targetMaxx), abs(targetMinx)) + 1):
            for startingVelocityy in range(-max(abs(targetMiny), abs(targetMaxy)), max(abs(targetMiny), abs(targetMaxy)) + 1):
                    yVelocity = startingVelocityy
                    xVelocity = startingVelocityx
                    pos = startPos
                    curMaxy = 0
                    while pos[0] <= (targetMaxx if abs(targetMaxx) > abs(targetMinx) else targetMinx) and pos[1] >= (targetMiny if abs(targetMiny)> abs(targetMaxy) else targetMaxy):
                        pos = (pos[0] + xVelocity, pos[1] + yVelocity)
                        if xVelocity < 0:
                            xVelocity += drag
                        elif xVelocity > 0:
                            xVelocity -= drag
                        yVelocity -= gravity
                        if pos == (0, 0):
                            break
                        if pos[1] > curMaxy:
                            curMaxy = pos[1]
                        elif pos[1] < curMaxy:
                            if partOne and curMaxy != 0 and curMaxy < maxY:
                                break
                        if pos[0] in range(targetMinx, targetMaxx + 1) and pos[1] in range(targetMiny, targetMaxy + 1):
                            count += 1
                            if curMaxy > maxY:
                                maxY = curMaxy
                            break
        return maxY if partOne else count


print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partOne(False))
