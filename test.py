import main
import time


myGame = main.game()

myGame.board.setContent([3,3], main.cellStatus.LIGHT)
myGame.board.setContent([3,4], main.cellStatus.LIGHT)
myGame.board.setContent([3,5], main.cellStatus.LIGHT)
myGame.board.setContent([3,6], main.cellStatus.LIGHT)
myGame.board.setContent([3,7], main.cellStatus.LIGHT)
myGame.board.setContent([3,8], main.cellStatus.LIGHT)
myGame.board.setContent([3,9], main.cellStatus.LIGHT)
myGame.board.setContent([3,10], main.cellStatus.LIGHT)
myGame.board.setContent([4,10], main.cellStatus.LIGHT)
myGame.board.setContent([4,11], main.cellStatus.LIGHT)
myGame.board.setContent([3,11], main.cellStatus.LIGHT)
myGame.board.setContent([3,12], main.cellStatus.LIGHT)
myGame.board.setContent([4,12], main.cellStatus.LIGHT)
myGame.board.setContent([5,12], main.cellStatus.LIGHT)
myGame.board.setContent([6,12], main.cellStatus.LIGHT)
myGame.board.setContent([7,12], main.cellStatus.LIGHT)
myGame.board.setContent([8,12], main.cellStatus.LIGHT)
myGame.board.setContent([9,12], main.cellStatus.LIGHT)
myGame.board.setContent([9,13], main.cellStatus.LIGHT)
myGame.board.setContent([9,14], main.cellStatus.LIGHT)
myGame.board.setContent([9,15], main.cellStatus.LIGHT)
myGame.board.setContent([10,15], main.cellStatus.LIGHT)
myGame.board.setContent([10,3], main.cellStatus.LIGHT)
myGame.board.setContent([10,4], main.cellStatus.LIGHT)
myGame.board.setContent([10,5], main.cellStatus.LIGHT)
myGame.board.setContent([10,6], main.cellStatus.LIGHT)
myGame.board.setContent([10,7], main.cellStatus.LIGHT)
myGame.board.setContent([10,8], main.cellStatus.LIGHT)
myGame.board.setContent([9,3], main.cellStatus.LIGHT)
myGame.board.setContent([9,4], main.cellStatus.LIGHT)
myGame.board.setContent([9,5], main.cellStatus.LIGHT)
myGame.board.setContent([9,6], main.cellStatus.LIGHT)
myGame.board.setContent([20,3], main.cellStatus.LIGHT)
myGame.board.setContent([20,4], main.cellStatus.LIGHT)
myGame.board.setContent([20,5], main.cellStatus.LIGHT)
myGame.board.setContent([20,6], main.cellStatus.LIGHT)
myGame.board.setContent([20,7], main.cellStatus.LIGHT)
myGame.board.setContent([20,8], main.cellStatus.LIGHT)
myGame.board.setContent([20,9], main.cellStatus.LIGHT)
myGame.board.setContent([20,10], main.cellStatus.LIGHT)
myGame.board.setContent([20,11], main.cellStatus.LIGHT)
myGame.board.setContent([20,12], main.cellStatus.LIGHT)
myGame.board.setContent([21,12], main.cellStatus.LIGHT)
myGame.board.setContent([21,13], main.cellStatus.LIGHT)
myGame.board.setContent([21,14], main.cellStatus.LIGHT)
myGame.board.setContent([21,15], main.cellStatus.LIGHT)
myGame.board.setContent([21,16], main.cellStatus.LIGHT)

myGame.setMyPosition(7, 21)

while 1:

    #Collet the inputs
    start_time = time.time()
    #helper_bots = int(raw_input())

    #for i in xrange(player_count):
    #    x, y = [int(j) for j in raw_input().split()]
    #    if x > -1:
        # real player have x,y > 0
    #        if i == my_id:
    #            myGame.setMyPosition(x, y)
    #        else:
    #            myGame.refreshPosition(x, y)
    #removal_count = int(raw_input())
    #for i in xrange(removal_count):
    #    remove_x, remove_y = [int(j) for j in raw_input().split()]
    #    myGame.refreshRemovePosition([remove_x, remove_y])

    myGame.applyPosition()
    #myGame.setRemainingBots(helper_bots)

    retour = main.miniMax.miniMax(myGame, 4)
    #print >> sys.stderr, "Debug messages...", retour

    myGame.applyRefresh(retour)

    #theWinMove = miniMax.miniMax(myGame)
    end_time = time.time()

    print "Debug messages..." ,end_time-start_time

    print main.getLabel(retour.value)


    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."