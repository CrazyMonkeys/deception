import sys
import math
import copy
import time

class cellStatus:
    EMPTY=0
    PLAYER=1
    LIGHT=2
    DRONE=3

class actions:
    UP=0
    DOWN=1
    RIGHT=2
    LEFT=3
    
def getLabel(iLabel):
    if iLabel == 0:
        return "UP"
    elif iLabel == 1:
        return "DOWN"
    elif iLabel == 2:
        return "RIGHT"
    elif iLabel == 3:
        return "LEFT"

class boardSize:
    X=29
    Y=14
    
def normalizePosition(iPos, iAction):
    aNewX = iPos[0]
    aNewY = iPos[1]
    if iAction == actions.UP:
        aNewY -=1 
    elif iAction == actions.DOWN:
        aNewY +=1
    elif iAction == actions.RIGHT:
        aNewX +=1
    elif iAction == actions.LEFT:
        aNewX -=1
    if aNewX<0:
        aNewX = boardSize.X
    if aNewX>boardSize.X:
        aNewX = 0
    if aNewY<0:
        aNewY = boardSize.Y
    if aNewY>boardSize.Y:
        aNewY = 0
    aOutput = [aNewX,aNewY]
    return aOutput

class board:
    def __init__(self):
        self.xMax = 30
        self.yMax = 15
        self.grille = []
        for i in range(0,self.yMax):
            self.grille.append([cellStatus.EMPTY]*self.xMax)

    def getContent(self, iPos):
        return self.grille[iPos[1]][iPos[0]]
        
    def setContent(self, iX, iY,iContent):
        self.grille[iY][iX]=iContent

class move:
    def __init__(self, iEnumMove):
        self.value = iEnumMove

    def getNewCoord(self,iPos):
        return normalizePosition(iPos,self.value)


class game:
    def __init__(self):
        self.board = board()
        self.playerPosition = []
        self.playerDronePosition = []
        self.myPosition = [-1, -1]

    def getMoves(self):

        aList = []
        if self.board.getContent(normalizePosition(self.myPosition, actions.UP)) == cellStatus.EMPTY:
            aList.append(move(actions.UP))
        if self.board.getContent(normalizePosition(self.myPosition, actions.DOWN)) == cellStatus.EMPTY:
            aList.append(move(actions.DOWN))
        if self.board.getContent(normalizePosition(self.myPosition, actions.RIGHT)) == cellStatus.EMPTY:
            aList.append(move(actions.RIGHT))
        if self.board.getContent(normalizePosition(self.myPosition, actions.LEFT)) == cellStatus.EMPTY:
            aList.append(move(actions.LEFT))
        return aList


    def refreshPosition(self, iX, iY):
        self.playerPosition.append([iX, iY])

    def setMyPosition(self, x ,y):
        self.myPosition = [x, y]

    def refreshRemovePosition(self, iX, iY):
        self.playerDronePosition = [iX, iY]

    def applyPosition(self):
        for position in self.playerPosition:
            self.board.setContent(position[0], position[1], cellStatus.PLAYER)

        self.board.setContent(self.myPosition[0], self.myPosition[1], cellStatus.PLAYER)

    def applyRefresh(self):
        for position in self.playerPosition:
            self.board.setContent(position[0], position[1], cellStatus.LIGHT)

        self.board.setContent(self.myPosition[0], self.myPosition[1], cellStatus.LIGHT)

    def applyMove(self, iMove):
        # return a copy a the current game after the move is applied
        newGame = copy.deepcopy(self)
        newGame.myPosition = iMove.getNewCoord(newGame.myPosition)
        return newGame

    def evaluate(self):
        pos = self.myPosition
        res = 0
        
        testedPos = normalizePosition(pos, actions.UP)
        while self.board.getContent(testedPos) == cellStatus.EMPTY:
            testedPos = normalizePosition(testedPos, actions.UP)
            res+=1
        
        testedPos = normalizePosition(pos, actions.DOWN)
        while self.board.getContent(testedPos) == cellStatus.EMPTY:
            testedPos = normalizePosition(testedPos, actions.DOWN)
            res+=1
        
        testedPos = normalizePosition(pos, actions.RIGHT)
        while self.board.getContent(testedPos) == cellStatus.EMPTY:
            testedPos = normalizePosition(testedPos, actions.RIGHT)
            res+=1
        
        testedPos = normalizePosition(pos, actions.LEFT)
        while self.board.getContent(testedPos) == cellStatus.EMPTY:
            testedPos = normalizePosition(testedPos, actions.LEFT)
            res+=1
        return res
        
class miniMax:
    @classmethod
    def calcMin(iClass,iState,iCurrentLevel, iMaxLevel):
        #iState.display()
        if iCurrentLevel == iMaxLevel:
            return iState.evaluate()
        else:
            valueBestMove = +100000
            for move in iState.getMoves():
                temp = iClass.calcMax(iState.applyMove(move),iCurrentLevel+1,iMaxLevel)
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
                temp = iClass.calcMin(iState.applyMove(move),iCurrentLevel+1,iMaxLevel)
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
            temp = iClass.calcMin(iState.applyMove(move),1,iMaxLevel)
            if temp > valueBestMove:
                valueBestMove=temp
                bestMove=move
        #print "valueBestMove="+str(valueBestMove)
        return bestMove


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

player_count = int(raw_input())
my_id = int(raw_input())

# game loop

myGame = game()

while 1:
    start_time = time.time()
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

    myGame.applyPosition()

    retour = miniMax.miniMax(myGame, 4)
    #print >> sys.stderr, "Debug messages...", retour
    
    myGame.applyRefresh()

    #theWinMove = miniMax.miniMax(myGame)
    end_time = time.time()

    print >> sys.stderr, "Debug messages..." ,end_time-start_time
    
    print getLabel(retour.value)
    

    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
