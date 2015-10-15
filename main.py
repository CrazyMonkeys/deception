import sys
import math
import copy

class cellStatus:
    EMPTY=0
    PLAYER=1
    LIGHT=2
    DRONE=3

class actions:
    UP=0
    DOWN=1
    RIGHT=3
    LEFT=4

class boardSize:
    X=29
    Y=14

class board:
    def __init__(self):
        self.xMax = 30
        self.yMax = 15
        self.grille = []
        for i in range(0,self.yMax):
            self.grille.append([cellStatus.EMPTY]*self.xMax)

    def getContent(self, iX, iY):
        return self.grille[iY][iX]
        
    def setContent(self, iX, iY,iContent):
        self.grille[iY][iX]=iContent

class move:
    def __init__(self, iEnumMove):
        self.value = iEnumMove

    def getNewCoord(self,iX,iY):
        aNewX = iX
        aNewY = iY
        if self.value == actions.UP:
            aNewY -=1 
        elif self.value == actions.DOWN:
            aNewY +=1
        elif self.value == actions.RIGHT:
            aNewX +=1
        elif self.value == actions.LEFT:
            aNewX -=1
        if aNewX<0:
            aNewX = boardSize.X
        if aNewX>boardSize.X:
            aNewX = 0
        if aNewY<0:
            aNewX = boardSize.Y
        if aNewX>boardSize.Y:
            aNewX = 0
        aOutput = [aNewX,aNewY]
        return aOutput


class game:
    def __init__(self):
        self.board = board()
        self.playerPosition = []
        self.playerDronePosition = []
        self.myPosition = [-1, -1]


    def refreshPosition(self, iX, iY):
        self.playerPosition.append([iX, iY])

    def setMyPosition(self, x ,y):
        self.myPosition = [x, y]

    def refreshRemovePosition(self, iX, iY):
        self.playerDronePosition[iX, iY]

    def applyRefresh(self):
        for position in self.playerPosition:
            self.board.setContent()

    def applyPosition(self):
        for position in self.playerPosition:
            self.board.setContent()

    def applyMove(self, iMove):
        # return a copy a the current game after the move is applied
        newGame = copy.copy(self)
        newGame.setMyPosition = iMove.getNewCoord(newGame.myPostion())
        return newGame


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
        if i == my_id:
            myGame.setMyPosition(x, y)
        else:
            myGame.refreshPosition(x, y)
    removal_count = int(raw_input())
    for i in xrange(removal_count):
        remove_x, remove_y = [int(j) for j in raw_input().split()]
        myGame.refreshRemovePosition(remove_x, remove_y)

    myGame.applyRefresh()

    #theWinMove = miniMax.miniMax(myGame)
    print "UP"

    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
