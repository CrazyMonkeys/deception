import sys
import math
import copy
import time


#possible status of a cell of the board
class cellStatus:
    EMPTY=0
    PLAYER=1
    LIGHT=2
    DRONE=3

#Possible actions for a player
class actions:
    UP=0
    DOWN=1
    RIGHT=2
    LEFT=3
    DEPLOY=4
    
#Give the string label for the action to perform
def getLabel(iLabel):
    if iLabel == 0:
        return "UP"
    elif iLabel == 1:
        return "DOWN"
    elif iLabel == 2:
        return "RIGHT"
    elif iLabel == 3:
        return "LEFT"
    elif iLabel == 4:
        return "DEPLOY"

        
#Board size, origin position = 0
class boardSize:
    X=29
    Y=14
    
#Static method retuning an updated position based on  current pos + move. Thore board is taken into account
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
        #creates represntation of the board
        for i in range(0,self.yMax):
            self.grille.append([cellStatus.EMPTY]*self.xMax)
            
    #get the content of cell located at iPos
    def getContent(self, iPos):
        return self.grille[iPos[1]][iPos[0]]
        
    #Set the content of cell located at iPos       
    def setContent(self, iPos,iContent):
        self.grille[iPos[1]][iPos[0]]=iContent


class move:
    def __init__(self, iEnumMove):
        self.value = iEnumMove
        
    #Transforms current coords to new coords dependgin on move type
    def getNewCoord(self,iPos):
        return normalizePosition(iPos,self.value)


class game:
    def __init__(self):
        self.board = board()
        self.playerPosition = []
        self.playerDronePosition = []
        self.myPosition = [-1, -1]
        self.previousAction = None
        self.remainingBots= 0

    #List the possible moves for the current player
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
        if normalizePosition(self.myPosition, self.previousAction) == cellStatus.LIGHT:
            aList.append(move(actions.DEPLOY))
        if not aList:
            aList.append(move(actions.DEPLOY))
        return aList

    #Init step: set the position of players
    def refreshPosition(self, iX, iY):
        self.playerPosition.append([iX, iY])

    #Init step: set the position of our player
    def setMyPosition(self, x ,y):
        self.myPosition = [x, y]

    def setRemainingBots(self, iCount):
        self.remainingBots=iCount
            
    def refreshRemovePosition(self, iPos):
        self.board.setContent(iPos, cellStatus.EMPTY)

    #Init step: Update the game with player positions
    def applyPosition(self):
        for position in self.playerPosition:
            self.board.setContent(position, cellStatus.PLAYER)

        self.board.setContent(self.myPosition, cellStatus.PLAYER)
        
    #Post run step: update the game with the light trail
    def applyRefresh(self,iPreviousAction):
        self.previousAction = iPreviousAction
        for position in self.playerPosition:
            self.board.setContent(position, cellStatus.LIGHT)

        self.board.setContent(self.myPosition, cellStatus.LIGHT)

    #Apply a move to the current game and return a copy of the game
    def applyMove(self, iMove):
        # return a copy a the current game after the move is applied
        newGame = copy.deepcopy(self)
        newGame.board.setContent(newGame.myPosition, cellStatus.LIGHT)
        if iMove.value == actions.DEPLOY:
            print >> sys.stderr, "DEPLOY envisager" 
            newGame.myPosition = self.previousAction.getNewCoord(newGame.myPosition)
            newGame.board.setContent(newGame.myPosition, cellStatus.PLAYER)
        else:
            newGame.myPosition = iMove.getNewCoord(newGame.myPosition)
        newGame.previousAction = iMove
        return newGame

    #Evaluate a game
    def evaluate(self):
        pos = self.myPosition
        res = 0
        guard = 0
        testedPos = normalizePosition(pos, actions.UP)
        while self.board.getContent(testedPos) == cellStatus.EMPTY and guard < 15:
            testedPos = normalizePosition(testedPos, actions.UP)
            res+=1
            guard +=1

        guard = 0
        testedPos = normalizePosition(pos, actions.DOWN)
        while self.board.getContent(testedPos) == cellStatus.EMPTY and guard < 15:
            testedPos = normalizePosition(testedPos, actions.DOWN)
            res+=1
            guard +=1

        guard = 0
        testedPos = normalizePosition(pos, actions.RIGHT)
        while self.board.getContent(testedPos) == cellStatus.EMPTY and guard < 15:
            testedPos = normalizePosition(testedPos, actions.RIGHT)
            res+=1
            guard +=1

        guard = 0
        testedPos = normalizePosition(pos, actions.LEFT)
        while self.board.getContent(testedPos) == cellStatus.EMPTY and guard < 15:
            testedPos = normalizePosition(testedPos, actions.LEFT)
            res+=1
            guard +=1
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
                temp = iClass.calcMax(iState.applyMove(move),iCurrentLevel+1,iMaxLevel)
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
            temp = iClass.calcMax(iState.applyMove(move),1,iMaxLevel)
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

    #Collet the inputs
    start_time = time.time()
    helper_bots = int(raw_input())
    
    for i in xrange(player_count):
        x, y = [int(j) for j in raw_input().split()]
        if x > -1:
        # real player have x,y > 0
            if i == my_id:
                myGame.setMyPosition(x, y)
            else:
                myGame.refreshPosition(x, y)
    removal_count = int(raw_input())
    for i in xrange(removal_count):
        remove_x, remove_y = [int(j) for j in raw_input().split()]
        myGame.refreshRemovePosition([remove_x, remove_y])

    myGame.applyPosition()
    myGame.setRemainingBots(helper_bots)

    retour = miniMax.miniMax(myGame, 4)
    #print >> sys.stderr, "Debug messages...", retour
    
    myGame.applyRefresh(retour)

    #theWinMove = miniMax.miniMax(myGame)
    end_time = time.time()

    print >> sys.stderr, "Debug messages..." ,end_time-start_time
    
    print getLabel(retour.value)
    

    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
