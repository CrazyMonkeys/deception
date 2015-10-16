import sys
import math
import copy
import time
import cProfile
import random

LOGGING = False

def cprint(iString):
    if LOGGING:
        print str(iString)

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
        if iPreviousAction and iPreviousAction.value != actions.DEPLOY:
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
            #print >> sys.stderr, "DEPLOY envisager" 
            newGame.myPosition = self.previousAction.getNewCoord(newGame.myPosition)
            newGame.board.setContent(newGame.myPosition, cellStatus.PLAYER)
        else:
            newGame.myPosition = iMove.getNewCoord(newGame.myPosition)
            newGame.previousAction = iMove
        return newGame
        
class miniMax:

    @classmethod
    def calcMax(iClass,iState,iCurrentLevel, iMaxLevel):
        #iState.display()
        cprint("CALCMAX LEVEL="+str(iCurrentLevel))
        #iState.printObject()
        if iCurrentLevel == iMaxLevel:
            cprint ("max prof =" + str(iCurrentLevel))
            return iCurrentLevel
        else:
            valueBestMove =-100000
            M = iState.getMoves()
            cprint("Possible moves in calcMax :"+str([getLabel(m.value) for m in M]))
            for m in M:
                cprint( "calcMax :Evaluating move"+' '+ getLabel(m.value)+' at level'+str(iCurrentLevel))
                temp = iClass.calcMax(iState.applyMove(m),iCurrentLevel+1,iMaxLevel)
                cprint( "calcMax :Result="+ str(temp))
                
                if temp > valueBestMove:
                    valueBestMove=temp
            if not M:
                cprint("leaf = " + str(iCurrentLevel))
                return iCurrentLevel
                
            return valueBestMove

    
    @classmethod
    def miniMax(iClass,iState,iMaxLevel):
        #iState.display()
        bestMove = None
        valueBestMove = -100000
        for m in iState.getMoves():
            cprint( "miniMax :Evaluating"+' '+ getLabel(m.value))
            temp = iClass.calcMax(iState.applyMove(m),1,iMaxLevel)
            #print "m is", temp, " best move is ", valueBestMove
            
            #Apply risk factor on temp
            if iClass.isRisky(iState,m):
                temp = round(temp / 2.0)
            if temp > valueBestMove:
                valueBestMove=temp
                bestMove=m
        return bestMove

    @classmethod        
    def isRisky(iClass,iState,iMove):
        newPos = normalizePosition(iState.mState.myPosition, iMove)
        numPlayers = 0
        if iState.getPatchedContent(normalizePosition(newPos, actions.UP)) == cellStatus.PLAYER:
            numPlayers+=1
        if iState.getPatchedContent(normalizePosition(newPos, actions.DOWN)) == cellStatus.PLAYER:
            numPlayers+=1
        if iState.getPatchedContent(normalizePosition(newPos, actions.RIGHT)) == cellStatus.PLAYER:
            numPlayers+=1
        if iState.getPatchedContent(normalizePosition(newPos, actions.LEFT)) == cellStatus.PLAYER:
            numPlayers+=1
        return numPlayers > 2
        
        
    
    
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
        
    def printObject(self):
        cprint ("Evaluating board")
        for i in range(0,15):
            line =''
            for j in range(0,30):
                line += str(self.getPatchedContent([j,i])).replace("0", ".")+' '
            cprint(line)

    def setStateFromGame(self,iGame):
        self.mState.myPosition = iGame.myPosition
        self.mState.previousAction = iGame.previousAction
        self.mState.remainingBots= iGame.remainingBots

    def setStateFromProxyGame(self,iMutableState):
        self.mState = iMutableState
    
    def getPatchedContent(self,iPos):
        k = tuple(iPos)
        if k in self.mState.patchDict:
            return self.mState.patchDict[k]
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
        random.shuffle(aList)
        if self.mState.previousAction:
            #print "get moves / remaining bots: ",getLabel(self.mState.previousAction.value) , normalizePosition(self.mState.myPosition, self.mState.previousAction.value)
            if self.getPatchedContent(normalizePosition(self.mState.myPosition, self.mState.previousAction.value)) == cellStatus.LIGHT and self.mState.remainingBots >0:
                aList.append(move(actions.DEPLOY))
                #print "Deployed considered"
        
        #if not aList:
            #aList.append(move(actions.DEPLOY))
        cprint("Possible moves :"+str([getLabel(m.value) for m in aList]))
        return aList


    #Apply a move to the current game and return a copy of the game
    def applyMove(self, iMove):
        # return a copy a the current game proxy after the move is applied
        mState = copy.copy(self.mState)
        newGame = copy.copy(self)
        newGame.setStateFromProxyGame(mState)
        #INVARIANT: newGame and self are light copies
        
        newGame.mState.patchDict[tuple(newGame.mState.myPosition)] = cellStatus.LIGHT
        if iMove.value == actions.DEPLOY:
            newGame.mState.remainingBots -=1
            
            newGame.mState.myPosition = self.mState.previousAction.getNewCoord(newGame.mState.myPosition)
        else:
            newGame.mState.myPosition = iMove.getNewCoord(newGame.mState.myPosition)
            newGame.mState.previousAction = iMove
        
        #INVARIANT : position is update accordingly to move
        newGame.mState.patchDict[tuple(newGame.mState.myPosition)] = cellStatus.PLAYER
        #newGame.printObject()
        return newGame

    #Evaluate a game
    def evaluate(self,iProf):
        #print "prof",iProf
        return iProf


player_count = int(raw_input())
my_id = int(raw_input())

# game loop

myGame = game()

while 1:

    #Collet the inputs
    start_time = time.time()
    helper_bots = int(raw_input())
    myGame.setRemainingBots(helper_bots)

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

    aGameProxy = gameProxy(myGame)

    aGameProxy.setStateFromGame(myGame)
    retour = miniMax.miniMax(aGameProxy, 500)
    #print >> sys.stderr, "Debug messages...", retour

    myGame.applyRefresh(retour)
    end_time = time.time()

    print(getLabel(retour.value))
    

    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."