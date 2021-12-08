def partOne():
    with open("input.txt", "r") as inputFile:
        lines = inputFile.readlines()
        elems = [x.strip().split('|') for x in lines]
        searchForLength = set([2, 4, 3, 7])
        count = 0
        for _, outSignal in elems:
            sigs = outSignal.split(' ')
            for s in sigs:
                if len(s) in searchForLength:
                    count += 1
        return count


def partTwo():
    with open("input.txt", "r") as inputFile:
        lines = inputFile.readlines()
        elems = [x.strip().split('|') for x in lines]
        one = set()
        four = set()
        summ = 0
        for inSig, outSignal in elems:
            sigs = outSignal.split(' ') + inSig.split(' ')
            for s in sigs:
                if len(s) == 2:
                    one = set(s)
                elif len(s) == 4:
                    four = set(s)
            output = ''
            for out in outSignal.split(' '):
                out = set(out)
                if len(out) == 2:
                    output += '1'
                elif len(out) == 3:
                    output +=  '7'
                elif len(out) == 4:
                    output +=  '4'
                elif len(out) == 5:
                    if len(out.difference(one)) == 3:
                        output += '3'
                    elif len(out.intersection(four)) == 3:
                        output += '5'
                    elif len(out.intersection(four)) == 2:
                        output += '2'
                elif len(out) == 6:
                    if len(out.difference(one)) == 5:
                        output += '6'
                    elif len(out.difference(four)) == 2:
                        output += '9'
                    elif len(out.difference(four)) == 3:
                        output += '0'
                elif len(out) == 7:
                    output +=  '8'
            summ += int(output)
        return summ



print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
