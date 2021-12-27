import copy
import heapq

class Board:
    agents = { 'A': 0, 'B': 1, 'C': 2, 'D': 3 }
    def __init__(self, hallwaySize, roomSize):
        self.hallway = [None for _ in range(hallwaySize)]
        self.rooms = [[None] * roomSize for _ in range(4)]
        self.cost = 0

    def printState(self):
        string = '#'
        for r in self.hallway:
            if r != None:
                string += r
            else:
                string += '.'
        print(string + '#')

        for row in zip(*self.rooms):
            string = '###'
            for r in row:
                if r != None:
                    string += r + '#'
                else:
                    string += '.#'
            print(string + '##')
        print()

    def setStartingState(self, boardStr):
        for i in range(len(boardStr)):
            for j in range(len(boardStr[i])):
                if boardStr[i][j] in self.agents:
                    if i != 1:
                        self.rooms[(j-3)//2][i-2] = boardStr[i][j]
                    else:
                        self.hallway[j - 1] = boardStr[i][j]

    def getPossilbeMoves(self):
        statesAfterMove = []
        def makeMoveToHallway(r, i, j):
            costList = {'A':1, 'B':10, 'C':100, 'D':1000}
            newBoard = Board(len(self.hallway), len(self.rooms[0]))
            newBoard.hallway = copy.deepcopy(self.hallway)
            newBoard.rooms = copy.deepcopy(self.rooms)
            newBoard.hallway[r] = self.rooms[i][j]
            newBoard.rooms[i][j] = None
            newBoard.cost = costList[newBoard.hallway[r]]*(abs(r-(i*2+2)) + j + 1)
            return newBoard

        def makeMoveToRoom(r, i, j):
            newBoard = Board(len(self.hallway), len(self.rooms[0]))
            newBoard.hallway = copy.deepcopy(self.hallway)
            newBoard.rooms = copy.deepcopy(self.rooms)
            newBoard.rooms[i][j] = self.hallway[r]
            newBoard.hallway[r] = None
            costList = {'A':1, 'B':10, 'C':100, 'D':1000}
            newBoard.cost = costList[newBoard.rooms[i][j]]*(abs(r-(i*2+2)) + j + 1)
            return newBoard

        def isAtDestination(i, j, ch):
            if ch != sorted(self.agents.keys())[i]:
                return False
            for y in range(j+1, len(self.rooms[i])):
                if self.rooms[i][y] != ch:
                    return False
            return True

        #from room to hallway
        for i in range(4):
            j = len(self.rooms[i]) - 1
            while j >= 0 :
                if self.rooms[i][j] != None:
                    if not isAtDestination(i, j, self.rooms[i][j]):
                        if (j != 0 and self.rooms[i][:j] == [None]*(j)) or j == 0:
                            foundObstacle = False
                            for r in range(2*i+3, len(self.hallway)-1, 2):
                                if self.hallway[r] == None:
                                    statesAfterMove.append(makeMoveToHallway(r, i, j))
                                else:
                                    foundObstacle = True
                                    break
                            if not foundObstacle:
                                if self.hallway[-1] == None:
                                    statesAfterMove.append(makeMoveToHallway(len(self.hallway) - 1, i, j))
                            foundObstacle = False
                            for r in range(2*i+1, 0, -2):
                                if self.hallway[r] == None:
                                    statesAfterMove.append(makeMoveToHallway(r, i, j))
                                else:
                                    foundObstacle = True
                                    break
                            if not foundObstacle:
                                if self.hallway[0] == None:
                                    statesAfterMove.append(makeMoveToHallway(0, i, j))
                            break
                j -= 1

        #from hallway to room
        for i in range(4):
            j = len(self.rooms[i]) - 1
            while j >= 0:
                if self.rooms[i][j] == None:
                    foundObstacle = False
                    for r in range(2*i+3, len(self.hallway)-1, 2):
                        if self.hallway[r] != None:
                            if isAtDestination(i, j, self.hallway[r]):
                                statesAfterMove.append(makeMoveToRoom(r, i, j))
                            foundObstacle = True
                            break
                    if not foundObstacle:
                        if self.hallway[-1] != None:
                            if isAtDestination(i, j, self.hallway[-1]):
                                statesAfterMove.append(makeMoveToRoom(len(self.hallway) - 1, i, j))
                    foundObstacle = False
                    for r in range(2*i+1, 0, -2):
                        if self.hallway[r] != None:
                            if isAtDestination(i, j, self.hallway[r]):
                                statesAfterMove.append(makeMoveToRoom(r, i, j))
                            foundObstacle = True
                            break
                    if not foundObstacle:
                        if self.hallway[0] != None:
                            if isAtDestination(i, j, self.hallway[0]):
                                statesAfterMove.append(makeMoveToRoom(0, i, j))
                    break
                j -= 1
        return statesAfterMove

    def isWin(self):
        for x in self.hallway:
            if x != None:
                return False
        for ag in self.agents:
            for j in range(len(self.rooms[self.agents[ag]])):
                if self.rooms[self.agents[ag]][j] != ag:
                    return False
        return True

    def __eq__(self, other):
        for x in range(len(self.hallway)):
            if self.hallway[x] != other.hallway[x]:
                return False
        for i in range(len(self.rooms)):
            for j in range(len(self.rooms[i])):
                if self.rooms[i][j] != other.rooms[i][j]:
                    return False
        return True

    def __lt__(self, other):
        return self.cost < other.cost

    def __hash__(self):
        return hash(self.toStr())

    def toStr(self):
        roomStr = ''
        for x in self.rooms:
            for c in x:
                if c == None:
                    roomStr += '0'
                else:
                    roomStr += c
        return ''.join(['0' if x == None else x for x in self.hallway ]) + roomStr


def getShortestWin(board):
    #Dijkstra
    memo = {}
    queue = [(0, board)]
    heapq.heapify(queue)
    memo[board]= 0
    visited = set()
    while queue:
        cost, board = heapq.heappop(queue)
        if board.isWin():
            return cost
        if board in visited:
            continue
        visited.add(board)
        for move in board.getPossilbeMoves():
            newCost = cost + move.cost
            if move not in memo or newCost < memo[move]:
                memo[move] = newCost
                heapq.heappush(queue, (newCost, move))

def partOne():
    with open('input.txt', 'r') as inputFile:
        board = inputFile.readlines()
        b = Board(len(board[0].strip()) - 2, len(board) - 3)
        b.setStartingState(board)
        return getShortestWin(b)


def partTwo():
    with open('input.txt', 'r') as inputFile:
        board = inputFile.readlines()
        board = board[:3] + ['  #D#C#B#A#'] +['  #D#B#A#C#'] + board[3:]
        b = Board(len(board[0].strip()) - 2, len(board) - 3)
        b.setStartingState(board)
        return getShortestWin(b)

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
