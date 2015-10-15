import sys
import math
import copy
import time
import cProfile

def do_cprofile(func):
    def profiled_func(*args, **kwargs):
        profile = cProfile.Profile()
        try:
            profile.enable()
            result = func(*args, **kwargs)
            profile.disable()
            return result
        finally:
            profile.print_stats()
    return profiled_func

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
    
    def printObject(self):
        for line in self.grille:
            print(str((' ').join([str(i).replace("0", ".") for i in line])))


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
        
class miniMax:
    @classmethod
    def calcMin(iClass,iState,iCurrentLevel, iMaxLevel):
        #iState.display()
        if iCurrentLevel == iMaxLevel:
            return iState.evaluate(iCurrentLevel)
        else:
            valueBestMove = +100000
            for move in iState.getMoves():
                temp = iClass.calcMax(iState.applyMove(move),iCurrentLevel+1,iMaxLevel)
                if temp < valueBestMove:
                    valueBestMove=temp
                    bestMove=move
            else:
                return iState.evaluate(iCurrentLevel)
            return valueBestMove

    @classmethod
    def calcMax(iClass,iState,iCurrentLevel, iMaxLevel):
        #iState.display()
        if iCurrentLevel == iMaxLevel:
            return iState.evaluate(iCurrentLevel)
        else:
            valueBestMove =-100000
            for move in iState.getMoves():
                temp = iClass.calcMax(iState.applyMove(move),iCurrentLevel+1,iMaxLevel)
                if temp > valueBestMove:
                    valueBestMove=temp
            else:
                return iState.evaluate(iCurrentLevel)
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
        return bestMove
    
class mutableState:
    def __init__(self):
        self.myPosition = [-1, -1]
        self.previousAction = None
        self.remainingBots= 0
        self.patchDict = {}

class gameProxy:
    def __init__(self,iGame):
        self.board = iGame.board
        self.mState = mutableState()
        self.mState.myPosition =iGame.myPosition
        self.mState.previousAction =iGame.previousAction
        self.mState.remainingBots =iGame.remainingBots
    
    def getPatchedContent(self,iPos):
        k = tuple(iPos)
        if tuple(k) in self.mState.patchDict:
            return self.mState.patchDict[tuple(k)]
        else:
            return self.board.getContent(iPos)

    #List the possible moves for the current player
    def getMoves(self):
        aList = []
        if self.getPatchedContent(normalizePosition(self.mState.myPosition, actions.UP)) == cellStatus.EMPTY:
            aList.append(move(actions.UP))
        if self.getPatchedContent(normalizePosition(self.mState.myPosition, actions.DOWN)) == cellStatus.EMPTY:
            aList.append(move(actions.DOWN))
        if self.getPatchedContent(normalizePosition(self.mState.myPosition, actions.RIGHT)) == cellStatus.EMPTY:
            aList.append(move(actions.RIGHT))
        if self.getPatchedContent(normalizePosition(self.mState.myPosition, actions.LEFT)) == cellStatus.EMPTY:
            aList.append(move(actions.LEFT))
        #if normalizePosition(self.myPosition, self.previousAction) == cellStatus.LIGHT:
            #aList.append(move(actions.DEPLOY))
        if not aList:
            aList.append(move(actions.DEPLOY))
        print aList
        return aList


    #Apply a move to the current game and return a copy of the game
    def applyMove(self, iMove):
        # return a copy a the current game proxy after the move is applied
        newGame = copy.copy(self)
        #newGame.board = self.board
        #newGame.mState = copy.copy(self.mState)
        newGame.mState.patchDict[tuple(newGame.mState.myPosition)] = cellStatus.LIGHT
        newGame.mState.myPosition = iMove.getNewCoord(newGame.mState.myPosition)
        newGame.mState.previousAction = iMove
        return newGame

    #Evaluate a game
    def evaluate(self,iProf):
        return iProf


@do_cprofile
def main():
    # game loop
    start_time = time.time()
    mygame = game()
    mygame.setMyPosition(10, 10)
    aGameProxy = gameProxy(mygame)
    retour = miniMax.miniMax(aGameProxy, 50)
    
    print >> sys.stderr, "Retour=",getLabel(retour.value)
    
    end_time = time.time()

    print >> sys.stderr, "debug messages..." ,end_time -start_time
    
#main()
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
