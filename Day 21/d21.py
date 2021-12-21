class Game:
    def __init__(self, pos1, pos2, score1, score2):
        self.pos1 = pos1
        self.pos2 = pos2
        self.score1 = score1
        self.score2 = score2
        self.turn = 0

    def __eq__(self, other):
        return (self.pos1 == other.pos1 and
                self.pos2 == other.pos2 and
                self.score1 == other.score1 and
                self.score2 == other.score2 and
                self.turn == other.turn)

    def __hash__(self):
        return hash((self.pos1, self.pos2, self.score1, self.score2, self.turn))

    def changeTurn(self):
        self.turn = (self.turn + 1)%2

    def checkWin(self, targetScore):
        if self.turn == 0:
            return self.score1 >= targetScore
        else:
            return self.score2 >= targetScore

    def play(self, roll):
        if self.turn == 0:
            self.pos1 = (self.pos1 -1 + roll)%10 + 1
            self.score1 += self.pos1
        else:
            self.pos2 = (self.pos2 -1 + roll)%10 + 1
            self.score2 += self.pos2


def partOne():
    with open("input.txt", "r") as inputFile:
        lines = inputFile.readlines()
        start1 = int(lines[0].strip().split(' ')[-1])
        start2 = int(lines[1].strip().split(' ')[-1])
        game = Game(start1, start2, 0, 0)
        die = 0
        while game.score1 < 1000 and game.score2 < 1000:
            move = 0
            for _ in range(3):
                move += die%100 + 1
                die += 1
            game.play(move%10)
            game.changeTurn()
        if game.score1 >= 1000:
            return game.score2 * die
        else:
            return game.score1 * die

class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, game):
        if not (game) in self.memo:
            self.memo[game] = self.f(game)
        return self.memo[game]

@Memoize
def playGame(game):
    countUniverses1 = 0
    countUniverses2 = 0
    diracRollsCounter = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1} # dieroll : counter
    for r in diracRollsCounter:
        newGame = Game(game.pos1, game.pos2, game.score1, game.score2)
        newGame.turn = game.turn
        newGame.play(r)
        if newGame.checkWin(21):
            if newGame.turn == 0:
                countUniverses1 += diracRollsCounter[r]
            else:
                countUniverses2 += diracRollsCounter[r]
            continue
        newGame.changeTurn()
        c1, c2 = playGame(newGame)
        countUniverses1  += c1 * diracRollsCounter[r]
        countUniverses2  += c2 * diracRollsCounter[r]
    return (countUniverses1, countUniverses2)


def partTwo():
    with open("input.txt", "r") as inputFile:
        lines = inputFile.readlines()
        start1 = int(lines[0].strip().split(' ')[-1])
        start2 = int(lines[1].strip().split(' ')[-1])

        (countUniverses1, countUniverses2) = playGame(Game(start1, start2, 0, 0))
        return max(countUniverses1, countUniverses2)


print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
