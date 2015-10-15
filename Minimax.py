#!/usr/bin/python
    
import sys
import copy
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


###############
### EXAMPLE ###
###############

class moveTicTacToe:
	def __init__(oSelf,iX,iY,iPlayer):
		oSelf.x = iX
		oSelf.y = iY
		oSelf.player = iPlayer

class player:
	def __init__(oSelf, iPlayer):
		oSelf.player = iPlayer
	
	def getNextPlayer(iSelf):
		if iSelf.player == "X":
			return player("O")
		elif iSelf.player == "O":
			return player("X")
			
	def getMark(iSelf):
		return iSelf.player
		
class state:
	def __init__(oSelf):
		oSelf.board = [ [None, None, None], [None, None, None], [None, None, None]]
		oSelf.lastPlayer = player("X") # "O" always starts
		
	def evalLines(iSelf, iPlayer):
		res = 0
		otherMark = iPlayer.getNextPlayer().getMark()
		for line in iSelf.board:
			for pos in line:
				if pos == otherMark:
					break #no win here, switch to next one
			res+=1
		return res
	
	def evalColumns(iSelf, iPlayer):
		res = 0
		otherMark = iPlayer.getNextPlayer().getMark()
		for i in range(0,3):
			for j in range(0,3):
				if iSelf.board[j][i] == otherMark:
					break #no win here, switch to next one
			res+=1
		return res
	
	def evalDiags(iSelf, iPlayer):
		res = 0
		otherMark = iPlayer.getNextPlayer().getMark()
		for i in range(0,3):
			if iSelf.board[i][i] == otherMark:
				break #no win here, switch to next one
			res+=1
		for i in range(0,3):
			if iSelf.board[2-i][i] == otherMark:
				break #no win here, switch to next one
			res+=1 
		return res

	def evaluate(iSelf):
		""" returns the number of open wining possibilities"""
		otherPlayer = iSelf.lastPlayer
		currentPlayer = iSelf.lastPlayer.getNextPlayer()
		return (iSelf.evalLines(currentPlayer)
			+	iSelf.evalColumns(currentPlayer)
			+	iSelf.evalDiags(currentPlayer)
			-	iSelf.evalLines(otherPlayer)
			-	iSelf.evalColumns(otherPlayer)
			-	iSelf.evalDiags(otherPlayer))
		
	
	def getMoves(iSelf):
		res=[]
		currentPlayer = iSelf.lastPlayer.getNextPlayer()
		for i in range(0,3):
			for j in range(0,3):
				if iSelf.board[i][j] == None:
					res.append(moveTicTacToe(i,j,currentPlayer))
		return res
	
	def playMove(ioSelf, iMove):
		res = copy.deepcopy(ioSelf)
		res.board[iMove.x][iMove.y] = iMove.player.getMark()
		res.lastPlayer = iMove.player
		return res
	
	def display(iSelf):
		for line in iSelf.board:
			print "_________"
			for case in line:
				if case == None:
					sys.stdout.write("| |")
				else:
					sys.stdout.write("|"+case+"|")
			print
		print "_________"

			

def mainLoop():
	currentState = state()
	for i in range(0,10):
		currentState.display()
		nextMove = miniMax.miniMax(currentState,4)
		currentState = currentState.playMove(nextMove)

mainLoop()
