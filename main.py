import sys
import math


class board:
    def __init__(self):
        self.xMax = 30
        self.yMax = 15
        self.grille = createGrille()
    def createGrille():
        pass

    def getContent(self, x, y):
        pass


class move:
    def __init__(self, iEnumMove):
        self.value = iEnumMove

class game:
    def __init__(self):
        self.board = board()
        self.playerPosition = []
        self.playerDronePosition = []

    def refreshPosition(iSelf, iX, iY):
        iSelf.playerPosition = [iX, iY]

    def refreshRemovePosition(iSelf, iX, iY):
        iSelf.playerDronePosition[iX, iY]

    def applyRefresh(iSelf):
        pass

    def applyMove(self, iMove):
        # return a copy a the current game after the move is applied
        pass


class miniMax:
    @classmethod
    def calcMin(iClass,iState,iCurrentLevel, iMaxLevel):
        #iState.display()
        if iCurrentLevel == iMaxLevel:
            return iState.evaluate()
        else:
            valueBestMove = +100000
            for move in iState.getMoves():
                temp = iClass.calcMax(iState.playMove(move),iCurrentLevel+1,iMaxLevel)
                if temp < valueBestMove:
                    valueBestMove=temp
                    bestMove=move
            else:
                return iState.evaluate()
            return valueBestMove

    @classmethod
    def calcMax(iClass,iState,iCurrentLevel, iMaxLevel):
        #iState.display()
        if iCurrentLevel == iMaxLevel:
            return iState.evaluate()
        else:
            valueBestMove =-100000
            for move in iState.getMoves():
                temp = iClass.calcMin(iState.playMove(move),iCurrentLevel+1,iMaxLevel)
                if temp > valueBestMove:
                    valueBestMove=temp
            else:
                return iState.evaluate()
            return	valueBestMove

    @classmethod
    def miniMax(iClass,iState,iMaxLevel):
        #iState.display()
        bestMove = None
        valueBestMove = -100000
        for move in iState.getMoves():
            temp = iClass.calcMin(iState.playMove(move),1,iMaxLevel)
            if temp > valueBestMove:
                valueBestMove=temp
                bestMove=move
        print "valueBestMove="+str(valueBestMove)
        return bestMove


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

player_count = int(raw_input())
my_id = int(raw_input())

# game loop

myGame = game()

while 1:
    helper_bots = int(raw_input())
    for i in xrange(player_count):
        x, y = [int(j) for j in raw_input().split()]
        game.refreshPosition(x, y)
    removal_count = int(raw_input())
    for i in xrange(removal_count):
        remove_x, remove_y = [int(j) for j in raw_input().split()]
        game.refreshRemovePosition(remove_x, remove_y)

    game.applyRefresh()

    theWinMove = miniMax.miniMax(myGame)
    print theWinMove.getvalue()

    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
