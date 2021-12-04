def checkWin(board):
    return any((row == [-1]*len(row) for row in  board)) or any(col == [-1]*len(col) for col in [list(x) for x in zip(*board)])

def mark(board, num):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]  == num:
                board[i][j] = -1

def partOne():
    with open("input.txt", "r") as inputFile:
        elems =inputFile.read().split('\n\n')
        boards = [[[int(x) for x in row.split()] for row in board] for board in [x.strip().split('\n') for x in elems[1:]]]

        for num in map(lambda k: int(k), elems[0].split(',')):
            for board in boards:
                mark(board, num)
                if checkWin(board):
                    return num*sum(filter(lambda k: k != -1, sum(board, [])))


def partTwo():
    with open("input.txt", "r") as inputFile:
        elems =inputFile.read().split('\n\n')
        boards = [[[int(x) for x in row.split()] for row in board] for board in [x.strip().split('\n') for x in elems[1:]]]

        won = set()
        for num in map(lambda k: int(k), elems[0].split(',')):
            for i in range(len(boards)):
                if i in won:
                    continue
                mark(boards[i], num)
                if checkWin(boards[i]):
                    won.add(i)
                    if len(won) == len(boards):
                        return num*sum(filter(lambda k: k != -1, sum(boards[i], [])))

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())

